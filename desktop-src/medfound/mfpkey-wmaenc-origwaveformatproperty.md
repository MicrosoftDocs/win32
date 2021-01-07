---
description: Specifies the WAVEFORMATEX structure describing the input audio content.
ms.assetid: d424f243-5ad6-46f2-b99b-9bb780715e8a
title: MFPKEY_WMAENC_ORIGWAVEFORMAT Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_WMAENC\_ORIGWAVEFORMAT Property

Specifies the [**WAVEFORMATEX**](/previous-versions/dd757713(v=vs.85)) structure describing the input audio content.

## Constant for IPropertyBag

g\_wszWMACOriginalWaveFormat

## Data Type

VT\_ARRAY \| VT\_UI1 ([**WAVEFORMATEX**](/previous-versions/dd757713(v=vs.85)) as an array of bytes)

## Remarks

When transcoding Windows Media Audio-based content to a lower bit rate, you can pass the [**WAVEFORMATEX**](/previous-versions/dd757713(v=vs.85)) structure of the content to the codec to enable the codec to optimize its algorithms. This feature, called smart recompression, provides better results than decompressing the content and then feeding the reconstructed PCM samples back through the codec.

When passing the [**WAVEFORMATEX**](/previous-versions/dd757713(v=vs.85)) structure, include any extra bytes at the end of the structure specified by **WAVEFORMATEX.cbSize**.

The audio encoder accepts only inputs and outputs for which the number of channels, bits per sample, and sample rate are identical. You can transcode content only to a lower bit rate within those parameters. In any case, you must decode the content and pass the uncompressed samples as input to the encoder. Setting this property gives the encoder some information about the processing that has already been performed on the content.

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

 

 
