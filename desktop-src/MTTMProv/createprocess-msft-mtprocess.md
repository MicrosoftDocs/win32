---
title: CreateProcess method of the MSFT\_MTProcess class
description: Create a new process.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 569d3f10-88b3-4d87-9eb6-45abb5a957ec
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CreateProcess method
- CreateProcess method, MSFT_MTProcess class
- MSFT_MTProcess class, CreateProcess method
topic_type:
- apiref
api_name:
- MSFT_MTProcess.CreateProcess
api_location:
- MtTmProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CreateProcess method of the MSFT\_MTProcess class

Create a new process.

## Syntax


```mof
uint32 CreateProcess(
  [in]  string CommandLine,
  [in]  uint32 WaitMilliseconds,
  [out] uint32 ProcessId,
  [out] string ActualCommandLine
);
```



## Parameters

<dl> <dt>

*CommandLine* \[in\]
</dt> <dd>

The command line to be run.

</dd> <dt>

*WaitMilliseconds* \[in\]
</dt> <dd>

Time, in milliseconds, to wait for the process to end.

</dd> <dt>

*ProcessId* \[out\]
</dt> <dd>

Returns the process identifier of the new process.

</dd> <dt>

*ActualCommandLine* \[out\]
</dt> <dd>

Returns the actual command line used to start the process, with any environment variables expanded.

</dd> </dl>

## Return value

Returns the exit code of the process, or 259 if the process did not exit before *WaitMilliseconds* elapsed.

## Remarks

The command line supports parameters and environment variables. If *WaitMilliseconds* is specified, this method will return the exit code of the process. If the process has not exited within the time specified, this method will return code 259. This method can be forced to wait indefinitely for the process to exit by specifying 0xffffffff (4294967295) in *WaitMilliseconds*.

## Examples

This PowerShell snippet connects to the *TestSrv1* computer and enumerates the processes, creates a new Cmd.exe process, and then enumerates the processes again.


```PowerShell
$option = New-CimSessionOption -Protocol WSMan
$session = New-CimSession -ComputerName TestSrv1 -SessionOption $option -Credential (Get-Credential)
Get-CimInstance  -CimSession $session -Namespace Root/Microsoft/Windows/ManagementTools -ClassName MSFT_MTProcess | Select Name,CpuPercent,ProcessId
Invoke-CimMethod -CimSession $session -Namespace Root/Microsoft/Windows/ManagementTools -ClassName MSFT_MTProcess -MethodName CreateProcess -Arguments @{ CommandLine = "Cmd.exe" }
Get-CimInstance  -CimSession $session -Namespace Root/Microsoft/Windows/ManagementTools -ClassName MSFT_MTProcess | Select Name,CpuPercent,ProcessId
```



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                          |
| Namespace<br/>                | Root\\Microsoft\\Windows\\ManagementTools<br/>                                    |
| MOF<br/>                      | <dl> <dt>MtTmProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MtTmProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_MTProcess**](msft-mtprocess.md)
</dt> </dl>

 

 





