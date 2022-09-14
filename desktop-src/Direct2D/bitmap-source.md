---
title: Bitmap source effect
description: Use the bitmap source effect to generate an ID2D1Image from a IWICBitmapSource for use as an input in an effect graph.
ms.assetid: 86646111-208A-4E6D-A28C-7B23A1742D24
keywords:
- bitmap source effect
ms.topic: article
ms.date: 05/31/2018
---

# Bitmap source effect

Use the bitmap source effect to generate an [**ID2D1Image**](/windows/win32/api/d2d1/nn-d2d1-id2d1image) from a [**IWICBitmapSource**](/windows/desktop/api/wincodec/nn-wincodec-iwicbitmapsource) for use as an input in an effect graph. This effect performs scaling and rotation on the CPU. It can also optionally generate a system memory mipmap, which can be a performance optimization for actively scaling very large images at various reduced resolutions.

> [!Note]  
> The bitmap source effect takes its input as a property, not as an image input. You must use the [**SetValue**](/windows/win32/api/d2d1_1/nf-d2d1_1-id2d1properties-setvalue(uint32_constbyte_uint32)) method, not the [**SetInput**](/windows/win32/api/d2d1_1/nf-d2d1_1-id2d1effect-setinput) method. The *WicBitmapSource* property is where you specify the image input data.

 

The CLSID for this effect is CLSID\_D2D1BitmapSource.

-   [Effect properties](#effect-properties)
-   [Interpolation modes](#interpolation-modes)
-   [Orientation](#orientation)
-   [Alpha modes](#alpha-modes)
-   [Remarks](#remarks)
-   [Requirements](#requirements)
-   [Related topics](#related-topics)

## Effect properties



| Display name and index enumeration                                                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                |
|---------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WicBitmapSource<br/> D2D1\_BITMAPSOURCE\_PROP\_WIC\_BITMAP\_SOURCE<br/>         | The [IWICBitmapSource](/windows/desktop/wic/-wic-imp-iwicbitmapsource) containing the image data to be loaded.<br/> The type is [IWICBitmapSource](/windows/desktop/wic/-wic-imp-iwicbitmapsource).<br/> The default value is NULL.<br/>                                                                                                                                                                                                                   |
| Scale<br/> D2D1\_BITMAPSOURCE\_PROP\_SCALE<br/>                                 | The scale amount in the X and Y direction. The effect multiplies the width by the X value and the height by the Y value. This property is a D2D1\_VECTOR\_2F defined as: (X scale, Y scale). The scale amounts are FLOAT, unitless, and must be positive or 0.<br/> The type is D2D1\_VECTOR\_2F.<br/> The default value is {1.0f, 1.0f}.<br/>                                                                           |
| InterpolationMode.<br/> D2D1\_BITMAPSOURCE\_PROP\_INTERPOLATION\_MODE<br/>      | The interpolation mode used to scale the image. See [Interpolation modes](#interpolation-modes) for more info.<br/> If the mode disables the mipmap, then BitmapSouce will cache the image at the resolution determined by the Scale and EnableDPICorrection properties.<br/> The type is D2D1\_BITMAPSOURCE\_INTERPOLATION\_MODE.<br/> The default value is D2D1\_BITMAPSOURCE\_INTERPOLATION\_MODE\_LINEAR.<br/> |
| EnableDPICorrection<br/> D2D1\_BITMAPSOURCE\_PROP\_ENABLE\_DPI\_CORRECTION<br/> | If you set this to TRUE, the effect will scale the input image to convert the DPI reported by [**IWICBitmapSource**](/windows/desktop/api/wincodec/nn-wincodec-iwicbitmapsource) to the DPI of the device context. The effect uses the interpolation mode you set with the InterpolationMode property. If you set this to FALSE, the effect uses a DPI of 96.0 for the output image.<br/> The type is BOOL.<br/> The default value is FALSE.<br/>   |
| AlphaMode<br/> D2D1\_BITMAPSOURCE\_PROP\_ALPHA\_MODE<br/>                       | The alpha mode of the output. This can be either premultiplied or straight. See [Alpha modes](#alpha-modes) for more info.<br/> The type is D2D1\_BITMAPSOURCE\_ALPHA\_MODE.<br/> The default value is D2D1\_BITMAPSOURCE\_ALPHA\_MODE\_PREMULTIPLIED.<br/>                                                                                                                                                              |
| Orientation<br/> D2D1\_BITMAPSOURCE\_PROP\_ORIENTATION<br/>                     | A flip and/or rotation operation to be performed on the image. See [Orientation](#orientation) for more info.<br/> The type is D2D1\_BITMAPSOURCE\_ORIENTATION.<br/> The default value is D2D1\_BITMAPSOURCE\_ORIENTATION\_DEFAULT.<br/>                                                                                                                                                                                 |



 

## Interpolation modes

The effect interpolates using this mode when it scales an image or when it corrects the DPI. The interpolation modes this effect uses are calculated by the CPU, not the GPU.



| Name                                                       | Description                                                                                                                                                                                                                          |
|------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| D2D1\_BITMAPSOURCE\_INTERPOLATION\_MODE\_NEAREST\_NEIGHBOR | Samples the nearest single point and uses that. Doesn't generate a mipmap.                                                                                                                                                           |
| D2D1\_BITMAPSOURCE\_INTERPOLATION\_MODE\_LINEAR            | Uses a four point sample and linear interpolation. Doesn't generate a mipmap.                                                                                                                                                        |
| D2D1\_BITMAPSOURCE\_INTERPOLATION\_MODE\_CUBIC             | Uses a 16 sample cubic kernel for interpolation. Doesn't generate a mipmap.                                                                                                                                                          |
| D2D1\_BITMAPSOURCE\_INTERPOLATION\_MODE\_FANT              | Uses the WIC fant interpolation, the same as the [**IWICBitmapScaler**](/windows/desktop/api/wincodec/nn-wincodec-iwicbitmapscaler) interface. Doesn't generate a mipmap.                                                                                       |
| D2D1\_BITMAPSOURCE\_INTERPOLATION\_MODE\_MIPMAP\_LINEAR    | Generates mipmap chain in system memory using bilinear interpolation. For each mipmap the effect scales to the nearest multiple of 0.5 using bilinear interpolation and then scales the remaining amount using linear interpolation. |



 

## Orientation

The Orientation property can be used to apply an EXIF orientation flag that is embedded within an image.



| Name                                                                    | Description                                                        |
|-------------------------------------------------------------------------|--------------------------------------------------------------------|
| D2D1\_BITMAPSOURCE\_ORIENTATION\_DEFAULT                                | Default. The effect doesn't change the orientation of the input.   |
| D2D1\_BITMAPSOURCE\_ORIENTATION\_FLIP\_HORIZONTAL                       | Flips the image horizontally.                                      |
| D2D1\_BITMAPSOURCE\_ORIENTATION\_ROTATE\_CLOCKWISE180                   | Rotates the image clockwise 180 degrees.                           |
| D2D1\_BITMAPSOURCE\_ORIENTATION\_ROTATE\_CLOCKWISE180\_FLIP\_HORIZONTAL | Rotates the image clockwise 180 degrees and flips it horizontally. |
| D2D1\_BITMAPSOURCE\_ORIENTATION\_ROTATE\_CLOCKWISE270\_FLIP\_HORIZONTAL | Rotates the image clockwise 270 degrees and flips it horizontally. |
| D2D1\_BITMAPSOURCE\_ORIENTATION\_ROTATE\_CLOCKWISE90                    | Rotates the image clockwise 90 degrees.                            |
| D2D1\_BITMAPSOURCE\_ORIENTATION\_ROTATE\_CLOCKWISE90\_FLIP\_HORIZONTAL  | Rotates the image clockwise 90 degrees and flips it horizontally.  |
| D2D1\_BITMAPSOURCE\_ORIENTATION\_ROTATE\_CLOCKWISE270                   | Rotates the image clockwise 270 degrees.                           |



 

This code snippet demonstrates how to convert from EXIF orientation values (defined in propkey.h) to D2D1\_BITMAPSOURCE\_ORIENTATION values.


```C++
#include <propkey.h>
#include <d2d1effects.h>

D2D1_BITMAPSOURCE_ORIENTATION GetBitmapSourceOrientation(unsigned short PhotoOrientation)
{
       switch (PhotoOrientation)
       {
       case PHOTO_ORIENTATION_NORMAL:
              return D2D1_BITMAPSOURCE_ORIENTATION_DEFAULT;
       case PHOTO_ORIENTATION_FLIPHORIZONTAL:
              return D2D1_BITMAPSOURCE_ORIENTATION_FLIP_HORIZONTAL;
       case PHOTO_ORIENTATION_ROTATE180:
              return D2D1_BITMAPSOURCE_ORIENTATION_ROTATE_CLOCKWISE180;
       case PHOTO_ORIENTATION_FLIPVERTICAL:
              return D2D1_BITMAPSOURCE_ORIENTATION_ROTATE_CLOCKWISE180_FLIP_HORIZONTAL;
       case PHOTO_ORIENTATION_TRANSPOSE: 
              return D2D1_BITMAPSOURCE_ORIENTATION_ROTATE_CLOCKWISE90_FLIP_HORIZONTAL;
       case PHOTO_ORIENTATION_ROTATE270:
              return D2D1_BITMAPSOURCE_ORIENTATION_ROTATE_CLOCKWISE90;
       case PHOTO_ORIENTATION_TRANSVERSE:
              return D2D1_BITMAPSOURCE_ORIENTATION_ROTATE_CLOCKWISE270_FLIP_HORIZONTAL;
       case PHOTO_ORIENTATION_ROTATE90:
              return D2D1_BITMAPSOURCE_ORIENTATION_ROTATE_CLOCKWISE270;
       default:
              return D2D1_BITMAPSOURCE_ORIENTATION_DEFAULT;
       }
}
```



## Alpha modes



| Name                                           | Description                                            |
|------------------------------------------------|--------------------------------------------------------|
| D2D1\_BITMAPSOURCE\_ALPHA\_MODE\_PREMULTIPLIED | The effect output uses premultiplied alpha.<br/> |
| D2D1\_BITMAPSOURCE\_ALPHA\_MODE\_STRAIGHT      | The effect output uses straight alpha.<br/>      |



 

## Remarks

To optimize performance when using WIC and [Direct2D](./direct2d-portal.md) together, you should use [**IWICFormatConverter**](/windows/desktop/api/wincodec/nn-wincodec-iwicformatconverter) to convert to an appropriate pixel format based your app s scenario and the image s native precision.

In most cases, either your app s [Direct2D](./direct2d-portal.md) pipeline only requires 8 bits per channel (bpc) of precision, or the image only provides 8 bpc precision, and therefore you should convert to GUID\_WICPixelFormat32bppPBGRA. However, if you want to take advantage of extra precision provided by an image (for example, a JPEG-XR or TIFF stored with greater than 8 bpc precision), you should use an RGBA-based pixel format. The below table provides more details.



| Desired precision   | Native precision of the image | Recommended pixel format                |
|---------------------|-------------------------------|-----------------------------------------|
| 8 bits per channel  | <= 8 bits per channel      | GUID\_WICPixelFormat32bppPBGRA          |
| As high as possible | <= 8 bits per channel      | GUID\_WICPixelFormat32bppPBGRA          |
| As high as possible | > 8 bits per channel       | RGBA channel order, premultiplied alpha |



 

Because many image formats support multiple levels of precision, you should use [**IWICBitmapSource::GetPixelFormat**](/windows/desktop/wic/-wic-codec-iwicbitmapsource-getpixelformat-proxy) to obtain the image s native pixel format, and then use [**IWICPixelFormatInfo**](/windows/desktop/api/wincodec/nn-wincodec-iwicpixelformatinfo) to determine how many bits per channel of precision are available for that format. Also, note that not all hardware supports high precision pixel formats. In those cases your app may need to fall back to the WARP device to support high precision.

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

 

