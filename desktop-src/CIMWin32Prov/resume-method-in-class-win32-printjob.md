---
Description: The Resume WMI class method continues a paused print job.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: acfbca2b-19af-4339-bbca-834db50c3d8d
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: Resume method of the Win32\_PrintJob class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Resume method of the Win32\_PrintJob class

The **Resume** [WMI class](https://msdn.microsoft.com/library/aa393244) method continues a paused print job.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 Resume();
```



## Parameters

This method has no parameters.

## Return value

Returns one of the values listed in the following list, or any other value to indicate an error.

<dl> <dt>

**0**
</dt> <dd>

Success

</dd> <dt>

**5**
</dt> <dd>

Access Denied

</dd> </dl>

## Examples

The following VBScript code sample resumes all the print jobs on a computer.


```VB
strComputer = "." 
Set objWMIService = GetObject("winmgmts:" _ 
    & "{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2") 
 
Set colPrintJobs =  objWMIService.ExecQuery _ 
    ("Select * from Win32_PrintJob") 
 
For Each objPrintJob in colPrintJobs  
    objPrintJob.Resume 
Next 
```



## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                        |
| MOF<br/>                      | <dl> <dt>Win32\_Printer.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl>       |



## See also

<dl> <dt>

[Computer System Hardware Classes](computer-system-hardware-classes.md)
</dt> <dt>

[**Win32\_PrintJob**](win32-printjob.md)
</dt> </dl>

 

 




