---
Description: Specifies how an audio decoder should transform multichannel audio to stereo output. This process is also called fold-down.
ms.assetid: 6dfe2b97-1ebc-4954-b478-85b3bbba89e3
title: MF\_MT\_AUDIO\_FOLDDOWN\_MATRIX attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_MT\_AUDIO\_FOLDDOWN\_MATRIX attribute

Specifies how an audio decoder should transform multichannel audio to stereo output. This process is also called *fold-down*.

## Data type

Byte array

## Remarks

This attribute applies to audio media types.

The value of this attribute is an [**MFFOLDDOWN\_MATRIX**](/windows/win32/mfapi/ns-mfapi-_mffolddown_matrix?branch=master) structure.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps \| UWP apps\]<br/>                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps \| UWP apps\]<br/>                        |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFAttributes::GetBlob**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getblob?branch=master)
</dt> <dt>

[**IMFAttributes::SetBlob**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setblob?branch=master)
</dt> <dt>

[**IMFMediaType**](/windows/win32/mfobjects/nn-mfobjects-imfmediatype?branch=master)
</dt> <dt>

[Media Type Attributes](media-type-attributes.md)
</dt> </dl>

 

 




