---
title: About the Sample Audio DSP Plug-in
description: About the Sample Audio DSP Plug-in
ms.assetid: e60b055b-77e6-470e-91f6-9882827cf238
keywords:
- Windows Media Player plug-ins,samples
- plug-ins,samples
- digital signal processing plug-ins,samples
- DSP plug-ins,samples
- Windows Media Player plug-ins,audio DSP
- plug-ins,audio DSP
- digital signal processing plug-ins,audio samples
- DSP plug-ins,audio samples
- samples,DSP plug-ins
- audio DSP plug-ins,samples
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# About the Sample Audio DSP Plug-in

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The sample audio DSP plug-in provides a simple processing implementation that scales the amplitude of the audio by a factor provided by the user in the property page. The plug-in accepts values between zero and 1. The default value is 1. A value of 1 has no effect upon the sound; other scale factors are multipliers for the audio samples. For instance, a value of .5 would result in a 6 decibel decrease in volume. A value of zero results in silence.

The sample audio DSP plug-in works with stereo or mono PCM audio.

## Related topics

<dl> <dt>

[**Building a DSP Plug-in**](building-a-dsp-plug-in.md)
</dt> </dl>

 

 




