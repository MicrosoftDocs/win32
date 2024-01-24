---
title: GetUserAssignment method of the Win32_RDMSVirtualDesktop class
description: Retrieves the username and domain name of the user that is assigned to the virtual desktop.
ms.assetid: 1887c49d-85df-4fb4-9b40-42fb7763bf95
ms.tgt_platform: multiple
keywords:
- GetUserAssignment method Remote Desktop Services
- GetUserAssignment method Remote Desktop Services , Win32_RDMSVirtualDesktop class
- Win32_RDMSVirtualDesktop class Remote Desktop Services , GetUserAssignment method
topic_type:
- apiref
api_name:
- Win32_RDMSVirtualDesktop.GetUserAssignment
api_location:
- RDMS.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# GetUserAssignment method of the Win32\_RDMSVirtualDesktop class

Retrieves the username and domain name of the user that is assigned to the virtual desktop.

## Syntax


```mof
uint32 GetUserAssignment(
  [out] string UserName,
  [out] string UserDomain
);
```



## Parameters

<dl> <dt>

*UserName* \[out\]
</dt> <dd>

Receives the username.

</dd> <dt>

*UserDomain* \[out\]
</dt> <dd>

Receives the domain name.

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

 

 





