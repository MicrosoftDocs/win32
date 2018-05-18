---
title: Get method of the MSFT\_DtcClusterDefaultTask class
description: Retrieves the cluster DTC.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'e4550735-4ec9-44fd-8376-0f9f700e1a05'
ms.prod: 'windows-server-dev'
ms.technology:
- 'distributed-transaction-coordinator'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Get method", "Get method, MSFT_DtcClusterDefaultTask class", "MSFT_DtcClusterDefaultTask class, Get method"]
topic_type:
- apiref
api_name:
- MSFT_DtcClusterDefaultTask.Get
api_location:
- MsDtcWmi.dll
api_type:
- COM
---

# Get method of the MSFT\_DtcClusterDefaultTask class

Retrieves the cluster DTC.

## Syntax


```mof
uint32 Get(
  [out] string cmdletOutput
);
```



## Parameters

<dl> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The name of the retrieved cluster DTC.

</dd> </dl>

## Return value

Returns "0" on success, otherwise returns a WMI error code.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\MsDTC<br/>                                                                  |
| Header<br/>                   | <dl> <dt>Wbemcli.h</dt> </dl>    |
| MOF<br/>                      | <dl> <dt>Msdtcwmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsDtcWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_DtcClusterDefaultTask**](msft-dtcclusterdefaulttask.md)
</dt> </dl>

 

 





