from typing import Dict

class TeamsCards:
    """class to provide cards for MS Teams Channel"""
    def card(self, text) -> Dict:
        card = {
                    "attachments": [
                        {
                        "contentType": "application/vnd.microsoft.card.adaptive",
                        "content": {
                                "type": "AdaptiveCard",
                                "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                                "version": "1.2",
                                "body": [
                                    {
                                        "type": "TextBlock",
                                        "text": text,
                                        "wrap": "true"
                                    }
                                ]
                        }
                        }
                    ]
                    }
        return card

    def button(self, title, response)  -> Dict:
        button = {
                    "type": "Action.Submit",
                    "title": title,
                    # "value": response
                    "data": {
                        "msteams": {
                            "type": "messageBack",
                            "displayText": title,
                            "text": response
                            # "value":{
                            #     property:response
                            # }
                            # "value": response
                            # "value": {
                            #     "option": "opt1"
                            # }
                            # "payload": response
                        }
                    },
                    "style": "positive"
                }
        return button
