---
description: A value that defines the units for a depth value in a video frame.
ms.assetid: 0D7238F3-C224-48BD-8654-B3182DFB244C
title: MF_MT_DEPTH_VALUE_UNIT attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_MT\_DEPTH\_VALUE\_UNIT attribute

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

A value that defines the units for a depth value in a video frame.

## Data type

**UINT64**

## Remarks

The unit value is a UINT64 value in nanometers, in the range 1e - 9 meters. If this value is not present, the default value of the unit is 1e-3, which indicates each pixel level is measured in 1 millimeter in physical space.

Depth cameras cannot sense the depth of all pixels. When the confidence of a pixel is low, because of material, occlusion, or out of range etc, the depth value on that pixel can be invalid.

When a depth pixel value is 0, the pixel is invalid.

Some depth cameras attach bitmask metadata for each pixel in addition to the depth value to represent the reason why the depth of pixel is invalid, due to material, occlusion or out of range etc. We recommend that you avoid attaching such metadata as bits in depth value, because it will typically lead to difficulty when using such values in pixel shader. Instead. we recommend that you use a separate 8bit image buffer with same resolution and attach it as attribute of the [**IMFSample**](/windows/desktop/api/mfobjects/nn-mfobjects-imfsample). Such metadata varies for each camera vendor and is not standardized by the platform. We recommend using full 16 bits for the depth value for easier processing downstream and using a fixed value such as 0 for invalidation.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709 \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows Server, version 1709 \[desktop apps only\]<br/>                      |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



 

 




