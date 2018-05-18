---
Description: 'This section contains information about interfaces provided by the Microsoft XAudio2 API.'
ms.assetid: '96691e00-9ed0-b31c-fbe9-4daaba0daf98'
title: Interfaces
---

# Interfaces

This section contains information about interfaces provided by the Microsoft XAudio2 API.

## In this section



| Topic                                                               | Description                                                                                                                                                                                                                                                                                                                              |
|---------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IXAudio2**](ixaudio2.md)<br/>                             | IXAudio2 is the interface for the [XAudio2](xaudio2-apis-portal.md) object that manages all audio engine states, the audio processing thread, the voice graph, and so forth. <br/>                                                                                                                                                |
| [**IXAudio2Voice**](ixaudio2voice.md)<br/>                   | [**IXAudio2Voice**](ixaudio2voice.md) represents the base interface from which [**IXAudio2SourceVoice**](ixaudio2sourcevoice.md), [**IXAudio2SubmixVoice**](ixaudio2submixvoice.md) and [**IXAudio2MasteringVoice**](ixaudio2masteringvoice.md) are derived. The methods listed below are common to all voice subclasses.<br/> |
| [**IXAudio2SourceVoice**](ixaudio2sourcevoice.md)<br/>       | Use a source voice to submit audio data to the XAudio2 processing pipeline.<br/>                                                                                                                                                                                                                                                   |
| [**IXAudio2SubmixVoice**](ixaudio2submixvoice.md)<br/>       | A submix voice is used primarily for performance improvements and effects processing. <br/>                                                                                                                                                                                                                                        |
| [**IXAudio2MasteringVoice**](ixaudio2masteringvoice.md)<br/> | A mastering voice is used to represent the audio output device.<br/>                                                                                                                                                                                                                                                               |
| [**IXAudio2EngineCallback**](ixaudio2enginecallback.md)<br/> | The IXAudio2EngineCallback interface contains methods that notify the client when certain events happen in the [**IXAudio2**](ixaudio2.md) engine.<br/>                                                                                                                                                                           |
| [**IXAudio2VoiceCallback**](ixaudio2voicecallback.md)<br/>   | The [**IXAudio2VoiceCallback**](ixaudio2voicecallback.md) interface contains methods that notify the client when certain events happen in a given [**IXAudio2SourceVoice**](ixaudio2sourcevoice.md). <br/>                                                                                                                       |
| [**IXAPO**](ixapo.md)<br/>                                   | The interface for an Audio Processing Object which be used in an XAudio2 effect chain.<br/>                                                                                                                                                                                                                                        |
| [**IXAPOParameters**](ixapoparameters.md)<br/>               | An optional interface that allows an XAPO to use effect-specific parameters.<br/>                                                                                                                                                                                                                                                  |
| [**IXAPOHrtfParameters**](ixapohrtfparameters.md)<br/>       | The interface used to set parameters that control how head-related transfer function (HRTF) is applied to a sound.<br/>                                                                                                                                                                                                            |



 

## Related topics

<dl> <dt>

[Programming Reference](programming-reference.md)
</dt> <dt>

[Programming Reference](XAudio2.Programming_Reference)
</dt> </dl>

 

 




