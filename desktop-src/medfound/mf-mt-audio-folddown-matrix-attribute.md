---
description: Specifies how an audio decoder should transform multichannel audio to stereo output. This process is also called fold-down.
ms.assetid: 6dfe2b97-1ebc-4954-b478-85b3bbba89e3
title: MF_MT_AUDIO_FOLDDOWN_MATRIX attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_MT\_AUDIO\_FOLDDOWN\_MATRIX attribute

Specifies how an audio decoder should transform multichannel audio to stereo output. This process is also called *fold-down*.

## Data type

Byte array

## Remarks

This attribute applies to audio media types.

The value of this attribute is an [**MFFOLDDOWN\_MATRIX**](/windows/desktop/api/mfapi/ns-mfapi-mffolddown_matrix) structure.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps \| UWP apps\]<br/>                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps \| UWP apps\]<br/>                        |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFAttributes::GetBlob**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getblob)
</dt> <dt>

[**IMFAttributes::SetBlob**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setblob)
</dt> <dt>

[**IMFMediaType**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediatype)
</dt> <dt>

[Media Type Attributes](media-type-attributes.md)
</dt> </dl>

 

 




