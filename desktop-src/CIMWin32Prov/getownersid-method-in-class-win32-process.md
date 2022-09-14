---
description: The GetOwnerSid&\#8194;WMI class method retrieves the security identifier (SID) for the owner of this process.
ms.assetid: f856b06c-8080-4145-a775-51361f741873
ms.tgt_platform: multiple
title: GetOwnerSid method of the Win32_Process class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_Process.GetOwnerSid
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# GetOwnerSid method of the Win32\_Process class

The **GetOwnerSid** [WMI class](/windows/desktop/WmiSdk/retrieving-a-class) method retrieves the security identifier (SID) for the owner of this process.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](/windows/desktop/WmiSdk/calling-a-method).

## Syntax


```mof
uint32 GetOwnerSid(
  [out] string Sid
);
```



## Parameters

<dl> <dt>

*Sid* \[out\]
</dt> <dd>

Returns the security identifier descriptor for this process.

</dd> </dl>

## Return value

Returns zero (0) to indicate success. Any other number indicates an error. For additional error codes, see [**WMI Error Constants**](/windows/desktop/WmiSdk/wmi-error-constants) or [**WbemErrorEnum**](/windows/desktop/api/wbemdisp/ne-wbemdisp-wbemerrorenum). For general **HRESULT** values, see [System Error Codes](/windows/desktop/Debug/system-error-codes).

<dl> <dt>

**Successful completion** (0)
</dt> <dt>

**Access denied** (2)
</dt> <dt>

**Insufficient privilege** (3)
</dt> <dt>

**Unknown failure** (8)
</dt> <dt>

**Path not found** (9)
</dt> <dt>

**Invalid parameter** (21)
</dt> <dt>

**Other** (22 4294967295)
</dt> </dl>

## Examples

The [Find the logged on users on a remote system/s version 2](https://Gallery.TechNet.Microsoft.Com/Find-the-logged-on-users-1161bd92) PowerShell code example queries remote machines to see who is logged on.

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

[**Win32\_Process**](win32-process.md)
</dt> </dl>

 

