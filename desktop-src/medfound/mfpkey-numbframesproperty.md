---
description: Specifies the number of bidirectional predictive frames (B-frames).
ms.assetid: 8bd95baa-c130-4616-8ab7-7d902162e4ed
title: MFPKEY_NUMBFRAMES Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_NUMBFRAMES Property

Specifies the number of bidirectional predictive frames (B-frames).

## Constant for IPropertyBag

g\_wszWMVCNumBFrames

## Data Type

VT-I4

## Default Value

0

## Remarks

By default, Windows Media Video 9 uses only intraframes (I-frames), also known as key frames or anchor frames, which are fully encoded frames, and predictive frames (P-frames), which are encoded as a difference from the previous I-frame. B-frames are different from P-frames because they store both the differences from the previous frame and the differences from the following frame.

When you configure the codec to uses B-frames, it will use the specified number of B-frames between each pair of frames of either I or P type.

For example, if a sequence of frames without B-frames is "IPPPPPPPPI" then the same sequence encoding with two B-frames would be "IBBPBBPBBI".

For most content either one or two B-frames are appropriate. At higher data rates, one B-frame is normally the optimal choice. Three or more are rarely useful.

The valid range of values for this property is 0 to 7.

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

 

 




