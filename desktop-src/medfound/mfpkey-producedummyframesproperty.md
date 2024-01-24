---
description: Specifies whether the encoder produces dummy frame entries in the bit stream for duplicate frames.
ms.assetid: dc09cecb-98c0-40bb-9e5d-f4661bf98522
title: MFPKEY_PRODUCEDUMMYFRAMES Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_PRODUCEDUMMYFRAMES Property

Specifies whether the encoder produces dummy frame entries in the bit stream for duplicate frames.

## Constant for IPropertyBag

g\_wszWMVCProduceDummyFrames

## Data Type

VT\_BOOL

## Default Value

VARIANT\_FALSE

## Remarks

If this value is VARIANT\_FALSE, the codec will not put any data in the bit stream for duplicate frames.

Dummy frames can be important in applications where frame numbers are persisted. A common example is when SMPTE time codes are maintained for encoded content.

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

 

 




