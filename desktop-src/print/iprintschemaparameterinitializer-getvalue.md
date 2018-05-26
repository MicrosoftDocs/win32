---
Description: The Value (get\_Value) property gets the current value of the IPrintSchemaParameterInitializer object.
ms.assetid: CDBAB58C-F051-4047-A538-5504F0E28EC7
title: IPrintSchemaParameterInitializerValue property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IPrintSchemaParameterInitializer::Value property

The **Value** (get\_Value) property gets the current value of the [**IPrintSchemaParameterInitializer**](iprintschemaparameterinitializer.md) object.

In PrintTicket XML, that’s the value of the &lt;psf:Value&gt; child element for the &lt;psf:ParameterInit&gt; element.

This property is read-only.

## Syntax


```C++
HRESULT get_Value(
  [out, retval] VARIANT *pVar
);
```



## Property value

The current value of the **IPrintSchemaParameterInitializer** object.

## Error codes

Returns an **HRESULT** value, if the property call was successful. Otherwise it returns the appropriate error code.

## Remarks

The **Value** (get\_Value) property returns the current value of the **IPrintSchemaParameterInitializer** object in the form of a Variant variable. Here's how the value and type are stored in the Variant for the different parameter data types:



| Parameter DataType                          | Variant type            | Variant value |
|---------------------------------------------|-------------------------|---------------|
| PrintSchemaParameterDataType\_Integer       | V\_VT(pVar) is VT\_I4   | V\_I4(pVar)   |
| PrintSchemaParameterDataType\_NumericString | V\_VT(pVar) is VT\_BSTR | V\_BSTR(pVar) |
| PrintSchemaParameterDataType\_String        | V\_VT(pVar) is VT\_BSTR | V\_BSTR(pVar) |



 

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                             |
| Header<br/>                   | <dl> <dt>Printerextension.h</dt> </dl> |



## See also

<dl> <dt>

[**IPrintSchemaParameterInitializer**](iprintschemaparameterinitializer.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintSchemaParameterInitializer::Value%20property%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





