---
Description: 'The filter pipeline supports the discard control.'
ms.assetid: '30c6fb0c-42ea-441f-b0a2-3310f8a5b407'
title: IPartDiscardControl interface
---

# IPartDiscardControl interface

The filter pipeline supports the discard control. Filters can use this object, if they obtain it from [**IXpsDocumentProvider::GetXpsPart**](ixpsdocumentprovider-getxpspart.md) method. In some cases, processing this object might just include forwarding it to the next filter by using the [**IXpsDocumentConsumer::SendXpsUnknown**](ixpsdocumentconsumer-sendxpsunknown.md) method.

Filters can also create discard controls. To create a discard control, the filter must create an object that implements the **IPartDiscardControl** interface. Because the filter transfers ownership of the discard control when it sends it to the next filter, the filter must manage the lifetime of the discard control. If a filter creates a discard control, the filter DLL must not unload until the discard control has been released.

## Members

The **IPartDiscardControl** interface inherits from the [**IUnknown**](com.iunknown) interface. **IPartDiscardControl** also has these types of members:

-   [Methods](#methods)

### Methods

The **IPartDiscardControl** interface has these methods.



| Method                                                                                        | Description                                                                                |
|:----------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------|
| [**IPartDiscardControl::GetDiscardProperties**](ipartdiscardcontrol-getdiscardproperties.md) | The **GetDiscardProperties** method gets the properties of the discard control.<br/> |



 

## Requirements



|                   |                                                                                                                        |
|-------------------|------------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Filterpipeline.h (include Filterpipeline.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPartDiscardControl%20interface%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




