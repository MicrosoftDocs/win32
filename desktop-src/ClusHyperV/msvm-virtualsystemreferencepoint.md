---
title: Msvm\_VirtualSystemReferencePoint class
description: Represents a reference point for a virtual machine.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ad2ed23c-aa47-4610-a0a6-161a0e55aed1
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Msvm_VirtualSystemReferencePoint class
- Msvm_VirtualSystemReferencePoint class, described
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemReferencePoint
- Msvm_VirtualSystemReferencePoint.Caption
- Msvm_VirtualSystemReferencePoint.Description
- Msvm_VirtualSystemReferencePoint.ElementName
- Msvm_VirtualSystemReferencePoint.InstanceID
- Msvm_VirtualSystemReferencePoint.ReferencePointType
- Msvm_VirtualSystemReferencePoint.ConsistencyLevel
- Msvm_VirtualSystemReferencePoint.VirtualSystemIdentifier
- Msvm_VirtualSystemReferencePoint.HasAssociatedData
- Msvm_VirtualSystemReferencePoint.VirtualDiskIdentifiers
- Msvm_VirtualSystemReferencePoint.ResilientChangeTrackingIdentifiers
api_location:
- VMMS.exe
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Msvm\_VirtualSystemReferencePoint class

Represents a reference point for a virtual machine.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_VirtualSystemReferencePoint : CIM_ManagedElement
{
  string  Caption;
  string  Description;
  string  ElementName;
  string  InstanceID;
  uint16  ReferencePointType;
  uint16  ConsistencyLevel;
  string  VirtualSystemIdentifier;
  boolean HasAssociatedData;
  string  VirtualDiskIdentifiers[];
  string  ResilientChangeTrackingIdentifiers[];
};
```

## Members

The **Msvm\_VirtualSystemReferencePoint** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_VirtualSystemReferencePoint** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

A short textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**ConsistencyLevel**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The consistency level of the reference point.

<dt>

<span id="Application_Consistent"></span><span id="application_consistent"></span><span id="APPLICATION_CONSISTENT"></span>

<span id="Application_Consistent"></span><span id="application_consistent"></span><span id="APPLICATION_CONSISTENT"></span>**Application Consistent** (1)


</dt> <dd>

The reference point indicates a point in time when the virtual machine was in an application consistent state.

</dd> <dt>

<span id="Crash_Consistent"></span><span id="crash_consistent"></span><span id="CRASH_CONSISTENT"></span>

<span id="Crash_Consistent"></span><span id="crash_consistent"></span><span id="CRASH_CONSISTENT"></span>**Crash Consistent** (2)


</dt> <dd>

The reference point indicates a point in time when the virtual machine was in a crash consistent state.

</dd> </dl>

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties, identity data, and description information.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**HasAssociatedData**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**true** if the reference point is log based and has associated data; otherwise, **false**. For log based reference points, once the log is discarded this value becomes **false**.

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("InstanceID"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The unique identification of the reference point object.

</dd> <dt>

**ReferencePointType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The type of the reference point.

The possible values are:

<dt>

<span id="Log_based"></span><span id="log_based"></span><span id="LOG_BASED"></span>

<span id="Log_based"></span><span id="log_based"></span><span id="LOG_BASED"></span>**Log based** (1)


</dt> <dd>

Hyper-V replica log tracking.

</dd> <dt>

<span id="RCT_based"></span><span id="rct_based"></span><span id="RCT_BASED"></span>

<span id="RCT_based"></span><span id="rct_based"></span><span id="RCT_BASED"></span>**RCT based** (2)


</dt> <dd>

Resilient Change Tracking (RCT) of virtual disks.

</dd> </dl>

</dd> <dt>

**ResilientChangeTrackingIdentifiers**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array of RCT IDs that correspond to the virtual disks of the VM when reference point was created. This property is only used by RCT based reference points.

</dd> <dt>

**VirtualDiskIdentifiers**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array of WMI instance IDs that correspond to the virtual disks of the VM when the reference point was created. The virtual disks have RCT IDs associated with them.

</dd> <dt>

**VirtualSystemIdentifier**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ComputerSystem**](cim-computersystem.md).**Name**")
</dt> </dl>

The name of the [**CIM\_ComputerSystem**](cim-computersystem.md) that contains the reference point.

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

[**CIM\_ManagedElement**](cim-managedelement.md)
</dt> <dt>

[Failover Clustering Hyper-V WMI Provider](failover-clustering-hyper-v-wmi-provider-portal.md)
</dt> </dl>

 

 





