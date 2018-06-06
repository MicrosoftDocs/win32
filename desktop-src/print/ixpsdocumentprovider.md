---
Description: The IxpsDocumentProvider interface provides interfaces to consume parts of a document.
ms.assetid: e1fac90f-5c21-4857-a52f-04c5366d7b18
title: IXpsDocumentProvider interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IXpsDocumentProvider interface

The `IxpsDocumentProvider` interface provides interfaces to consume parts of a document.

> [!Note]  
> The XPS print filter pipeline does not preserve digital signatures or story fragments. You may be able to work around this by using stream filters.

 

## Members

The **IXpsDocumentProvider** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/33f1d79a-33fc-4ce5-a372-e08bda378332) interface. **IXpsDocumentProvider** also has these types of members:

-   [Methods](#methods)

### Methods

The **IXpsDocumentProvider** interface has these methods.



| Method                                                                      | Description                                                                                |
|:----------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------|
| [**IXpsDocumentProvider::GetXpsPart**](ixpsdocumentprovider-getxpspart.md) | The `GetXpsPart` method retrieves several objects that make up an XPS document.<br/> |



 

## Requirements



|                   |                                                                                                                        |
|-------------------|------------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Filterpipeline.h (include Filterpipeline.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IXpsDocumentProvider%20interface%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




