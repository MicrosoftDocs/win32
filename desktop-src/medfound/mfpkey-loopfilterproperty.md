---
description: Specifies whether the codec should use the in-loop deblocking filter during encoding.
ms.assetid: 395a356a-5f58-46b4-b2ff-47f98106f487
title: MFPKEY_LOOPFILTER Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_LOOPFILTER Property

Specifies whether the codec should use the in-loop deblocking filter during encoding.

## Constant for IPropertyBag

g\_wszWMVCLoopFilter

## Data Type

VT\_BOOL

## Remarks

The in-loop filter is a deblocking method that is applied during both encoding and decoding, to reduce blocking artifacts at encoding time ("in the loop") so that future P-frames and B-frames don't carry them forward.

The effect of applying the in-loop filter is that the edges of the macro-blocks in the output video frames are less noticeable. At the same time the image can become softer in appearance.

Although the in-loop filter can lead to reduced image detail in some frames, the overall video quality will benefit noticeably. The biggest disadvantage to using in-loop filtering is the additional decoding performance cost.

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

 

 




