---
description: Encoder and Decoder Development
ms.assetid: 075aaf0f-63c6-4286-966e-fdc72d0acb6e
title: Encoder and Decoder Development
ms.topic: article
ms.date: 05/31/2018
---

# Encoder and Decoder Development

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

 

 



