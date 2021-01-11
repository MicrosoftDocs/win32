---
description: Sets the parameters of the shared resource.
ms.assetid: 592d0fa6-c865-4f70-89c3-b58204a8c5a6
ms.tgt_platform: multiple
title: SetShareInfo method of the Win32_ClusterShare class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_ClusterShare.SetShareInfo
api_type: 
- COM
api_location: 
- CIMWin32.dll
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

Security descriptor for user-level permissions. A security descriptor contains information about the permission, owner, and access capabilities of the resource. For more information, see [**Win32\_SecurityDescriptor**](/previous-versions/windows/desktop/secrcw32prov/win32-securitydescriptor).

</dd> </dl>

## Requirements



| Requirement | Value |
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

 

