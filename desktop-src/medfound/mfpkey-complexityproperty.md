---
description: MFPKEY_COMPLEXITY Property - Specifies the encoder algorithm complexity.
ms.assetid: 1537e98b-d7ed-49e6-aa25-8f2f124c88eb
title: MFPKEY_COMPLEXITY Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_COMPLEXITY Property

\[[**MFPKEY\_COMPLEXITY**](mfpkey-complexityexproperty.md) is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, use **MFPKEY\_COMPLEXITYEX**.\]

Specifies the encoder algorithm complexity.

## Constant for IPropertyBag

g\_wszWMVCComplexityMode

## Data Type

VT\_I4

## Default Value

The default value depends on the version of the video encoder, as shown in the following table.



| Encoder version                 | Default value |
|---------------------------------|---------------|
| Windows Media Video 9 encoder   | 3             |
| Windows Media Video 7/8 encoder | 1             |



 

## Remarks

This integer value ranges from 0 to 3. Lower values cause the codec to use less complicated encoding algorithms. Although the simpler algorithms produce lower-quality output, the encoding process is faster and requires less processing power.

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

 

 




