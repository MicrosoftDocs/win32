---
Description: Contains a pointer to the applications callback interface for the Source Reader.
ms.assetid: de226a5a-03c0-4bfe-bb20-8969ce43cf53
title: MF\_SOURCE\_READER\_ASYNC\_CALLBACK attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_SOURCE\_READER\_ASYNC\_CALLBACK attribute

Contains a pointer to the application's callback interface for the [Source Reader](source-reader.md).

## Data type

**IMFSourceReaderCallback\*** stored as **IUnknown\***

## Get/set

To get this attribute, call [**IMFAttributes::GetUnknown**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getunknown?branch=master).

To set this attribute, call [**IMFAttributes::SetUnknown**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setunknown?branch=master).

## Remarks

The value of this attribute is a pointer to the application's [**IMFSourceReaderCallback**](/windows/win32/mfreadwrite/nn-mfreadwrite-imfsourcereadercallback?branch=master) interface.

Use this attribute with the following functions:

-   [**MFCreateSourceReaderFromByteStream**](/windows/win32/mfreadwrite/nf-mfreadwrite-mfcreatesourcereaderfrombytestream?branch=master)
-   [**MFCreateSourceReaderFromMediaSource**](/windows/win32/mfreadwrite/nf-mfreadwrite-mfcreatesourcereaderfrommediasource?branch=master)
-   [**MFCreateSourceReaderFromURL**](/windows/win32/mfreadwrite/nf-mfreadwrite-mfcreatesourcereaderfromurl?branch=master)

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

 

 




