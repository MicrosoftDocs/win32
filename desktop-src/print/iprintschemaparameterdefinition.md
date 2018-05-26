---
Description: The IPrintSchemaParameterDefinition interface represents a parameter definition, as defined in the Print Schema Specification.
ms.assetid: 205A4F09-6FE5-459E-A94A-13B1839AF489
title: IPrintSchemaParameterDefinition interface
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IPrintSchemaParameterDefinition interface

The **IPrintSchemaParameterDefinition** interface represents a parameter definition, as defined in the [Print Schema Specification](http://msdn.microsoft.com/en-us/library/windows/hardware/gg463385.aspx).

For more information about the four data types that you can use with the &lt;psf:ParameterDef&gt; element, see section 2.1.3.1 of the [Print Schema Specification](http://msdn.microsoft.com/en-us/library/windows/hardware/gg463385.aspx).

## Members

The **IPrintSchemaParameterDefinition** interface inherits from [**IPrintSchemaDisplayableElement**](iprintschemadisplayableelement-interface.md). **IPrintSchemaParameterDefinition** also has these types of members:

-   [Properties](#properties)

### Properties

The **IPrintSchemaParameterDefinition** interface has these properties.



| Property                                                                                   | Access type          | Description                                                                                                                                                                                                  |
|:-------------------------------------------------------------------------------------------|:---------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DataType**](-iprintschemaparameterdefinition-datatype.md)<br/>                   | Read-only<br/> | The **DataType** property gets the [**PrintSchemaParameterDataType**](tagprintschemaparameterdatatype.md) enumerated value that indicates the expected data type for the Print Schema parameter.<br/> |
| [**RangeMax**](-iprintschemaparameterdefinition-rangemax.md)<br/>                   | Read-only<br/> | The **RangeMax** property gets the maximum value of the allowed data range.<br/>                                                                                                                       |
| [**RangeMin**](-iprintschemaparameterdefinition-rangemin.md)<br/>                   | Read-only<br/> | The **RangeMin** property gets the minimum value of the allowed data range.<br/>                                                                                                                       |
| [**UnitType**](-iprintschemaparameterdefinition-unittype.md)<br/>                   | Read-only<br/> | The **UnitType** property gets the unit type.<br/>                                                                                                                                                     |
| [**UserInputRequired**](-iprintschemaparameterdefinition-userinputrequired.md)<br/> | Read-only<br/> | The **UserInputRequired** property gets the Boolean value that indicates whether or not a user input value is required for the Print Schema parameter.<br/>                                            |



 

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                             |
| Header<br/>                   | <dl> <dt>Printerextension.h</dt> </dl> |



## See also

<dl> <dt>

[**IPrintSchemaDisplayableElement**](iprintschemadisplayableelement-interface.md)
</dt> <dt>

[Print Schema Specification](http://msdn.microsoft.com/en-us/library/windows/hardware/gg463385.aspx)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintSchemaParameterDefinition%20interface%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





