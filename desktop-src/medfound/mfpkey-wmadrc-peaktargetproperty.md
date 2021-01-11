---
description: Specifies the desired maximum volume level of output audio content.
ms.assetid: 231b7296-ca80-4918-bae6-674b976db24c
title: MFPKEY_WMADRC_PEAKTARGET Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_WMADRC\_PEAKTARGET Property

Specifies the desired maximum volume level of output audio content.

## Constant for IPropertyBag

g\_wszWMADRCPeakTarget

## Data Type

VT\_I4

## Default Value

See Remarks.

## Remarks

You can set this value on the decoder for the purpose of dynamic range control, but it will have an effect only if the [MFPKEY\_WMADEC\_DRCMODE](mfpkey-wmadec-drcmodeproperty.md) property is set.

If you request dynamic range control from the decoder when this property is not set, the codec will compute a default value.

Use the [MFPKEY\_WMADRC\_AVGREF](mfpkey-wmadrc-avgrefproperty.md) and [MFPKEY\_WMADRC\_PEAKREF](mfpkey-wmadrc-peakrefproperty.md) properties to compute appropriate values for this property.

For more information on dynamic range control, see the web article [Windows Media Audio Professional Codec Features](/previous-versions/ms867218(v=msdn.10)).

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

 

 
