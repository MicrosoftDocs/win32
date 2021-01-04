---
title: Win32_RDMSVirtualDesktopCollection class
description: Creates and manages a virtual desktop collection.
ms.assetid: fe0a484e-f9e3-4b99-8e69-da8f337ae957
ms.tgt_platform: multiple
keywords:
- Win32_RDMSVirtualDesktopCollection class Remote Desktop Services
- Win32_RDMSVirtualDesktopCollection class Remote Desktop Services , described
topic_type:
- apiref
api_name:
- Win32_RDMSVirtualDesktopCollection
- Win32_RDMSVirtualDesktopCollection.Alias
- Win32_RDMSVirtualDesktopCollection.Type
- Win32_RDMSVirtualDesktopCollection.IsManaged
- Win32_RDMSVirtualDesktopCollection.Name
- Win32_RDMSVirtualDesktopCollection.CollectionDescription
- Win32_RDMSVirtualDesktopCollection.SecurityDescriptor
- Win32_RDMSVirtualDesktopCollection.VmFarmSettings
- Win32_RDMSVirtualDesktopCollection.UserVHDSetting
- Win32_RDMSVirtualDesktopCollection.IconContents
- Win32_RDMSVirtualDesktopCollection.ShowInPortal
- Win32_RDMSVirtualDesktopCollection.IsHA
- Win32_RDMSVirtualDesktopCollection.IsUserAdmin
- Win32_RDMSVirtualDesktopCollection.RollbackEnabled
api_location:
- RDMS.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Win32\_RDMSVirtualDesktopCollection class

Creates and manages a virtual desktop collection.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("Win32_RDManagement_Prov"), AMENDMENT]
class Win32_RDMSVirtualDesktopCollection
{
  string  Alias;
  uint32  Type;
  boolean IsManaged;
  string  Name;
  string  CollectionDescription;
  string  SecurityDescriptor;
  string  VmFarmSettings;
  string  UserVHDSetting;
  uint8   IconContents[];
  boolean ShowInPortal;
  boolean IsHA;
  boolean IsUserAdmin;
  boolean RollbackEnabled;
};
```

## Members

The **Win32\_RDMSVirtualDesktopCollection** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32\_RDMSVirtualDesktopCollection** class has these methods.



| Method                                                                                            | Description                                                                                                                                     |
|:--------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddVirtualDesktop**](addvirtualdesktop-win32-rdmsvirtualdesktopcollection.md)                 | Adds a virtual desktop to a virtual desktop collection.<br/>                                                                              |
| [**CancelPatch**](cancelpatch-win32-rdmsvirtualdesktopcollection.md)                             | Cancels a software update provisioning job for the virtual machines in a virtual desktop collection.<br/>                                 |
| [**GetInt32Property**](getint32property-win32-rdmsvirtualdesktopcollection.md)                   | Retrieves an integer property value from a virtual desktop collection.<br/>                                                               |
| [**GetPatchProperties**](getpatchproperties-win32-rdmsvirtualdesktopcollection.md)               | Retrieves the properties of a software update provisioning job for the virtual machines in a virtual desktop collection.<br/>             |
| [**GetStringProperty**](getstringproperty-win32-rdmsvirtualdesktopcollection.md)                 | Retrieves a string property value from a virtual desktop collection.<br/>                                                                 |
| [**ProvisioningEnumerateJobs**](provisioningenumeratejobs-win32-rdmsvirtualdesktopcollection.md) | Enumerates virtual desktop provisioning jobs for this service.<br/>                                                                       |
| [**ProvisioningJobCancel**](provisioningjobcancel-win32-rdmsvirtualdesktopcollection.md)         | Cancels a virtual desktop provisioning job.<br/>                                                                                          |
| [**ProvisioningJobExecute**](provisioningjobexecute-win32-rdmsvirtualdesktopcollection.md)       | Runs a virtual desktop provisioning job.<br/>                                                                                             |
| [**ProvisioningJobGetReport**](provisioningjobgetreport-win32-rdmsvirtualdesktopcollection.md)   | Gets a report about the status of a virtual desktop provisioning job.<br/>                                                                |
| [**ProvisioningPrepJob**](win32-rdmsvirtualdesktopcollection-provisioningprepjob.md)             | Creates a virtual desktop provisioning job.<br/>                                                                                          |
| [**RemoveVirtualDesktop**](removevirtualdesktop-win32-rdmsvirtualdesktopcollection.md)           | Removes a virtual desktop from a virtual desktop collection.<br/>                                                                         |
| [**SchedulePatch**](schedulepatch-win32-rdmsvirtualdesktopcollection.md)                         | Schedules a software update provisioning job that installs software updates on the virtual machines in a virtual desktop collection.<br/> |
| [**SetInt32Property**](setint32property-win32-rdmsvirtualdesktopcollection.md)                   | Updates an integer property value of a virtual desktop collection.<br/>                                                                   |
| [**SetStringProperty**](setstringproperty-win32-rdmsvirtualdesktopcollection.md)                 | Updates a string property value of a virtual desktop collection.<br/>                                                                     |



 

### Properties

The **Win32\_RDMSVirtualDesktopCollection** class has these properties.

<dl> <dt>

**Alias**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

Gets or sets the alias of the collection

</dd> <dt>

**CollectionDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**optional**](/windows/desktop/WmiSdk/standard-wmi-qualifiers)
</dt> </dl>

Gets or sets the description of the collection

</dd> <dt>

**IconContents**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**optional**](/windows/desktop/WmiSdk/standard-wmi-qualifiers)
</dt> </dl>

Gets or sets an array of values that specify icons for the collection.

</dd> <dt>

**IsHA**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets or sets a values that indicates whether the collection contains highly available VMs. **TRUE** if the collection contains highly available VMs; otherwise, **FALSE**.

</dd> <dt>

**IsManaged**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets or sets a value that indicates whether the collection is managed. **TRUE** if the collection is managed; otherwise, **FALSE**.

</dd> <dt>

**IsUserAdmin**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets or sets a values that indicates whether a user is an administrator on a VM. **TRUE** if the user is an administrator on a VM; otherwise, **FALSE**.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets or sets the name of the collection.

</dd> <dt>

**RollbackEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets or sets a values that indicates whether a VM was rolled with a VM snapshot. **TRUE** if the VM was rolled with a VM snapshot; otherwise, **FALSE**.

</dd> <dt>

**SecurityDescriptor**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**optional**](/windows/desktop/WmiSdk/standard-wmi-qualifiers)
</dt> </dl>

Gets or sets an SSDL formated security descriptor that controls access to the collection.

</dd> <dt>

**ShowInPortal**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets or sets a values that indicates whether the collection is displayed in Terminal Services Web Access (TS Web Access). **TRUE** to display the collection in TS Web Access; otherwise, **FALSE**.

</dd> <dt>

**Type**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets or sets a value that indicates the type of virtual machine sessions hosted by the collection.

This property contains one of the following values:

<dt>

<span id="TempVM"></span><span id="tempvm"></span><span id="TEMPVM"></span>

<span id="TempVM"></span><span id="tempvm"></span><span id="TEMPVM"></span>**TempVM** (1)


</dt> <dd>

Temporary virtual machines.

</dd> <dt>

<span id="ManualPersonalVM"></span><span id="manualpersonalvm"></span><span id="MANUALPERSONALVM"></span>

<span id="ManualPersonalVM"></span><span id="manualpersonalvm"></span><span id="MANUALPERSONALVM"></span>**ManualPersonalVM** (2)


</dt> <dd>

Manually created virtual machines.

</dd> <dt>

<span id="AutoPersonalVM"></span><span id="autopersonalvm"></span><span id="AUTOPERSONALVM"></span>

<span id="AutoPersonalVM"></span><span id="autopersonalvm"></span><span id="AUTOPERSONALVM"></span>**AutoPersonalVM** (3)


</dt> <dd>

Auto-generated virtual machines.

</dd> </dl>

</dd> <dt>

**UserVHDSetting**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**optional**](/windows/desktop/WmiSdk/standard-wmi-qualifiers)
</dt> </dl>

Gets or sets the user data VHD setting for the collection.

</dd> <dt>

**VmFarmSettings**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**optional**](/windows/desktop/WmiSdk/standard-wmi-qualifiers)
</dt> </dl>

Gets or sets he desktop settings for the virtual machines in the collection.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                              |
| Namespace<br/>                | Root\\cimv2\\rdms<br/>                                                                |
| MOF<br/>                      | <dl> <dt>RDManagement.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RDMS.dll</dt> </dl>         |



## See also

<dl> <dt>

[Remote Desktop Management Services Provider](rdms-api-reference.md)
</dt> </dl>

 

