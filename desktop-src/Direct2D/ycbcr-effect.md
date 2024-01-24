---
title: YCbCr Effect
description: Converts planar and chroma subsampled JPEG YCbCr data to RGB.
ms.assetid: E4492996-54DA-4C5F-B44C-8FBE97C8DD7D
ms.topic: article
ms.date: 05/31/2018
---

# YCbCr Effect

Converts planar and chroma subsampled JPEG YC<sub>b</sub>C<sub>r</sub> data to RGB. This effect assumes that the YC<sub>b</sub>C<sub>r</sub> data is formatted in compliance with the JPEG standard. Data for the inputs may be obtained from IWICPlanarBitmapSourceTransform. The YC<sub>b</sub>C<sub>r</sub> effect requires two inputs; the first must be a DXGI\_FORMAT\_R8 bitmap containing luma data, and the second must be a DXGI\_FORMAT\_R8G8 bitmap containing subsampled chroma data. For more information about using this effect, see [JPEG YCbCr Support](/windows/desktop/wic/jpeg-ycbcr-support).

The CLSID for this effect is CLSID\_D2D1YCbCr.

-   [Effect properties](#effect-properties)
-   [Subsampling modes](#subsampling-modes)
-   [Interpolation modes](#interpolation-modes)
-   [Output bitmap](#output-bitmap)
-   [Requirements](#requirements)
-   [Related topics](#related-topics)

## Effect properties



| Display name and index enumeration                                          | Description                                                                                                                                                                                                                                                                                             |
|-----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ChromaSubsampling<br/> D2D1\_YCBCR\_CHROMA\_SUBSAMPLING<br/>    | Specifies the chroma subsampling of the input chroma image. <br/> The type is D2D1\_YCBCR\_CHROMA\_SUBSAMPLING.<br/> The default value is D2D1\_YCBCR\_CHROMA\_SUBSAMPLING\_AUTO.<br/>                                                                                                |
| TransformMatrix <br/> D2D1\_YCBCR\_PROP\_TRANSFORM\_MATRIX<br/> | A [3x2 Matrix](/previous-versions/dotnet/netframework-3.0/ms750596(v=vs.85)) specifying the axis-aligned affine transform of the image. Axis aligned transforms include Scale, Flips, and 90 degree rotations. <br/> The type is D2D1\_MATRIX\_3X2\_F.<br/> The default value is Matrix3x2F::Identity().<br/> |
| InterpolationMode<br/> D2D1\_YCBCR\_INTERPOLATION\_MODE<br/>    | The interpolation mode.<br/> The type is D2D1\_YCBCR\_INTERPOLATION\_MODE.<br/>                                                                                                                                                                                                             |



 

## Subsampling modes



| Enumeration                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| D2D1\_YCBCR\_CHROMA\_SUBSAMPLING\_AUTO<br/> | This mode attempts to infer the chroma subsampling from the bounds of the input images. When this option is selected, the smaller plane is upsampled to the size of the larger plane and this effect s output rectangle is the intersection of the two planes. When using this mode, care should be taken when applying effects to the input planes that change the image bounds, such as the border transform, so that the desired size ratio between the planes is maintained. <br/> |
| D2D1\_YCBCR\_CHROMA\_SUBSAMPLING\_420<br/>  | The chroma plane is horizontally subsampled by   and vertically subsampled by  . When this option is selected, the chroma plane is horizontally and vertically upsampled by 2x and this effect s output rectangle is the intersection of the two planes.<br/>                                                                                                                                                                                                                          |
| D2D1\_YCBCR\_CHROMA\_SUBSAMPLING\_422<br/>  | The chroma plane is horizontally subsampled by  . When this option is selected, the chroma plane is horizontally upsampled by 2x and this effect s output rectangle is the intersection of the two planes.<br/>                                                                                                                                                                                                                                                                        |
| D2D1\_YCBCR\_CHROMA\_SUBSAMPLING\_444<br/>  | The chroma plane is not subsampled. When this option is selected this effect s output rectangle is the intersection of the two planes.<br/>                                                                                                                                                                                                                                                                                                                                            |
| D2D1\_YCBCR\_CHROMA\_SUBSAMPLING\_440<br/>  | The chroma plane is vertically subsampled by  . When this option is selected, the chroma plane is vertically upsampled by 2x and this effect s output rectangle is the intersection of the two planes.<br/>                                                                                                                                                                                                                                                                            |



 

## Interpolation modes



| Enumeration                                             | Description                                                                                                                                                                                          |
|---------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| D2D1\_YCBCR\_INTERPOLATION\_MODE\_NEAREST\_NEIGHBOR     | Samples the nearest single point and uses that. This mode uses less processing time, but outputs the lowest quality image.                                                                           |
| D2D1\_YCBCR\_INTERPOLATION\_MODE\_LINEAR                | Uses a four point sample and linear interpolation. This mode uses more processing time than the nearest neighbor mode, but outputs a higher quality image.                                           |
| D2D1\_YCBCR\_INTERPOLATION\_MODE\_CUBIC                 | Uses a 16 sample cubic kernel for interpolation. This mode uses the most processing time, but outputs a higher quality image.                                                                        |
| D2D1\_YCBCR\_INTERPOLATION\_MODE\_MULTI\_SAMPLE\_LINEAR | Uses 4 linear samples within a single pixel for good edge anti-aliasing. This mode is good for scaling down by small amounts on images with few pixels.                                              |
| D2D1\_YCBCR\_INTERPOLATION\_MODE\_ANISOTROPIC           | Uses anisotropic filtering to sample a pattern according to the transformed shape of the bitmap.                                                                                                     |
| D2D1\_YCBCR\_INTERPOLATION\_MODE\_HIGH\_QUALITY\_CUBIC  | Uses a variable size high quality cubic kernel to perform a pre-downscale the image if downscaling is involved in the transform matrix. Then uses the cubic interpolation mode for the final output. |



 

## Output bitmap

The size of the output bitmap depends on the transform matrix that is applied to the image.

The effect performs the transform operation and then applies a bounding box around the result. The output bitmap is the size of the bounding box.

## Requirements



| Requirement | Value |
|--------------------------|---------------------------------------------------------------|
| Minimum supported client | Windows 8.1 \[desktop apps \| Windows Store apps\]            |
| Minimum supported server | Windows Server 2012 R2 \[desktop apps \| Windows Store apps\] |
| Header                   | d2d1effects\_1.h                                              |
| Library                  | d2d1.lib, dxguid.lib                                          |



 

## Related topics

<dl> <dt>

[**ID2D1Effect**](/windows/win32/api/d2d1_1/nn-d2d1_1-id2d1effect)
</dt> <dt>

[JPEG YCbCr Support](/windows/desktop/wic/jpeg-ycbcr-support)
</dt> <dt>

[**IWICPlanarBitmapSourceTransform**](/windows/desktop/api/wincodec/nn-wincodec-iwicplanarbitmapsourcetransform)
</dt> </dl>

 

