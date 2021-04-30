---
description: Specifies whether the codec should attempt to detect noisy frame edges and remove them.
ms.assetid: fdb4f3a8-1447-4e1e-a208-0f9b717f7626
title: MFPKEY_NOISEEDGEREMOVAL Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_NOISEEDGEREMOVAL Property

Specifies whether the codec should attempt to detect noisy frame edges and remove them.

## Constant for IPropertyBag

g\_wszWMVCNoiseEdgeRemoval

## Data Type

VT\_BOOL

## Default Value

FALSE

## Remarks

A noisy frame edge is usually the vertical blanking interval (VBI) data from a frame of broadcast television. The VBI is the first 21 scan lines of the television frame. These scan lines do not contain video data—they contain data about the broadcast. When a television signal is recorded by a capture card, the VBI is usually removed from the frame. The noisy edge detection and correction performed by the codec can only correct an edge that has three or fewer lines of noise. If captured video contains more than three noisy lines, there is a problem with the hardware used to capture the video.

If the codec is set to remove noisy edges, it duplicates lines adjacent to the noisy edge to fill in the frame.

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

 

 




