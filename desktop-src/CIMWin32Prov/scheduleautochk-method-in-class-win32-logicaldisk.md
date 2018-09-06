---
Description: Schedules Autochk to be run on the disk drive represented by the Win32\_LogicalDisk at the next reboot if the dirty bit is set.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 34f4c26b-6bfb-45d9-9d6c-0a9b735355f3
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: ScheduleAutoChk method of the Win32_LogicalDisk class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_LogicalDisk.ScheduleAutoChk
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# ScheduleAutoChk method of the Win32\_LogicalDisk class

The **ScheduleAutoChk** class method schedules Autochk to be run on the disk drive represented by the [**Win32\_LogicalDisk**](win32-logicaldisk.md) at the next reboot if the dirty bit is set.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 ScheduleAutoChk(
  [in] string LogicalDisk[]
);
```



## Parameters

<dl> <dt>

*LogicalDisk* \[in\]
</dt> <dd>

Specifies the list of drives to schedule for Autochk at the next reboot. The string syntax consists of the drive letter followed by a colon for the logical disk, for example: "C:"

> [!Note]  
> Always check the validity of the drive letters in the *LogicalDisk* array when the data comes from an unknown source, or a source that you do not trust.

 

</dd> </dl>

## Return value

Returns a value of 0 (zero) if successful, and some other value if any other error occurs. Values are listed in the following list. For additional error codes, see [**WMI Error Constants**](https://msdn.microsoft.com/library/aa394559) or [**WbemErrorEnum**](https://msdn.microsoft.com/library/aa393978). For general **HRESULT** values, see [System Error Codes](https://msdn.microsoft.com/library/windows/desktop/ms681381).

<dl> <dt>

**No Error** (0)
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

This method is only applicable to those instances of logical disk that represent a physical disk in the machine. This method is not applicable to mapped logical drives.

## Examples

The following VBScript and PowerShell samples schedule Autochk.exe to run against drive C the next time the computer reboots.


```VB
strComputer = "." 
Set objWMIService = GetObject("winmgmts:" _ 
    & "{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2") 
 
Set objDisk = objWMIService.Get("Win32_LogicalDisk") 
 
errReturn = objDisk.ScheduleAutoChk(Array("C:")) 
```

<span codelanguage="PowerShell"></span>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>PowerShell</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>Invoke-WmiMethod -path win32_logicaldisk -Name ScheduleAutoChk -ArgumentList @(&quot;C:&quot;)</code></pre></td>
</tr>
</tbody>
</table>



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_LogicalDisk**](win32-logicaldisk.md)
</dt> </dl>

 

 




