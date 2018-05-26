---
title: CIM\_ProtocolControllerForUnit class
description: This association is used to define a relationship between a ProtocolController and an exposed Logical Unit (for example a Storage Volume or a MediaAccessDevice such as a tape drive).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3ced85bb-2546-443b-bd51-8b41bc1ff42a
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_ProtocolControllerForUnit class iSCSI Software Target API
- CIM_ProtocolControllerForUnit class iSCSI Software Target API , described
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
- SMiSCSITargetProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_ProtocolControllerForUnit class

This association is used to define a relationship between a ProtocolController and an exposed Logical Unit (for example a Storage Volume or a MediaAccessDevice such as a tape drive). An example of the use of this association is SCSI, where it link the target controller and Logical Units. This subclass is provided so that an enumeration of related controllers and units can be performed without retrieving any connected ports or other controllers.

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

This property describes the priority given to accesses of the device through this Controller. The highest priority path will have the lowest value for this parameter.

This property is inherited from [**CIM\_ProtocolControllerForDevice**](cim-protocolcontrollerfordevice.md).

</dd> <dt>

**AccessState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The AccessState property describes the accessibility of the LogicalDevice through the ProtocolController.

Unknown (0) indicates the instrumentation does not know whether access is or is not functioning.

Active (2) indicates normal access.

Inactive (3) indicates the instrumentation knows this path is not active, and one of the other values (below) does not apply.

Replication in Progress (4) indicates that the path is temporarily inactive due to a replication activity.

Mapping Inconsistency (5) indicates the instrumentation has detected that this path is inactive due to an inconsistency in the DeviceNumber/DeviceAccess configuration.

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

The ProtocolController.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_LogicalDevice**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

The logical unit (eg StorageVolume) 'behind' the ProtocolController.

</dd> <dt>

**DeviceAccess**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The access rights granted to the referenced logical unit as exposed through referenced ProtocolController. The 'No Access' value is used in implementations where the DeviceNumber is reserved, but no access is granted.

If the instrumentation exposes PrivilegeManagementService, this property MUST be synchronized with the Activities property of any Privilege instances associated with StorageHardwareIDs associated to the referenced ProtocolController and the referenced LogicalDevice. In particular, when this property is 'Read Write', Privilege.Activities MUST include entries for 'Read' and 'Write'. When this property is 'Read-Only', Privilege.Activities MUST include an entry for 'Read'. The corresponding entries for Privilege.ActivityQualifiers MUST be 'CDB=\*' and the corresponding entries for Privilege.QualifierFormat MUST be 'SCSI Command'.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Read_Write"></span><span id="read_write"></span><span id="READ_WRITE"></span>

**Read Write** (2)


</dt> <dd></dd> <dt>

<span id="Read-Only"></span><span id="read-only"></span><span id="READ-ONLY"></span>

**Read-Only** (3)


</dt> <dd></dd> <dt>

<span id="No_Access"></span><span id="no_access"></span><span id="NO_ACCESS"></span>

**No Access** (4)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>5 15999</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>16000 65535</dd> </dl>

</dd> <dt>

**DeviceNumber**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Address of the associated Device in the context of the Antecedent Controller.

This property is inherited from [**CIM\_ProtocolControllerForDevice**](cim-protocolcontrollerfordevice.md).

</dd> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ProtocolControllerForDevice**](cim-protocolcontrollerfordevice.md)
</dt> </dl>

 

 





