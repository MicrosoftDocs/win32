---
Description: A filter uses the IXpsDocumentConsumer interface when it generates XPS content for the pipeline to consume.
ms.assetid: 98e603e6-2786-4bc8-ad8a-0e91b0d444d8
title: IXpsDocumentConsumer interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IXpsDocumentConsumer interface

A filter uses the `IXpsDocumentConsumer` interface when it generates XPS content for the pipeline to consume.

> [!Note]  
> The XPS print filter pipeline does not preserve digital signatures or story fragments. You may be able to work around this by using stream filters.

 

## Members

The **IXpsDocumentConsumer** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/33f1d79a-33fc-4ce5-a372-e08bda378332) interface. **IXpsDocumentConsumer** also has these types of members:

-   [Methods](#methods)

### Methods

The **IXpsDocumentConsumer** interface has these methods.



| Method                                                                                                    | Description                                                                                                         |
|:----------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------|
| [**IXpsDocumentConsumer::CloseSender**](ixpsdocumentconsumer-closesender.md)                             | The `CloseSender` method tells the Pipeline Manager that the filter is done sending XPS parts.<br/>           |
| [**IXpsDocumentConsumer::GetNewEmptyPart**](ixpsdocumentconsumer-getnewemptypart.md)                     | The `GetNewEmptyPart` method creates a new XPS part.<br/>                                                     |
| [**IXpsDocumentConsumer::SendFixedDocument**](ixpsdocumentconsumer-sendfixeddocument.md)                 | The `SendFixedDocument` method sends a fixed document object to the pipeline.<br/>                            |
| [**IXpsDocumentConsumer::SendFixedDocumentSequence**](ixpsdocumentconsumer-sendfixeddocumentsequence.md) | The **SendFixedDocumentSequence** method sends a fixed document sequence to the pipeline.<br/>                |
| [**IXpsDocumentConsumer::SendFixedPage**](ixpsdocumentconsumer-sendfixedpage.md)                         | The `SendFixedPage` method sends a fixed page of an XPS document to the pipeline.<br/>                        |
| [**IXpsDocumentConsumer::SendXpsDocument**](ixpsdocumentconsumer-sendxpsdocument.md)                     | The `SendXpsDocument` method sends an XPS document to the pipeline. <br/>                                     |
| [**IXpsDocumentConsumer::SendXpsUnknown**](ixpsdocumentconsumer-sendxpsunknown.md)                       | The `SendXpsUnknown` method sends an XPS document part that cannot be identified to the filter pipeline.<br/> |



 

## Requirements



|                   |                                                                                                                        |
|-------------------|------------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Filterpipeline.h (include Filterpipeline.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IXpsDocumentConsumer%20interface%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




