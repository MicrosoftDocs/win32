---
title: SetUserAssignment method of the Win32_RDMSVirtualDesktop class
description: Assigns a virtual desktop to a user.
ms.assetid: 6a96ccb7-5d3d-4164-a0a3-286a700b414c
ms.tgt_platform: multiple
keywords:
- SetUserAssignment method Remote Desktop Services
- SetUserAssignment method Remote Desktop Services , Win32_RDMSVirtualDesktop class
- Win32_RDMSVirtualDesktop class Remote Desktop Services , SetUserAssignment method
topic_type:
- apiref
api_name:
- Win32_RDMSVirtualDesktop.SetUserAssignment
api_location:
- RDMS.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SetUserAssignment method of the Win32\_RDMSVirtualDesktop class

Assigns a virtual desktop to a user.

## Syntax


```mof
uint32 SetUserAssignment(
  [in] string UserName,
  [in] string UserDomain
);
```



## Parameters

<dl> <dt>

*UserName* \[in\]
</dt> <dd>

The username of the user.

</dd> <dt>

*UserDomain* \[in\]
</dt> <dd>

The domain name of the user.

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

 

 





