---
description: Specifies whether the decoder should perform Lt-Rt fold down.
ms.assetid: ce1dc4ea-4326-40ab-bb30-ff1a34f06d79
title: MFPKEY_WMADEC_LTRTOUTPUT Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_WMADEC\_LTRTOUTPUT Property

Specifies whether the decoder should perform Lt-Rt fold down.

## Constant for IPropertyBag

Available only by using [**IPropertyStore**](/windows/win32/api/propsys/nn-propsys-ipropertystore).

## Data Type

**VT\_BOOL**

## Default Value

**VARIANT\_FALSE**

## Remarks

If this property has a value of VARIANT\_FALSE and the output is stereo, the audio decoder uses simple channel fold down. If this property has a value of VARIANT\_TRUE, the audio decoder performs Lt-Rt (matrixed) fold down to stereo, and then any Dolby Surround decoder can be used to decode the matrixed surround . For example, the audio decoder could perform Lt-Rt fold down on 5.1 or 7.1 content.

This property is supported only when the decoder is acting as a DirectX Media Object (DMO). No fold down of any kind is supported when the decoder is acting as a Media Foundation Transform (MFT).

On Windows Vista, if you obtain an **IPropertyStore** interface on an audio decoder, the decoder acts as an MFT. Consequently, this property cannot be used on Windows Vista. For information on when a decoder acts as a DMO or an MFT, see the individual codec reference pages under [Codec Objects](codecobjects.md).

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

 

 
