---
description: Specifies the method used to encode the motion vector information.
ms.assetid: 22ffdb77-9266-42e5-be41-fc7457141bba
title: MFPKEY_DELTAMVRANGEINDEX Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_DELTAMVRANGEINDEX Property

Specifies the method used to encode the motion vector information.

## Constant for IPropertyBag

g\_wszWMVCDeltaMVRangeIndex

## Data Type

VT\_I4

## Default Value

0

## Remarks

If this property is set, the encoder increases the delta motion vector range in fields. Motion vector information is valid only for interlaced fields.

This property may be set to one of the following values:



| Value | Description                                                                          |
|-------|--------------------------------------------------------------------------------------|
| 0     | Use the existing delta motion vector range.                                          |
| 1     | Double the delta motion vector range in the horizontal direction.                    |
| 2     | Double the delta motion vector range in the vertical direction.                      |
| 3     | Double the delta motion vector range in both the horizontal and vertical directions. |



 

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

 

 




