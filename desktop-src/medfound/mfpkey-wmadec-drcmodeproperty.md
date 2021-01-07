---
description: Specifies the dynamic range control mode that the audio decoder will use.
ms.assetid: 0dbe0c40-39ac-4c1b-9da2-9b142b5bb0eb
title: MFPKEY_WMADEC_DRCMODE Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_WMADEC\_DRCMODE Property

Specifies the dynamic range control mode that the audio decoder will use.

## Constant for IPropertyBag

g\_wszWMACDRCSetting

## Data Type

VT\_I4

## Default Value

0

## Remarks

This integer value ranges from 0 to 2. The greater the value, the smaller the dynamic range of the uncompressed audio output. A value of 0 signals the codec to perform no dynamic range control, that is, the codec will not alter the inherent dynamic range of the encoded content.

If this value is set to 1 or 2, the codec will use the following properties to determine the needed dynamic range control:

-   [MFPKEY\_WMADRC\_AVGREF](mfpkey-wmadrc-avgrefproperty.md)
-   [MFPKEY\_WMADRC\_PEAKREF](mfpkey-wmadrc-peakrefproperty.md)
-   [MFPKEY\_WMADRC\_AVGTARGET](mfpkey-wmadrc-avgtargetproperty.md)
-   [MFPKEY\_WMADRC\_PEAKTARGET](mfpkey-wmadrc-peaktargetproperty.md)

If you do not provide target values, the codec will provide its own.

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

 

 




