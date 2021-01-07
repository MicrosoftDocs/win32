---
description: Why does a decoder not accept the input format that I set?
ms.assetid: 19aa5677-bc3f-41d7-ad64-7c75021d907b
title: Why does a decoder not accept the input format that I set?
ms.topic: article
ms.date: 05/31/2018
---

# Why does a decoder not accept the input format that I set?

There are many reasons why a decoder might reject a format. The most common is missing or incorrect extended format data. The extended format data is codec-specific information that is appended to the structure describing the media type.

When you enumerate an output type using an encoder object, the **pbFormat** member of the [**DMO\_MEDIA\_TYPE**](/previous-versions/windows/desktop/api/mediaobj/ns-mediaobj-dmo_media_type) structure will point to a **WAVEFORMATEX** structure. This structure has extended format data appended to it, and the size of that data is stored in the **WAVEFORMATEX.cbSize** member. Regardless of the container used to store the compressed data, you must persist the **WAVEFORMATEX** structure and use it in the input type for the decoder. Without the extended format data, the decoder cannot decompress the content.

For video formats, you must manually retrieve the extended format data and append it to the **VIDEOINFOHEADER** structure. For more information, see [Using Video Codec Private Data](usingvideocodecprivatedata.md).

## Related topics

<dl> <dt>

[Frequently Asked Questions](frequentlyaskedquestions.md)
</dt> </dl>

 

 
