---
Description: Enables or disables format conversions by the source reader or sink writer.
ms.assetid: 282b70c3-c81c-47dd-bfa2-7e77138ccb91
title: MF\_READWRITE\_DISABLE\_CONVERTERS attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_READWRITE\_DISABLE\_CONVERTERS attribute

Enables or disables format conversions by the source reader or sink writer.

## Data type

**UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getuint32?branch=master).

To set this attribute, call [**IMFAttributes::SetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setuint32?branch=master).

## Remarks

By default, the source reader and sink writer can perform some format conversions on uncompressed audio and video streams. To disable this behavior, set this attribute to **TRUE** when you create the source reader or sink writer.

Use this attribute with the following functions:

-   [**MFCreateSourceReaderFromByteStream**](/windows/win32/mfreadwrite/nf-mfreadwrite-mfcreatesourcereaderfrombytestream?branch=master)
-   [**MFCreateSourceReaderFromMediaSource**](/windows/win32/mfreadwrite/nf-mfreadwrite-mfcreatesourcereaderfrommediasource?branch=master)
-   [**MFCreateSourceReaderFromURL**](/windows/win32/mfreadwrite/nf-mfreadwrite-mfcreatesourcereaderfromurl?branch=master)
-   [**MFCreateSinkWriterFromMediaSink**](/windows/win32/mfreadwrite/nf-mfreadwrite-mfcreatesinkwriterfrommediasink?branch=master)
-   [**MFCreateSinkWriterFromURL**](/windows/win32/mfreadwrite/nf-mfreadwrite-mfcreatesinkwriterfromurl?branch=master)

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

[Sink Writer Attributes](sink-writer-attributes.md)
</dt> <dt>

[Source Reader Attributes](source-reader-attributes.md)
</dt> </dl>

 

 




