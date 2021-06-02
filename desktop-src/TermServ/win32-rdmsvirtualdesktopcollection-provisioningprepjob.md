---
title: ProvisioningPrepJob method of the Win32_RDMSVirtualDesktopCollection class
description: Creates a virtual desktop provisioning job.
ms.assetid: 240D4BE6-95BD-4858-8F8F-A00C92042AEF
ms.tgt_platform: multiple
keywords:
- ProvisioningPrepJob method Remote Desktop Services
- ProvisioningPrepJob method Remote Desktop Services , Win32_RDMSVirtualDesktopCollection interface
- Win32_RDMSVirtualDesktopCollection interface Remote Desktop Services , ProvisioningPrepJob method
topic_type:
- apiref
api_name:
- Win32_RDMSVirtualDesktopCollection.ProvisioningPrepJob
api_location:
- RDMS.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ProvisioningPrepJob method of the Win32\_RDMSVirtualDesktopCollection class

Creates a virtual desktop provisioning job.

## Syntax


```mof
uint32 ProvisioningPrepJob(
  [in]  string  CollectionAlias,
  [in]  string  VMHostName,
  [in]  string  VMName,
  [in]  string  ExportToLocation,
  [in]  boolean bSysPrep,
  [in]  string  MachineName,
  [in]  string  UserName,
  [in]  string  Password,
  [out] string  JobGuid
);
```



## Parameters

<dl> <dt>

*CollectionAlias* \[in\]
</dt> <dd>

The alias of the collection that hosts the virtual desktop.

</dd> <dt>

*VMHostName* \[in\]
</dt> <dd>

The virtual machine host name.

</dd> <dt>

*VMName* \[in\]
</dt> <dd>

The name of the virtual machine.

</dd> <dt>

*ExportToLocation* \[in\]
</dt> <dd>

The full path the location to export the provisioning job.

</dd> <dt>

*bSysPrep* \[in\]
</dt> <dd>

Indicates whether the provisioning job represents a Sysprep deployment.

</dd> <dt>

*MachineName* \[in\]
</dt> <dd>

The machine name of the computer that hosts the virtual machine.

</dd> <dt>

*UserName* \[in\]
</dt> <dd>

The user name of the administrator of the virtual machine.

</dd> <dt>

*Password* \[in\]
</dt> <dd>

The password of the administrator of the virtual machine.

</dd> <dt>

*JobGuid* \[out\]
</dt> <dd>

The **GUID** that uniquely identifies the provisioning job.

</dd> </dl>

## Return value

Returns 0 on success, otherwise returns a WMI error code.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                              |
| Namespace<br/>                | Root\\cimv2\\rdms<br/>                                                                |
| MOF<br/>                      | <dl> <dt>RDManagement.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RDMS.dll</dt> </dl>         |



## See also

<dl> <dt>

[**Win32\_RDMSVirtualDesktopCollection**](win32-rdmsvirtualdesktopcollection.md)
</dt> </dl>

 

 





