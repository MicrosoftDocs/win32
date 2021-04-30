---
description: Specifies a Multimedia Class Scheduler Service (MMCSS) class for the Source Reader or Sink Writer.
ms.assetid: A3A295E8-AC9C-4641-ADDA-B97D5AB13A9A
title: MF_READWRITE_MMCSS_CLASS attribute (Mfreadwrite.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_READWRITE\_MMCSS\_CLASS attribute

Specifies a [Multimedia Class Scheduler Service](../procthread/multimedia-class-scheduler-service.md) (MMCSS) class for the Source Reader or Sink Writer.

## Data type

**LPWSTR**

## Get/set

To get this attribute, call [**IMFAttributes::GetString**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getstring).

To set this attribute, call [**IMFAttributes::SetString**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setstring).

## Remarks

Optionally set this attribute when you create an instance of the [Source Reader](source-reader.md) or [Sink Writer](sink-writer.md). The value of the attribute must be a valid MMCSS class name.

If this attribute is set, the Source Reader or Sink Writer registers all of its threads with the specified MMCSS class. The MMCSS ensures that data processing in the Source Reader or Sink Writer has priority over other system tasks.

To specify the base priority, set the [MF\_READWRITE\_MMCSS\_PRIORITY](mf-readwrite-mmcss-priority.md) attribute. If that attribute is not set, the base priority is zero.

For audio-processing threads, the [MF\_READWRITE\_MMCSS\_CLASS\_AUDIO](mf-readwrite-mmcss-class-audio.md) attribute (if set) overrides this attribute.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps \| UWP apps\]<br/>                              |
| Header<br/>                   | <dl> <dt>Mfreadwrite.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> </dl>

 

 
