---
description: Excludes disks from the autochk operation to be run at the next reboot.
ms.assetid: 5df2bc3b-e149-4853-aa02-af4cb8af6da0
ms.tgt_platform: multiple
title: ExcludeFromAutochk method of the Win32_LogicalDisk class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_LogicalDisk.ExcludeFromAutochk
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# ExcludeFromAutochk method of the Win32\_LogicalDisk class

The **ExcludeFromAutochk** method excludes disks from the **autochk** operation to be run at the next reboot.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](/windows/desktop/WmiSdk/calling-a-method).

## Syntax


```mof
uint32 ExcludeFromAutochk(
  [in] string LogicalDisk[]
);
```



## Parameters

<dl> <dt>

*LogicalDisk* \[in\]
</dt> <dd>

List of drives that should be excluded from **autochk** at the next reboot. The string syntax consists of the drive letter followed by a colon for the logical disk.

Example: "C:"

</dd> </dl>

## Return value

Returns a value of 0 (zero) when no error occurs. Values are listed in the following list. For additional error codes, see [**WMI Error Constants**](/windows/desktop/WmiSdk/wmi-error-constants) or [**WbemErrorEnum**](/windows/desktop/api/wbemdisp/ne-wbemdisp-wbemerrorenum). For general **HRESULT** values, see [System Error Codes](/windows/desktop/Debug/system-error-codes).

<dl> <dt>

**Success** (0)
</dt> <dt>

**Error - Remote Drive** (1)
</dt> <dt>

**Error - Removable Drive** (2)
</dt> <dt>

**Error - Drive Not Root Directory** (3)
</dt> <dt>

**Error - Unknown Drive** (4)
</dt> </dl>

## Remarks

If not excluded, **autochk** is performed on the disk when the dirty bit is set for the disk. Note that the calls to exclude disks are not cumulative. If a call is made to exclude some disks, then the new list is not added to the list of disks that are already marked for exclusion. The new list of disks overwrites the previous list. This method is only applicable to those instances of logical disk that represent a physical disk in the machine. It is not applicable to mapped logical drives.

## Examples

The following VBScript code sample ensures that Autochk.exe will not run against drive C the next time the computer reboots, even if the "dirty bit" has been set on drive C.


```VB
strComputer = "." 
Set objWMIService = GetObject("winmgmts:" _ 
    & "{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2") 
 
Set objDisk = objWMIService.Get("Win32_LogicalDisk") 
 
errReturn = objDisk.ExcludeFromAutoChk(Array("C:")) 
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

[**Win32\_LogicalDisk**](win32-logicaldisk.md)
</dt> <dt>

[Computer System Hardware Classes](computer-system-hardware-classes.md)
</dt> </dl>

 

