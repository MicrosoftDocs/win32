---
Description: The IPrintSchemaParameterInitializer interface represents a parameter initialization value, as defined in the print schema specification.
ms.assetid: A4A1C231-3D71-4952-B5FA-0C8275DEF4F1
title: IPrintSchemaParameterInitializer interface
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IPrintSchemaParameterInitializer interface

The **IPrintSchemaParameterInitializer** interface represents a parameter initialization value, as defined in the print schema specification.

For more information about the four data types that you can use with the &lt;psf:ParameterInit&gt; element, see section 2.1.3.2 of the [Print Schema Specification](http://msdn.microsoft.com/en-us/library/windows/hardware/gg463385.aspx).

## Members

The **IPrintSchemaParameterInitializer** interface inherits from [**IPrintSchemaElement**](iprintschemaelement-interface.md). **IPrintSchemaParameterInitializer** also has these types of members:

-   [Properties](#properties)

### Properties

The **IPrintSchemaParameterInitializer** interface has these properties.



| Property                                                              | Access type           | Description                                                                                                               |
|:----------------------------------------------------------------------|:----------------------|:--------------------------------------------------------------------------------------------------------------------------|
| [**Value**](iprintschemaparameterinitializer-getvalue.md)<br/> | Read-only<br/>  | The **Value** (get\_Value) property gets the current value of the **IPrintSchemaParameterInitializer** object.<br/> |
| [**Value**](iprintschemaparameterinitializer-putvalue.md)<br/> | Write-only<br/> | The **Value** (put\_Value) property modifies the value of the **IPrintSchemaParameterInitializer** object. <br/>    |



 

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                             |
| Header<br/>                   | <dl> <dt>Printerextension.h</dt> </dl> |



## See also

<dl> <dt>

[**IPrintSchemaElement**](iprintschemaelement-interface.md)
</dt> <dt>

[**IPrintSchematicket2::GetParameterInitializer**](iprintschematicket2-getparameterinitializer.md)
</dt> <dt>

[Print Schema Specification](http://msdn.microsoft.com/en-us/library/windows/hardware/gg463385.aspx)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintSchemaParameterInitializer%20interface%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





