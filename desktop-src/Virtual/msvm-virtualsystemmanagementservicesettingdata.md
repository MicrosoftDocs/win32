---
title: Msvm\_VirtualSystemManagementServiceSettingData class
description: Represents the settings for the virtualization service present on a single host system.
ms.assetid: 52681cf1-1db0-475f-8566-a2501dd456be
keywords:
- Msvm_VirtualSystemManagementServiceSettingData class Hyper-V
- Msvm_VirtualSystemManagementServiceSettingData class Hyper-V , described
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemManagementServiceSettingData
- Msvm_VirtualSystemManagementServiceSettingData.Caption
- Msvm_VirtualSystemManagementServiceSettingData.Description
- Msvm_VirtualSystemManagementServiceSettingData.InstanceID
- Msvm_VirtualSystemManagementServiceSettingData.ElementName
- Msvm_VirtualSystemManagementServiceSettingData.PrimaryOwnerName
- Msvm_VirtualSystemManagementServiceSettingData.PrimaryOwnerContact
- Msvm_VirtualSystemManagementServiceSettingData.ScopeOfResidence
- Msvm_VirtualSystemManagementServiceSettingData.DefaultExternalDataRoot
- Msvm_VirtualSystemManagementServiceSettingData.DefaultVirtualHardDiskPath
- Msvm_VirtualSystemManagementServiceSettingData.MinimumMacAddress
- Msvm_VirtualSystemManagementServiceSettingData.MaximumMacAddress
- Msvm_VirtualSystemManagementServiceSettingData.NumaSpanningEnabled
- Msvm_VirtualSystemManagementServiceSettingData.BiosLockString
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

# Msvm\_VirtualSystemManagementServiceSettingData class

Represents the settings for the virtualization service present on a single host system. The properties for this class cannot be modified directly. The client must call the [**ModifyServiceSettings**](modifyservicesettings-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class to modify any of these properties.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_VirtualSystemManagementServiceSettingData : CIM_SettingData
{
  string  Caption = "Virtual System Management Service";
  string  Description = "Settings for the Virtual System Management Service";
  string  InstanceID = "Microsoft:host";
  string  ElementName = "Virtual System Management Service";
  string  PrimaryOwnerName = "Administrators";
  string  PrimaryOwnerContact = "";
  string  ScopeOfResidence = "";
  string  DefaultExternalDataRoot = "root\ProgramData\Microsoft\Windows\Virtualization";
  string  DefaultVirtualHardDiskPath = "root\Users\Public\Documents\Virtual Hard Disks";
  string  MinimumMacAddress;
  string  MaximumMacAddress;
  boolean NumaSpanningEnabled;
  string  BiosLockString;
};
```

## Members

The **Msvm\_VirtualSystemManagementServiceSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_VirtualSystemManagementServiceSettingData** class has these properties.

<dl> <dt>

**BiosLockString**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Maxlen**](https://msdn.microsoft.com/library/aa393650) (32)
</dt> </dl>

Used by OEMs to allow BIOS-locked Windows operating systems to run in the virtual machine. This string must be exactly 32 characters in length.

This is a read-only property, but it can be changed using the [**ModifyServiceSettings**](modifyservicesettings-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

A short textual description (one-line string) of the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) and it is set to "Virtual System Management Service".

</dd> <dt>

**DefaultExternalDataRoot**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**Msvm\_ComputerSystem**](msvm-computersystem.md).**ExternalDataRoot**")
</dt> </dl>

The default external data root. By default, "*root*\\ProgramData\\Microsoft\\Windows\\Virtualization".

This is a read-only property, but it can be changed using the [**ModifyServiceSettings**](modifyservicesettings-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

</dd> <dt>

**DefaultVirtualHardDiskPath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The default virtual hard disk path. By default, "*root*\\Users\\Public\\Documents\\Virtual Hard Disks".

This is a read-only property, but it can be changed using the [**ModifyServiceSettings**](modifyservicesettings-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) and it is set to "Settings for the Virtual System Management Service".

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

A user-friendly name for the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) and it is set to "Virtual System Management Service". Changing this property will change the **ElementName** property of the associated [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) derivative.

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

This property is inherited from [**CIM\_SettingData**](https://msdn.microsoft.com/library/cc136911) and it is set to "Microsoft:*host*", where *host* is the NetBIOS name of the hosting computer system.

</dd> <dt>

**MaximumMacAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum MAC address for dynamically generated MAC addresses.

This is a read-only property, but it can be changed using the [**ModifyServiceSettings**](modifyservicesettings-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

</dd> <dt>

**MinimumMacAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The minimum MAC address for dynamically generated MAC addresses.

This is a read-only property, but it can be changed using the [**ModifyServiceSettings**](modifyservicesettings-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

</dd> <dt>

**NumaSpanningEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies if memory can be allocated from remote nonuniform memory access (NUMA) nodes when starting a VM or when assigning memory to a VM by dynamic memory. This can be one of the following values.



| Value                                                                                | Meaning                                                                        |
|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| <dl> <dt>**TRUE**</dt> </dl>  | Memory can be allocated from both local and remote NUMA nodes.<br/>      |
| <dl> <dt>**FALSE**</dt> </dl> | Memory can be allocated only from the NUMA node assigned to the VM.<br/> |



 

This is a read-only property, but it can be changed by using the [**ModifyServiceSettings**](modifyservicesettings-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

**Windows Server 2008 R2:** Reserved for future use. Note that this behavior has changed with Windows Server 2008 R2 with SP1.

**Windows Server 2008:** The **NumaSpanningEnabled** property is not available before Windows Server 2008 R2.

</dd> <dt>

**PrimaryOwnerContact**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Maxlen**](https://msdn.microsoft.com/library/aa393650) (256), [**Mappingstrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|General Information\|001.4")
</dt> </dl>

Describes how the primary system owner can be reached (for example, phone number or email address). By default, empty. This name may not exceed 256 characters in length.

This is a read-only property, but it can be changed using the [**ModifyServiceSettings**](modifyservicesettings-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

</dd> <dt>

**PrimaryOwnerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Maxlen**](https://msdn.microsoft.com/library/aa393650) (64), [**Mappingstrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|General Information\|001.3")
</dt> </dl>

The name of the primary system owner. By default, "Administrators". This value may not exceed 64 characters in length.

This is a read-only property, but it can be changed using the [**ModifyServiceSettings**](modifyservicesettings-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

</dd> <dt>

**ScopeOfResidence**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The scope. By default, empty.

This is a read-only property, but it can be changed using the [**ModifyServiceSettings**](modifyservicesettings-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

</dd> </dl>

## Remarks

Access to the **Msvm\_VirtualSystemManagementServiceSettingData** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

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

[**CIM\_SettingData**](cim-settingdata.md)
</dt> <dt>

[**CIM\_SettingData**](https://msdn.microsoft.com/library/cc136911)
</dt> <dt>

[Virtual System Management Classes](virtual-system-management-classes.md)
</dt> </dl>

 

 





