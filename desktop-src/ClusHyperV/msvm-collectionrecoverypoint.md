---
title: Msvm\_CollectionRecoveryPoint class
description: Represents a recovery point of a collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 630b6d65-93e9-4e7d-b4ab-7ab5f392cda8
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Msvm_CollectionRecoveryPoint class
- Msvm_CollectionRecoveryPoint class, described
topic_type:
- apiref
api_name:
- Msvm_CollectionRecoveryPoint
- Msvm_CollectionRecoveryPoint.Caption
- Msvm_CollectionRecoveryPoint.Description
- Msvm_CollectionRecoveryPoint.InstanceID
- Msvm_CollectionRecoveryPoint.CollectionID
- Msvm_CollectionRecoveryPoint.ElementName
- Msvm_CollectionRecoveryPoint.CreationTime
- Msvm_CollectionRecoveryPoint.VirtualMachineIds
- Msvm_CollectionRecoveryPoint.RecoveryPointIds
- Msvm_CollectionRecoveryPoint.ConsistencyLevel
api_location:
- VMMS.exe
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Msvm\_CollectionRecoveryPoint class

Represents a recovery point of a collection.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_CollectionRecoveryPoint : CIM_ManagedElement
{
  string   Caption;
  string   Description;
  string   InstanceID;
  string   CollectionID;
  string   ElementName;
  datetime CreationTime;
  string   VirtualMachineIds[];
  string   RecoveryPointIds[];
  uint16   ConsistencyLevel;
};
```

## Members

The **Msvm\_CollectionRecoveryPoint** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_CollectionRecoveryPoint** class has these properties.

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

**CollectionID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The unique identification of the collection object to which the recovery point belongs.

</dd> <dt>

**ConsistencyLevel**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Consistency level of the recovery point.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Application_Consistent"></span><span id="application_consistent"></span><span id="APPLICATION_CONSISTENT"></span>

<span id="Application_Consistent"></span><span id="application_consistent"></span><span id="APPLICATION_CONSISTENT"></span>**Application Consistent** (1)


</dt> <dd>

The recovery point indicates a point in time when the virtual system was in application consistent state.

</dd> <dt>

<span id="Crash_Consistent"></span><span id="crash_consistent"></span><span id="CRASH_CONSISTENT"></span>

<span id="Crash_Consistent"></span><span id="crash_consistent"></span><span id="CRASH_CONSISTENT"></span>**Crash Consistent** (2)


</dt> <dd>

The recovery point indicates a point in time when the virtual system was in crash consistent state.

</dd> <dt>

<span id="Group_Crash_Consistent"></span><span id="group_crash_consistent"></span><span id="GROUP_CRASH_CONSISTENT"></span>

<span id="Group_Crash_Consistent"></span><span id="group_crash_consistent"></span><span id="GROUP_CRASH_CONSISTENT"></span>**Group Crash Consistent** (3)


</dt> <dd>

The recovery point indicates a point in time when the group was in crash consistent state.

</dd> </dl>

</dd> <dt>

**CreationTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Time when the collection recovery point was created.

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
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("ElementName")
</dt> </dl>

A user-defined name for the collection. Note this is not guaranteed to be unique.

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("InstanceID"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The unique identification of the recovery point object of a collection.

</dd> <dt>

**RecoveryPointIds**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed")
</dt> </dl>

Array of recovery point IDs which are members of this collection recovery point.

</dd> <dt>

**VirtualMachineIds**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed")
</dt> </dl>

Array of virtual machine IDs which are members of this collection recovery point.

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**CIM\_ManagedElement**](cim-managedelement.md)
</dt> </dl>

 

 





