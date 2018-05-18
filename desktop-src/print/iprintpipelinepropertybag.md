---
Description: 'The IPrintPipelinePropertyBag interface is implemented by the PrintFilterPipelineSvc service and is made available to filters through methods in the IPrintPipelineFilter interface. IprintPipelinePropertyBag inherits from the IUnknown interface.'
ms.assetid: '3997291f-0af3-4fa8-8d36-20ff36551f42'
title: IPrintPipelinePropertyBag interface
---

# IPrintPipelinePropertyBag interface

The `IPrintPipelinePropertyBag` interface is implemented by the PrintFilterPipelineSvc service and is made available to filters through methods in the [IPrintPipelineFilter](iprintpipelinefilter.md) interface. `IprintPipelinePropertyBag` inherits from the **IUnknown** interface.

The properties of the property bag are described in [**Print Pipeline Property Bag**](print.print_pipeline_property_bag).

## Members

The **IPrintPipelinePropertyBag** interface inherits from the [**IUnknown**](com.iunknown) interface. **IPrintPipelinePropertyBag** also has these types of members:

-   [Methods](#methods)

### Methods

The **IPrintPipelinePropertyBag** interface has these methods.



| Method                                                                                        | Description                                                                    |
|:----------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------|
| [**IPrintPipelinePropertyBag::AddProperty**](iprintpipelinepropertybag-addproperty.md)       | The `AddProperty` method adds a property to a property bag.<br/>         |
| [**IPrintPipelinePropertyBag::DeleteProperty**](iprintpipelinepropertybag-deleteproperty.md) | The `DeleteProperty` method deletes a property from a property bag.<br/> |
| [**IPrintPipelinePropertyBag::GetProperty**](iprintpipelinepropertybag-getproperty.md)       | The `GetProperty` method gets a property from a property bag.<br/>       |



 

## Requirements



|                   |                                                                                                                        |
|-------------------|------------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Filterpipeline.h (include Filterpipeline.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintPipelinePropertyBag%20interface%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




