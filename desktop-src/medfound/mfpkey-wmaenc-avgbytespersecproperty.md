---
description: Specifies the average bytes per second in a quality-based variable-bit-rate (VBR) audio stream.
ms.assetid: dcee969a-617e-4045-a468-8158afb06356
title: MFPKEY_WMAENC_AVGBYTESPERSEC Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_WMAENC\_AVGBYTESPERSEC Property

Specifies the average bytes per second in a quality-based variable-bit-rate (VBR) audio stream.

## Constant for IPropertyBag

g\_wszWMACAvgBytesPerSecond

## Data Type

VT\_I4

## Remarks

You can get this value from the decoder after the stream is encoded.

This value is required by the audio decoder to properly decompress the content.

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

 

 




