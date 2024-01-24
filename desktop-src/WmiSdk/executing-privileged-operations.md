---
description: Privileged operations require security privileges such as SeLoadDriverPrivilege (wbemPrivilegeLoadDriver in the Scripting API Constants), a privilege that must be enabled for an account that is loading a device driver.
ms.assetid: 11bb8723-f329-4083-8219-2256ce44a5e3
ms.tgt_platform: multiple
title: Executing Privileged Operations
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Executing Privileged Operations

Privileged operations require security privileges such as **SeLoadDriverPrivilege** (**wbemPrivilegeLoadDriver** in the [Scripting API Constants](scripting-api-constants.md)), a privilege that must be enabled for an account that is loading a device driver. You cannot add privileges to an administrator or user through WMI, you can only enable privileges that the account already has. For a list of privileges, see [**Privilege\_Constants**](privilege-constants.md).

By default, a local user on a computer can read static data from the [*WMI repository*](gloss-w.md), write to instances supplied by providers, and execute provider methods, unless the provider enforces special security requirements of its own. Only administrators can [connect to a remote computer](connecting-to-wmi-on-a-remote-computer.md), change security descriptors, or change static WMI repository data, such as a WMI class definition. All privileges are enabled for a remote connection. For more information, see [Securing a Remote WMI Connection](securing-a-remote-wmi-connection.md).

The privilege constants for C++ differ from those that are used by automation languages such as Visual Basic. Scripts must use the value of the constant rather than the name. For more information, see [Executing Privileged Operations Using C++](executing-privileged-operations-using-c-.md) or [Executing Privileged Operations Using VBScript](executing-privileged-operations-using-vbscript.md).

A common cause of access denied errors when using WMI is the lack of an enabled privilege for operations, such as getting all instances of [**Win32\_NTEventlogFile**](/previous-versions/windows/desktop/legacy/aa394225(v=vs.85)). Without enabling the **SeSecurity** privilege, you cannot access the Security log file.

The following VBScript code example shows how to set the **SeSecurity** privilege in the moniker string. When used in the moniker, the privilege name in parentheses drops the initial "Se". For more information, see [Constructing a Moniker String](constructing-a-moniker-string.md).


```VB
strComputer = "."
Set objWMIService = GetObject("winmgmts:" _
    & "{impersonationLevel=impersonate,(Security)}!\\" _
    & strComputer & "\root\cimv2")
Set colFiles = objWMIService.ExecQuery _
    ("Select * from Win32_NTEventLogFile " _
    & "Where LogFileName='Security'")
For Each LogFile in colFiles
Wscript.Echo LogFile.NumberOfRecords
Next
```



## Related topics

<dl> <dt>

[**Privilege Constants**](privilege-constants.md)
</dt> </dl>

 

 
