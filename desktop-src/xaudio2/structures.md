---
Description: This section contains information about structures provided by the Microsoft XAudio2 API.
ms.assetid: 3656aaf9-7a3a-2a5b-50f5-d279ce8a9e6c
title: Structures
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Structures

This section contains information about structures provided by the Microsoft XAudio2 API.



| Structure                                                                                 | Description                                                                                                                                    |
|-------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| [**XAUDIO2\_BUFFER**](/windows/win32/xaudio2/ns-xaudio2-xaudio2_buffer?branch=master)                                                 | Represents an audio data buffer.<br/>                                                                                                    |
| [**XAUDIO2\_BUFFER\_WMA**](/windows/win32/xaudio2/ns-xaudio2-xaudio2_buffer_wma?branch=master)                                        | Represents a WMA audio data buffer.<br/>                                                                                                 |
| [**XAUDIO2\_DEBUG\_CONFIGURATION**](/windows/win32/xaudio2/ns-xaudio2-xaudio2_debug_configuration?branch=master)                      | Sets a new global debug configuration for XAudio2 when used by the SetDebugConfiguration function.                                             |
| [**XAUDIO2\_EFFECT\_CHAIN**](/windows/win32/xaudio2/ns-xaudio2-xaudio2_effect_chain?branch=master)                                    | Defines an effect chain.<br/>                                                                                                            |
| [**XAUDIO2\_EFFECT\_DESCRIPTOR**](/windows/win32/xaudio2/ns-xaudio2-xaudio2_effect_descriptor?branch=master)                          | Defines an effect.<br/>                                                                                                                  |
| [**XAUDIO2\_FILTER\_PARAMETERS**](/windows/win32/xaudio2/ns-xaudio2-xaudio2_filter_parameters?branch=master)                          | Defines filter parameters for a source voice.<br/>                                                                                       |
| [**XAUDIO2\_PERFORMANCE\_DATA**](/windows/win32/xaudio2/ns-xaudio2-xaudio2_performance_data?branch=master)                            | Retrieves performance information.<br/>                                                                                                  |
| [**XAUDIO2\_SEND\_DESCRIPTOR**](/windows/win32/xaudio2/ns-xaudio2-xaudio2_send_descriptor?branch=master)                              | Describes a voice send destination.<br/>                                                                                                 |
| [**XAUDIO2\_VOICE\_DETAILS**](/windows/win32/xaudio2/ns-xaudio2-xaudio2_voice_details?branch=master)                                  | Contains information about the creation flags, input channels, and sample rate of a voice.<br/>                                          |
| [**XAUDIO2\_VOICE\_SENDS**](/windows/win32/xaudio2/ns-xaudio2-xaudio2_voice_sends?branch=master)                                      | Defines a set of voices to receive data from a single output voice.<br/>                                                                 |
| [**XAUDIO2\_VOICE\_STATE**](/windows/win32/xaudio2/ns-xaudio2-xaudio2_voice_state?branch=master)                                      | Returns the voice's current state and cursor position data.<br/>                                                                         |
| [**XAUDIO2FX\_REVERB\_I3DL2\_PARAMETERS**](/windows/win32/xaudio2fx/ns-xaudio2fx-xaudio2fx_reverb_i3dl2_parameters?branch=master)         | Describes I3DL2 (Interactive 3D Audio Rendering Guidelines Level 2.0) parameters for use in the ReverbConvertI3DL2ToNative function.           |
| [**XAUDIO2FX\_REVERB\_PARAMETERS**](/windows/win32/xaudio2fx/ns-xaudio2fx-xaudio2fx_reverb_parameters?branch=master)                      | Describes parameters for use in the reverb APO.                                                                                                |
| [**XAUDIO2FX\_VOLUMEMETER\_LEVELS**](/windows/win32/xaudio2fx/ns-xaudio2fx-xaudio2fx_volumemeter_levels?branch=master)                    | Describes parameters for use with the volume meter APO.                                                                                        |
| [**XAPO\_LOCKFORPROCESS\_BUFFER\_PARAMETERS**](/windows/win32/xapo/ns-xapo-xapo_lockforprocess_buffer_parameters?branch=master) | Defines buffer parameters that remain constant while an XAPO is locked.<br/>                                                             |
| [**XAPO\_PROCESS\_BUFFER\_PARAMETERS**](/windows/win32/xapo/ns-xapo-xapo_process_buffer_parameters?branch=master)               | Defines buffer parameters that may change from one call to the next.<br/>                                                                |
| [**XAPO\_REGISTRATION\_PROPERTIES**](/windows/win32/xapo/ns-xapo-xapo_registration_properties?branch=master)                    | Describes general characteristics of an XAPO.<br/>                                                                                       |
| [**FXECHO\_INITDATA**](/windows/win32/xapofx/ns-xapofx-fxecho_initdata?branch=master)                                               | Initialization parameters for use with the FXECHO XAPO.<br/>                                                                             |
| [**FXECHO\_PARAMETERS**](/windows/win32/xapofx/ns-xapofx-fxecho_parameters?branch=master)                                           | Parameters for use with the FXECHO XAPO.<br/>                                                                                            |
| [**FXEQ\_PARAMETERS**](/windows/win32/xapofx/ns-xapofx-fxeq_parameters?branch=master)                                               | Parameters for use with the FXEQ XAPO.<br/>                                                                                              |
| [**FXMASTERINGLIMITER\_PARAMETERS**](/windows/win32/xapofx/ns-xapofx-fxmasteringlimiter_parameters?branch=master)                   | Parameters for use with the FXMasteringLimiter XAPO.<br/>                                                                                |
| [**FXREVERB\_PARAMETERS**](/windows/win32/xapofx/ns-xapofx-fxreverb_parameters?branch=master)                                       | Parameters for use with the FXReverb XAPO.<br/>                                                                                          |
| [**X3DAUDIO\_CONE**](/windows/win32/x3daudio/ns-x3daudio-x3daudio_cone?branch=master)                                                   | Specifies directionality for a single-channel non-LFE emitter by scaling DSP behavior with respect to the emitter's orientation.<br/>    |
| [**X3DAUDIO\_DISTANCE\_CURVE**](/windows/win32/x3daudio/ns-x3daudio-x3daudio_distance_curve?branch=master)                              | Defines an explicit piecewise curve made up of linear segments, directly defining DSP behavior with respect to normalized distance.<br/> |
| [**X3DAUDIO\_DISTANCE\_CURVE\_POINT**](/windows/win32/x3daudio/ns-x3daudio-x3daudio_distance_curve_point?branch=master)                 | Defines a DSP setting at a given normalized distance.<br/>                                                                               |
| [**X3DAUDIO\_DSP\_SETTINGS**](/windows/win32/x3daudio/ns-x3daudio-x3daudio_dsp_settings?branch=master)                                  | Receives the results from a call to X3DAudioCalculate.<br/>                                                                              |
| [**X3DAUDIO\_EMITTER**](/windows/win32/x3daudio/ns-x3daudio-x3daudio_emitter?branch=master)                                             | Defines a single or multi-point 3D audio source used with an arbitrary number of sound channels.<br/>                                    |
| [**X3DAUDIO\_LISTENER**](/windows/win32/x3daudio/ns-x3daudio-x3daudio_listener?branch=master)                                           | Defines a point of 3D audio reception.<br/>                                                                                              |



 

## Related topics

<dl> <dt>

[Programming Reference](programming-reference.md)
</dt> </dl>

 

 




