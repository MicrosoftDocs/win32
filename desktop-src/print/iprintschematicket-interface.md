---
Description: Provides the primary method to access and validate a PrintTicket.
ms.assetid: 190B0B88-6018-4B43-8699-78427421D6FF
title: IPrintSchemaTicket interface
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IPrintSchemaTicket interface

Provides the primary method to access and validate a PrintTicket.

## Members

The **IPrintSchemaTicket** interface inherits from [**IPrintSchemaElement**](iprintschemaelement-interface.md). **IPrintSchemaTicket** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IPrintSchemaTicket** interface has these methods.



| Method                                                                | Description                                                                                                                                                                                                    |
|:----------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CommitAsync**](iprintschematicket-commitasync.md)                 | Gets an asynchronous PrintTicket commit operation context.<br/>                                                                                                                                          |
| [**GetCapabilities**](iprintschematicket-getcapabilities.md)         | Gets an [**IPrintSchemaCapabilities**](iprintschemacapabilities-interface.md) object that represents the printer capabilities based on the current settings of this **IPrintSchemaTicket** object.<br/> |
| [**GetFeature**](iprintschematicket-getfeature.md)                   | Gets a named feature from the PrintTicket, by name and full namespace URI.<br/>                                                                                                                          |
| [**GetFeatureByKeyName**](iprintschematicket-getfeaturebykeyname.md) | Gets a feature from the PrintTicket based on the specified key name.<br/>                                                                                                                                |
| [**NotifyXmlChanged**](iprintschematicket-notifyxmlchanged.md)       | Notifies the print system that the XML DOM object has changed.<br/>                                                                                                                                      |
| [**ValidateAsync**](iprintschematicket-validateasync.md)             | Gets an asynchronous PrintTicket validation operation context.<br/>                                                                                                                                      |



 

### Properties

The **IPrintSchemaTicket** interface has these properties.



| Property                                                                                 | Access type           | Description                     |
|:-----------------------------------------------------------------------------------------|:----------------------|:--------------------------------|
| [**JobCopiesAllDocuments**](iprintschematicket-jobcopiesalldocuments.md)<br/>     | Read-only<br/>  | Gets the copy count.<br/> |
| [**JobCopiesAllDocuments**](iprintschematicket-put-jobcopiesalldocuments.md)<br/> | Write-only<br/> | Sets the copy count.<br/> |



 

## Remarks

To obtain an IXMLDOMDocument2 object for the PrintTicket object, you must first dereference the *ppXmlNode* parameter of the [**XmlNode**](iprintschemaelement-xmlnode.md) property (using \*ppXmlNode ). This retrieves a pointer to an interface of type **IUnknown**. Use this pointer to call the **QueryInterface** method of the PrintTicket object to access the underlying IXMLDOMDocument2 object.

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

[**IPrintSchemaAsyncOperationEvent::Completed**](iprintschemaasyncoperationevent-completed.md)
</dt> <dt>

[**IPrintSchemaCapabilities**](iprintschemacapabilities-interface.md)
</dt> <dt>

[**IPrintSchemaElement::XmlNode**](iprintschemaelement-xmlnode.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintSchemaTicket%20interface%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





