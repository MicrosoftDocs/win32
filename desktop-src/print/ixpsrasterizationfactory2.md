---
Description: In Windows 10, the IXpsRasterizationFactory2 interface represents an object factory for creating components that can convert content from XPS to PWG Raster using the XPS Rasterization Service. PWG Raster supports non-square DPIs.
ms.assetid: 23994CD9-A65B-4BD7-9070-3F575D011953
title: IXpsRasterizationFactory2 interface
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IXpsRasterizationFactory2 interface

In Windows 10, the **IXpsRasterizationFactory2** interface represents an object factory for creating components that can convert content from XPS to PWG Raster using the [XPS Rasterization Service](xps-rasterization-service-reference.md). PWG Raster supports non-square DPIs.

## Members

The **IXpsRasterizationFactory2** interface inherits from the [**IUnknown**](com.iunknown) interface. **IXpsRasterizationFactory2** also has these types of members:

-   [Methods](#methods)

### Methods

The **IXpsRasterizationFactory2** interface has these methods.



| Method                                                                 | Description                                                                                                                                                                                                                                       |
|:-----------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateRasterizer**](ixpsrasterizationfactory2-createrasterizer.md) | The **CreateRasterizer** method creates an XPS rasterizer object that can convert content from XPS to PWG Raster using the [XPS Rasterization Service](xps-rasterization-service-reference.md). PWG Raster supports non-square DPIs. <br/> |



 

## Requirements



|                   |                                                                                        |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Xpsrassvc.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IXpsRasterizationFactory2%20interface%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




