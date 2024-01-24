---
title: Using the Echo Sample DSP Plug-in
description: Using the Echo Sample DSP Plug-in
ms.assetid: 62e393a4-0787-40e2-8693-678971a25fbf
keywords:
- Windows Media Player plug-ins,Echo sample testing
- plug-ins,Echo sample testing
- digital signal processing plug-ins,Echo sample testing
- DSP plug-ins,Echo sample testing
- Echo DSP plug-in sample,testing
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Using the Echo Sample DSP Plug-in

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

When you create an error-free build of your Windows Media Player echo DSP plug-in, you can use it in Windows Media Player to hear the effect. When you start Windows Media Player, the plug-in should be enabled by default. If you play audio or video with audio, you should hear a one-second echo in the sound that plays at the same volume as the original sound.

You can experiment with different delay times and effects levels by changing the values in the echo plug-in property page. Try the effect on different types of source material, such as music or speech. A delay time of 200 ms with an effects level of 30 will result in a tightly spaced echo that sounds like the effect used on early rock and roll recordings. Effects levels greater than 50 will result in the original signal being lower in volume than the echo, which is called a pre-echo effect.

## Related topics

<dl> <dt>

[**The Echo Sample**](the-echo-sample.md)
</dt> </dl>

 

 




