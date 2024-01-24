---
title: XAudio2 structures
description: This section contains information about structures provided by the Microsoft XAudio2 API.
ms.assetid: 3656aaf9-7a3a-2a5b-50f5-d279ce8a9e6c
ms.topic: article
ms.date: 05/31/2018
---

# XAudio2 structures

This section contains information about structures provided by the Microsoft XAudio2 API.



| Structure                                                                                 | Description                                                                                                                                    |
|-------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| [**XAUDIO2\_BUFFER**](/windows/desktop/api/xaudio2/ns-xaudio2-xaudio2_buffer)                                                 | Represents an audio data buffer.<br/>                                                                                                    |
| [**XAUDIO2\_BUFFER\_WMA**](/windows/desktop/api/xaudio2/ns-xaudio2-xaudio2_buffer_wma)                                        | Represents a WMA audio data buffer.<br/>                                                                                                 |
| [**XAUDIO2\_DEBUG\_CONFIGURATION**](/windows/desktop/api/xaudio2/ns-xaudio2-xaudio2_debug_configuration)                      | Sets a new global debug configuration for XAudio2 when used by the SetDebugConfiguration function.                                             |
| [**XAUDIO2\_EFFECT\_CHAIN**](/windows/desktop/api/xaudio2/ns-xaudio2-xaudio2_effect_chain)                                    | Defines an effect chain.<br/>                                                                                                            |
| [**XAUDIO2\_EFFECT\_DESCRIPTOR**](/windows/desktop/api/xaudio2/ns-xaudio2-xaudio2_effect_descriptor)                          | Defines an effect.<br/>                                                                                                                  |
| [**XAUDIO2\_FILTER\_PARAMETERS**](/windows/desktop/api/xaudio2/ns-xaudio2-xaudio2_filter_parameters)                          | Defines filter parameters for a source voice.<br/>                                                                                       |
| [**XAUDIO2\_PERFORMANCE\_DATA**](/windows/desktop/api/xaudio2/ns-xaudio2-xaudio2_performance_data)                            | Retrieves performance information.<br/>                                                                                                  |
| [**XAUDIO2\_SEND\_DESCRIPTOR**](/windows/desktop/api/xaudio2/ns-xaudio2-xaudio2_send_descriptor)                              | Describes a voice send destination.<br/>                                                                                                 |
| [**XAUDIO2\_VOICE\_DETAILS**](/windows/desktop/api/xaudio2/ns-xaudio2-xaudio2_voice_details)                                  | Contains information about the creation flags, input channels, and sample rate of a voice.<br/>                                          |
| [**XAUDIO2\_VOICE\_SENDS**](/windows/desktop/api/xaudio2/ns-xaudio2-xaudio2_voice_sends)                                      | Defines a set of voices to receive data from a single output voice.<br/>                                                                 |
| [**XAUDIO2\_VOICE\_STATE**](/windows/desktop/api/xaudio2/ns-xaudio2-xaudio2_voice_state)                                      | Returns the voice's current state and cursor position data.<br/>                                                                         |
| [**XAUDIO2FX\_REVERB\_I3DL2\_PARAMETERS**](/windows/desktop/api/xaudio2fx/ns-xaudio2fx-xaudio2fx_reverb_i3dl2_parameters)         | Describes I3DL2 (Interactive 3D Audio Rendering Guidelines Level 2.0) parameters for use in the ReverbConvertI3DL2ToNative function.           |
| [**XAUDIO2FX\_REVERB\_PARAMETERS**](/windows/desktop/api/xaudio2fx/ns-xaudio2fx-xaudio2fx_reverb_parameters)                      | Describes parameters for use in the reverb APO.                                                                                                |
| [**XAUDIO2FX\_VOLUMEMETER\_LEVELS**](/windows/desktop/api/xaudio2fx/ns-xaudio2fx-xaudio2fx_volumemeter_levels)                    | Describes parameters for use with the volume meter APO.                                                                                        |
| [**XAPO\_LOCKFORPROCESS\_BUFFER\_PARAMETERS**](/windows/win32/api/xapo/ns-xapo-xapo_lockforprocess_parameters) | Defines buffer parameters that remain constant while an XAPO is locked.<br/>                                                             |
| [**XAPO\_PROCESS\_BUFFER\_PARAMETERS**](/windows/desktop/api/xapo/ns-xapo-xapo_process_buffer_parameters)               | Defines buffer parameters that may change from one call to the next.<br/>                                                                |
| [**XAPO\_REGISTRATION\_PROPERTIES**](/windows/desktop/api/xapo/ns-xapo-xapo_registration_properties)                    | Describes general characteristics of an XAPO.<br/>                                                                                       |
| [**FXECHO\_INITDATA**](/windows/desktop/api/xapofx/ns-xapofx-fxecho_initdata)                                               | Initialization parameters for use with the FXECHO XAPO.<br/>                                                                             |
| [**FXECHO\_PARAMETERS**](/windows/desktop/api/xapofx/ns-xapofx-fxecho_parameters)                                           | Parameters for use with the FXECHO XAPO.<br/>                                                                                            |
| [**FXEQ\_PARAMETERS**](/windows/desktop/api/xapofx/ns-xapofx-fxeq_parameters)                                               | Parameters for use with the FXEQ XAPO.<br/>                                                                                              |
| [**FXMASTERINGLIMITER\_PARAMETERS**](/windows/desktop/api/xapofx/ns-xapofx-fxmasteringlimiter_parameters)                   | Parameters for use with the FXMasteringLimiter XAPO.<br/>                                                                                |
| [**FXREVERB\_PARAMETERS**](/windows/desktop/api/xapofx/ns-xapofx-fxreverb_parameters)                                       | Parameters for use with the FXReverb XAPO.<br/>                                                                                          |
| [**X3DAUDIO\_CONE**](/windows/desktop/api/x3daudio/ns-x3daudio-x3daudio_cone)                                                   | Specifies directionality for a single-channel non-LFE emitter by scaling DSP behavior with respect to the emitter's orientation.<br/>    |
| [**X3DAUDIO\_DISTANCE\_CURVE**](/windows/desktop/api/x3daudio/ns-x3daudio-x3daudio_distance_curve)                              | Defines an explicit piecewise curve made up of linear segments, directly defining DSP behavior with respect to normalized distance.<br/> |
| [**X3DAUDIO\_DISTANCE\_CURVE\_POINT**](/windows/desktop/api/x3daudio/ns-x3daudio-x3daudio_distance_curve_point)                 | Defines a DSP setting at a given normalized distance.<br/>                                                                               |
| [**X3DAUDIO\_DSP\_SETTINGS**](/windows/desktop/api/x3daudio/ns-x3daudio-x3daudio_dsp_settings)                                  | Receives the results from a call to X3DAudioCalculate.<br/>                                                                              |
| [**X3DAUDIO\_EMITTER**](/windows/desktop/api/x3daudio/ns-x3daudio-x3daudio_emitter)                                             | Defines a single or multi-point 3D audio source used with an arbitrary number of sound channels.<br/>                                    |
| [**X3DAUDIO\_LISTENER**](/windows/desktop/api/x3daudio/ns-x3daudio-x3daudio_listener)                                           | Defines a point of 3D audio reception.<br/>                                                                                              |



 

## Related topics

<dl> <dt>

[Programming Reference](programming-reference.md)
</dt> </dl>

 

 




