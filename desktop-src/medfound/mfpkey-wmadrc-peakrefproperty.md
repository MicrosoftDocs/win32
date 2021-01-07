---
description: Specifies the highest volume level occurring in audio content.
ms.assetid: 177311c4-c348-4d38-8c8d-b6690643529c
title: MFPKEY_WMADRC_PEAKREF Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_WMADRC\_PEAKREF Property

Specifies the highest volume level occurring in audio content.

## Constant for IPropertyBag

g\_wszWMADRCPeakReference

## Data Type

VT\_I4

## Remarks

You can get this value from the encoder after the content is processed. This value can also be set on the decoder for dynamic range control.

For more information on dynamic range control, see the web article [Windows Media Audio Professional Codec Features](/previous-versions/ms867218(v=msdn.10)).

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

 

 
