---
Description: The IPrintSchemaTicket2 interface is an extension to the IPrintSchemaTicket interface, which provides wrapper methods over a print ticket document.
ms.assetid: 52D9FA01-578B-43C2-A0B1-F3CD0BAAFAE4
title: IPrintSchemaTicket2 interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IPrintSchemaTicket2 interface

The **IPrintSchemaTicket2** interface is an extension to the [**IPrintSchemaTicket**](iprintschematicket-interface.md) interface, which provides wrapper methods over a print ticket document.

## Members

The **IPrintSchemaTicket2** interface inherits from [**IPrintSchemaTicket**](iprintschematicket-interface.md). **IPrintSchemaTicket2** also has these types of members:

-   [Methods](#methods)

### Methods

The **IPrintSchemaTicket2** interface has these methods.



| Method                                                                         | Description                                                                                                                                                                                                                          |
|:-------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetParameterInitializer**](iprintschematicket2-getparameterinitializer.md) | The **GetParameterInitializer** method retrieves the [**IPrintSchemaParameterInitializer**](iprintschemaparameterinitializer.md) object, and it represents the &lt;psf:ParameterInit&gt; element in the PrintTicket XML.<br/> |



 

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                             |
| Header<br/>                   | <dl> <dt>Printerextension.h</dt> </dl> |



## See also

<dl> <dt>

[**IPrintSchemaTicket**](iprintschematicket-interface.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintSchemaTicket2%20interface%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





