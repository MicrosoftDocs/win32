---
description: Specifies the buffer window, in milliseconds, of a constrained variable-bit-rate (VBR) stream at its peak bit rate (specified by MFPKEY\_RMAX).
ms.assetid: ef27b179-4d9b-4ce7-867a-f62b0f9b735d
title: MFPKEY_BMAX Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_BMAX Property

Specifies the buffer window, in milliseconds, of a constrained variable-bit-rate (VBR) stream at its peak bit rate (specified by [MFPKEY\_RMAX](mfpkey-rmaxproperty.md)).

## Constant for IPropertyBag

g\_wszWMVCBMax

## Data Type

VT\_I4

## Default Value

No default.

## Remarks

You must set this value for peak-constrained VBR encoding. After you begin processing samples, you must not query for this value until you are finished encoding the stream. The codec interprets a request for this value as a signal that the encoding session is over; the next sample that you process is treated as the beginning of a new session.

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

 

 




