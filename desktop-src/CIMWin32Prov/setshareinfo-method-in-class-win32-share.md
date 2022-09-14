---
description: The SetShareInfo&\#8194;WMI class method sets the parameters of a shared resource.
ms.assetid: f6379261-9325-4b7f-92df-438c5029569f
ms.tgt_platform: multiple
title: SetShareInfo method of the Win32_Share class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_Share.SetShareInfo
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# SetShareInfo method of the Win32\_Share class

The **SetShareInfo** [WMI class](/windows/desktop/WmiSdk/retrieving-a-class) method sets the parameters of a shared resource.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](/windows/desktop/WmiSdk/calling-a-method).

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

Example: 10. This parameter is optional.

</dd> <dt>

*Description* \[in, optional\]
</dt> <dd>

Optional comment to describe the resource being shared.

</dd> <dt>

*Access* \[in, optional\]
</dt> <dd>

Security descriptor for user-level permissions. A security descriptor contains information about the permission, owner, and access capabilities of the resource. For more information, see [**Win32\_SecurityDescriptor**](/previous-versions/windows/desktop/secrcw32prov/win32-securitydescriptor).

</dd> </dl>

## Return value

Returns one of the values listed in the following list or any other value to indicate an error.

<dl> <dt>

**Success** (0)
</dt> <dt>

**Access denied** (2)
</dt> <dt>

**Unknown failure** (8)
</dt> <dt>

**Invalid name** (9)
</dt> <dt>

**Invalid level** (10)
</dt> <dt>

**Invalid parameter** (21)
</dt> <dt>

**Duplicate share** (22)
</dt> <dt>

**Redirected path** (23)
</dt> <dt>

**Unknown device or directory** (24)
</dt> <dt>

**Net name not found** (25)
</dt> <dt>

**Other** (26 4294967295)
</dt> </dl>

## Remarks

**SetShareInfo** method is a dynamic object method and is used on an occurrence of this class.

Only members of the Administrators or Account Operators local group or those with Communication, Print, or Server operator group membership can successfully execute **SetShareInfo**. The print operator can only set printer queues. The Communication operator can only set communication device queues.

## Examples

The following PowerShell sample updates the name of the **newShare** share.


```PowerShell
$newShare = Get-WmiObject win32_share | Where-Object {$_.name -eq "newShare"}
[void]$newShare.SetShareInfo($null,"This is my new description",$null)
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[Operating System Classes](/previous-versions//aa392727(v=vs.85))
</dt> <dt>

[**Win32\_Share**](win32-share.md)
</dt> </dl>

 

