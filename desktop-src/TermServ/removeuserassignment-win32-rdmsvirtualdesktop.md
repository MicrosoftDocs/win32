---
title: RemoveUserAssignment method of the Win32_RDMSVirtualDesktop class
description: Removes the user assignment from the virtual desktop.
ms.assetid: 7ebb34b4-94f6-4a00-87a9-44ad28d103cb
ms.tgt_platform: multiple
keywords:
- RemoveUserAssignment method Remote Desktop Services
- RemoveUserAssignment method Remote Desktop Services , Win32_RDMSVirtualDesktop class
- Win32_RDMSVirtualDesktop class Remote Desktop Services , RemoveUserAssignment method
topic_type:
- apiref
api_name:
- Win32_RDMSVirtualDesktop.RemoveUserAssignment
api_location:
- RDMS.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# RemoveUserAssignment method of the Win32\_RDMSVirtualDesktop class

Removes the user assignment from the virtual desktop.

## Syntax


```mof
uint32 RemoveUserAssignment(
  [in] string VMName
);
```



## Parameters

<dl> <dt>

*VMName* \[in\]
</dt> <dd>

The virtual machine name of the virtual desktop.

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

 

 





