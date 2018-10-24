---
Description: Contains the MPEG-1 or MPEG-2 sequence header for a video media type.
ms.assetid: 17b7f76c-404c-4aa9-9746-1488fee027f2
title: MF_MT_MPEG_SEQUENCE_HEADER attribute
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MF\_MT\_MPEG\_SEQUENCE\_HEADER attribute

Contains the MPEG-1 or MPEG-2 sequence header for a video media type.

## Data type

Byte array

## Remarks

This attribute corresponds to the **dwSequenceHeader** member of the [**MPEG2VIDEOINFO**](https://msdn.microsoft.com/en-us/library/Dd390707(v=VS.85).aspx) structure, or the **bSequenceHeader** member of the [**MPEG1VIDEOINFO**](https://msdn.microsoft.com/en-us/library/Dd390700(v=VS.85).aspx) structure.

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

[**IMFAttributes::GetBlob**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getblob)
</dt> <dt>

[**IMFAttributes::SetBlob**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setblob)
</dt> <dt>

[**IMFMediaType**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediatype)
</dt> <dt>

[Media Type Attributes](media-type-attributes.md)
</dt> </dl>

 

 




