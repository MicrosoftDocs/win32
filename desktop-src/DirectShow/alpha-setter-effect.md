---
description: Alpha Setter Effect
ms.assetid: dd3ab119-328b-4782-811a-f06909c17dec
title: Alpha Setter Effect
ms.topic: article
ms.date: 05/31/2018
---

# Alpha Setter Effect

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The Alpha Setter effect sets the alpha bits on a video image.

Class ID (CLSID): {506D89AE-909A-44f7-9444-ABD575896E35}

CLSID Variable Name: CLSID\_DxtAlphaSetter

Friendly Name: "DxtAlphaSetter"

### Properties



| Property  | Type   | Default | Description                                                 |
|-----------|--------|---------|-------------------------------------------------------------|
| Alpha     | BYTE   | -1      | Sets the alpha for the entire image.                        |
| AlphaRamp | double | -1.0    | Sets the alpha as a percentage of the original alpha value. |



 

## Remarks

A property with a negative value is ignored. Only one property can have a non-negative value. The Alpha property specifies a constant alpha value for every pixel in the image. This property overwrites the alpha values from the original image. The AlphaRamp property specifies each pixel's alpha value as a percentage of the pixel's original value, from 0.0 to 1.0.

## Related topics

<dl> <dt>

[Alpha Blending](alpha-blending.md)
</dt> </dl>

 

 



