---
title: 3D perspective transform effect
description: Use the 3D perspective transform effect to rotate the image in 3 dimensions as if viewed from a distance.
ms.assetid: 0E1A940E-2DCA-4772-BB68-7E5EF5CEF833
keywords:
- 3d perspective transform effect
ms.topic: article
ms.date: 05/31/2018
---

# 3D perspective transform effect

Use the 3D perspective transform effect to rotate the image in 3 dimensions as if viewed from a distance.

The 3D perspective transform is more convenient than the 3D transform effect, but only exposes a subset of the functionality. You can compute a full 3D transformation matrix and apply a more arbitrary transform matrix to an image using the [3D transform](3d-transform.md) effect.

The CLSID for this effect is CLSID\_D2D13DPerspectiveTransform.

-   [Example image](#example-image)
-   [Effect properties](#effect-properties)
-   [Interpolation modes](#interpolation-modes)
-   [Border modes](#border-modes)
-   [Output bitmap](#output-bitmap)
-   [Requirements](#requirements)
-   [Related topics](#related-topics)

## Example image



| Before                                                               |
|----------------------------------------------------------------------|
| ![the image before the effect.](images/default-before.jpg)           |
| After                                                                |
| ![the image after the effect.](images/23-3dperspectivetransform.png) |



 


```C++
ComPtr<ID2D1Effect> perspectiveTransformEffect;
m_d2dContext->CreateEffect(CLSID_D2D13DPerspectiveTransform, &perspectiveTransformEffect);

perspectiveTransformEffect->SetInput(0, bitmap);

perspectiveTransformEffect->SetValue(D2D1_3DPERSPECTIVETRANSFORM_PROP_PERSPECTIVE_ORIGIN, D2D1::Vector3F(0.0f, 192.0f, 0.0f));
perspectiveTransformEffect->SetValue(D2D1_3DPERSPECTIVETRANSFORM_PROP_ROTATION, D2D1::Vector3F(0.0f, 30.0f, 0.0f));

m_d2dContext->BeginDraw();
m_d2dContext->DrawImage(perspectiveTransformEffect.Get());
m_d2dContext->EndDraw();
```



## Effect properties



| Display name and index enumeration                                                              | Description                                                                                                                                                                                                                                                                                        |
|-------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| InterpolationMode<br/> D2D1\_3DPERSPECTIVETRANSFORM\_PROP\_INTERPOLATION\_MODE<br/> | The interpolation mode the effect uses on the image. There are 5 scale modes that range in quality and speed.<br/> Type is D2D1\_3DPERSPECTIVETRANSFORM\_INTERPOLATION\_MODE.<br/> Default value is D2D1\_3DPERSPECTIVETRANSFORM\_INTERPOLATION\_MODE\_LINEAR.<br/>              |
| BorderMode<br/> D2D1\_3DPERSPECTIVETRANSFORM\_PROP\_BORDER\_MODE<br/>               | The mode used to calculate the border of the image, soft or hard. See [Border modes](https://www.bing.com/search?q=Border+modes) for more info.<br/> Type is D2D1\_BORDER\_MODE.<br/> Default value is D2D1\_BORDER\_MODE\_SOFT.<br/>                                                              |
| Depth<br/> D2D1\_3DPERSPECTIVETRANSFORM\_PROP\_DEPTH<br/>                           | The distance from the *PerspectiveOrigin* to the projection plane. The value specified in DIPs and must be greater than 0.<br/> Type is FLOAT.<br/> Default value is 1000.0f.<br/>                                                                                               |
| PerspectiveOrigin<br/> D2D1\_3DPERSPECTIVETRANSFORM\_PROP\_PERSPECTIVE\_ORIGIN<br/> | The X and Y location of the viewer in the 3D scene. This property is a D2D1\_VECTOR\_2F defined as: (point X, point Y). The units are in DIPs.<br/> You set the Z value with the *Depth* property.<br/> Type is D2D1\_VECTOR\_2F.<br/> Default value is {0.0f, 0.0f}.<br/> |
| LocalOffset<br/> D2D1\_3DPERSPECTIVETRANSFORM\_PROP\_LOCAL\_OFFSET<br/>             | A translation the effect performs before it rotates the projection plane. This property is a D2D1\_VECTOR\_3F defined as: (X, Y, Z). The units are in DIPs.<br/> Type is D2D1\_VECTOR\_3F.<br/> Default value is {0.0f, 0.0f, 0.0f}.<br/>                                        |
| GlobalOffset<br/> D2D1\_3DPERSPECTIVETRANSFORM\_PROP\_GLOBAL\_OFFSET<br/>           | A translation the effect performs after it rotates the projection plane. This property is a D2D1\_VECTOR\_3F defined as: (X, Y, Z). The units are in DIPs.<br/> Type is D2D1\_VECTOR\_3F.<br/> Default value is {0.0f, 0.0f, 0.0f}.<br/>                                         |
| RotationOrigin<br/> D2D1\_3DPERSPECTIVETRANSFORM\_PROP\_ROTATION\_ORIGIN<br/>       | The center point of the rotation the effect performs. This property is a D2D1\_VECTOR\_3F defined as: (X, Y, Z). The units are in DIPs.<br/> Type is D2D1\_VECTOR\_3F.<br/> Default value is {0.0f, 0.0f, 0.0f}.<br/>                                                            |
| Rotation<br/> D2D1\_3DPERSPECTIVETRANSFORM\_PROP\_ROTATION<br/>                     | The angles of rotation for each axis. This property is a D2D1\_VECTOR\_3F defined as: (X, Y, Z). The units are in degrees.<br/> Type is D2D1\_VECTOR\_3F.<br/> Default value is {0.0f, 0.0f, 0.0f}.<br/>                                                                         |



 

## Interpolation modes



| Enumeration                                                              | Description                                                                                                                                                |
|--------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| D2D1\_3DPERSPECTIVETRANSFORM\_INTERPOLATION\_MODE\_NEAREST\_NEIGHBOR     | Samples the nearest single point and uses that. This mode uses less processing time, but outputs the lowest quality image.                                 |
| D2D1\_3DPERSPECTIVETRANSFORM\_INTERPOLATION\_MODE\_LINEAR                | Uses a four point sample and linear interpolation. This mode uses more processing time than the nearest neighbor mode, but outputs a higher quality image. |
| D2D1\_3DPERSPECTIVETRANSFORM\_INTERPOLATION\_MODE\_CUBIC                 | Uses a 16 sample cubic kernel for interpolation. This mode uses the most processing time, but outputs a higher quality image.                              |
| D2D1\_3DPERSPECTIVETRANSFORM\_INTERPOLATION\_MODE\_MULTI\_SAMPLE\_LINEAR | Uses 4 linear samples within a single pixel for good edge anti-aliasing. This mode is good for scaling down by small amounts on images with few pixels.    |
| D2D1\_3DPERSPECTIVETRANSFORM\_INTERPOLATION\_MODE\_ANISOTROPIC           | Uses anisotropic filtering to sample a pattern according to the transformed shape of the bitmap.                                                           |



 

> [!Note]  
> If you don't select a mode, the effect defaults to D2D1\_3DPERSPECTIVETRANSFORM\_INTERPOLATION\_MODE\_LINEAR.

 

> [!Note]  
> Anisotropic mode generates mipmaps when scaling, however, if you set the **Cached** property to true on the effects that are input to this effect, the mipmaps won't be generated every time for sufficiently small images.

 

## Border modes



| Name                     | Description                                                                                                      |
|--------------------------|------------------------------------------------------------------------------------------------------------------|
| D2D1\_BORDER\_MODE\_SOFT | The effect pads the image with transparent black pixels as it interpolates, resulting in a soft edge.<br/> |
| D2D1\_BORDER\_MODE\_HARD | The effect clamps the output to the size of the input image. <br/>                                         |



 

## Output bitmap

The size of the output bitmap depends on the transform matrix that is applied to the image.

The effect performs the transform operation and then applies a bounding box around the result. The output bitmap is the size of the bounding box.

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

 

