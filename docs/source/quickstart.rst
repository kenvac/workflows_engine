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
                status_message_template="Screen complete"
            )

    print(json.dumps(QuickWorkflow().as_dict(), indent=4))

Produces the output:

.. testoutput::

    {
        "validators": {},
        "components": {
            "HelloWorldMessage": {
                "type": "message_box",
                "message": {
                    "template": "HelloWorld",
                    "type": "info"
                },
                "size": "normal"
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
                        "template": "Screen complete"
                    }
                }
            ]
        },
        "hash": "1a85414df82bdb74b36ad28150b4ec339b69a9b1772ad55d5aaea15d5926ec6aa5782ac08d28503e7ca4d13da79731e522e56e9be153c30fe73b8a68ab8643cf",
        "context": {}
    }
