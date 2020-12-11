---
title: Cross-fade effect
description: This effect combines two images by adding weighted pixels from input images. It has two inputs, named Destination and Source.
ms.assetid: 5214b70a-d024-ba3e-771f-07d98d2278ba
ms.topic: article
ms.date: 05/31/2018
---

# Cross-fade effect

This effect combines two images by adding weighted pixels from input images. It has two inputs, named Destination and Source.

The cross fade formula is **output = weight \* Destination + (1 - weight) \* Source**.

The CLSID for this effect is CLSID\_D2D1CrossFade.

## Effect properties

| Display name and index enumeration             | Type and default value | Description                                                                                                                                                                                                                                                       |
|------------------------------------------------|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WeightD2D1\_CROSSFADE\_PROP\_WEIGHT<br/> | FLOAT0.5f<br/>   | How much to weigh the source image color values versus the destination image. The minimum value is 0.0f (exclusively use the destination image to determine the output) and the maximum value is 1.0f (exclusively use the source image to determine the output). |



 

## Requirements



| Requirement | Value |
|--------------------------|---------------------------------------------------|
| Minimum supported client | Windows 10 \[desktop apps \| Windows Store apps\] |
| Minimum supported server | Windows 10 \[desktop apps \| Windows Store apps\] |
| Header                   | d2d1effects\_2.h                                  |
| Library                  | d2d1.lib, dxguid.lib                              |

## Related topics

* [ID2D1Effect interface](/windows/desktop/api/d2d1_1/nn-d2d1_1-id2d1effect)
