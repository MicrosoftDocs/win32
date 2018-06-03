---
title: Msvm\_VirtualSystemExportSettingData class
description: Provides additional information to be used with the ExportVirtualSystemEx method of the Msvm\_VirtualSystemManagementService class.
ms.assetid: 0974e237-4c3e-43bc-ada5-645f1d6f895b
keywords:
- Msvm_VirtualSystemExportSettingData class Hyper-V
- Msvm_VirtualSystemExportSettingData class Hyper-V , described
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemExportSettingData
- Msvm_VirtualSystemExportSettingData.Caption
- Msvm_VirtualSystemExportSettingData.Description
- Msvm_VirtualSystemExportSettingData.InstanceID
- Msvm_VirtualSystemExportSettingData.ElementName
- Msvm_VirtualSystemExportSettingData.CopyVmStorage
- Msvm_VirtualSystemExportSettingData.CopyVmRuntimeInformation
- Msvm_VirtualSystemExportSettingData.CreateVmExportSubdirectory
- Msvm_VirtualSystemExportSettingData.CopySnapshotConfiguration
- Msvm_VirtualSystemExportSettingData.SnapshotVirtualSystem
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

# Msvm\_VirtualSystemExportSettingData class

Provides additional information to be used with the [**ExportVirtualSystemEx**](msvm-virtualsystemmanagementservice-exportvirtualsystemex.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_VirtualSystemExportSettingData : CIM_SettingData
{
  string  Caption;
  string  Description;
  string  InstanceID;
  string  ElementName;
  boolean CopyVmStorage;
  boolean CopyVmRuntimeInformation;
  boolean CreateVmExportSubdirectory;
  uint8   CopySnapshotConfiguration;
  string  SnapshotVirtualSystem;
};
```

## Members

The **Msvm\_VirtualSystemExportSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_VirtualSystemExportSettingData** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

A short description (one-line string) of the object. This property is inherited from [**CIM\_SettingData**](https://msdn.microsoft.com/library/cc136911).

</dd> <dt>

**CopySnapshotConfiguration**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates what snapshots are to be exported with the VM.

<dt>

<span id="ExportAllSnapshots"></span><span id="exportallsnapshots"></span><span id="EXPORTALLSNAPSHOTS"></span>

<span id="ExportAllSnapshots"></span><span id="exportallsnapshots"></span><span id="EXPORTALLSNAPSHOTS"></span>**ExportAllSnapshots** (0)


</dt> <dd>

All snapshots will be exported with the VM.

</dd> <dt>

<span id="ExportNoSnapshots"></span><span id="exportnosnapshots"></span><span id="EXPORTNOSNAPSHOTS"></span>

<span id="ExportNoSnapshots"></span><span id="exportnosnapshots"></span><span id="EXPORTNOSNAPSHOTS"></span>**ExportNoSnapshots** (1)


</dt> <dd>

No snapshots will be exported with the VM.

</dd> <dt>

<span id="ExportOneSnapshot"></span><span id="exportonesnapshot"></span><span id="EXPORTONESNAPSHOT"></span>

<span id="ExportOneSnapshot"></span><span id="exportonesnapshot"></span><span id="EXPORTONESNAPSHOT"></span>**ExportOneSnapshot** (2)


</dt> <dd>

The snapshots identified by the **SnapshotVirtualSystem** property will be exported with the VM. The **CopyVmStorage** and **CopyVmRuntimeInformation** properties are ignored, storage and run-time information is exported with the VM, and any VHD differencing disks will be merged into a new VHD.

</dd> </dl>

</dd> <dt>

**CopyVmRuntimeInformation**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether the VM run-time information will be copied when the VM is exported.



| Value                                                                                | Meaning                                                    |
|--------------------------------------------------------------------------------------|------------------------------------------------------------|
| <dl> <dt>**TRUE**</dt> </dl>  | The VM run-time information will be copied.<br/>     |
| <dl> <dt>**FALSE**</dt> </dl> | The VM run-time information will not be copied.<br/> |



 

</dd> <dt>

**CopyVmStorage**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether the VM storage will be copied when the VM is exported.



| Value                                                                                | Meaning                                       |
|--------------------------------------------------------------------------------------|-----------------------------------------------|
| <dl> <dt>**TRUE**</dt> </dl>  | The VM storage will be copied.<br/>     |
| <dl> <dt>**FALSE**</dt> </dl> | The VM storage will not be copied.<br/> |



 

</dd> <dt>

**CreateVmExportSubdirectory**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether a subdirectory with the name of the VM will be created when the VM is exported.



| Value                                                                                | Meaning                                        |
|--------------------------------------------------------------------------------------|------------------------------------------------|
| <dl> <dt>**TRUE**</dt> </dl>  | A subdirectory will be created.<br/>     |
| <dl> <dt>**FALSE**</dt> </dl> | A subdirectory will not be created.<br/> |



 

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A description of the object. This property is inherited from [**CIM\_SettingData**](https://msdn.microsoft.com/library/cc136911).

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The display name for this instance. In addition, the display name can be used as an index property for a search or query. (Note: The name does not have to be unique within a namespace.) This property is inherited from [**CIM\_SettingData**](https://msdn.microsoft.com/library/cc136911).

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Within the scope of the instantiating Namespace, **InstanceID** opaquely and uniquely identifies an instance of this class. This property is inherited from [**CIM\_SettingData**](https://msdn.microsoft.com/library/cc136911).

</dd> <dt>

**SnapshotVirtualSystem**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Path to a [**Msvm\_VirtualSystemSettingData**](msvm-virtualsystemsettingdata.md) instance that represents the snapshot to be exported with the VM. If the **CopySnapshotConfiguration** property is not set to 2 (ExportOneSnapshot), this property is ignored.

</dd> </dl>

## Remarks

Access to the **Msvm\_VirtualSystemExportSettingData** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                                    |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012 R2<br/>                                                                    |
| Namespace<br/>                | Root\\Virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_SettingData**](cim-settingdata.md)
</dt> <dt>

[Virtual System Management Classes](virtual-system-management-classes.md)
</dt> <dt>

[**ExportVirtualSystemEx**](msvm-virtualsystemmanagementservice-exportvirtualsystemex.md)
</dt> </dl>

 

 





