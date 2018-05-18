---
Description: 'Gets the IXMLDOMNode object associated with this item.'
ms.assetid: '5E7F2292-1F71-4581-8E34-86F1464EC08F'
title: 'IPrintSchemaElement::XmlNode property'
---

# IPrintSchemaElement::XmlNode property

Gets the IXMLDOMNode object associated with this item.

This property is read-only.

## Syntax


```C++
HRESULT get_XmlNode(
  [out, retval] IXMLDOMNode **ppXmlNode
);
```



## Property value

The returned node.

## Error codes

Returns an **HRESULT** value, if the property call was successful. Otherwise it returns the appropriate error code.

## Remarks

When you dereference the *ppXmlNode* parameter (using \*ppXmlNode ), you obtain a pointer to an interface of type **IUnknown**. Use this pointer to call the **QueryInterface** method, to access the underlying [IXMLDOMElement](http://msdn.microsoft.com/en-us/library/windows/desktop/ms760248.aspx) object.print.

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Header<br/>                   | <dl> <dt>Printerextension.h</dt> </dl> |



## See also

<dl> <dt>

[**IPrintSchemaCapabilities**](iprintschemacapabilities-interface.md)
</dt> <dt>

[**IPrintSchemaElement**](iprintschemaelement-interface.md)
</dt> <dt>

[**IPrintSchemaTicket**](iprintschematicket-interface.md)
</dt> <dt>

[**IPrintSchemaTicket\_GetCapabilities**](iprintschematicket-getcapabilities.md)
</dt> <dt>

[**IPrintSchemaTicket::NotifyXmlChanged**](iprintschematicket-notifyxmlchanged.md)
</dt> <dt>

[IXMLDOMElement](http://msdn.microsoft.com/en-us/library/windows/desktop/ms760248.aspx)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintSchemaElement::XmlNode%20property%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





