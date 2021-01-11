---
description: Represents the settings for the virtualization service present on a single host system.
ms.assetid: E3265AFE-0117-4F59-9A6B-34CEA7A61EDD
title: Msvm_VirtualSystemManagementServiceSettingData class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_VirtualSystemManagementServiceSettingData
- Msvm_VirtualSystemManagementServiceSettingData.InstanceID
- Msvm_VirtualSystemManagementServiceSettingData.Caption
- Msvm_VirtualSystemManagementServiceSettingData.Description
- Msvm_VirtualSystemManagementServiceSettingData.ElementName
- Msvm_VirtualSystemManagementServiceSettingData.BiosLockString
- Msvm_VirtualSystemManagementServiceSettingData.DefaultExternalDataRoot
- Msvm_VirtualSystemManagementServiceSettingData.DefaultVirtualHardDiskPath
- Msvm_VirtualSystemManagementServiceSettingData.MaximumMacAddress
- Msvm_VirtualSystemManagementServiceSettingData.MinimumMacAddress
- Msvm_VirtualSystemManagementServiceSettingData.NumaSpanningEnabled
- Msvm_VirtualSystemManagementServiceSettingData.PrimaryOwnerContact
- Msvm_VirtualSystemManagementServiceSettingData.PrimaryOwnerName
- Msvm_VirtualSystemManagementServiceSettingData.HbaLunTimeout
- Msvm_VirtualSystemManagementServiceSettingData.MaximumWWPNAddress
- Msvm_VirtualSystemManagementServiceSettingData.MinimumWWPNAddress
- Msvm_VirtualSystemManagementServiceSettingData.CurrentWWNNAddress
- Msvm_VirtualSystemManagementServiceSettingData.DefaultVirtualHardDiskCachingMode
- Msvm_VirtualSystemManagementServiceSettingData.HypervisorRootSchedulerEnabled
- Msvm_VirtualSystemManagementServiceSettingData.EnhancedSessionModeEnabled
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_VirtualSystemManagementServiceSettingData class

Represents the settings for the virtualization service present on a single host system. The properties for this class cannot be modified directly. The client must call the [**ModifyServiceSettings**](modifyservicesettings-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class to modify any of these properties.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_VirtualSystemManagementServiceSettingData : CIM_SettingData
{
  string  InstanceID = "Microsoft:host";
  string  Caption = "Hyper-V Virtual System Management Service";
  string  Description = "Settings for the Virtual System Management Service";
  string  ElementName = "Hyper-V Virtual System Management Service";
  string  BiosLockString;
  string  DefaultExternalDataRoot = "root\ProgramData\Microsoft\Windows\Virtualization";
  string  DefaultVirtualHardDiskPath = "root\Users\Public\Documents\Virtual Hard Disks";
  string  MaximumMacAddress;
  string  MinimumMacAddress;
  boolean NumaSpanningEnabled;
  string  PrimaryOwnerContact = "";
  string  PrimaryOwnerName = "Administrators";
  uint32  HbaLunTimeout;
  string  MaximumWWPNAddress;
  string  MinimumWWPNAddress;
  string  CurrentWWNNAddress;
  uint16  DefaultVirtualHardDiskCachingMode;
  boolean HypervisorRootSchedulerEnabled;
  boolean EnhancedSessionModeEnabled;
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

Qualifiers: [**Maxlen**](/windows/desktop/WmiSdk/standard-qualifiers) (32)
</dt> </dl>

Used by OEMs to allow BIOS-locked Windows operating systems to run in the virtual machine. This string must be exactly 32 characters in length.

This is a read-only property, but it can be changed by using the [**ModifyServiceSettings**](modifyservicesettings-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A short description of the object. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement), and it is always set to "Hyper-V Virtual System Management Service".

</dd> <dt>

**CurrentWWNNAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The world wide node name (WWNN) address for dynamically generated world wide name addresses used for synthetic host bus adapters.

This is a read-only property, but it can be changed by using the [**ModifyServiceSettings**](modifyservicesettings-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

</dd> <dt>

**DefaultExternalDataRoot**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("[**Msvm\_VirtualSystemSettingData**](msvm-virtualsystemsettingdata.md).**ConfigurationDataRoot**")
</dt> </dl>

The default external data root. By default, "*root*\\ProgramData\\Microsoft\\Windows\\Virtualization".

This is a read-only property, but it can be changed by using the [**ModifyServiceSettings**](modifyservicesettings-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

</dd> <dt>

**DefaultVirtualHardDiskCachingMode**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether in-memory file caching should be used for disks by default. This value can be overridden on a per-disk basis in the **CachingMode** field of the [**Msvm\_StorageAllocationSettingData**](msvm-storageallocationsettingdata.md) class.

> [!Note]  
> Added in Windows 10 and Windows Server 2016.

 

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="No_Caching"></span><span id="no_caching"></span><span id="NO_CACHING"></span>

**No Caching** (3)


</dt> <dd></dd> <dt>

<span id="Cache_Sharable_Parents"></span><span id="cache_sharable_parents"></span><span id="CACHE_SHARABLE_PARENTS"></span>

**Cache Sharable Parents** (4)


</dt> <dd></dd> </dl>

</dd> <dt>

**DefaultVirtualHardDiskPath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The default virtual hard disk path. By default, "*root*\\Users\\Public\\Documents\\Virtual Hard Disks".

This is a read-only property, but it can be changed by using the [**ModifyServiceSettings**](modifyservicesettings-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A description of the object. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement), and it is always set to "Settings for the Virtual System Management Service".

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A display name for the object. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement), and it is always set to "Hyper-V Virtual System Management Service". Changing this property will change the **ElementName** property of the associated [**CIM\_LogicalDevice**](/windows/desktop/CIMWin32Prov/cim-logicaldevice) derivative.

</dd> <dt>

**EnhancedSessionModeEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether enhanced session mode is permitted on the server. **True** indicates permitted, otherwise **False**.

**Windows 8.1:** This value is not supported until Windows 8.1 and Windows Server 2012 R2.

</dd> <dt>

**HbaLunTimeout**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the amount of time that the synthetic Fibre Channel virtual device will wait for a logical unit number (LUN) to appear before starting a virtual machine.

This is a read-only property, but it can be changed by using the [**ModifyServiceSettings**](modifyservicesettings-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

</dd> <dt>

**HypervisorRootSchedulerEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether or not the hypervisor root scheduler is enabled.

> [!Note]  
> Added in Windows 10, version 1709.

 

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

Uniquely identifies an instance of this class. This property is inherited from [**CIM\_SettingData**](/previous-versions//cc136911(v=vs.85)), and it is always set to "Microsoft:*host*", where *host* is the NetBIOS name of the hosting computer system.

</dd> <dt>

**MaximumMacAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum MAC address for dynamically generated MAC addresses.

This is a read-only property, but it can be changed by using the [**ModifyServiceSettings**](modifyservicesettings-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

</dd> <dt>

**MaximumWWPNAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum world wide port name (WWPN) address for dynamically generated world wide name addresses used for synthetic host bus adapters.

This is a read-only property, but it can be changed by using the [**ModifyServiceSettings**](modifyservicesettings-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

</dd> <dt>

**MinimumMacAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The minimum MAC address for dynamically generated MAC addresses.

This is a read-only property, but it can be changed by using the [**ModifyServiceSettings**](modifyservicesettings-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

</dd> <dt>

**MinimumWWPNAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The minimum world wide port name address for dynamically generated world wide name addresses used for synthetic host bus adapters.

This is a read-only property, but it can be changed by using the [**ModifyServiceSettings**](modifyservicesettings-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

</dd> <dt>

**NumaSpanningEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies whether memory can be allocated from remote nonuniform memory access (NUMA) nodes when starting a virtual machine or when assigning memory to a virtual machine by dynamic memory. This can be one of the following values.



| Value                                                                                | Meaning                                                                                     |
|--------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| <dl> <dt>**True**</dt> </dl>  | Memory can be allocated from both local and remote NUMA nodes.<br/>                   |
| <dl> <dt>**False**</dt> </dl> | Memory can be allocated only from the NUMA node assigned to the virtual machine.<br/> |



 

This is a read-only property, but it can be changed by using the [**ModifyServiceSettings**](modifyservicesettings-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

</dd> <dt>

**PrimaryOwnerContact**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Maxlen**](/windows/desktop/WmiSdk/standard-qualifiers) (256), [**Mappingstrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|General Information\|001.4")
</dt> </dl>

Describes how the primary system owner can be reached (for example, phone number or email address). By default, empty. This name may not exceed 256 characters in length.

This is a read-only property, but it can be changed by using the [**ModifyServiceSettings**](modifyservicesettings-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

</dd> <dt>

**PrimaryOwnerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Maxlen**](/windows/desktop/WmiSdk/standard-qualifiers) (64), [**Mappingstrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|General Information\|001.3")
</dt> </dl>

The name of the primary system owner. By default, "Administrators". This value may not exceed 64 characters in length.

This is a read-only property, but it can be changed by using the [**ModifyServiceSettings**](modifyservicesettings-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

</dd> </dl>

## Remarks

Access to the **Msvm\_VirtualSystemManagementServiceSettingData** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](/windows/desktop/WmiSdk/user-account-control-and-wmi).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_SettingData**](cim-settingdata.md)
</dt> <dt>

[**ModifyServiceSettings**](modifyservicesettings-msvm-virtualsystemmanagementservice.md)
</dt> <dt>

[**CIM\_SettingData**](/previous-versions//cc136911(v=vs.85))
</dt> <dt>

[Virtual System Management Classes](virtual-system-management-classes.md)
</dt> </dl>

 

