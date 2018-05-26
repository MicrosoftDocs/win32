---
title: Win32\_ControllerHasHub class
description: The Win32\_ControllerHasHub association WMI class represents the hubs downstream from the universal serial bus (USB) controller.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 64e5a2d9-a653-4269-b965-b29e07940773
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Win32_ControllerHasHub class
- Win32_ControllerHasHub class, described
topic_type:
- apiref
api_name:
- Win32_ControllerHasHub
- Win32_ControllerHasHub.AccessState
- Win32_ControllerHasHub.NegotiatedDataWidth
- Win32_ControllerHasHub.NegotiatedSpeed
- Win32_ControllerHasHub.NumberOfHardResets
- Win32_ControllerHasHub.NumberOfSoftResets
- Win32_ControllerHasHub.Dependent
- Win32_ControllerHasHub.Antecedent
api_location:
- Wmipcima.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Win32\_ControllerHasHub class

The **Win32\_ControllerHasHub** association [WMI class](https://msdn.microsoft.com/library/aa393244) represents the hubs downstream from the universal serial bus (USB) controller.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32a"), AMENDMENT]
class Win32_ControllerHasHub : CIM_USBControllerHasHub
{
  uint16                  AccessState;
  uint32                  NegotiatedDataWidth;
  uint64                  NegotiatedSpeed;
  uint32                  NumberOfHardResets;
  uint32                  NumberOfSoftResets;
  Win32_USBHub        REF Dependent;
  Win32_USBController REF Antecedent;
};
```

## Members

The **Win32\_ControllerHasHub** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_ControllerHasHub** class has these properties.

<dl> <dt>

**AccessState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

When a logical device can be commanded by or accessed through multiple controllers, this property indicates whether the controller is actively commanding or accessing the device. This property is inherited from [**CIM\_ControlledBy**](https://msdn.microsoft.com/library/aa387230).

<dt>

0
</dt> <dd>

Unknown

</dd> <dt>

1
</dt> <dd>

Active

</dd> <dt>

2
</dt> <dd>

Inactive

</dd> </dl>

</dd> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_USBController**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent"), [**Min**](https://msdn.microsoft.com/library/aa393650) (1), [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The USBController.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_USBHub**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent"), [**Min**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

Reference to an instance that represents the USB hub associated with the controller. This property is inherited from [**CIM\_Dependency**](https://msdn.microsoft.com/library/aa387238).

</dd> <dt>

**NegotiatedDataWidth**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

When several bus or connection data widths are possible, this property defines the one in use between the devices. Data width is specified in bits. If the data width is not negotiated, or if this information is not available or important to device management, the property should be set to 0. This property is inherited from [**CIM\_DeviceConnection**](https://msdn.microsoft.com/library/aa387242).

</dd> <dt>

**NegotiatedSpeed**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

When several bus or connection speeds are possible, this property defines the one in use between the devices. Speed is specified in bits-per-second. If connection or bus speeds are not negotiated, or if this information is not available or important to device management, the property should be set to 0 (zero). This property is inherited from [**CIM\_DeviceConnection**](https://msdn.microsoft.com/library/aa387242).

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> <dt>

**NumberOfHardResets**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of hard resets issued by the controller. A hard reset returns the device to its initialization or boot-up state. All internal device state information and data are lost. This property is inherited from [**CIM\_ControlledBy**](https://msdn.microsoft.com/library/aa387230).

</dd> <dt>

**NumberOfSoftResets**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of soft resets issued by the controller. A soft reset does not completely clear current device state and data. Exact semantics are dependent on the device and on the protocols and mechanisms used to communicate with it. This property is inherited from [**CIM\_ControlledBy**](https://msdn.microsoft.com/library/aa387230).

</dd> </dl>

## Remarks

The **Win32\_ControllerHasHub** class is inherited from [**CIM\_ControlledBy**](https://msdn.microsoft.com/library/aa387230).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Wmipcima.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wmipcima.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_USBControllerHasHub**](https://msdn.microsoft.com/library/aa388647)
</dt> <dt>

[Computer System Hardware Classes](https://msdn.microsoft.com/library/aa389273)
</dt> </dl>

 

 





