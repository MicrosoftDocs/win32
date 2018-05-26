---
Description: XPS Rasterization Service Interfaces
ms.assetid: 86c98c94-0324-403c-9fc4-b0411d84abc8
title: XPS Rasterization Service Interfaces
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# XPS Rasterization Service Interfaces

In Windows 7 and later, the [XPS rasterization service](print.using_the_xps_rasterization_service) performs the rasterization of fixed pages in XPS documents for XPSDrv filters. The service provides an XPS rasterization factory that a filter uses to create XPS rasterizers. The filter can tell an XPS rasterizer to create a bitmap to represent an entire fixed page, or the filter can partition the fixed page into a number of axis-aligned, rectangular regions and tell the rasterizer to create a separate bitmap for each region.

During the initialization of an XPSDrv filter, the print filter pipeline manager passes a [**print pipeline property bag**](print.print_pipeline_property_bag) to the filter. Through the property bag, the filter can obtain the **IXpsRasterizationFactory** interface of the XPS rasterization factory. As the filter renders an XPS document, the filter can obtain from the factory a new XPS rasterizer--with an **IXpsRasterizer** interface--to render each successive fixed page in the document.

The XPS rasterization service implements the following interfaces:

<dl>

[IXpsRasterizer](ixpsrasterizer-interface.md)  
[IXpsRasterizationFactory](ixpsrasterizationfactory-interface.md)  
[IXpsRasterizationFactory1](xpsrasterizationfactory1.md)  
[**IXpsRasterizationFactory2**](ixpsrasterizationfactory2.md)  
</dl>

An XPSDrv filter should also implement the following interface if it needs to cancel an in-progress XPS rasterization operation before the operation completes:

<dl>

[IXpsRasterizerNotificationCallback](ixpsrasterizernotificationcallback-interface.md)  
</dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20XPS%20Rasterization%20Service%20Interfaces%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



