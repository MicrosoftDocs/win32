---
title: CIM\_ProtocolControllerForUnit class
description: Represents an association between a protocol controller and an exposed logical unit.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: cae4ad07-c73d-4019-8117-ac5999990b2d
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_ProtocolControllerForUnit class
- CIM_ProtocolControllerForUnit class, described
topic_type:
- apiref
api_name:
- CIM_ProtocolControllerForUnit
- CIM_ProtocolControllerForUnit.DeviceNumber
- CIM_ProtocolControllerForUnit.AccessPriority
- CIM_ProtocolControllerForUnit.AccessState
- CIM_ProtocolControllerForUnit.Antecedent
- CIM_ProtocolControllerForUnit.Dependent
- CIM_ProtocolControllerForUnit.DeviceAccess
api_location:
- VMMS.exe
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_ProtocolControllerForUnit class

Represents an association between a protocol controller and an exposed logical unit. An example is an SCSI target controller that is linked to logical units. This subclass is provided so that an enumeration of related controllers and logical units can be accessed without retrieving connected ports or other controllers.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Abstract, Version("2.8.0"), UMLPackagePath("CIM::Device::ProtocolController")]
class CIM_ProtocolControllerForUnit : CIM_ProtocolControllerForDevice
{
  string                     DeviceNumber;
  uint16                     AccessPriority;
  uint16                     AccessState;
  CIM_ProtocolController REF Antecedent;
  CIM_LogicalDevice      REF Dependent;
  uint16                     DeviceAccess;
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

**DeviceAccess**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The access rights granted to the logical unit through the protocol controller.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Read_Write"></span><span id="read_write"></span><span id="READ_WRITE"></span>

<span id="Read_Write"></span><span id="read_write"></span><span id="READ_WRITE"></span>**Read Write** (2)


</dt> <dd></dd> <dt>

<span id="Read-Only"></span><span id="read-only"></span><span id="READ-ONLY"></span>

<span id="Read-Only"></span><span id="read-only"></span><span id="READ-ONLY"></span>**Read-Only** (3)


</dt> <dd></dd> <dt>

<span id="No_Access"></span><span id="no_access"></span><span id="NO_ACCESS"></span>

<span id="No_Access"></span><span id="no_access"></span><span id="NO_ACCESS"></span>**No Access** (4)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved**


</dt> <dd>

Reserved

</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>**Vendor Reserved**


</dt> <dd>

Reserved

</dd> </dl>

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



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**CIM\_ProtocolControllerForDevice**](cim-protocolcontrollerfordevice.md)
</dt> <dt>

[Failover Clustering Hyper-V WMI Provider](failover-clustering-hyper-v-wmi-provider-portal.md)
</dt> </dl>

 

 





