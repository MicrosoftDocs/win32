---
title: Msvm\_CollectionSnapshotExportSettingData class
description: The export setting data to pass to the ExportSnapshot method of the Msvm\_CollectionSnapshotService class.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'f024a596-55e2-42c3-bec8-48b4da754d84'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Msvm_CollectionSnapshotExportSettingData class", "Msvm_CollectionSnapshotExportSettingData class, described"]
topic_type:
- apiref
api_name:
- Msvm_CollectionSnapshotExportSettingData
- Msvm_CollectionSnapshotExportSettingData.Caption
- Msvm_CollectionSnapshotExportSettingData.Description
- Msvm_CollectionSnapshotExportSettingData.InstanceID
- Msvm_CollectionSnapshotExportSettingData.ElementName
- Msvm_CollectionSnapshotExportSettingData.CopyVmStorage
- Msvm_CollectionSnapshotExportSettingData.DifferentialBackupBase
- Msvm_CollectionSnapshotExportSettingData.BackupIntent
api_location:
- VMMS.exe
api_type:
- DllExport
---

# Msvm\_CollectionSnapshotExportSettingData class

The export setting data to pass to the [**ExportSnapshot**](msvm-collectionsnapshotservice-exportsnapshot.md) method of the [**Msvm\_CollectionSnapshotService**](msvm-collectionsnapshotservice.md) class.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_CollectionSnapshotExportSettingData : CIM_SettingData
{
  string  Caption;
  string  Description;
  string  InstanceID;
  string  ElementName;
  boolean CopyVmStorage;
  string  DifferentialBackupBase;
  uint16  BackupIntent;
};
```

## Members

The **Msvm\_CollectionSnapshotExportSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_CollectionSnapshotExportSettingData** class has these properties.

<dl> <dt>

**BackupIntent**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates the intent how the exported backup sets would be used

<dt>

<span id="BackupIntentPreserveChain"></span><span id="backupintentpreservechain"></span><span id="BACKUPINTENTPRESERVECHAIN"></span>

<span id="BackupIntentPreserveChain"></span><span id="backupintentpreservechain"></span><span id="BACKUPINTENTPRESERVECHAIN"></span>**BackupIntentPreserveChain** (1)


</dt> <dd>

All exported full and differential backup sets would be preserved as they are.

</dd> <dt>

<span id="BackupIntentMerge"></span><span id="backupintentmerge"></span><span id="BACKUPINTENTMERGE"></span>

<span id="BackupIntentMerge"></span><span id="backupintentmerge"></span><span id="BACKUPINTENTMERGE"></span>**BackupIntentMerge** (2)


</dt> <dd>

The exported full and differential backup sets would be merged to synthesize full backup sets.

</dd> </dl>

</dd> <dt>

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

**CopyVmStorage**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**true** to copy VM storage when a VM is exported; otherwise, **false**.

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

**DifferentialBackupBase**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The base for a differential export. This value is either path to a [**Msvm\_ReferencePointCollection**](msvm-referencepointcollection.md) instance that represents the reference point, or path to a [**Msvm\_SnapshotCollection**](msvm-snapshotcollection.md) instance that represents the snapshot to use as a base for a differential export.

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The user-friendly name for an instance of this class. In addition, the user-friendly name can be used as an index for a search or query. The name does not have to be unique within a namespace.

This property is inherited from [**CIM\_SettingData**](cim-settingdata.md).

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Uniquely identifies an instance of this class within the scope of the containing namespace.

> \[!Important\]
>
> In order to ensure uniqueness within the namespace, the value of the **InstanceID** property should be constructed in the following pattern: *OrgID*:*LocalID*
>
> -   *OrgID* must include a copyrighted, trademarked or otherwise unique name that is owned by the business entity that defines the **InstanceID** property, or be a registered ID that is assigned by a recognized global authority.
> -   *OrgID* must not contain a colon. The first colon in **InstanceID** must be between the *OrgID* and*LocalID*.
> -   *LocalID* is chosen by the business entity and should not be re-used to identify different underlying real-world elements.
> -   If the above pattern is not used, the defining entity must assure that the resultant **InstanceID** value is not re-used across any **InstanceID** properties that are produced by this provider or other providers for this namespace.
> -   For DMTF defined instances, the pattern must be used with the *OrgID* set to "CIM".

 

This property is inherited from [**CIM\_SettingData**](cim-settingdata.md).

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**CIM\_SettingData**](cim-settingdata.md)
</dt> <dt>

[Failover Clustering Hyper-V WMI Provider](failover-clustering-hyper-v-wmi-provider-portal.md)
</dt> </dl>

 

 





