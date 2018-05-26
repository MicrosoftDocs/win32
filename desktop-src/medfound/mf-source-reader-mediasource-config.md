---
Description: Contains configuration properties for the Source Reader.
ms.assetid: f7e5ef6a-5fc3-4f39-acc0-61ce79030211
title: MF\_SOURCE\_READER\_MEDIASOURCE\_CONFIG attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_SOURCE\_READER\_MEDIASOURCE\_CONFIG attribute

Contains configuration properties for the [Source Reader](source-reader.md).

## Data type

**IPropertyStore\*** stored as **IUnknown\***

## Get/set

To get this attribute, call [**IMFAttributes::GetUnknown**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getunknown?branch=master).

To set this attribute, call [**IMFAttributes::SetUnknown**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setunknown?branch=master).

## Remarks

The value of this attribute is a pointer to the **IPropertyStore** interface of a property store. You can use this attribute to pass configuration properties to the media source.

Use this attribute with the following functions:

-   [**MFCreateSourceReaderFromByteStream**](/windows/win32/mfreadwrite/nf-mfreadwrite-mfcreatesourcereaderfrombytestream?branch=master)
-   [**MFCreateSourceReaderFromURL**](/windows/win32/mfreadwrite/nf-mfreadwrite-mfcreatesourcereaderfromurl?branch=master)

Internally, the source reader passes the **IPropertyStore** pointer to the source resolver. For more information, see [Configuring a Media Source](configuring-a-media-source.md).

## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps \| UWP apps\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps \| UWP apps\]<br/>                           |
| Header<br/>                   | <dl> <dt>Mfreadwrite.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Source Reader](source-reader.md)
</dt> <dt>

[Source Reader Attributes](source-reader-attributes.md)
</dt> </dl>

 

 




