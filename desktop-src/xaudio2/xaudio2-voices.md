---
description: 'There are three types of XAudio2 voice objects: source, submix, and mastering voices.'
ms.assetid: 3a4acc03-e47a-ff33-dee8-a374051f85f6
title: XAudio2 Voices
ms.topic: article
ms.date: 05/31/2018
---

# XAudio2 Voices

There are three types of XAudio2 voice objects: *source*, *submix*, and *mastering* voices. Source voices operate on audio data provided by the client. Source and submix voices send their output to one or more submix or mastering voices. Submix and mastering voices mix the audio from all voices feeding them, and operate on the result. Mastering voices write audio data to an audio device.

## Actions Performed by All Voices

All voices perform the following actions in order on the audio that travels though them.

1.  Overall volume adjustment, affecting all audio channels. See [**IXAudio2Voice::SetVolume**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2voice-setvolume).
2.  An optional client-specified chain of one or more DSP effects, such as the built-in reverb or a user effect defined by the [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo) interface. See [XAudio2 Audio Effects](xaudio2-audio-effects.md).
3.  Per-channel output volume adjustment. See [**IXAudio2Voice::SetChannelVolumes**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2voice-setchannelvolumes).
4.  Separate matrix mix to each of the destination voices or to the audio output device for mastering voices. This mix changes the number of channels in the audio, if necessary.

## Source Voices

Use source voices to submit audio data into the XAudio2 processing pipeline. They are the entry points into the [XAudio2 Audio Graph](xaudio2-audio-graph.md). You must send voice data to a mastering voice to be heard, either directly or through intermediate submix voices.

In addition to the actions performed by all voices, source voices perform the following actions.

-   If necessary, a decoder runs first to convert encoded source data to Pulse Code Modulation (PCM).
-   A variable-rate sample rate conversion (SRC) converts the voice's source audio data to the sample rate expected by its destination voices, if necessary, and also supports dynamic pitch changes.
-   An optional state-variable filter can be used to color the sound in various ways. See [**IXAudio2Voice::SetFilterParameters**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2voice-setfilterparameters).
-   An optional filter can be applied to the voice's outputs. See [**IXAudio2Voice::SetOutputFilterParameters**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2voice-setoutputfilterparameters).

## Submix Voices

A submix voice is used primarily for performance improvements and effects processing. You cannot submit data buffers directly to submix voices. It will not be audible unless you submit it to a mastering voice. You can use a submix voice to ensure that a particular set of voice data is converted to the same format and to have a particular effect chain processed on the collective result.

In addition to the actions performed by all voices, submix voices perform the following actions.

-   A fixed-rate SRC runs on the voice's output, if necessary, to convert the audio to the sample rate expected by its destination voices.
-   An optional state-variable filter can be used to color the sound in various ways. See [**IXAudio2Voice::SetFilterParameters**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2voice-setfilterparameters).
-   An optional filter can be applied to the voice's outputs. See [**IXAudio2Voice::SetOutputFilterParameters**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2voice-setoutputfilterparameters).

## Mastering Voices

Use a mastering voice to represent the audio output device. You cannot submit data buffers directly to mastering voices, but data submitted to other types of voices must go to a mastering voice to be heard.

In addition to the actions performed by all voices, mastering voices perform the following actions.

-   If you create the mastering voice with an explicit *InputSampleRate* value that is not supported by the audio device, a fixed-rate SRC is used to convert to the closest sample rate supported by the device.
-   Clip the final output audio, if it is required by the output device.

## Related topics

<dl> <dt>

[Voices](voices.md)
</dt> <dt>

[XAudio2 Programming Guide](programming-guide.md)
</dt> <dt>

[**IXAudio2SourceVoice**](/windows/desktop/api/xaudio2/nn-xaudio2-ixaudio2sourcevoice)
</dt> <dt>

[**IXAudio2SubmixVoice**](/windows/desktop/api/xaudio2/nn-xaudio2-ixaudio2submixvoice)
</dt> <dt>

[**IXAudio2MasteringVoice**](/windows/desktop/api/xaudio2/nn-xaudio2-ixaudio2masteringvoice)
</dt> </dl>

 

 
