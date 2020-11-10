from ask_sdk_model.interfaces.alexa.presentation.apl import RenderDocumentDirective as RenderApl
from ask_sdk_model.interfaces.alexa.presentation.apla import RenderDocumentDirective as RenderApla

aplaDatasource = {
            "data": {
                "text": speak_output
            }
        }
		
datasource = {
            "data": {
                "type": "object",
                "properties": {
                    "xs": xs,
                }
            }
        }
		
rb = handler_input.response_builder

if ask_utils.get_supported_interfaces(handler_input) \
		.alexa_presentation_apl is not None:
	rb.add_directive(
		RenderApl(
			# type="Alexa.Presentation.APL.RenderDocument",
			token=TOKEN,
			document=_load_apl_document(path),
			datasources=datasource
		)
	)
rb.add_directive(
	RenderApla(
		# type="Alexa.Presentation.APLA.RenderDocument",
		token=SPEECH_TOKEN,
		document=_load_apl_document(speechPath),
		datasources=aplaDatasource
	)
)

return (
	rb
	# .speak(speak_output)
	.set_should_end_session(True)
	.response
)

