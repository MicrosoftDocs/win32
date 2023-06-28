---
description: Encoder and Decoder Development
ms.assetid: 075aaf0f-63c6-4286-966e-fdc72d0acb6e
title: Encoder and Decoder Development
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Encoder and Decoder Development

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This section contains articles about encoder and decoder development for DirectShow. These topics are not relevant for application developers.

A software decoder that supports DirectX Video Acceleration (VA) must be implemented as a DirectShow copy transform filter. If the decoder does not support DirectX VA, it can also be implemented as a DirectX Media Object (DMO). A decoder that connects to a video renderer should not be implemented as a trans-in-place filter, because this will result in significant performance degradation. For information on how to write a copy transform filter, see [Writing Transform Filters](writing-transform-filters.md).

Software encoders can be implemented as either transform filters or DMOs. Encoders do not use DirectX VA, since DirectX VA currently is only used for decompression. The Encoder API specification described in this section is relevant for both hardware and software encoders.

This section contains the following topics:

-   [Encoder API](encoder-api.md)
-   [Decoder Interfaces and Specifications](decoder-interfaces-and-specifications.md)
-   [Decoder Settings for Windows Media Center Edition](decoder-settings-for-windows-media-center-edition.md)

## Related topics

<dl> <dt>

[Using the VMR for DirectShow Filter Developers](using-the-vmr-for-directshow-filter-developers.md)
</dt> </dl>

 

 



