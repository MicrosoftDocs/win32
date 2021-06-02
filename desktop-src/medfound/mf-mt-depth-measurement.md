---
description: A value that defines the measurement system for a depth value in a video frame.
ms.assetid: 7BFA846B-E614-4117-A196-298E065CB7F8
title: MF_MT_DEPTH_MEASUREMENT attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_MT\_DEPTH\_MEASUREMENT attribute

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

A value that defines the measurement system for a depth value in a video frame.

## Data type

**UINT32**

## Remarks

This value is a member of the [**\_MFDepthMeasurement**](/windows/win32/api/mfapi/ne-mfapi-mfdepthmeasurement) enumeration

If this attribute is not present it is assumed to be **DistanceToFocalPlane**. The distance to focal plane is typically easier to consume in a 3D Euclidian coordinate system.

![illustration of distancetofocalplane](images/distance-to-focal-plane.png)

The distance to focal center format is typically raw data from sensor such as time of flight cameras.

![illustration of distancetoopticalcenter](images/distance-to-optical-center.png)

Depth cameras cannot sense the depth of all pixels. When the confidence of a pixel is low, because of material, occlusion, or out of range etc, the depth value on that pixel can be invalid.

When a depth pixel value is 0, the pixel is invalid.

Some depth cameras attach bitmask metadata for each pixel in addition to the depth value to represent the reason why the depth of pixel is invalid, due to material, occlusion or out of range etc. We recommend that you avoid attaching such metadata as bits in depth value, because it will typically lead to difficulty when using such values in pixel shader. Instead. we recommend that you use a separate 8bit image buffer with same resolution and attach it as attribute of the [**IMFSample**](/windows/desktop/api/mfobjects/nn-mfobjects-imfsample). Such metadata varies for each camera vendor and is not standardized by the platform. We recommend using full 16 bits for the depth value for easier processing downstream and using a fixed value such as 0 for invalidation.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709 \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows Server, version 1709 \[desktop apps only\]<br/>                      |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



 

 




