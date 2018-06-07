---
Description: The Namespace property of the SWbemObjectPath object contains the name of the namespace that is part of the object path.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: be88670d-6f0d-4b9d-886f-3e70bf4758ed
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: SWbemObjectPath.Namespace property
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SWbemObjectPath.Namespace property

The **Namespace** property of the [**SWbemObjectPath**](swbemobjectpath.md) object contains the name of the namespace that is part of the object path. For example, the following path shows the namespace property that returns root\\cimv2:

``` syntax
\\computer\root\cimv2:win32_logicaldisk="a:"
```

For the syntax explanation, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

This property is read/write.

## Syntax


```VB
SWbemObjectPath.Namespace As String
```



## Property value

## Examples

The following example shows you how to obtain the namespace name from instances of [**Win32\_LogicalDisk**](https://msdn.microsoft.com/library/aa394173) that are hard disks. The script connects to the default namespace.


```VB
Const HARD_DISK = 3
strComputer = "."
Set objWMIService = GetObject("winmgmts:" _
    & "{impersonationLevel=impersonate}!\\" & strComputer)

Set colDisks = objWMIService.ExecQuery _
    ("Select * from Win32_LogicalDisk " _
    & "Where DriveType = " & HARD_DISK & "")
For Each objDisk in colDisks
    Set objpath = objDisk.path_
    Wscript.Echo "Path of Win32_Logical disk instance " _
    & objDisk.DeviceID & " = " & objpath.Namespace   
Next
```



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Wbemdisp.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Wbemdisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemdisp.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_SWbemObjectPath<br/>                                                       |
| IID<br/>                      | IID\_ISWbemObjectPath<br/>                                                        |



 

 




