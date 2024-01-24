---
description: MFPKEY_COMPLEXITYEX Property - Specifies the encoder algorithm complexity.
ms.assetid: abfc84d5-954f-4524-b3cb-5c5b9cfc7fa0
title: MFPKEY_COMPLEXITYEX Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_COMPLEXITYEX Property

Specifies the encoder algorithm complexity.

## Constant for IPropertyBag

g\_wszWMVCComplexityEx

## Data Type

VT\_I4

## Default Value

The default value depends on the version of the video encoder, as shown in the following table.



| Encoder version                 | Default value |
|---------------------------------|---------------|
| Windows Media Video 9 encoder   | 3             |
| Windows Media Video 7/8 encoder | 1             |



 

## Possible Values

The possible values depend on the version of the video encoder, as shown in the following table.



| Encoder version                 | Possible values  |
|---------------------------------|------------------|
| Windows Media Video 9 encoder   | 0, 1, 2, 3, 4, 5 |
| Windows Media Video 7/8 encoder | 0, 1             |



 

## Remarks

Lower values cause the codec to use less complicated encoding algorithms. Although the simpler algorithms produce lower-quality output, the encoding process is faster and requires less processing power. This can be important when encoding content from a live source because the encoder must process inputs fast enough to keep up with the source.

Any value assigned to this property will be ignored if the [MFPKEY\_COMPRESSIONOPTIMIZATIONTYPE](mfpkey-compressionoptimizationtypeproperty.md) property is set to 1. In that case, MFPKEY\_COMPLEXITYEX is automatically set to 3.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Wmcodecdsp.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> </dl>

 

 




