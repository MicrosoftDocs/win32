---
title: RdvSetupVMPermissions method of the Win32_RdvhManagement class
description: Sets the permissions on a virtual machine for the current user.
ms.assetid: 6ac45983-d468-4a3b-875f-48717ba23ed0
ms.tgt_platform: multiple
keywords:
- RdvSetupVMPermissions method Remote Desktop Services
- RdvSetupVMPermissions method Remote Desktop Services , Win32_RdvhManagement class
- Win32_RdvhManagement class Remote Desktop Services , RdvSetupVMPermissions method
topic_type:
- apiref
api_name:
- Win32_RdvhManagement.RdvSetupVMPermissions
api_location:
- TSVmHostWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# RdvSetupVMPermissions method of the Win32\_RdvhManagement class

Sets the permissions on a virtual machine for the current user.

## Syntax


```mof
uint32 RdvSetupVMPermissions(
  [in] string VmName
);
```



## Parameters

<dl> <dt>

*VmName* \[in\]
</dt> <dd>

The name of the virtual machine to set permissions on.

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

 

 





