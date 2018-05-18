---
title: Get method of the MSFT\_DtcClusterTMMappingTask class
description: Retrieves cluster DTC mapping data.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '7bc2475a-b46d-47d1-9cf1-40820393f7f8'
ms.prod: 'windows-server-dev'
ms.technology:
- 'distributed-transaction-coordinator'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Get method", "Get method, MSFT_DtcClusterTMMappingTask class", "MSFT_DtcClusterTMMappingTask class, Get method"]
topic_type:
- apiref
api_name:
- MSFT_DtcClusterTMMappingTask.Get
api_location:
- MsDtcWmi.dll
api_type:
- COM
---

# Get method of the MSFT\_DtcClusterTMMappingTask class

Retrieves cluster DTC mapping data.

## Syntax


```mof
uint32 Get(
  [in]  string              Name,
  [out] DtcClusterTMMapping cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The name of the mapping data. If this parameter is not set, all Transaction Manager (TM) mappings are retrieved.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An array of [**DtcClusterTMMapping**](dtcclustertmmapping.md) embedded instances containing the retrieved mapping data.

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

[**MSFT\_DtcClusterTMMappingTask**](msft-dtcclustertmmappingtask.md)
</dt> </dl>

 

 





