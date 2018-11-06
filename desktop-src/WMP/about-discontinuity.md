---
title: About Discontinuity
description: About Discontinuity
ms.assetid: 29210758-a1e6-47f2-9428-38f79623fbca
keywords:
- Windows Media Player plug-ins,audio DSP
- plug-ins,audio DSP
- digital signal processing plug-ins,audio discontinuity
- DSP plug-ins,audio discontinuity
- audio DSP plug-ins,discontinuity
ms.topic: article
ms.date: 05/31/2018
---

# About Discontinuity

At any time, Windows Media Player can signal a break in the input stream by calling the **IMediaObject::Discontinuity** method. This occurs routinely at the start and end of a stream, and also prior to each seek operation or when streaming content is interrupted for any reason. The sample DSP plug-in that the Windows Media Player Plug-in wizard generates does not need to deal with discontinuities for the following reasons:

-   PCM samples are atomic, meaning they can be processed without regard to the other samples in the stream. Some video formats contain data that depends on key frames and compressed samples.
-   The sample code is written to always force the client to process all output before the plug-in will accept more input.

The default implementation of **IMediaObject::Discontinuity** simply returns S\_OK.

## Related topics

<dl> <dt>

[**Implementing an Audio DSP Plug-in**](implementing-an-audio-dsp-plug-in.md)
</dt> </dl>

 

 




