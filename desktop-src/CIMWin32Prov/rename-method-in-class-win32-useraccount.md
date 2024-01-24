---
description: Renames a user account name.
ms.assetid: 90258256-7470-4ec8-afce-bea0f64b90fb
ms.tgt_platform: multiple
title: Rename method of the Win32_UserAccount class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_UserAccount.Rename
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# Rename method of the Win32\_UserAccount class

The **Rename** [WMI class](/windows/desktop/WmiSdk/retrieving-a-class) method renames a user account name.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](/windows/desktop/WmiSdk/calling-a-method).

## Syntax


```mof
uint32 Rename(
  [in] string Name
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

New account name.

</dd> </dl>

## Return value

Returns one of the values listed in the following list. For additional error codes, see [**WMI Error Constants**](/windows/desktop/WmiSdk/wmi-error-constants) or [**WbemErrorEnum**](/windows/desktop/api/wbemdisp/ne-wbemdisp-wbemerrorenum). For general **HRESULT** values, see [System Error Codes](/windows/desktop/Debug/system-error-codes).

<dl> <dt>

**Success**
</dt> <dd>

0

Success.

</dd> <dt>

**Instance not found**
</dt> <dd>

1

Instance not found.

</dd> <dt>

**Instance required**
</dt> <dd>

2

Instance required.

</dd> <dt>

**Invalid parameter**
</dt> <dd>

3

Invalid parameter.

</dd> <dt>

**User not found**
</dt> <dd>

4

User not found.

</dd> <dt>

**Domain not found**
</dt> <dd>

5

Domain not found.

</dd> <dt>

**Operation is allowed only on the primary domain controller of the domain**
</dt> <dd>

6

Operation is allowed only on the primary domain controller of the domain.

</dd> <dt>

**Operation is not allowed on the last administrative account.**
</dt> <dd>

7

</dd> <dt>

**Operation is not allowed on specified special groups; user, admin, local or guest.**
</dt> <dd>

8

Operation is not allowed on specified special groups: user, admin, local, or guest.

</dd> <dt>

**Other API error**
</dt> <dd>

9

Other API error.

</dd> <dt>

**Internal error**
</dt> <dd>

10

Internal error.

</dd> </dl>

## Remarks

This functionality is implemented as a method to provide a separate context for the new name that is distinguishable from the key property value for Name that is associated with the instance to be modified.

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

[**Win32\_UserAccount**](win32-useraccount.md)
</dt> <dt>

[Operating System Classes](/previous-versions//aa392727(v=vs.85))
</dt> </dl>

 

