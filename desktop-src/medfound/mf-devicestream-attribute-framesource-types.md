---
description: Represents the frame source type.
ms.assetid: 4A2B427E-E654-48BA-8BF4-16F1B1F8D266
title: MF_DEVICESTREAM_ATTRIBUTE_FRAMESOURCE_TYPES attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_DEVICESTREAM\_ATTRIBUTE\_FRAMESOURCE\_TYPES attribute

Represents the frame source type.

## Data type

**UINT32**

## Remarks

This value of this attribute should be a bitmask of one or more values from the [**MFFrameSourceTypes**](/windows/desktop/api/mfapi/ne-mfapi-mfframesourcetypes) enumeration. To support backward compatibility, when this attribute is not defined for a media type, it is assumed to have the value **MFFrameSourceTypes::Color**.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1607 \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



 

 




