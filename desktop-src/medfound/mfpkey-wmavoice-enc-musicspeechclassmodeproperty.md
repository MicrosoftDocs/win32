---
description: Specifies the mode of the voice codec.
ms.assetid: 8425cdab-e43c-41ca-9c20-09ab6a5f06f4
title: MFPKEY_WMAVOICE_ENC_MusicSpeechClassMode Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_WMAVOICE\_ENC\_MusicSpeechClassMode Property

Specifies the mode of the voice codec.

## Constant for IPropertyBag

g\_wszWMACMusicSpeechClassMode

## Data Type

VT\_I4

## Default Value

1

## Remarks

A value of 1 informs the codec that the content is voice-only, a value of 2 has the codec determine the mode automatically, and any other value informs the codec to use music mode.

If automatic mode is not encoding mixed voice and music properly, you can specify encoding for individual sections of the file by using the [MFPKEY\_WMAVOICE\_ENC\_EDL](mfpkey-wmavoice-enc-edlproperty.md) property.

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

 

 




