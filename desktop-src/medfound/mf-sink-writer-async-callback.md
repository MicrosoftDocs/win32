---
Description: Contains a pointer to the applications callback interface for the sink writer.
ms.assetid: 22df1fa0-469d-4501-aaf0-a0379b7ed096
title: MF\_SINK\_WRITER\_ASYNC\_CALLBACK attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_SINK\_WRITER\_ASYNC\_CALLBACK attribute

Contains a pointer to the application's callback interface for the sink writer.

## Data type

**[**IMFSinkWriterCallback**](/windows/win32/mfreadwrite/nn-mfreadwrite-imfsinkwritercallback?branch=master)\*** stored as **IUnknown\***

## Get/set

To get this attribute, call [**IMFAttributes::GetUnknown**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getunknown?branch=master).

To set this attribute, call [**IMFAttributes::SetUnknown**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setunknown?branch=master).

## Remarks

The value of this attribute is a pointer to the application's [**IMFSinkWriterCallback**](/windows/win32/mfreadwrite/nn-mfreadwrite-imfsinkwritercallback?branch=master) interface.

Use this attribute with the following functions:

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
</dt> </dl>

 

 




