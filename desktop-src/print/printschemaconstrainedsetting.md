---
Description: The PrintSchemaConstrainedSetting enumeration specifies whether the Option is available based on the current device configuration. The constrained attribute appears only in a PrintCapabilities document.
ms.assetid: 637A210F-9FD7-49BD-AF71-8A77E07D5C20
title: PrintSchemaConstrainedSetting enumeration
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# PrintSchemaConstrainedSetting enumeration

The PrintSchemaConstrainedSetting enumeration specifies whether the Option is available based on the current device configuration. The **constrained** attribute appears only in a PrintCapabilities document.

## Syntax


```C++
typedef enum tagPrintSchemaConstrainedSetting { 
  PrintSchemaConstrainedSetting_None         = 0,
  PrintSchemaConstrainedSetting_PrintTicket  = 1,
  PrintSchemaConstrainedSetting_Admin        = 2,
  PrintSchemaConstrainedSetting_Device       = 3
} PrintSchemaConstrainedSetting;
```



## Constants

<dl> <dt>

<span id="PrintSchemaConstrainedSetting_None"></span><span id="printschemaconstrainedsetting_none"></span><span id="PRINTSCHEMACONSTRAINEDSETTING_NONE"></span>**PrintSchemaConstrainedSetting\_None**
</dt> <dd>

The Option is not constrained.

</dd> <dt>

<span id="PrintSchemaConstrainedSetting_PrintTicket"></span><span id="printschemaconstrainedsetting_printticket"></span><span id="PRINTSCHEMACONSTRAINEDSETTING_PRINTTICKET"></span>**PrintSchemaConstrainedSetting\_PrintTicket**
</dt> <dd>

The Option is constrained by the PrintTicket settings. Changing the PrintTicket document settings should be able to remove the constraint.

</dd> <dt>

<span id="PrintSchemaConstrainedSetting_Admin"></span><span id="printschemaconstrainedsetting_admin"></span><span id="PRINTSCHEMACONSTRAINEDSETTING_ADMIN"></span>**PrintSchemaConstrainedSetting\_Admin**
</dt> <dd>

The Option is constrained by the administrator's settings. The Option constraint should not be removable by a user without administrator privileges.

</dd> <dt>

<span id="PrintSchemaConstrainedSetting_Device"></span><span id="printschemaconstrainedsetting_device"></span><span id="PRINTSCHEMACONSTRAINEDSETTING_DEVICE"></span>**PrintSchemaConstrainedSetting\_Device**
</dt> <dd>

The Option is constrained by the device configuration. The Option should not be removable by either a user or administrator without changing the device configuration.

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Header<br/>                   | <dl> <dt>Printerextension.h</dt> </dl> |



## See also

<dl> <dt>

[**IPrintSchemaOption::Constrained**](iprintschemaoption-constrained.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20PrintSchemaConstrainedSetting%20enumeration%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





