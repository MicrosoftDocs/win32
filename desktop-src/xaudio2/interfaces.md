---
Description: This section contains information about interfaces provided by the Microsoft XAudio2 API.
ms.assetid: 96691e00-9ed0-b31c-fbe9-4daaba0daf98
title: Interfaces
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Interfaces

This section contains information about interfaces provided by the Microsoft XAudio2 API.

## In this section



| Topic                                                               | Description                                                                                                                                                                                                                                                                                                                              |
|---------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IXAudio2**](/windows/win32/xaudio2/nn-xaudio2-ixaudio2?branch=master)<br/>                             | IXAudio2 is the interface for the [XAudio2](xaudio2-apis-portal.md) object that manages all audio engine states, the audio processing thread, the voice graph, and so forth. <br/>                                                                                                                                                |
| [**IXAudio2Voice**](/windows/win32/xaudio2/nn-xaudio2-ixaudio2voice?branch=master)<br/>                   | [**IXAudio2Voice**](/windows/win32/xaudio2/nn-xaudio2-ixaudio2voice?branch=master) represents the base interface from which [**IXAudio2SourceVoice**](/windows/win32/xaudio2/nn-xaudio2-ixaudio2sourcevoice?branch=master), [**IXAudio2SubmixVoice**](/windows/win32/xaudio2/nn-xaudio2-ixaudio2submixvoice?branch=master) and [**IXAudio2MasteringVoice**](/windows/win32/xaudio2/nn-xaudio2-ixaudio2masteringvoice?branch=master) are derived. The methods listed below are common to all voice subclasses.<br/> |
| [**IXAudio2SourceVoice**](/windows/win32/xaudio2/nn-xaudio2-ixaudio2sourcevoice?branch=master)<br/>       | Use a source voice to submit audio data to the XAudio2 processing pipeline.<br/>                                                                                                                                                                                                                                                   |
| [**IXAudio2SubmixVoice**](/windows/win32/xaudio2/nn-xaudio2-ixaudio2submixvoice?branch=master)<br/>       | A submix voice is used primarily for performance improvements and effects processing. <br/>                                                                                                                                                                                                                                        |
| [**IXAudio2MasteringVoice**](/windows/win32/xaudio2/nn-xaudio2-ixaudio2masteringvoice?branch=master)<br/> | A mastering voice is used to represent the audio output device.<br/>                                                                                                                                                                                                                                                               |
| [**IXAudio2EngineCallback**](/windows/win32/xaudio2/nn-xaudio2-ixaudio2enginecallback?branch=master)<br/> | The IXAudio2EngineCallback interface contains methods that notify the client when certain events happen in the [**IXAudio2**](/windows/win32/xaudio2/nn-xaudio2-ixaudio2?branch=master) engine.<br/>                                                                                                                                                                           |
| [**IXAudio2VoiceCallback**](/windows/win32/xaudio2/nn-xaudio2-ixaudio2voicecallback?branch=master)<br/>   | The [**IXAudio2VoiceCallback**](/windows/win32/xaudio2/nn-xaudio2-ixaudio2voicecallback?branch=master) interface contains methods that notify the client when certain events happen in a given [**IXAudio2SourceVoice**](/windows/win32/xaudio2/nn-xaudio2-ixaudio2sourcevoice?branch=master). <br/>                                                                                                                       |
| [**IXAPO**](/windows/win32/XAPO/nn-xapo-ixapo?branch=master)<br/>                                   | The interface for an Audio Processing Object which be used in an XAudio2 effect chain.<br/>                                                                                                                                                                                                                                        |
| [**IXAPOParameters**](/windows/win32/XAPO/nn-xapo-ixapoparameters?branch=master)<br/>               | An optional interface that allows an XAPO to use effect-specific parameters.<br/>                                                                                                                                                                                                                                                  |
| [**IXAPOHrtfParameters**](/windows/win32/HrtfApoApi/?branch=master)<br/>       | The interface used to set parameters that control how head-related transfer function (HRTF) is applied to a sound.<br/>                                                                                                                                                                                                            |



 

## Related topics

<dl> <dt>

[Programming Reference](programming-reference.md)
</dt> <dt>

[Programming Reference](XAudio2.Programming_Reference)
</dt> </dl>

 

 




