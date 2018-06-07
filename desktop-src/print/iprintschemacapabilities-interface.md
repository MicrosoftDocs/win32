---
Description: Provides the primary method to access PrintCapabilities.
ms.assetid: A148C1B4-99A3-4AF3-B2D6-73684978425F
title: IPrintSchemaCapabilities interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IPrintSchemaCapabilities interface

Provides the primary method to access PrintCapabilities.

## Members

The **IPrintSchemaCapabilities** interface inherits from [**IPrintSchemaElement**](iprintschemaelement-interface.md). **IPrintSchemaCapabilities** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IPrintSchemaCapabilities** interface has these methods.



| Method                                                                                            | Description                                                                                                      |
|:--------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------|
| [**GetFeature**](iprintschemacapabilities-getfeature.md)                                         | Gets a named feature from the PrintCapabilities, by name and full namespace URI.<br/>                      |
| [**GetFeatureByKeyName**](iprintschemacapabilities-getfeaturebykeyname.md)                       | Gets a feature from the PrintCapabilities based on a given key name.<br/>                                  |
| [**GetOptions**](iprintschemacapabilities-getoptions.md)                                         | Gets all the options of a feature.<br/>                                                                    |
| [**GetSelectedOptionInPrintTicket**](iprintschemacapabilities-getselectedoptioninprintticket.md) | Gets the selected option for a feature in [**IPrintSchemaTicket**](iprintschematicket-interface.md).<br/> |



 

### Properties

The **IPrintSchemaCapabilities** interface has these properties.



| Property                                                                                                       | Access type          | Description                                                            |
|:---------------------------------------------------------------------------------------------------------------|:---------------------|:-----------------------------------------------------------------------|
| [**JobCopiesAllDocumentsMaxValue**](iprintschemacapabilities-get-jobcopiesalldocumentsmaxvalue.md)<br/> | Read-only<br/> | Gets the **JobCopiesAllDocuments** parameter maximum value.<br/> |
| [**JobCopiesAllDocumentsMinValue**](iprintschemacapabilities-jobcopiesalldocumentsminvalue.md)<br/>     | Read-only<br/> | Gets the **JobCopiesAllDocuments** parameter minimum value.<br/> |
| [**PageImageableSize**](iprintschemacapabilities-pageimageablesize.md)<br/>                             | Read-only<br/> | Gets the imageable area information of the printer.<br/>         |



 

## Remarks

To obtain an IXMLDOMDocument2 object for the PrintCapabilities object, you must first dereference the *ppXmlNode* parameter of the [**XmlNode**](iprintschemaelement-xmlnode.md) property (using \*ppXmlNode ). This retrieves a pointer to an interface of type **IUnknown**. Use this pointer to call the **QueryInterface** method of the PrintCapabilities object to access the underlying IXMLDOMDocument2 object.

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Header<br/>                   | <dl> <dt>Printerextension.h</dt> </dl> |



## See also

<dl> <dt>

[**IPrintSchemaElement**](iprintschemaelement-interface.md)
</dt> <dt>

[Developing v4 print drivers](http://msdn.microsoft.com/en-us/library/windows/hardware/br259124)
</dt> <dt>

[**IPrintSchemaElement::XmlNode**](iprintschemaelement-xmlnode.md)
</dt> <dt>

[**IPrintSchemaTicket**](iprintschematicket-interface.md)
</dt> <dt>

[**IPrintSchemaTicket\_GetCapabilities**](iprintschematicket-getcapabilities.md)
</dt> <dt>

[V4 Printer Driver Localization](https://www.bing.com/search?q=V4+Printer+Driver+Localization)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintSchemaCapabilities%20interface%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





