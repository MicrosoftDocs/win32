---
description: Specifies the cost method used by the codec to determine which macroblock mode to use.
ms.assetid: 2ba9b943-0daa-40c1-87ea-2fa647fb7095
title: MFPKEY_MACROBLOCKMODECOSTMETHOD Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_MACROBLOCKMODECOSTMETHOD Property

Specifies the cost method used by the codec to determine which macroblock mode to use.

## Constant for IPropertyBag

g\_wszWMVCMacroblockModeCostMethod

## Data Type

VT\_I4

## Default Value

0

## Remarks

This property may be set to one of the following values.



| Value | Method used                                                                                            |
|-------|--------------------------------------------------------------------------------------------------------|
| 0     | SAD/Hadamard. This option configures the codec to use only distortion when computing cost.             |
| 1     | RD cost. This option configures the codec to account for both rate and distortion when computing cost. |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Wmcodecdsp.h</dt> </dl> |



## See also

<dl> <dt>

[MFPKEY\_MOTIONMATCHMETHOD](mfpkey-motionmatchmethodproperty.md)
</dt> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> </dl>

 

 




