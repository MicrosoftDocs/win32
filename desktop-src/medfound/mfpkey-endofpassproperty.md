---
description: Specifies the end of an encoding pass.
ms.assetid: 8a7e6e09-766c-4346-8893-eea5614b2aa4
title: MFPKEY_ENDOFPASS Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_ENDOFPASS Property

Specifies the end of an encoding pass.

## Data Type

**VT\_BOOL**

## Constant for IPropertyBag

g\_wszWMVCEndOfPass

## Data Type for IPropertyBag

No data type is required. To set this property, pass an uninitialized **VARIANT**.

## Remarks

This property is not a normal property because it has the same effect regardless of whether the value is VARIANT\_TRUE or VARIANT\_FALSE. You must set this property after you process the last input samples for a preprocessing pass. If you are performing multiple passes, you must set this property at the end of each preprocessing pass (at present none of the codecs supports more than one). If you do not set this property, the codec will assume that you are still passing samples for preprocessing.

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

 

 




