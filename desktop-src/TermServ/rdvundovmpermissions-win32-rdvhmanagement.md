---
title: RdvUndoVMPermissions method of the Win32_RdvhManagement class
description: Reverts permissions set by RdvSetupVMPermissions on the specified virtual machine.
ms.assetid: 3331430e-7427-42f7-ab09-27fece8dc3ca
ms.tgt_platform: multiple
keywords:
- RdvUndoVMPermissions method Remote Desktop Services
- RdvUndoVMPermissions method Remote Desktop Services , Win32_RdvhManagement class
- Win32_RdvhManagement class Remote Desktop Services , RdvUndoVMPermissions method
topic_type:
- apiref
api_name:
- Win32_RdvhManagement.RdvUndoVMPermissions
api_location:
- TSVmHostWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# RdvUndoVMPermissions method of the Win32\_RdvhManagement class

Reverts permissions set by [**RdvSetupVMPermissions**](rdvsetupvmpermissions-win32-rdvhmanagement.md) on the specified virtual machine.

## Syntax


```mof
uint32 RdvUndoVMPermissions(
  [in] string VmName
);
```



## Parameters

<dl> <dt>

*VmName* \[in\]
</dt> <dd>

Name of the virtual machine to undo permissions on.

</dd> </dl>

## Return value

Returns 0 on success, otherwise returns a WMI error code. Refer to [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md) for a list of these values.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                             |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                   |
| MOF<br/>                      | <dl> <dt>TSVmHost.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>TSVmHostWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_RdvhManagement**](win32-rdvhmanagement.md)
</dt> </dl>

 

 





