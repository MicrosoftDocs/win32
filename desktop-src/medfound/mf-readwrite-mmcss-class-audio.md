---
description: Specifies a Multimedia Class Scheduler Service (MMCSS) class for audio-processing threads in the Source Reader or Sink Writer.
ms.assetid: F1B8A8C8-2E41-4321-A94D-C50447C69941
title: MF_READWRITE_MMCSS_CLASS_AUDIO attribute (Mfreadwrite.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_READWRITE\_MMCSS\_CLASS\_AUDIO attribute

Specifies a [Multimedia Class Scheduler Service](../procthread/multimedia-class-scheduler-service.md) (MMCSS) class for audio-processing threads in the Source Reader or Sink Writer.

## Data type

**LPWSTR**

## Get/set

To get this attribute, call [**IMFAttributes::GetString**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getstring).

To set this attribute, call [**IMFAttributes::SetString**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setstring).

## Remarks

Optionally set this attribute when you create an instance of the [Source Reader](source-reader.md) or [Sink Writer](sink-writer.md). The value of the attribute must be a valid MMCSS class name.

If this attribute is set, the Source Reader or Sink Writer registers its audio-processing threads with the specified MMCSS class. The MMCSS ensures that data processing in the Source Reader or Sink Writer has priority over other system tasks.

To specify the base priority for audio threads, set the [MF\_READWRITE\_MMCSS\_PRIORITY\_AUDIO](mf-readwrite-mmcss-priority-audio.md) attribute. If that attribute is not set, the base priority for audio threads is zero.

This attribute overrides the [MF\_READWRITE\_MMCSS\_CLASS](mf-readwrite-mmcss-class.md) attribute for audio-processing threads. If neither attribute is set, audio threads are not registered with MCSS.

For most applications, audio glitching is much more noticeable to the user than video glitching, and therefore less acceptable. For this reason, an application should typically set MF\_READWRITE\_MMCSS\_CLASS\_AUDIO to a higher-priority MMCSS class than [MF\_READWRITE\_MMCSS\_CLASS](mf-readwrite-mmcss-class.md). This ensures that audio processing is given higher priority than other tasks.

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

 

 
