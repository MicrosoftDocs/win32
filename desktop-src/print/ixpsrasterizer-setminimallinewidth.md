---
Description: The SetMinimalLineWidth method allows the caller to set the minimum thickness (in pixels) of the lines that the device can render.
ms.assetid: daf84d1a-d499-4a6e-be87-39fd16f3d87d
title: IXpsRasterizerSetMinimalLineWidth method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IXpsRasterizer::SetMinimalLineWidth method

The `SetMinimalLineWidth` method allows the caller to set the minimum thickness (in pixels) of the lines that the device can render. The default minimum thickness value is 1 pixel if `SetMinimalLineWidth` is not called. This minimum thickness value only applies to the Nominal Width Stroke as defined in the XPS Specification v1.0, Sec 11.6.12. **IXpsRasterizer** requires that any Nominal Width Stroke is rasterized with either the width specified by its **StrokeThickness** attribute, or the pixel value set by `SetMinimalLineWidth` (1 pixel if `SetMinimalLineWidth` is not called), whichever is bigger.

## Syntax


```C++
HRESULT STDMETHODCALLTYPE SetMinimalLineWidth(
  [in] INT width
);
```



## Parameters

<dl> <dt>

*width* \[in\]
</dt> <dd>

The minimum thickness (in pixels) of the lines the device is capable of rendering. The value should be greater than 1.

</dd> </dl>

## Return value

`SetMinimalLineWidth` always returns S\_OK.

## Remarks

This method is supported in Windows 7 and later. It is not supported in versions of the Windows operating system before Windows 7.

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

[**IXpsRasterizer::RasterizeRect**](ixpsrasterizer-rasterizerect.md)
</dt> <dt>

[IXpsRasterizerNotificationCallback](ixpsrasterizernotificationcallback-interface.md)
</dt> <dt>

[**IXpsRasterizationFactory::CreateRasterizer**](ixpsrasterizationfactory-createrasterizer.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IXpsRasterizer::SetMinimalLineWidth%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





