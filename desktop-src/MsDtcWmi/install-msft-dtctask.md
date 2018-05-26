---
title: Install method of the MSFT\_DtcTask class
description: Installs the local transactions coordinator.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e26937a2-7798-479c-bad0-aaeab6e268a7
ms.prod: windows-server-dev
ms.technology:
- distributed-transaction-coordinator
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Install method
- Install method, MSFT_DtcTask class
- MSFT_DtcTask class, Install method
topic_type:
- apiref
api_name:
- MSFT_DtcTask.Install
api_location:
- MsDtcWmi.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Install method of the MSFT\_DtcTask class

Installs the local transactions coordinator.

## Syntax


```mof
uint32 Install(
  [in] string LogPath,
  [in] string StartType
);
```



## Parameters

<dl> <dt>

*LogPath* \[in\]
</dt> <dd>

The path of the log file. If not specified, this method uses the default log path.

</dd> <dt>

*StartType* \[in\]
</dt> <dd>

The start type for the local transactions coordinator.

The possible values are.

"AutoStart"

"DemandStart"

"Disabled"

</dd> </dl>

## Return value

Returns "0" on success, otherwise returns a WMI error code.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\MsDTC<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Msdtcwmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsDtcWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_DtcTask**](msft-dtctask.md)
</dt> </dl>

 

 





