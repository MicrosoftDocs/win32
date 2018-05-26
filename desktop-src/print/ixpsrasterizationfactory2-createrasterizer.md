---
Description: The CreateRasterizer method creates an XPS rasterizer object that can convert content from XPS to PWG Raster using the XPS Rasterization Service. PWG Raster supports non-square DPIs.
ms.assetid: C31681A0-17C6-4255-9068-7486A2101AB7
title: IXpsRasterizationFactory2CreateRasterizer method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IXpsRasterizationFactory2::CreateRasterizer method

The **CreateRasterizer** method creates an XPS rasterizer object that can convert content from XPS to PWG Raster using the [XPS Rasterization Service](xps-rasterization-service-reference.md). PWG Raster supports non-square DPIs.

## Syntax


```C++
HRESULT CreateRasterizer(
  [in, optional]  IXpsOMPage              *xpsPage,
  [in]            FLOAT                   dpiX,
  [in]            FLOAT                   dpiY,
  [in]            XPSRAS_RENDERING_MODE   nonTextRenderingMode,
  [in]            XPSRAS_RENDERING_MODE   textRenderingMode,
  [in]            XPSRAS_PIXEL_FORMAT     pixelFormat,
  [in]            XPSRAS_BACKGROUND_COLOR backgroundColor,
  [out, optional] IXpsRasterizer          **ppIXpsRasterizer
);
```



## Parameters

<dl> <dt>

*\*xpsPage* \[in, optional\]
</dt> <dd>

Pointer to an **IXpsOMPage** object that represents the XPS fixed page to render. This object encapsulates a FixedPage section from an XPS document.

</dd> <dt>

*dpiX* \[in\]
</dt> <dd>

Dots per inch which is applied to x dimension of the rasterized output bitmap. The DPI value is the resolution of the device that is to print or display the XPS fixed page.

</dd> <dt>

*dpiY* \[in\]
</dt> <dd>

Dots per inch which is applied to y dimension of the rasterized output bitmap.

</dd> <dt>

*nonTextRenderingMode* \[in\]
</dt> <dd>

Rendering mode for nontext items in the rasterized output. This parameter indicates whether to generate antialiased output. Set this parameter to one of the following [**XPSRAS\_RENDERING\_MODE**](xpsras-rendering-mode-enumeration.md) enumeration values:

-   XPSRAS\_RENDERING\_MODE\_ANTIALIASED

-   XPSRAS\_RENDERING\_MODE\_ALIASED

</dd> <dt>

*textRenderingMode* \[in\]
</dt> <dd>

Rendering mode for text in the rasterized output. This parameter indicates whether to generate antialiased output. Set this parameter to one of the following XPSRAS\_RENDERING\_MODE enumeration values:

-   XPSRAS\_RENDERING\_MODE\_ANTIALIASED

-   XPSRAS\_RENDERING\_MODE\_ALIASED

</dd> <dt>

*pixelFormat* \[in\]
</dt> <dd>

Allows a caller to select the pixel format used by the IWICBitmap returned by [**IXpsRasterizer::RasterizeRect**](ixpsrasterizer-rasterizerect.md). Set this parameter to one of the following [**XPSRAS\_PIXEL\_FORMAT**](xpsras-pixel-format.md) enumeration values:

-   XPSRAS\_PIXEL\_FORMAT\_32BPP\_PBGRA\_UINT\_SRGB

-   XPSRAS\_PIXEL\_FORMAT\_64BPP\_PRGBA\_HALF\_SCRGB

-   XPSRAS\_PIXEL\_FORMAT\_128BPP\_PRGBA\_FLOAT\_SCRGB

</dd> <dt>

*backgroundColor* \[in\]
</dt> <dd>

Allows a caller to select background color. Set this parameter to one of the following [**XPSRAS\_BACKGROUND\_COLOR**](xpsras-background-color.md) enumeration values:

-   XPSRAS\_BACKGROUND\_COLOR\_TRANSPARENT

-   XPSRAS\_BACKGROUND\_COLOR\_OPAQUE

The default background color is XPSRAS\_BACKGROUND\_COLOR\_TRANSPARENT.

</dd> <dt>

*\*\*ppIXpsRasterizer* \[out, optional\]
</dt> <dd>

This parameter points to a location into which the method writes a pointer to the [IXpsRasterizer](ixpsrasterizer-interface.md) interface of the newly created XPS rasterizer object. If the method fails, it writes **NULL** to this location and returns an error code.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                            |                                                                                                              |
|----------------------------|--------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                           |
| Minimum support<br/> | Windows 10<br/>                                                                                        |
| Header<br/>          | <dl> <dt>Xpsrassvc.h (include Xpsrassvc.h)</dt> </dl> |



## See also

<dl> <dt>

[**IXpsRasterizationFactory2**](ixpsrasterizationfactory2.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IXpsRasterizationFactory2::CreateRasterizer%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





