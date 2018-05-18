---
title: CIM\_ProtocolControllerForUnit class
description: Represents an association between a protocol controller and an exposed logical unit.
ms.assetid: 'b88d954c-cde8-4693-8bd2-044a4c2c1257'
keywords: ["CIM_ProtocolControllerForUnit class Hyper-V", "CIM_ProtocolControllerForUnit class Hyper-V , described"]
topic_type:
- apiref
api_name:
- CIM_ProtocolControllerForUnit
- CIM_ProtocolControllerForUnit.DeviceNumber
- CIM_ProtocolControllerForUnit.AccessPriority
- CIM_ProtocolControllerForUnit.AccessState
- CIM_ProtocolControllerForUnit.Antecedent
- CIM_ProtocolControllerForUnit.Dependent
api_location:
- Root\virtualization
api_type:
- Schema
---

# CIM\_ProtocolControllerForUnit class

Represents an association between a protocol controller and an exposed logical unit. An example is an SCSI target controller that is linked to logical units. This subclass is provided so that an enumeration of related controllers and logical units can be accessed without retrieving connected ports or other controllers.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, Association, Version("2.8.0"), AMENDMENT]
class CIM_ProtocolControllerForUnit : CIM_ProtocolControllerForDevice
{
  string                     DeviceNumber;
  uint16                     AccessPriority;
  uint16                     AccessState;
  CIM_ProtocolController REF Antecedent;
  CIM_LogicalDevice      REF Dependent;
};
```

## Members

The **CIM\_ProtocolControllerForUnit** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_ProtocolControllerForUnit** class has these properties.

<dl> <dt>

**AccessPriority**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The access priority given to the device through the protocol controller. The highest priority has the lowest value.

This property is inherited from [**CIM\_ProtocolControllerForDevice**](cim-protocolcontrollerfordevice.md).

</dd> <dt>

**AccessState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The accessibility of the logical device through the protocol controller

This property is inherited from [**CIM\_ProtocolControllerForDevice**](cim-protocolcontrollerfordevice.md).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Active"></span><span id="active"></span><span id="ACTIVE"></span>

**Active** (2)


</dt> <dd></dd> <dt>

<span id="Inactive"></span><span id="inactive"></span><span id="INACTIVE"></span>

**Inactive** (3)


</dt> <dd></dd> <dt>

<span id="Replication_In_Progress"></span><span id="replication_in_progress"></span><span id="REPLICATION_IN_PROGRESS"></span>

**Replication In Progress** (4)


</dt> <dd></dd> <dt>

<span id="Mapping_Inconsistency"></span><span id="mapping_inconsistency"></span><span id="MAPPING_INCONSISTENCY"></span>

**Mapping Inconsistency** (5)


</dt> <dd></dd> </dl>

</dd> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ProtocolController**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent")
</dt> </dl>

The protocol controller.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_LogicalDevice**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

The logical unit associated with the protocol controller.

</dd> <dt>

**DeviceNumber**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The address of the associated device in the context of the protocol controler.

This property is inherited from [**CIM\_ProtocolControllerForDevice**](cim-protocolcontrollerfordevice.md).

</dd> </dl>

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012 R2<br/>                                                                    |
| Namespace<br/>                | Root\\virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ProtocolControllerForDevice**](cim-protocolcontrollerfordevice.md)
</dt> </dl>

 

 





