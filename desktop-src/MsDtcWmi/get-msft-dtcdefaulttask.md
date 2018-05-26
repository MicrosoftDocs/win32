---
title: Get method of the MSFT\_DtcDefaultTask class
description: Retrieves the default DTC instance.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8aa337e1-9384-4c51-8d39-a93b892f81f1
ms.prod: windows-server-dev
ms.technology:
- distributed-transaction-coordinator
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, MSFT_DtcDefaultTask class
- MSFT_DtcDefaultTask class, Get method
topic_type:
- apiref
api_name:
- MSFT_DtcDefaultTask.Get
api_location:
- MsDtcWmi.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Get method of the MSFT\_DtcDefaultTask class

Retrieves the default DTC instance.

## Syntax


```mof
uint32 Get(
  [out] string cmdletOutput
);
```



## Parameters

<dl> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The name of the retrieved DTC instance.

</dd> </dl>

## Return value

Returns "0" on success, otherwise returns a WMI error code.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\MsDTC<br/>                                                                  |
| Header<br/>                   | <dl> <dt>Wbemcli.h</dt> </dl>    |
| MOF<br/>                      | <dl> <dt>Msdtcwmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsDtcWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_DtcDefaultTask**](msft-dtcdefaulttask.md)
</dt> </dl>

 

 





