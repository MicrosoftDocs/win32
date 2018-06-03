---
Description: XPSRAS\_PIXEL\_FORMAT allows a caller to select the pixel format used by the IWICBitmap interface that is returned by the IXpsRasterizer::RasterizeRect method. XPSRAS\_PIXEL\_FORMAT is provided with Windows 8 and later versions of Windows.
ms.assetid: 54EA7ED6-BBE1-4110-8405-DEC0C5EA1C27
title: XPSRAS\_PIXEL\_FORMAT enumeration
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# XPSRAS\_PIXEL\_FORMAT enumeration

**XPSRAS\_PIXEL\_FORMAT** allows a caller to select the pixel format used by the [IWICBitmap](http://go.microsoft.com/fwlink/p/?linkid=133875) interface that is returned by the [**IXpsRasterizer::RasterizeRect**](ixpsrasterizer-rasterizerect.md) method. **XPSRAS\_PIXEL\_FORMAT** is provided with Windows 8 and later versions of Windows.

## Syntax


```C++
typedef enum _XPSRAS_PIXEL_FORMAT { 
  XPSRAS_PIXEL_FORMAT_32BPP_PBGRA_UINT_SRGB     = 1,
  XPSRAS_PIXEL_FORMAT_64BPP_PRGBA_HALF_SCRGB,
  XPSRAS_PIXEL_FORMAT_128BPP_PRGBA_FLOAT_SCRGB
} XPSRAS_PIXEL_FORMAT;
```



## Constants

<dl> <dt>

<span id="XPSRAS_PIXEL_FORMAT_32BPP_PBGRA_UINT_SRGB"></span><span id="xpsras_pixel_format_32bpp_pbgra_uint_srgb"></span>**XPSRAS\_PIXEL\_FORMAT\_32BPP\_PBGRA\_UINT\_SRGB**
</dt> <dd>

32-bit color pixel format. It is the default pixel format.

</dd> <dt>

<span id="XPSRAS_PIXEL_FORMAT_64BPP_PRGBA_HALF_SCRGB"></span><span id="xpsras_pixel_format_64bpp_prgba_half_scrgb"></span>**XPSRAS\_PIXEL\_FORMAT\_64BPP\_PRGBA\_HALF\_SCRGB**
</dt> <dd>

64-bit color pixel format.

</dd> <dt>

<span id="XPSRAS_PIXEL_FORMAT_128BPP_PRGBA_FLOAT_SCRGB"></span><span id="xpsras_pixel_format_128bpp_prgba_float_scrgb"></span>**XPSRAS\_PIXEL\_FORMAT\_128BPP\_PRGBA\_FLOAT\_SCRGB**
</dt> <dd>

128-bit color pixel format.

</dd> </dl>

## Remarks

For more information about rasterizing XPS documents, see [Using the XPS Rasterization Service](https://www.bing.com/search?q=Using the XPS Rasterization Service).

## Requirements



|                                     |                                                                                                              |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                                         |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                               |
| Header<br/>                   | <dl> <dt>Xpsrassvc.h (include Xpsrassvc.h)</dt> </dl> |



## See also

<dl> <dt>

[IWICBitmap](http://msdn.microsoft.com/en-us/library/windows/desktop/ee719675.aspx)
</dt> <dt>

[**IXpsRasterizationFactory1::CreateRasterizer1**](xpsrasterizationfactory1-createrasterizer1.md)
</dt> <dt>

[Using the XPS Rasterization Service](https://www.bing.com/search?q=Using the XPS Rasterization Service)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20XPSRAS_PIXEL_FORMAT%20enumeration%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





