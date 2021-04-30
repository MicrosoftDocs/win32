---
description: Working with DMO Media Types
ms.assetid: 1aaf7554-1a5f-439a-afb1-a031607e1a1e
title: Working with DMO Media Types
ms.topic: article
ms.date: 05/31/2018
---

# Working with DMO Media Types

The input and output media types that are used by the codec DMOs are defined using the [**DMO\_MEDIA\_TYPE**](/previous-versions/windows/desktop/api/mediaobj/ns-mediaobj-dmo_media_type) structure. This structure is identical to both [**WM\_MEDIA\_TYPE**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wm_media_type), which is defined in the Windows Media Format SDK, and [**AM\_MEDIA\_TYPE**](/windows/win32/api/strmif/ns-strmif-am_media_type), which is defined in Microsoft DirectShow®. Depending upon your application, you may use variables defined as any one of these three types. It is safe to cast a pointer to one of the media type structures as another. For example:


```
    DMO_MEDIA_TYPE MediaType;
    WM_MEDIA_TYPE* pMedia = NULL;
    pMedia = (WM_MEDIA_TYPE*)&MediaType;
```



The format types that are used by the codecs are generally limited to those described by the **VIDEOINFOHEADER** and **WAVEFORMATEX** structures. For convenience, constants for these format types are included in the wmcodecconst.h header file. The constant names are WMCFORMAT\_VideoInfo and WMCFORMAT\_WaveFormatEx respectively. The audio codecs can work with the **WAVEFORMATEXTENSIBLE** structure in some circumstances, and must use it in others. However, **DMO\_MEDIA\_TYPE.formattype** is set to the same value as it is for **WAVEFORMATEX**. For more information about using **WAVEFORMATEXTENSIBLE**, see [Using High-Definition Audio](usinghighdefinitionaudio.md).

> [!Note]  
>    You must include the format type structure used as the encoder output in whatever container you use to store the compressed data. The decoders require the original format structure to decompress the content. In addition to the members of the structure, compressed Windows Media Audio and Video types require additional format information, which is appended to the structure. For more information, see [Working with Audio](workingwithaudio.md) and [Working with Video](workingwithvideo.md).

 

## Related topics

<dl> <dt>

[Working with Codec DMOs](workingwithcodecdmos.md)
</dt> </dl>

 

 
