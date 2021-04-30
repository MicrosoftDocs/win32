---
description: Specifies the portions of content to be encoded as music by the voice codec.
ms.assetid: c63034ce-33d7-4f2f-9498-fc16e25b6d4d
title: MFPKEY_WMAVOICE_ENC_EDL Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_WMAVOICE\_ENC\_EDL Property

Specifies the portions of content to be encoded as music by the voice codec.

## Constant for IPropertyBag

g\_wszWMACVoiceBuffer

## Data Type

VT\_BSTR

## Default Value

No default value. If this property is not set, the codec will use the value of the [MFPKEY\_WMAVOICE\_ENC\_MusicSpeechClassMode](mfpkey-wmavoice-enc-musicspeechclassmodeproperty.md) property to determine how to encode the content.

## Remarks

You can use this property if the automatic mode of the codec is not giving satisfactory results.

This value is a comma-delimited string containing at least four integers. The first integer is the version number; always use 1 for this value. The second integer is the number of sections that need to be encoded as music. Following the second integer are a number of pairs of values representing ranges in milliseconds, one pair for each section of content that needs to be encoded as music.

For example, "1,2,100,200,500,600" informs the encoder to use version 1 with 2 sections of music. The first music section starts at 100 ms and ends at 200 ms. The second music section starts at 500 ms and ends at 600 ms.

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

 

 




