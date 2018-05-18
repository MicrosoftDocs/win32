---
Description: 'Gets an IPrintSchemaCapabilities object that represents the printer capabilities based on the current settings of this IPrintSchemaTicket object.'
ms.assetid: '5556BD5E-6489-4CCF-8C62-DDA53AD9F368'
title: 'IPrintSchemaTicket::GetCapabilities method'
---

# IPrintSchemaTicket::GetCapabilities method

Gets an [**IPrintSchemaCapabilities**](iprintschemacapabilities-interface.md) object that represents the printer capabilities based on the current settings of this [**IPrintSchemaTicket**](iprintschematicket-interface.md) object.

## Syntax


```C++
HRESULT GetCapabilities(
  [out, retval] IPrintSchemaCapabilities **ppPrintCapabilities
);
```



## Parameters

<dl> <dt>

*ppPrintCapabilities* \[out, retval\]
</dt> <dd>

The returned [**IPrintSchemaCapabilities**](iprintschemacapabilities-interface.md) object.

</dd> </dl>

## Return value

This method returns an **HRESULT** value.

## Remarks

Because this method retrieves a new PrintCapabilities document every time it is invoked, it is recommended that you invoke this method only when the [**IPrintSchemaTicket**](iprintschematicket-interface.md) object has been modified.

## Requirements



|                            |                                                                                               |
|----------------------------|-----------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>            |
| Header<br/>          | <dl> <dt>Printerextension.h</dt> </dl> |



## See also

<dl> <dt>

[**IPrintSchemaTicket**](iprintschematicket-interface.md)
</dt> <dt>

[**IPrintSchemaCapabilities**](iprintschemacapabilities-interface.md)
</dt> <dt>

[**IPrintSchemaFeature::SelectedOption**](iprintschemafeature-selectedoption.md)
</dt> <dt>

[**IPrintSchemaElement::XmlNode**](iprintschemaelement-xmlnode.md)
</dt> <dt>

[**IPrintSchemaTicket::put\_JobCopiesAllDocuments**](iprintschematicket-put-jobcopiesalldocuments.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintSchemaTicket::GetCapabilities%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





