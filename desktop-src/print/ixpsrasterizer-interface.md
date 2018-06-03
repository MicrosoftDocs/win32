---
Description: The IXpsRasterizer interface represents an XPS rasterizer that can create a bitmap image of an XPS fixed page or of a rectangular region of a fixed page.
ms.assetid: 1ef99120-2b3b-45aa-bcf7-16bcb9656089
title: IXpsRasterizer interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IXpsRasterizer interface

The **IXpsRasterizer** interface represents an XPS rasterizer that can create a bitmap image of an XPS fixed page or of a rectangular region of a fixed page.

A client obtains an **IXpsRasterizer** interface instance by calling the [**IXpsRasterizationFactory::CreateRasterizer**](ixpsrasterizationfactory-createrasterizer.md) method.

## Members

The **IXpsRasterizer** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/windows/desktop/33f1d79a-33fc-4ce5-a372-e08bda378332) interface. **IXpsRasterizer** also has these types of members:

-   [Methods](#methods)

### Methods

The **IXpsRasterizer** interface has these methods.



| Method                                                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|:------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**RasterizeRect**](ixpsrasterizer-rasterizerect.md)             | The `RasterizeRect` method rasterizes an axis-aligned, rectangular region of an XPS fixed page.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [**SetMinimalLineWidth**](ixpsrasterizer-setminimallinewidth.md) | The `SetMinimalLineWidth` method allows the caller to set the minimum thickness (in pixels) of the lines that the device can render. The default minimum thickness value is 1 pixel if `SetMinimalLineWidth` is not called. This minimum thickness value only applies to the Nominal Width Stroke as defined in the XPS Specification v1.0, Sec 11.6.12. **IXpsRasterizer** requires that any Nominal Width Stroke is rasterized with either the width specified by its **StrokeThickness** attribute, or the pixel value set by `SetMinimalLineWidth` (1 pixel if `SetMinimalLineWidth` is not called), whichever is bigger.<br/> |



 

## Requirements



|                   |                                                                                        |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Xpsrassvc.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IXpsRasterizer%20interface%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




