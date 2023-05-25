---
description: Calculating Parameter Values
ms.assetid: cc3c26ed-a007-4350-99be-0ebd94953689
title: Calculating Parameter Values
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Calculating Parameter Values

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Potentially, an input buffer could be very large. Ideally, when the DMO processes the buffer, the parameters will exactly follow their curves throughout the entire batch of data. However, a DMO has some leeway in how it calculates those values.

-   The most accurate approach is to calculate the exact value for every atomic unit of data; for example, each audio sample. This approach is the most computationally expensive.
-   Another approach is to slice the data into smaller units of some fixed size, such as 100 samples. This approach creates a "stair-stepping" effect. For some parameters, that might be acceptable. In audio effects, it might create audible artifacts.
-   A compromise is to use the previous technique, but within each batch, perform a linear interpolation of the parameter value for each sample.

These issues are especially important for audio processing. One second of audio might contain 48,000 audio samples per channel, which is a lot of calculations to perform, yet the ear is sensitive to artifacts such as aliasing.

## Related topics

<dl> <dt>

[Media Parameters](media-parameters.md)
</dt> </dl>

 

 



