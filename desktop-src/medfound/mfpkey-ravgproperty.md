---
description: Specifies the average bit rate, in bits per second, used for 2-pass, variable-bit-rate (VBR) encoding.
ms.assetid: 88a1888f-7bfb-4e24-9d48-92cfde02a14f
title: MFPKEY_RAVG Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_RAVG Property

Specifies the average bit rate, in bits per second, used for 2-pass, variable-bit-rate (VBR) encoding.

## Constant for IPropertyBag

g\_wszWMVCAvgBitrate

## Data Type

VT\_I4

## Remarks

In both constrained and unconstrained VBR, this value is the average bit rate across the duration of the content.

You must set this value for both modes of two-pass VBR encoding. After you begin processing samples, you must not query for this value until you are finished encoding the stream. The encoder interprets a request for this value as a signal that the encoding session is over; the next sample that you process is treated as the beginning of a new session.

This property can also be read at the end of a 1-pass VBR encoding session.

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

 

 




