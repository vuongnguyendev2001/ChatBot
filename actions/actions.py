
# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
#
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher



class ActionHandleFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Đây là nơi bạn có thể định nghĩa hành động xử lý khi chatbot không hiểu
        dispatcher.utter_message("Xin lỗi, tôi không hiểu yêu cầu của bạn. Bạn có thể đặt câu hỏi cụ thể hơn hoặc yêu cầu giúp đỡ về một chủ đề cụ thể nào đó.")
        return []