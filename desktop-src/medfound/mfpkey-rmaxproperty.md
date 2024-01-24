---
description: Specifies the peak bit rate, in bits per second, used for constrained 2-pass variable-bit-rate (VBR) playback.
ms.assetid: 51f161d2-f832-48d5-8f16-861e2a98a7f7
title: MFPKEY_RMAX Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_RMAX Property

Specifies the peak bit rate, in bits per second, used for constrained 2-pass variable-bit-rate (VBR) playback.

## Constant for IPropertyBag

g\_wszWMVCMaxBitrate

## Data Type

VT\_I4

## Default Value

No default.

## Remarks

This value represents the peak bit rate for playback. The value of [MFPKEY\_BMAX](mfpkey-bmaxproperty.md) is used to describe the buffer in terms of this bit rate; in effect, constrained VBR is similar to constant bit rate (CBR) using this value as the bit rate. However, a constrained VBR stream can be played back at a lower bit rate, as long as the buffer is increased.

You must set this value for peak-constrained two-pass VBR encoding. After you begin processing samples, you must not query for this value until you are finished encoding the stream. The encoder interprets a request for this value as a signal that the encoding session is over; the next sample that you process is treated as the beginning of a new session.

Typically, this value is two to three times greater than the value of [MFPKEY\_RAVG](mfpkey-ravgproperty.md).

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

 

 




