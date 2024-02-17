import asyncio
import signal
import vocode

from vocode.streaming.hosted_streaming_conversation import HostedStreamingConversation
from vocode.streaming.streaming_conversation import StreamingConversation
from vocode.helpers import create_microphone_input_and_speaker_output
from vocode.streaming.models.transcriber import (
    DeepgramTranscriberConfig,
    PunctuationEndpointingConfig,
)
from vocode.streaming.models.agent import ChatGPTAgentConfig
from vocode.streaming.models.message import BaseMessage
from vocode.streaming.models.synthesizer import AzureSynthesizerConfig

vocode.api_key = "{}"


if __name__ == "__main__":
    microphone_input, speaker_output = create_microphone_input_and_speaker_output(
    use_default_devices=True)

    conversation = HostedStreamingConversation(
        input_device=microphone_input,
        output_device=speaker_output,
        transcriber_config=DeepgramTranscriberConfig.from_input_device(
            microphone_input,
            endpointing_config=PunctuationEndpointingConfig(),
        ),
        agent_config=ChatGPTAgentConfig(
            initial_message=BaseMessage(text="Hello!"),
            prompt_preamble="Have a pleasant conversation about life",
        ),
        synthesizer_config=AzureSynthesizerConfig.from_output_device(speaker_output),
    )
    # This allows you to stop the conversation with a KeyboardInterrupt
    signal.signal(signal.SIGINT, lambda _0, _1: conversation.deactivate())
    asyncio.run(conversation.start())
from vocode.streaming.user_implemented_agent.restful_agent import RESTfulAgent
from vocode.streaming.models.agent import RESTfulAgentOutput, RESTfulAgentText, RESTfulAgentEnd

class YourAgent(RESTfulAgent):

    # input: the transcript from the Conversation that the agent must respond to
    async def respond(self, input: str, conversation_id: str) -> RESTfulAgentOutput:
        if "bye" in input:
            return RESTfulAgentEnd()  ## ends the conversation
        else:
            return RESTfulAgentText(response=input)  ## responds with the input received
