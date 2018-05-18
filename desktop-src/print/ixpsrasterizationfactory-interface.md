---
Description: 'The IXpsRasterizationFactory interface represents an object factory for creating XPS rasterizer objects.'
ms.assetid: '559bdc65-282e-42b2-998a-276202376c1e'
title: IXpsRasterizationFactory interface
---

# IXpsRasterizationFactory interface

The **IXpsRasterizationFactory** interface represents an object factory for creating XPS rasterizer objects. Rasterizer objects created by the factory implement [**IXpsRasterizer**](ixpsrasterizer-interface.md) interfaces. An XPSDrv filter uses a rasterizer object to convert an XPS fixed page to one or more bitmap images.

An XPSDrv filter obtains a reference to an **IXpsRasterizationFactory** interface instance from the property bag received from the print filter pipeline manager. The pipeline manager calls the filter's [**IPrintPipelineFilter::InitializeFilter**](iprintpipelinefilter-initializefilter.md) method and passes in an [**IPrintPipelinePropertyBag**](iprintpipelinepropertybag.md) pointer. The interface reference is a VT\_UNKNOWN property value that is identified by the property name **MS\_IXpsRasterizationFactory**.

## Members

The **IXpsRasterizationFactory** interface inherits from the [**IUnknown**](com.iunknown) interface. **IXpsRasterizationFactory** also has these types of members:

-   [Methods](#methods)

### Methods

The **IXpsRasterizationFactory** interface has these methods.



| Method                                                                | Description                                                               |
|:----------------------------------------------------------------------|:--------------------------------------------------------------------------|
| [**CreateRasterizer**](ixpsrasterizationfactory-createrasterizer.md) | The `CreateRasterize` method creates an XPS rasterizer object.<br/> |



 

## Requirements



|                   |                                                                                        |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Xpsrassvc.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IXpsRasterizationFactory%20interface%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




