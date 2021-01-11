---
description: Specifies whether the H.264 video remux MFT should mark I pictures as clean point for better seek-ability. This has the potential for corruptions on seeks in non-conforming final MP4 files.
ms.assetid: BB521E13-40A4-4643-B071-76B8CBC62074
title: MFT_REMUX_MARK_I_PICTURE_AS_CLEAN_POINT attribute (Mftransform.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFT\_REMUX\_MARK\_I\_PICTURE\_AS\_CLEAN\_POINT attribute

Specifies whether the H.264 video remux MFT should mark I pictures as clean point for better seek-ability. This has the potential for corruptions on seeks in non-conforming final MP4 files.

## Data type

**Bool** stored as **UINT32**

## Remarks

Clean point picture should be compressed IDR pictures by definition.

This is not recommended for recording or remuxing MP4 files, unless such an exercise is to produce some intermediate pseudo MP4 files for video editing.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps \| UWP apps\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps \| UWP apps\]<br/>                             |
| Header<br/>                   | <dl> <dt>Mftransform.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Mftransform.idl</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> </dl>

 

 




