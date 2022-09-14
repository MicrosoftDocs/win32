---
title: Point-specular lighting effect
description: Use the point-specular lighting effect to create an image that appears to be a reflective surface.
ms.assetid: 89E22FD0-BB7F-465F-A79C-056CA9F14F5D
keywords:
- point specular lighting effect
ms.topic: article
ms.date: 05/31/2018
---

# Point-specular lighting effect

Use the point-specular lighting effect to create an image that appears to be a reflective surface. The effect uses the alpha channel of the image as a height map and a point light source that you position, and calculates the reflection and light according to the specular portion of the Phong lighting model.

The color of the output bitmap is a result of light color, light position, and the surface geometry. The alpha channel output for each pixel with specular lighting is the maximum of the red, green, and blue channel outputs for that pixel.

The CLSID for this effect is CLSID\_D2D1PointSpecular.

-   [Example image](#example-image)
-   [Point light source](#point-light-source)
-   [Height map and normal vector](#height-map-and-normal-vector)
-   [Specular lighting constant and exponent](#specular-lighting-constant-and-exponent)
-   [Effect properties](#effect-properties)
-   [Scales modes](#scales-modes)
-   [Requirements](#requirements)
-   [Related topics](#related-topics)

## Example image

The example here shows the input and output images of the point-specular lighting effect.

![effect example screenshot that shows the input and output images of the point specular lighting effect.](images/point-spec-example.png)

Specular light refers to light that is reflected in a specific direction according to the Phong lighting model.

![a diagram of the vectors used to cacluate a specular lighting output for a bitmap.](images/point-spec-reflected1.png)

The effect calculates the final output pixel values using the equations here:

![the equations for calculating the final pixel values. ](images/point-spec-formula-output.png)

where<dl> k? = specular lighting constant.  
![the surface normal unit vector symbol.](images/point-spec-mathchar-n.png)= surface normal unit vector which is a function of x and y. See [Height map and normal vector](#height-map-and-normal-vector) for the calculations.  
![the halfway unit vector symbol.](images/point-spec-mathchar-h.png)= "halfway" unit vector between eye unit vector and light unit vector. See [Point light source](#point-light-source) for the calculations.  
L<sub>r</sub>, L<sub>g</sub>, L<sub>b</sub> = the light color in RGB components.  
</dl>

You set the specular lighting constant as the *SpecularConstant* property and the light color as the *Color* property.

## Point light source

A point light source emits light in all directions like in the image here.

![a point light emitting light in all directions.](images/point-spec-light.png)

You set the position of the light source using the *LightPosition* property. The effect calculates the light vector, L   , for a point light source using the equations here:

![the light vector equation.](images/point-spec-formula3.png)

where Light?, Light<sub>y</sub>, and Light<sub>z</sub> are the input light position. The effect calculates the halfway vector, ![halfway vector symbol.](images/point-spec-mathchar-h.png) as defined in the Phong lighting model, using the equation here. The lighting model assumes that the eye vector, ![the eye vector symbol](images/point-spec-mathchar-e.png), is located at (0,0,1).

![halfway vector equation.](images/point-spec-formula4.png)

Both L and H are normalized to unit-length vectors.

## Height map and normal vector

The effect generates a height map for the input image based on its alpha channel.

The height (Z) component is calculated using the equation:

![the equation for calculating the height (z) of the surface.](images/point-spec-formula6.png)

The effect calculates the surface normal, ![the normal vector symbol.](images/point-spec-mathchar-n.png), for the input bitmap using a Sobel gradient.

## Specular lighting constant and exponent

Specular light represents the light that is reflected from the surface of the of the image height map. You specify the *SpecularExponent* property that determines the amount of specular reflection from the bitmap.

Larger exponents represent shinier objects and reflect light in a more focused shape.

The *SpecularConstant* property K? defines the amount of reflected light as a ratio of the incoming light.

## Effect properties



| Display name and index enumeration                                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LightPosition<br/> D2D1\_POINTSPECULAR\_PROP\_LIGHT\_POSITION<br/>         | The light position of the point light source. The property is a D2D1\_VECTOR\_3F defined as (x, y, z). The units are in device-independent pixels (DIPs) and the values are unitless and unbounded. The type is D2D1\_VECTOR\_3F.<br/> The default value is {0.0f, 0.0f, 0.0f}.<br/>                                                                                                                                                                                      |
| SpecularExponent<br/> D2D1\_POINTSPECULAR\_PROP\_SPECULAR\_EXPONENT<br/>   | The exponent for the specular term in the Phong lighting equation. A larger value corresponds to a more reflective surface. This value is unitless and must be between 1.0 and 128. The type is FLOAT.<br/> The default value is 1.0f.<br/>                                                                                                                                                                                                                               |
| SpecularConstant<br/> D2D1\_POINTSPECULAR\_PROP\_SPECULAR\_CONSTANT<br/>   | The ratio of specular reflection to the incoming light. The value is unitless and must be between 0 and 10,000. The type is FLOAT.<br/> The default value is 1.0f.<br/>                                                                                                                                                                                                                                                                                                   |
| SurfaceScale<br/> D2D1\_POINTSPECULAR\_PROP\_SURFACE\_SCALE<br/>           | The scale factor in the Z direction for generating a height map. The value is unitless and must be between 0 and 10,000. The type is FLOAT.<br/> The default value is 1.0f.<br/>                                                                                                                                                                                                                                                                                          |
| Color<br/> D2D1\_POINTSPECULAR\_PROP\_COLOR<br/>                           | The color of the incoming light. This property is exposed as a D2D1\_VECTOR\_3F   (R, G, B) and used to compute L<sub>R</sub>, L<sub>G</sub>, L<sub>B</sub>. The type is D2D1\_VECTOR\_3F.<br/> The default value is {1.0f, 1.0f, 1.0f}.<br/>                                                                                                                                                                                                                             |
| KernelUnitLength<br/> D2D1\_POINTSPECULAR\_PROP\_KERNEL\_UNIT\_LENGTH<br/> | The size of an element in the Sobel kernel used to generate the surface normal in the X and Y directions. This property maps to the dx and dy values in the Sobel gradient. This property is a D2D1\_VECTOR\_2F(Kernel Unit Length X, Kernel Unit Length Y) and is defined in (DIPs/Kernel Unit). The effect uses bilinear interpolation to scale the bitmap to match size of kernel elements. The type is D2D1\_VECTOR\_2F.<br/> The default value is {1.0f, 1.0f}.<br/> |
| ScaleMode<br/> D2D1\_POINTSPECULAR\_PROP\_SCALE\_MODE<br/>                 | The interpolation mode the effect uses to scale the image to the corresponding kernel unit length. There are six scale modes that range in quality and speed. See [Scale modes](#scales-modes) for more info. <br/> The type is D2D1\_POINTSPECULAR\_SCALE\_MODE.<br/> The default value is D2D1\_POINTSPECULAR\_SCALE\_MODE\_LINEAR.<br/>                                                                                                                          |



 

## Scales modes



| Enumeration                                             | Description                                                                                                                                                                                          |
|---------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| D2D1\_POINTSPECULAR\_SCALE\_MODE\_NEAREST\_NEIGHBOR     | Samples the nearest single point and uses that. This mode uses less processing time, but outputs the lowest quality image.                                                                           |
| D2D1\_POINTSPECULAR\_SCALE\_MODE\_LINEAR                | Uses a four point sample and linear interpolation. This mode outputs a higher quality image than nearest neighbor.                                                                                   |
| D2D1\_POINTSPECULAR\_SCALE\_MODE\_CUBIC                 | Uses a 16 sample cubic kernel for interpolation. This mode uses the most processing time, but outputs a higher quality image.                                                                        |
| D2D1\_POINTSPECULAR\_SCALE\_MODE\_MULTI\_SAMPLE\_LINEAR | Uses 4 linear samples within a single pixel for good edge anti-aliasing. This mode is good for scaling down by small amounts on images with few pixels.                                              |
| D2D1\_POINTSPECULAR\_SCALE\_MODE\_ANISOTROPIC           | Uses anisotropic filtering to sample a pattern according to the transformed shape of the bitmap.                                                                                                     |
| D2D1\_POINTSPECULAR\_SCALE\_MODE\_HIGH\_QUALITY\_CUBIC  | Uses a variable size high quality cubic kernel to perform a pre-downscale the image if downscaling is involved in the transform matrix. Then uses the cubic interpolation mode for the final output. |



 

> [!Note]  
> If you don't select a mode, the effect defaults to D2D1\_POINTSPECULAR\_SCALE\_MODE\_LINEAR.

## Requirements



| Requirement | Value |
|--------------------------|------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 and Platform Update for Windows 7 \[desktop apps \| Windows Store apps\] |
| Minimum supported server | Windows 8 and Platform Update for Windows 7 \[desktop apps \| Windows Store apps\] |
| Header                   | d2d1effects.h                                                                      |
| Library                  | d2d1.lib, dxguid.lib                                                               |



 

## Related topics

<dl> <dt>

[**ID2D1Effect**](/windows/win32/api/d2d1_1/nn-d2d1_1-id2d1effect)
</dt> </dl>

 

