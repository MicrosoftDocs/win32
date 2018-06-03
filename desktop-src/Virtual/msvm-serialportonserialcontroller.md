---
title: Msvm\_SerialPortOnSerialController class
description: Associates a serial port with a serial controller.
ms.assetid: 92e19191-44d1-4e2a-803d-1136f3c237a9
keywords:
- Msvm_SerialPortOnSerialController class Hyper-V
- Msvm_SerialPortOnSerialController class Hyper-V , described
topic_type:
- apiref
api_name:
- Msvm_SerialPortOnSerialController
- Msvm_SerialPortOnSerialController.Antecedent
- Msvm_SerialPortOnSerialController.Dependent
api_location:
- Root\Virtualization
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Msvm\_SerialPortOnSerialController class

Associates a serial port with a serial controller.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Association, Aggregation, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_SerialPortOnSerialController : CIM_PortOnDevice
{
  CIM_LogicalDevice REF Antecedent;
  CIM_LogicalPort   REF Dependent;
};
```

## Members

The **Msvm\_SerialPortOnSerialController** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_SerialPortOnSerialController** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_LogicalDevice**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The serial controller to which the port is connected.

This property is inherited from [**CIM\_PortOnDevice**](cim-portondevice.md).

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_LogicalPort**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The port of the serial controller.

This property is inherited from [**CIM\_PortOnDevice**](cim-portondevice.md).

</dd> </dl>

## Remarks

Access to the **Msvm\_SerialPortOnSerialController** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012 R2<br/>                                                                    |
| Namespace<br/>                | Root\\Virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_PortOnDevice**](cim-portondevice.md)
</dt> <dt>

[**CIM\_PortOnDevice**](https://msdn.microsoft.com/library/mt146187)
</dt> <dt>

[Serial Devices Classes](serial-devices-classes.md)
</dt> </dl>

 

 





