---
description: Specifies a numeric representation of the tradeoff between motion smoothness and image quality of codec output.
ms.assetid: 63915450-71c5-4097-91d7-5817249c1cda
title: MFPKEY_CRISP Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_CRISP Property

Specifies a numeric representation of the tradeoff between motion smoothness and image quality of codec output.

## Constant for IPropertyBag

g\_wszWMVCCrisp

## Data Type

VT\_I4

## Default Value

75

## Remarks

This integer value can range from 0 to 100. The higher the value, the more the codec will optimize encoding for the image quality of individual frames, which usually reduces motion smoothness.

This property should be set only for constant-bit-rate (CBR) encoding. The optimizations for variable-bit-rate (VBR) encoding work differently.

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

 

 




