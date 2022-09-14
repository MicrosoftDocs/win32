---
description: Specifies the delta increase between the picture quantizer of the anchor frame and the picture quantizer of the B-frame.
ms.assetid: 8ab9401b-6fed-4178-955f-2e0bf950bf60
title: MFPKEY_BDELTAQP Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_BDELTAQP Property

Specifies the delta increase between the picture quantizer of the anchor frame and the picture quantizer of the B-frame.

## Constant for IPropertyBag

g\_wszWMVCBDeltaQP

## Data Type

VT\_I4

## Default Value

0

## Remarks

Picture quantizer (QP) is a measurement of how compressed a frame is. Higher values represent higher compression ratios. The QP can be set in half-point increments. A B-frame is typically compressed at a QP the same as or 0.5 higher than the anchor frame's QP. By specifying a B-frame QP delta higher than 0, it is possible to compress B-frames at an even higher compression ratio.

The B-frame delta QP can be set only in whole-point increments. This property must be set to an integer value from 0 to 31. The recommended value is 1.

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

 

 




