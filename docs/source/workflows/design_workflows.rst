Design Workflows
========================

A :class:`~citrine.informatics.workflows.design_workflow.DesignWorkflow` ranks materials according to a :doc:`score <scores>`.
This workflow is comprised of three modules:

-  :doc:`Design space <design_spaces>` defines all possible materials that can be generated.
-  :doc:`Predictor <predictors>` adds information to a material using predictions from a machine-learned model.
-  :doc:`Processor <processors>` defines how to pick the “next” material.

The following example demonstrates how to use the Citrine Python client to register a workflow (assuming a design space, predictor and processor were registered previously), wait for validation to complete and check the final status:

.. code:: python

    from citrine.informatics.workflows import DesignWorkflow
    from citrine.jobs.waiting import wait_while_validating

    # create a workflow using existing modules and register it with the project
    workflow = project.design_workflows.register(
        DesignWorkflow(
            name='Example workflow',
            predictor_id=predictor.uid,
            processor_id=processor.uid,
            design_space_id=design_space.uid
        )
    )

    # wait until the workflow is no longer validating
    wait_while_validating(collection=project.design_workflows, module=workflow, print_status_info=True)

    # print final validation status
    validated_workflow = project.design_workflows.get(workflow.uid)
    print(validated_workflow.status)
    # status info will contain relevant validation information
    # (i.e. why the workflow is valid/invalid)
    print(validated_workflow.status_info)


Execution and results
---------------------

When a design workflow is executed, the processor will search the design space for optimal materials using additional information provided by the predictor.
The result is a list of scored and ranked materials.
Materials at the head of the list are the best materials found from searching the design space.

A workflow can be run using the Citrine Python client.
Triggering a workflow returns a workflow execution object.
A workflow execution has a status (in progress, succeeded, or failed) and results (once execution has succeeded).

Candidate results are paginated and returned as `DesignCandidate <#design-candidate>`__ objects.

.. code:: python

    from citrine.informatics.objectives import ScalarMaxObjective
    from citrine.informatics.scores import LIScore
    from citrine.jobs.waiting import wait_while_executing


    # create a score with the desired objectives and baselines
    score = LIScore(
        # create an objective to maximize shear modulus
        # the descriptor key must match a descriptor in materials produced from the design space
        objectives=[ScalarMaxObjective(descriptor_key='Shear modulus')],
        baselines=[150.0] # one for each objective
    )

    # trigger a design run using a previously registered and validated workflow
    execution = workflow.design_executions.trigger(score)

    # wait for execution to complete
    wait_while_executing(collection=workflow.design_executions, execution=execution, print_status_info=True)

    # get the candidate generator
    execution_results = execution.candidates()

    # pull out the candidate with the highest shear modulus and its score
    # (this should be the candidate at the head of the list since we used shear modulus to score and rank materials)
    # Note that because execution_results is a generator, calling this multiple times will iterate through the generator, getting the next best candidate
    best_candidate = next(execution_results)
    print(best_candidate)
    best_score = best_candidate.primary_score
    print(best_score)

    # Alternatively, you can iterate over the candidates generator, looking at each candidate
    for candidate in execution.candidates():
        print(candidate.primary_score)

    # To save all candidates in memory in one list:
    all_candidates = list(execution.candidates())

    # we can confirm the best candidate is at the head of the list using
    # this candidate will be the same as best_candidate above
    candidate_with_max_shear_modulus = max(all_candidates, key=lambda candidate: candidate.material.values['Shear modulus'].mean)
    print(candidate_with_max_shear_modulus)


You can to look up what :doc:`score <scores>` was used for a particular execution, as well as which :doc:`descriptors <descriptors>` where used:

.. code:: python

    score = execution.score
    descriptors = execution.descriptors


Design Candidate
-----------------

A :class:`~citrine.informatics.design_candidate.DesignCandidate` represents the result of the Design Execution.
They contain the `primary score` of the candidate and the :class:`~citrine.informatics.design_candidate.DesignMaterial` for that candidate.
DesignMaterials are simpler approximations ("projections") of the materials information about a particular design candidate.

DesignMaterials approximate the distribution of values that a variable might take.
Each variable is represented as one of:

* :class:`~citrine.informatics.design_candidate.MeanAndStd`
* :class:`~citrine.informatics.design_candidate.TopCategories`
* :class:`~citrine.informatics.design_candidate.Mixture`
* :class:`~citrine.informatics.design_candidate.ChemicalFormula`
* :class:`~citrine.informatics.design_candidate.MolecularStructure`.

For example:

.. code:: python

    candidate = next(execution.candidates())

    # to get the score of a particular candidate
    score = candidate.primary_score

    # Assume a real descriptor, 'elastic limit', represented as a MeanAndStd variable
    candidate.material.values['elastic limit'].mean
    candidate.material.values['elastic limit'].std

    # Assume a categorical descriptor, 'color', represented as a TopCategories variable
    candidate.material.values['color'].probabilities

    # Assume a formulation descriptor, 'final mixture', represented as a Mixture variable
    candidate.material.values['final mixture'].quantities

    # Assume a chemical formula descriptor, 'alloying material', represented as a ChemicalFormula variable
    candidate.material.values['alloying material'].formula

    # Assume a molecular structure descriptor, 'solvent', represented as a MolecularStructure variable
    candidate.material.values['solvent'].smiles
