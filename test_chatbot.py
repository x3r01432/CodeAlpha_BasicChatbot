import io
import unittest
from unittest.mock import patch

import chatbot


class ChatbotTests(unittest.TestCase):
    def test_greetings_case_punct(self):
        for msg in ["hello", "HELLO!!", "  Hi. "]:
            self.assertIn("Hi!", chatbot.get_response(msg))

    def test_rules(self):
        self.assertIn("fine", chatbot.get_response("How are you?"))
        self.assertIn("CodeBot", chatbot.get_response("What's your name?"))
        self.assertIn("It's", chatbot.get_response("what time is it"))
        self.assertIn("bye", chatbot.get_response("help"))
        self.assertIn("Goodbye", chatbot.get_response("Bye!"))
        self.assertIn("don't understand", chatbot.get_response("blah"))

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_loop_stops_at_bye(self, out):
        with patch("builtins.input", side_effect=["hello", "BYE", "never read"]) as inp:
            chatbot.main()
        self.assertEqual(inp.call_count, 2)


if __name__ == "__main__":
    unittest.main()
