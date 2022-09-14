---
description: Specifies the maximum number of passes supported by the encoder.
ms.assetid: 7e21cd0f-f13f-4321-b246-f1adaa5c6094
title: MFPKEY_PASSESRECOMMENDED Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_PASSESRECOMMENDED Property

Specifies the maximum number of passes supported by the encoder. Read-only.

## Constant for IPropertyBag

g\_wszWMVCPassesRecommended, g\_wszWMCPMaxPasses

## Data Type

VT\_I4

## Remarks

You can get the value of this property calling [IWMCodecProps::GetCodecProp](/windows/desktop/api/wmcodecdsp/nf-wmcodecdsp-iwmcodecprops-getcodecprop). If you use **IPropertyBag**, you must first set the FOURCC value of the desired compressed format by using the [MFPKEY\_FOURCC](mfpkey-fourccproperty.md) property.

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

 

 




