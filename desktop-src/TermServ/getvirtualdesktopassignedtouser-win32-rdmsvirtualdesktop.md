---
title: GetVirtualDesktopAssignedToUser method of the Win32_RDMSVirtualDesktop class
description: Retrieves the virtual desktop that is assigned to the specified user.
ms.assetid: cbc22c45-4492-4651-b164-a6fd717c5ab4
ms.tgt_platform: multiple
keywords:
- GetVirtualDesktopAssignedToUser method Remote Desktop Services
- GetVirtualDesktopAssignedToUser method Remote Desktop Services , Win32_RDMSVirtualDesktop class
- Win32_RDMSVirtualDesktop class Remote Desktop Services , GetVirtualDesktopAssignedToUser method
topic_type:
- apiref
api_name:
- Win32_RDMSVirtualDesktop.GetVirtualDesktopAssignedToUser
api_location:
- RDMS.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# GetVirtualDesktopAssignedToUser method of the Win32\_RDMSVirtualDesktop class

Retrieves the virtual desktop that is assigned to the specified user.

## Syntax


```mof
uint32 GetVirtualDesktopAssignedToUser(
  [in]  string CollectionAlias,
  [in]  string UserName,
  [in]  string UserDomain,
  [out] string VMName
);
```



## Parameters

<dl> <dt>

*CollectionAlias* \[in\]
</dt> <dd>

The alias of the virtual desktop collection that contain the virtual desktop.

</dd> <dt>

*UserName* \[in\]
</dt> <dd>

The username of the user.

</dd> <dt>

*UserDomain* \[in\]
</dt> <dd>

The domain name of the user.

</dd> <dt>

*VMName* \[out\]
</dt> <dd>

Receives the virtual machine name of the virtual desktop.

</dd> </dl>

## Return value

Returns 0 on success, otherwise returns a WMI error code.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                              |
| Namespace<br/>                | Root\\CIMv2\\rdms<br/>                                                                |
| MOF<br/>                      | <dl> <dt>RDManagement.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RDMS.dll</dt> </dl>         |



## See also

<dl> <dt>

[**Win32\_RDMSVirtualDesktop**](win32-rdmsvirtualdesktop.md)
</dt> </dl>

 

 





