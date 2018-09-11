---
title: RdvMigrateVmToDifferentHost method of the Win32_RdvhManagement class
description: Initiates a live migration of a virtual machine to a specified host.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: aa4b1e57-a97c-410b-9b9d-423a1c77de70
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- RdvMigrateVmToDifferentHost method Remote Desktop Services
- RdvMigrateVmToDifferentHost method Remote Desktop Services , Win32_RdvhManagement class
- Win32_RdvhManagement class Remote Desktop Services , RdvMigrateVmToDifferentHost method
topic_type:
- apiref
api_name:
- Win32_RdvhManagement.RdvMigrateVmToDifferentHost
api_location:
- TSVmHostWmi.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RdvMigrateVmToDifferentHost method of the Win32\_RdvhManagement class

Initiates a live migration of a virtual machine to a specified host.

## Syntax


```mof
uint32 RdvMigrateVmToDifferentHost(
  [in] string VmName,
  [in] string DestinationHost
);
```



## Parameters

<dl> <dt>

*VmName* \[in\]
</dt> <dd>

Name of the virtual machine to migrate.

</dd> <dt>

*DestinationHost* \[in\]
</dt> <dd>

name of the destination host.

</dd> </dl>

## Return value

Returns 0 on success, otherwise returns a WMI error code. Refer to [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md) for a list of these values.

## Requirements



|                                     |                                                                                            |
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

 

 





