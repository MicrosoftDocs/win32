---
title: Msvm\_ProtocolControllerForUnit class
description: This association indicates that a subclass of logical device (for example a storage volume) is connected through a specific protocol controller.
ms.assetid: b7c24750-e88f-4b74-ac46-d9f624ff8cbf
keywords:
- Msvm_ProtocolControllerForUnit class Hyper-V
- Msvm_ProtocolControllerForUnit class Hyper-V , described
topic_type:
- apiref
api_name:
- Msvm_ProtocolControllerForUnit
- Msvm_ProtocolControllerForUnit.Antecedent
- Msvm_ProtocolControllerForUnit.Dependent
- Msvm_ProtocolControllerForUnit.DeviceNumber
- Msvm_ProtocolControllerForUnit.AccessPriority
- Msvm_ProtocolControllerForUnit.AccessState
api_location:
- Root\Virtualization
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Msvm\_ProtocolControllerForUnit class

This association indicates that a subclass of logical device (for example a storage volume) is connected through a specific protocol controller. In many situations (for example storage LUN masking), there may be many of these associations used to relate to different objects. Therefore, subclasses have been defined to optimize enumeration of the associations.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_ProtocolControllerForUnit : CIM_ProtocolControllerForUnit
{
  CIM_ProtocolController REF Antecedent;
  CIM_LogicalDevice      REF Dependent;
  string                     DeviceNumber;
  uint16                     AccessPriority;
  uint16                     AccessState;
};
```

## Members

The **Msvm\_ProtocolControllerForUnit** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_ProtocolControllerForUnit** class has these properties.

<dl> <dt>

**AccessPriority**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The priority given to accesses of the device through this controller. The highest priority path will have the lowest value for this parameter. This class is inherited from **CIM\_ProtocolControllerForDevice**.

</dd> <dt>

**AccessState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the controller is actively commanding or accessing the device (2) or not (3). Also, the value, 0 (Unknown), can be defined. This information is necessary when a logical device can be commanded by, or accessed through, multiple protocol controllers. This class is inherited from **CIM\_ProtocolControllerForDevice**.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Active"></span><span id="active"></span><span id="ACTIVE"></span>

**Active** (2)


</dt> <dd></dd> <dt>

<span id="Inactive"></span><span id="inactive"></span><span id="INACTIVE"></span>

**Inactive** (3)


</dt> <dd></dd> </dl>

</dd> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_ProtocolController**](https://msdn.microsoft.com/library/mt432251)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The protocol controller. This class is inherited from [**CIM\_ProtocolControllerForUnit**](https://msdn.microsoft.com/library/cc150672).

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The controlled device. This class is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884).

</dd> <dt>

**DeviceNumber**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The address of the associated device in the context of the antecedent controller. This class is inherited from **CIM\_ProtocolControllerForDevice**.

</dd> </dl>

## Remarks

Access to the **Msvm\_ProtocolControllerForUnit** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

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

[**CIM\_ProtocolControllerForUnit**](cim-protocolcontrollerforunit.md)
</dt> <dt>

[**CIM\_ProtocolControllerForUnit**](https://msdn.microsoft.com/library/cc150672)
</dt> <dt>

[Storage Classes](storage-classes.md)
</dt> </dl>

 

 





