---
title: Msvm\_VirtualSystemImportSettingData class
description: Represents settings of a virtual system to import.
ms.assetid: 'd121369f-9b97-48af-ba84-3349ea4e48c5'
keywords: ["Msvm_VirtualSystemImportSettingData class Hyper-V", "Msvm_VirtualSystemImportSettingData class Hyper-V , described"]
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemImportSettingData
- Msvm_VirtualSystemImportSettingData.Caption
- Msvm_VirtualSystemImportSettingData.Description
- Msvm_VirtualSystemImportSettingData.InstanceID
- Msvm_VirtualSystemImportSettingData.ElementName
- Msvm_VirtualSystemImportSettingData.GenerateNewId
- Msvm_VirtualSystemImportSettingData.CreateCopy
- Msvm_VirtualSystemImportSettingData.Name
- Msvm_VirtualSystemImportSettingData.SourceVmDataRoot
- Msvm_VirtualSystemImportSettingData.SourceSnapshotDataRoot
- Msvm_VirtualSystemImportSettingData.SourceVhdDataRoot
- Msvm_VirtualSystemImportSettingData.TargetVmDataRoot
- Msvm_VirtualSystemImportSettingData.TargetSnapshotDataRoot
- Msvm_VirtualSystemImportSettingData.TargetVhdDataRoot
- Msvm_VirtualSystemImportSettingData.SecurityScope
- Msvm_VirtualSystemImportSettingData.CurrentResourcePaths
- Msvm_VirtualSystemImportSettingData.SourceResourcePaths
- Msvm_VirtualSystemImportSettingData.TargetResourcePaths
- Msvm_VirtualSystemImportSettingData.SourceNetworkConnections
- Msvm_VirtualSystemImportSettingData.TargetNetworkConnections
api_location:
- Root\Virtualization
api_type:
- Schema
---

# Msvm\_VirtualSystemImportSettingData class

Represents settings of a virtual system to import. Used by the [**ImportVirtualSystemEx**](msvm-virtualsystemmanagementservice-importvirtualsystemex.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[AMENDMENT]
class Msvm_VirtualSystemImportSettingData : CIM_SettingData
{
  string  Caption;
  string  Description;
  string  InstanceID;
  string  ElementName;
  boolean GenerateNewId;
  boolean CreateCopy;
  string  Name;
  string  SourceVmDataRoot;
  string  SourceSnapshotDataRoot;
  string  SourceVhdDataRoot;
  string  TargetVmDataRoot;
  string  TargetSnapshotDataRoot;
  string  TargetVhdDataRoot;
  string  SecurityScope;
  string  CurrentResourcePaths[];
  string  SourceResourcePaths[];
  string  TargetResourcePaths[];
  string  SourceNetworkConnections[];
  string  TargetNetworkConnections[];
};
```

## Members

The **Msvm\_VirtualSystemImportSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_VirtualSystemImportSettingData** class has these properties.

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

**CreateCopy**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether the VM will be copied when imported.



| Value                                                                                | Meaning                                                                                                                                                                                                                                                                                                                        |
|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**TRUE**</dt> </dl>  | The VM will be copied when imported. The **TargetVmDataRoot**, **TargetSnapshotDataRoot**, **TargetVhdDataRoot** properties give the target for the new copy. The **TargetResourcePaths** property gives the target paths for the copies made from the resources specified in the **SourceResourcePaths** property.<br/> |
| <dl> <dt>**FALSE**</dt> </dl> | The VM will not be copied when imported. The **TargetVmDataRoot**, **TargetSnapshotDataRoot**, **TargetVhdDataRoot**, and **TargetResourcePaths** properties are ignored.<br/>                                                                                                                                           |



 

</dd> <dt>

**CurrentResourcePaths**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed")
</dt> </dl>

Array of strings that represents the current resources of the VM that is being imported. Each resource is represented as one string.

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

**GenerateNewId**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether new IDs will be generated for VMs that are imported.



| Value                                                                                | Meaning                                  |
|--------------------------------------------------------------------------------------|------------------------------------------|
| <dl> <dt>**TRUE**</dt> </dl>  | New IDs will be generated.<br/>    |
| <dl> <dt>**FALSE**</dt> </dl> | The IDs will remain the same.<br/> |



 

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Within the scope of the instantiating Namespace, **InstanceID** property opaquely and uniquely identifies an instance of this class. This property is inherited from [**CIM\_SettingData**](https://msdn.microsoft.com/library/cc136911).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If set, the imported VM will have this name.

</dd> <dt>

**SecurityScope**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If set, the imported VM will have this set as the **ScopeOfResidence** property.

</dd> <dt>

**SourceNetworkConnections**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed")
</dt> </dl>

Array of strings containing the **FriendlyName** properties of the source switches to which the VM is connected.

</dd> <dt>

**SourceResourcePaths**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed")
</dt> </dl>

Array of strings containing the source locations for the resources specified in the **CurrentResourcePaths** property.

</dd> <dt>

**SourceSnapshotDataRoot**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Represents the folder for the snapshot data files for the VM being imported. If VM was exported without state information, this property should contain the SnapshotDataRoot where the VM state files are present. [**ImportVirtualSystemEx**](msvm-virtualsystemmanagementservice-importvirtualsystemex.md) will not import the VM if a VM was exported without a state and this property is not satisfied. If VM is exported with state, this property will contain the SnapshotDataRoot directory under Import Directory.

</dd> <dt>

**SourceVhdDataRoot**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Represents the folder for the VM VHD data files for the VM being imported. If VM was exported without state information, this property should contain the VhdDataRoot where the VM state files are present. [**ImportVirtualSystemEx**](msvm-virtualsystemmanagementservice-importvirtualsystemex.md) will not import the VM if a VM was exported without a state and this property is not satisfied. If VM is exported with state, this property will contain the VhdDataRoot directory under Import Directory. If the VHD files are being stored on different directories, they will be specified with the **SourceResourcePaths** and **TargetResourcePaths** properties. In this case, this property will be ignored.

</dd> <dt>

**SourceVmDataRoot**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Represents the folder for the VM data files for the VM being imported. If VM was exported without state information, this property should contain the VmDataRoot where the VM state files are present. [**ImportVirtualSystemEx**](msvm-virtualsystemmanagementservice-importvirtualsystemex.md) will not import the VM if a VM was exported without a state and this property is not satisfied. If VM is exported with state, this property will contain the VmDataRoot directory under Import Directory.

</dd> <dt>

**TargetNetworkConnections**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed")
</dt> </dl>

Array of strings containing the **FriendlyName** properties for the target switches to which the VM is to be connected.

</dd> <dt>

**TargetResourcePaths**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed")
</dt> </dl>

Array of strings containing the target locations for the resources specified in the **CurrentResourcePaths** property.

</dd> <dt>

**TargetSnapshotDataRoot**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Represents the target snapshot data root for the VM being imported if the **CreateCopy** property is set to **TRUE**. If the **CreateCopy** property is set to **FALSE**, this property is ignored.

</dd> <dt>

**TargetVhdDataRoot**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Represents the target VHD data root for the VM being imported if the **CreateCopy** property is set to **TRUE**. If the **CreateCopy** property is set to **FALSE**, this property is ignored.

</dd> <dt>

**TargetVmDataRoot**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Represents the target VM data root for the VM being imported if the **CreateCopy** property is set to **TRUE**. If the **CreateCopy** property is set to **FALSE**, this property is ignored.

</dd> </dl>

## Remarks

Access to the **Msvm\_VirtualSystemImportSettingData** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                                    |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012 R2<br/>                                                                    |
| Namespace<br/>                | Root\\Virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_SettingData**](cim-settingdata.md)
</dt> <dt>

[Virtual System Management Classes](virtual-system-management-classes.md)
</dt> <dt>

[**ImportVirtualSystemEx**](msvm-virtualsystemmanagementservice-importvirtualsystemex.md)
</dt> </dl>

 

 





