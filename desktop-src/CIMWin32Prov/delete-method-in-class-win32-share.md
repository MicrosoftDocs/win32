---
description: Deletes a share name from a server's list of shared resources, disconnecting connections to the shared resource.
ms.assetid: 175f9c0e-0017-4a86-8e05-ad78e2c93c11
ms.tgt_platform: multiple
title: Delete method of the Win32_Share class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_Share.Delete
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# Delete method of the Win32\_Share class

The **Delete** [WMI class](/windows/desktop/WmiSdk/retrieving-a-class) method deletes a share name from a server's list of shared resources, disconnecting connections to the shared resource.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](/windows/desktop/WmiSdk/calling-a-method).

## Syntax


```mof
uint32 Delete();
```



## Parameters

This method has no parameters.

## Return value

Returns one of the values listed in the following list, or any other value to indicate an error. For additional error codes, see [**WMI Error Constants**](/windows/desktop/WmiSdk/wmi-error-constants) or [**WbemErrorEnum**](/windows/desktop/api/wbemdisp/ne-wbemdisp-wbemerrorenum). For general **HRESULT** values, see [System Error Codes](/windows/desktop/Debug/system-error-codes).

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

The **Delete** method is an object method and is used on an instance of a class.

Only members of the Administrators or Account Operators local group or those with Communication, Print, or Server operator group membership can successfully execute the method. The Print operator can delete only printer queues. The Communication operator can delete only communication-device queues.

## Examples

The following VBScript code sample deletes the specified share.


```VB
On Error Resume Next

ComputerName = InputBox("Enter the computer name:", "Delete Share", "localhost")

SName = InputBox("Enter the name of the share:", "Delete Share")



Set Shares = GetObject("winmgmts:\\" & ComputerName & _
 "\root\cimv2").ExecQuery("SELECT * FROM Win32_Share WHERE name = '" & SName & "'")



For Each Share in Shares
 Share.Delete()
Next
```



The following PowerShell code sample deletes blank shares.


```PowerShell
$Shares = Get-WMIObject Win32_Share | Where {$_.Name -eq ""}

Foreach ($Share in $Shares) {
   $Share.Delete()
}
"{0} blank shares found and removed" -f $shares.count
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

 

