---
description: Specifies the overhead, in bytes per packet, required for the container used to store the compressed content.
ms.assetid: 73ec52de-c74a-45b3-a453-7f32510b4484
title: MFPKEY_ASFOVERHEADPERFRAME Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_ASFOVERHEADPERFRAME Property

Specifies the overhead, in bytes per packet, required for the container used to store the compressed content.

## Constant for IPropertyBag

g\_wszWMVPacketOverhead

## Data Type

VT\_I4

## Default Value

17

## Remarks

If you are using the Advanced Systems Format (ASF) file structure, do not change this value from its default. If you are not storing the data in an ASF file, you must set this value to 0.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Wmcodecdsp.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> </dl>

 

 




