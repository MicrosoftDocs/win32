---
description: Specifies the quality of the output.
ms.assetid: 7b45633b-7f1c-4951-a462-ad6240b9ca31
title: MFPKEY_WMRESAMP_FILTERQUALITY Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_WMRESAMP\_FILTERQUALITY Property

Specifies the quality of the output.

## Constant for IPropertyBag

Available only by using [**IPropertyStore**](/windows/win32/api/propsys/nn-propsys-ipropertystore).

## Data Type

VT\_I4

## Applies To

-   [Audio Resampler DSP](audioresampler.md)

## Remarks

The valid range of this property is 1 to 60, inclusive. Higher values produce higher-quality output, but introduce more latency. A value of 1 is essentially the same as linear interpolation.

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

 

 
