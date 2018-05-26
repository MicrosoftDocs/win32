---
Description: The RangeMin property gets the minimum value of the allowed data range.
ms.assetid: ED8A29D9-84CE-4FB5-BCEE-C31DA9AB3D00
title: IPrintSchemaParameterDefinitionRangeMin property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IPrintSchemaParameterDefinition::RangeMin property

The **RangeMin** property gets the minimum value of the allowed data range.

This property is read-only.

## Syntax


```C++
HRESULT get_RangeMin(
  [out, retval] INT *pRangeMin
);
```



## Property value

The minimum value.

## Error codes

Returns an **HRESULT** value, if the property call was successful. Otherwise it returns the appropriate error code.

## Remarks

For the **PrintSchemaParameterDataType\_Integer** data type, the value returned by **RangeMin** maps to the &lt;psf:MinValue&gt; property value of the Print Schema parameter definition. This minimum value shows the minimum integer value that the driver supports.

For the **PrintSchemaParameterDataType\_NumericString** and **PrintSchemaParameterDataType\_String** data types, this maps to the &lt;psf:MinLength&gt; property value of the Print Schema parameter definition. This minimum value shows the minimum length of string that the driver supports.

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                             |
| Header<br/>                   | <dl> <dt>Printerextension.h</dt> </dl> |



## See also

<dl> <dt>

[**IPrintSchemaParameterDefinition**](iprintschemaparameterdefinition.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintSchemaParameterDefinition::RangeMin%20property%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





