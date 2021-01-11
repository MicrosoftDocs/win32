---
description: Specifies whether the codec will use the noise filter when encoding.
ms.assetid: 9e099378-bb77-4dca-9171-7fe58e0139de
title: MFPKEY_DENOISEOPTION Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_DENOISEOPTION Property

Specifies whether the codec will use the noise filter when encoding.

## Constant for IPropertyBag

g\_wszWMVCDenoiseOption

## Data Type

VT\_BOOL

## Default Value

FALSE

## Remarks

The noise filter can improve the quality of noisy video sources, such as film containing lots of grain or video shot in low light. This filter can be used in live encoding scenarios where external preprocessing is not an option.

This filter should be disabled for clean video sources since it can reduce image quality when the quality is good to start with.

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

 

 




