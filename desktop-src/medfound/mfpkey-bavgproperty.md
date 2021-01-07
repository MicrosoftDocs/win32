---
description: Specifies the buffer window, in milliseconds, of a constrained variable-bit-rate (VBR) stream at its average bit rate (specified by MFPKEY\_RAVG).
ms.assetid: 7eabceb5-976e-4ebc-9042-9c203044634c
title: MFPKEY_BAVG Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_BAVG Property

Specifies the buffer window, in milliseconds, of a constrained variable-bit-rate (VBR) stream at its average bit rate (specified by [MFPKEY\_RAVG](mfpkey-ravgproperty.md)).

## Constant for IPropertyBag

g\_wszWMVCBAvg

## Data Type

VT\_I4

## Default Value

No default value, but the codec will compute an appropriate value based on the other constrained VBR settings.

## Remarks

This value is computed by the codec after the final encoding pass. You should not query for this value until after encoding is complete. The codec interprets a request for this value as a signal that the encoding session is over; the next sample that you process is treated as the beginning of a new session.

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

 

 




