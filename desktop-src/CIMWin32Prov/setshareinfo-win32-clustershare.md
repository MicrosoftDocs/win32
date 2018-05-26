---
Description: Sets the parameters of the shared resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 592d0fa6-c865-4f70-89c3-b58204a8c5a6
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: SetShareInfo method of the Win32\_ClusterShare class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SetShareInfo method of the Win32\_ClusterShare class

Sets the parameters of the shared resource.

## Syntax


```mof
uint32 SetShareInfo(
  [in, optional] uint32                   MaximumAllowed,
  [in, optional] string                   Description,
  [in, optional] Win32_SecurityDescriptor Access
);
```



## Parameters

<dl> <dt>

*MaximumAllowed* \[in, optional\]
</dt> <dd>

Limit on the maximum number of users allowed to use this resource concurrently.

</dd> <dt>

*Description* \[in, optional\]
</dt> <dd>

Describes the resource being shared.

</dd> <dt>

*Access* \[in, optional\]
</dt> <dd>

Security descriptor for user-level permissions. A security descriptor contains information about the permission, owner, and access capabilities of the resource. For more information, see [**Win32\_SecurityDescriptor**](https://msdn.microsoft.com/library/aa394402).

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                       |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Cimwin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_ClusterShare**](win32-clustershare.md)
</dt> </dl>

 

 




