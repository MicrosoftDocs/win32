---
Description: 'Sets the base priority for audio-processing threads created by the Source Reader or Sink Writer.'
ms.assetid: 'C0E3A472-959F-4F74-8906-03630DE4CB8C'
title: 'MF\_READWRITE\_MMCSS\_PRIORITY\_AUDIO attribute'
---

# MF\_READWRITE\_MMCSS\_PRIORITY\_AUDIO attribute

Sets the base priority for audio-processing threads created by the Source Reader or Sink Writer.

## Data type

**INT32** stored as **UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](imfattributes-getuint32.md).

To set this attribute, call [**IMFAttributes::SetUINT32**](imfattributes-setuint32.md).

## Remarks

Optionally set this attribute when you create an instance of the [Source Reader](source-reader.md) or [Sink Writer](sink-writer.md). If you set this attribute, also set the [MF\_READWRITE\_MMCSS\_CLASS\_AUDIO](mf-readwrite-mmcss-class-audio.md) attribute. Otherwise, this attribute is ignored.

When the Source Reader or Sink Writer registers audio-processing threads with the [Multimedia Class Scheduler Service](base.multimedia_class_scheduler_service), the value of this attribute specifies the base thread priority. If this attribute is not set, the default value is zero.

## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps \| UWP apps\]<br/>                              |
| Header<br/>                   | <dl> <dt>Mfreadwrite.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> </dl>

 

 




