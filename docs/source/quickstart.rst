***********
Quick start
***********
.. testsetup::

    import json
    from workflows_engine import Workflow


.. testcode::

    import json
    from workflows_engine import Workflow, components

    class QuickWorkflow(Workflow):

        def flow(self):
            self.add_task(
                task_type="screen",
                name="HelloWorld",
                components=[
                    components.displays.info(
                        identifier="HelloWorldMessage",
                        template="HelloWorld",
                    )
                ],
            )

    print(json.dumps(QuickWorkflow().as_dict(), indent=4))

Produces the output:

.. testoutput::

    {
        "validators": {},
        "components": {
            "HelloWorldMessage": {
                "type": "message_box",
                "message_template": "HelloWorld",
                "message_type": "info"
            }
        },
        "flow": {
            "type": "flow",
            "name": "QuickWorkflow",
            "tasks": [
                {
                    "type": "screen",
                    "name": "HelloWorld",
                    "components": [
                        [
                            {
                                "name": "HelloWorldMessage"
                            }
                        ]
                    ],
                    "status_message": {
                        "type": "success",
                        "template": null
                    }
                }
            ]
        },
        "hash": "2e3b480ef9391f5c8b1f6114378ce7ae6f7b1f6ae6064162dff55c565aad1bdd7f970ff6becf30c92c0e818d5d3e5a5cacfd716e8891049d5bcbf1728dfd8509",
        "context": {}
    }
