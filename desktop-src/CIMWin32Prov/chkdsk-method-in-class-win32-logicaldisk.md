---
description: Invokes the chkdsk operation on the disk.
ms.assetid: 65942702-b660-46cd-b614-e3e1ec3df7b9
ms.tgt_platform: multiple
title: Chkdsk method of the Win32_LogicalDisk class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_LogicalDisk.Chkdsk
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# Chkdsk method of the Win32\_LogicalDisk class

The **Chkdsk** instance method invokes the **chkdsk** operation on the disk.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](/windows/desktop/WmiSdk/calling-a-method).

## Syntax


```mof
uint32 Chkdsk(
  [in] boolean FixErrors = ,
  [in] boolean VigorousIndexCheck = ,
  [in] boolean SkipFolderCycle = ,
  [in] boolean ForceDismount = ,
  [in] boolean RecoverBadSectors = ,
  [in] boolean OKToRunAtBootUp = 
);
```



## Parameters

<dl> <dt>

*FixErrors* \[in\]
</dt> <dd>

Indicates what should be done to errors found on the disk. If **true**, then errors are fixed. The default is **false**.

</dd> <dt>

*VigorousIndexCheck* \[in\]
</dt> <dd>

If **true**, a less vigorous check of index entries should be performed. The default is **false**.

</dd> <dt>

*SkipFolderCycle* \[in\]
</dt> <dd>

If **true**, the folder cycle checking should be skipped. The default is **true**.

</dd> <dt>

*ForceDismount* \[in\]
</dt> <dd>

If **true**, the drive should be forced to dismount before checking. The default is **false**.

</dd> <dt>

*RecoverBadSectors* \[in\]
</dt> <dd>

If **true**, the bad sectors should be located and the readable information should be recovered from these sectors. The default is **false**.

</dd> <dt>

*OKToRunAtBootUp* \[in\]
</dt> <dd>

If **true**, the **chkdsk** operation should be performed at next boot up time, in case the operation could not be performed because the disk is locked at time this method is called. The default is **false**.

</dd> </dl>

## Return value

Returns a value of 0 (zero) if successful. Other values are listed in the following list. For additional error codes, see [**WMI Error Constants**](/windows/desktop/WmiSdk/wmi-error-constants) or [**WbemErrorEnum**](/windows/desktop/api/wbemdisp/ne-wbemdisp-wbemerrorenum). For general **HRESULT** values, see [System Error Codes](/windows/desktop/Debug/system-error-codes).

<dl> <dt>

**Success - Chkdsk completed**
</dt> <dd>

0

Success - [**Chkdsk**](chkdsk-method-in-class-win32-logicaldisk.md) Completed

</dd> <dt>

**Success - Locked and chkdsk scheduled on reboot**
</dt> <dd>

1

</dd> <dt>

**Failure - Unknown file system**
</dt> <dd>

2

</dd> <dt>

**Failure - Unknown error**
</dt> <dd>

3

</dd> <dt>

**Failure - Unsupported File System**
</dt> <dd>

4

</dd> </dl>

## Remarks

This method is only applicable to those instances of logical disk that represent a physical disk in the machine. It is not applicable to mapped logical drives.

## Examples

The[Is CHKDSK Dirty Bit Set on a server](https://Gallery.TechNet.Microsoft.Com/57076851-97fb-4af6-8c5c-1e34156ceab4) PowerShell code sample examines the remote system and returns a true or false if the chkdsk /f flag was set.

The [Remotely scan disk](https://Gallery.TechNet.Microsoft.Com/Remotely-scan-disk-dd4fc267) PowerShell code sample remotely starts or schedules Scan Disk.

The following VBScript code sample Runs ChkDsk.exe against drive D on a computer.


```VB
Const FIX_ERRORS = True 
 
strComputer = "." 
Set objWMIService = GetObject("winmgmts:" _ 
    & "{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2") 
 
Set objDisk = objWMIService.Get("Win32_LogicalDisk.DeviceID='D:'") 
 
errReturn = objDisk.ChkDsk(FIX_ERRORS) 
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

 

