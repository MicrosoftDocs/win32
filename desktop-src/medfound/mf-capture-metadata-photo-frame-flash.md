---
description: Indicates if a flash was triggered for the captured frame.
ms.assetid: CF900CB4-8967-40F3-B60C-867192A641E9
title: MF_CAPTURE_METADATA_PHOTO_FRAME_FLASH attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_CAPTURE\_METADATA\_PHOTO\_FRAME\_FLASH attribute

Indicates if a flash was triggered for the captured frame.

## Data type

**UINT32**



| Value                                                                               | Meaning                                                                                                                                               |
|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>0</dt> </dl>        | A flash was not triggered on this frame.<br/>                                                                                                   |
| <dl> <dt>non-zero</dt> </dl> | A flash was triggered on this frame.<br/>                                                                                                       |
| <dl> <dt>1</dt> </dl>        | Reserved<br/> Do not explicitly check for a value of 1. Applications should only check for !=0 to indicate if a flash was triggered.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                            |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> </dl>

 

 




