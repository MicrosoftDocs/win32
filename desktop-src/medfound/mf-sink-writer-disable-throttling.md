---
Description: Specifies whether the sink writer limits the rate of incoming data.
ms.assetid: eb79bda7-ece0-4977-a0f9-d40bd5d220ab
title: MF\_SINK\_WRITER\_DISABLE\_THROTTLING attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_SINK\_WRITER\_DISABLE\_THROTTLING attribute

Specifies whether the sink writer limits the rate of incoming data.

## Data type

**UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getuint32?branch=master).

To set this attribute, call [**IMFAttributes::SetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setuint32?branch=master).

## Remarks

By default, the sink writer's [**IMFSinkWriter::WriteSample**](/windows/win32/mfreadwrite/nf-mfreadwrite-imfsinkwriter-writesample?branch=master) method limits the data rate by blocking the calling thread. This prevents the application from delivering samples too quickly. To disable this behavior, set the MF\_SINK\_WRITER\_DISABLE\_THROTTLING attribute to **TRUE** when you create the sink writer.

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

 

 




