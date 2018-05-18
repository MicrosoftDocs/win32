---
Description: 'Specifies whether the sink writer limits the rate of incoming data.'
ms.assetid: 'eb79bda7-ece0-4977-a0f9-d40bd5d220ab'
title: 'MF\_SINK\_WRITER\_DISABLE\_THROTTLING attribute'
---

# MF\_SINK\_WRITER\_DISABLE\_THROTTLING attribute

Specifies whether the sink writer limits the rate of incoming data.

## Data type

**UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](imfattributes-getuint32.md).

To set this attribute, call [**IMFAttributes::SetUINT32**](imfattributes-setuint32.md).

## Remarks

By default, the sink writer's [**IMFSinkWriter::WriteSample**](imfsinkwriter-writesample.md) method limits the data rate by blocking the calling thread. This prevents the application from delivering samples too quickly. To disable this behavior, set the MF\_SINK\_WRITER\_DISABLE\_THROTTLING attribute to **TRUE** when you create the sink writer.

Use this attribute with the following functions:

-   [**MFCreateSinkWriterFromMediaSink**](mfcreatesinkwriterfrommediasink.md)
-   [**MFCreateSinkWriterFromURL**](mfcreatesinkwriterfromurl.md)

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

 

 




