---
description: Specifies the average volume level of audio content.
ms.assetid: eabb36ff-300f-4ed1-aca3-9415627ac1a7
title: MFPKEY_WMADRC_AVGREF Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_WMADRC\_AVGREF Property

Specifies the average volume level of audio content.

## Constant for IPropertyBag

g\_wszWMADRCAverageReference

## Data Type

VT\_I4

## Remarks

You can get this value from the encoder after the content is processed. This value can also be set on the decoder for the purpose of dynamic range control, but it will have an effect only if the [MFPKEY\_WMADEC\_DRCMODE](mfpkey-wmadec-drcmodeproperty.md) property is set.

For more information on dynamic range control see the web article [Windows Media Audio Professional Codec Features](/previous-versions/ms867218(v=msdn.10)).

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

 

 
