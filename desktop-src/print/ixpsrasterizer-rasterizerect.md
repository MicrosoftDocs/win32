---
Description: The RasterizeRect method rasterizes an axis-aligned, rectangular region of an XPS fixed page.
ms.assetid: abf8dfc7-7921-4e9c-a338-ec783a01fca7
title: IXpsRasterizerRasterizeRect method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IXpsRasterizer::RasterizeRect method

The `RasterizeRect` method rasterizes an axis-aligned, rectangular region of an XPS fixed page.

## Syntax


```C++
HRESULT RasterizeRect(
  [in]            INT                                x,
  [in]            INT                                y,
  [in]            INT                                width,
  [in]            INT                                height,
  [in, optional]  IXpsRasterizerNotificationCallback *notificationCallback,
  [out, optional] IWICBitmap                         **bitmap
);
```



## Parameters

<dl> <dt>

*x* \[in\]
</dt> <dd>

The x coordinate, in pixels, at the left edge of the output bitmap.

</dd> <dt>

*y* \[in\]
</dt> <dd>

The y coordinate, in pixels, at the top edge of the output bitmap.

</dd> <dt>

*width* \[in\]
</dt> <dd>

The width, in pixels, of the output bitmap.

</dd> <dt>

*height* \[in\]
</dt> <dd>

The height, in pixels, of the output bitmap.

</dd> <dt>

*notificationCallback* \[in, optional\]
</dt> <dd>

Pointer to the [**IXpsRasterizerNotificationCallback**](ixpsrasterizernotificationcallback-interface.md) interface of a notification object that is implemented by the caller. This parameter is optional and can be **NULL** if the caller does not require notification callbacks.

</dd> <dt>

*bitmap* \[out, optional\]
</dt> <dd>

Pointer to a location into which the method writes a pointer to the [IWICBitmap](http://msdn.microsoft.com/en-us/library/windows/desktop/ee719675.aspx) interface of the newly created bitmap object. If the method fails, it writes **NULL** to this location and returns an error code.

</dd> </dl>

## Return value

`RasterizeRect` returns S\_OK if the call was successful. Otherwise, the method returns an error code. Possible error return values include:



| Return code                                                                                  | Description                                                          |
|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| <dl> <dt>**E\_POINTER**</dt> </dl>    | Parameter *bitmap* is **NULL**.<br/>                           |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Parameter *width* or *height* is less than or equal to 0.<br/> |



 

## Remarks

This method is supported in Windows 7 and later. It is not supported in versions of the Windows operating system before Windows 7.

If successful, this method creates a Windows imaging component (WIC) bitmap object and passes to the caller a counted reference to the object's [IWICBitmap](http://msdn.microsoft.com/en-us/library/windows/desktop/ee719675.aspx) interface. When the object is no longer needed, the caller is responsible for releasing the object by calling the [Release](http://go.microsoft.com/fwlink/p/?linkid=98433) method on the object's [IWICBitmap](http://msdn.microsoft.com/en-us/library/windows/desktop/ee719675.aspx) interface.

The WIC bitmap created by this method has a 32-bit pixel format that contains 8-bit red, green, and blue channels and uses the standard RGB (sRGB) color space. In addition, the format contains an 8-bit alpha component. The color components in each pixel value are pre-multiplied by the alpha component. The pixel format is specified by the GUID value **GUID\_WICPixelFormat32bppPBGRA**, which is defined in the header file Wincodec.h. For more information about this format, see [Native Pixel Formats Overview](http://go.microsoft.com/fwlink/p/?linkid=133874).

The [**IXpsRasterizationFactory::CreateRasterizer**](ixpsrasterizationfactory-createrasterizer.md) method's *DPI* parameter specifies the resolution, in dots per inch, at which the bitmap is to be rendered. As described in the [XPS specification](https://msdn.microsoft.com/library/windows/hardware/gg463431)<span class="underline">,</span> the width and height of a fixed page in an XPS document are specified in 1/96-inch units. To determine the dimensions (in pixels) of the bitmap required to represent the entire fixed page, multiply the width and height by *DPI*/96.

To accommodate printers that require a fixed page to be rasterized as a series of horizontal or vertical bands, parameters *x*, *y*, *width*, and *height* specify a rectangular region of the fixed page that is to be rasterized. All four parameter values are specified in pixels. Parameters *x* and *y* are the coordinates of the top, left corner of the rectangular region; they are specified as pixel displacements from the coordinate origin (0, 0). Parameters *width* and *height* are the dimensions of the rectangular region.

For example, if *w*XPS and *h*XPS are the width and height of an XPS fixed page in 1/96-inch units, `RasterizeRect` generates a bitmap representation of the bottom half of the fixed page if parameters *x*, *y*, *width*, and *height* are set to the following values:

<dl> *x* = 0  
*y* = (*h*XPS/2)\**DPI*/96  
*width* = *w*XPS\**DPI*/96  
*height* = (*h*XPS/2)\**DPI*/96  
</dl>

If the *notificationCallback* parameter is non-**NULL**, the `RasterizeRect` method takes a counted reference to the notification object's **IXpsRasterizerNotificationCallback** interface. It does so by calling the **AddRef** method on the interface before making any calls to the **IXpsRasterizerNotificationCallback::Continue** method. Before `RasterizeRect` returns, it releases the notification object by calling the **Release** method on the **IXpsRasterizerNotificationCallback** interface.

As explained in the [XPS specification](https://msdn.microsoft.com/library/windows/hardware/gg463431)<span class="underline">,</span> the optional **BleedBox** attribute can specify a bleed box that extends outside the boundaries of a fixed page. To accommodate bleed boxes, the rectangle defined by the parameters *x*, *y*, *width*, and *height* can also extend beyond the boundaries of the fixed page. The method accepts any values, positive or negative, for *x* and *y*, and it accepts any positive, nonzero values for *width* and *height*. The rectangle specified by these parameters defines the clipping region for the rasterization operation. If the rectangle extends beyond the boundaries of the fixed page, the clipping region also extends beyond these boundaries.

If the method fails and *bitmap* is non-**NULL**, the method sets \**bitmap* = **NULL**.

For a code example that calls the `RasterizeRect` method, see the XPSRasFilter sample in the WDK. This sample is located in the Src\\Print\\Xpsrasfilter folder in your WDK installation.

## Requirements



|                            |                                                                                        |
|----------------------------|----------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>     |
| Version<br/>         | Available in Windows 7 and later versions of the Windows operating system.<br/>  |
| Header<br/>          | <dl> <dt>Xpsrassvc.h</dt> </dl> |



## See also

<dl> <dt>

[**IXpsRasterizer**](ixpsrasterizer-interface.md)
</dt> <dt>

[IWICBitmap](http://msdn.microsoft.com/en-us/library/windows/desktop/ee719675.aspx)
</dt> <dt>

[**IXpsRasterizer::SetMinimalLineWidth**](ixpsrasterizer-setminimallinewidth.md)
</dt> <dt>

[IXpsRasterizerNotificationCallback](ixpsrasterizernotificationcallback-interface.md)
</dt> <dt>

[**IXpsRasterizationFactory::CreateRasterizer**](ixpsrasterizationfactory-createrasterizer.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IXpsRasterizer::RasterizeRect%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





