---
description: Specifies the desired average volume level of output audio content.
ms.assetid: 2e59537f-ee14-4186-b312-297225e91120
title: MFPKEY_WMADRC_AVGTARGET Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_WMADRC\_AVGTARGET Property

Specifies the desired average volume level of output audio content.

## Constant for IPropertyBag

g\_wszWMADRCAverageTarget

## Data Type

VT\_I4

## Default Value

See Remarks.

## Remarks

You can set this value on the decoder for the purpose of dynamic range control, but it will have an effect only if the [MFPKEY\_WMADEC\_DRCMODE](mfpkey-wmadec-drcmodeproperty.md) property is set.

> [!Note]  
> Setting the average target value is not recommended. Adjusting the average value does not affect the difference between loud and soft sounds. Instead, it cuts or boosts the overall average volume which may cause undesirable distortion during playback.

 

If you request dynamic range control from the decoder when this property is not set, the codec will compute a default value.

Use the [MFPKEY\_WMADRC\_AVGREF](mfpkey-wmadrc-avgrefproperty.md) and [MFPKEY\_WMADRC\_PEAKREF](mfpkey-wmadrc-peakrefproperty.md) properties to compute appropriate values for this property.

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

 

 




