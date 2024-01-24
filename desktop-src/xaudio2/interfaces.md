---
title: XAudio2 interfaces
description: This section contains information about interfaces provided by the Microsoft XAudio2 API.
ms.assetid: 96691e00-9ed0-b31c-fbe9-4daaba0daf98
ms.topic: article
ms.date: 05/31/2018
---

# XAudio2 interfaces

This section contains information about interfaces provided by the Microsoft XAudio2 API.

## In this section



| Topic                                                               | Description                                                                                                                                                                                                                                                                                                                              |
|---------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IXAudio2**](/windows/desktop/api/xaudio2/nn-xaudio2-ixaudio2)<br/>                             | IXAudio2 is the interface for the [XAudio2](xaudio2-apis-portal.md) object that manages all audio engine states, the audio processing thread, the voice graph, and so forth. <br/>                                                                                                                                                |
| [**IXAudio2Voice**](/windows/desktop/api/xaudio2/nn-xaudio2-ixaudio2voice)<br/>                   | [**IXAudio2Voice**](/windows/desktop/api/xaudio2/nn-xaudio2-ixaudio2voice) represents the base interface from which [**IXAudio2SourceVoice**](/windows/desktop/api/xaudio2/nn-xaudio2-ixaudio2sourcevoice), [**IXAudio2SubmixVoice**](/windows/desktop/api/xaudio2/nn-xaudio2-ixaudio2submixvoice) and [**IXAudio2MasteringVoice**](/windows/desktop/api/xaudio2/nn-xaudio2-ixaudio2masteringvoice) are derived. The methods listed below are common to all voice subclasses.<br/> |
| [**IXAudio2SourceVoice**](/windows/desktop/api/xaudio2/nn-xaudio2-ixaudio2sourcevoice)<br/>       | Use a source voice to submit audio data to the XAudio2 processing pipeline.<br/>                                                                                                                                                                                                                                                   |
| [**IXAudio2SubmixVoice**](/windows/desktop/api/xaudio2/nn-xaudio2-ixaudio2submixvoice)<br/>       | A submix voice is used primarily for performance improvements and effects processing. <br/>                                                                                                                                                                                                                                        |
| [**IXAudio2MasteringVoice**](/windows/desktop/api/xaudio2/nn-xaudio2-ixaudio2masteringvoice)<br/> | A mastering voice is used to represent the audio output device.<br/>                                                                                                                                                                                                                                                               |
| [**IXAudio2EngineCallback**](/windows/desktop/api/xaudio2/nn-xaudio2-ixaudio2enginecallback)<br/> | The IXAudio2EngineCallback interface contains methods that notify the client when certain events happen in the [**IXAudio2**](/windows/desktop/api/xaudio2/nn-xaudio2-ixaudio2) engine.<br/>                                                                                                                                                                           |
| [**IXAudio2VoiceCallback**](/windows/desktop/api/xaudio2/nn-xaudio2-ixaudio2voicecallback)<br/>   | The [**IXAudio2VoiceCallback**](/windows/desktop/api/xaudio2/nn-xaudio2-ixaudio2voicecallback) interface contains methods that notify the client when certain events happen in a given [**IXAudio2SourceVoice**](/windows/desktop/api/xaudio2/nn-xaudio2-ixaudio2sourcevoice). <br/>                                                                                                                       |
| [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo)<br/>                                   | The interface for an Audio Processing Object which be used in an XAudio2 effect chain.<br/>                                                                                                                                                                                                                                        |
| [**IXAPOParameters**](/windows/desktop/api/XAPO/nn-xapo-ixapoparameters)<br/>               | An optional interface that allows an XAPO to use effect-specific parameters.<br/>                                                                                                                                                                                                                                                  |
| [**IXAPOHrtfParameters**](/windows/win32/api/hrtfapoapi/nn-hrtfapoapi-ixapohrtfparameters)<br/>       | The interface used to set parameters that control how head-related transfer function (HRTF) is applied to a sound.<br/>                                                                                                                                                                                                            |



 

## Related topics

<dl> <dt>

[Programming Reference](programming-reference.md)
</dt> <dt>

[Programming Reference](./programming-reference.md)
</dt> </dl>

 

 
