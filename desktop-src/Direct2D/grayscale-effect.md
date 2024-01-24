---
title: Grayscale effect
description: Converts an image to monochromatic gray.
ms.assetid: 4e0b26ed-ba71-5f8f-db1e-f1b4e28fbd11
ms.topic: article
ms.date: 05/31/2018
---

# Grayscale effect

Converts an image to monochromatic gray.

Grayscale uses the color matrix effect to convert to grayscale, using the following matrix:

![conversion matrix](images/grayscale-effect-matrix.png)

The CLSID for this effect is CLSID\_D2D1Grayscale.

-   [Example Image](#example-image)
-   [Effect Properties](#effect-properties)
-   [Requirements](#requirements)
-   [Related topics](#related-topics)

## Example image

![example of effect output](images/grayscale-effect.png)

## Effect properties

This effect has no properties.

## Requirements



| Requirement | Value |
|--------------------------|---------------------------------------------------|
| Minimum supported client | Windows 10 \[desktop apps \| Windows Store apps\] |
| Minimum supported server | Windows 10 \[desktop apps \| Windows Store apps\] |
| Header                   | d2d1effects\_2.h                                  |
| Library                  | d2d1.lib, dxguid.lib                              |


## Related topics

* [ID2D1Effect interface](/windows/desktop/api/d2d1_1/nn-d2d1_1-id2d1effect)
