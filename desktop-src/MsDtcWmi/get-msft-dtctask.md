---
title: Get method of the MSFT\_DtcTask class
description: Retrieves a DTC instance.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'acdbbb99-fe52-49d6-9927-033a2bb4a03d'
ms.prod: 'windows-server-dev'
ms.technology:
- 'distributed-transaction-coordinator'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Get method", "Get method, MSFT_DtcTask class", "MSFT_DtcTask class, Get method"]
topic_type:
- apiref
api_name:
- MSFT_DtcTask.Get
api_location:
- MsDtcWmi.dll
api_type:
- COM
---

# Get method of the MSFT\_DtcTask class

Retrieves a DTC instance.

## Syntax


```mof
uint32 Get(
  [in]  string      DtcName,
  [out] DtcInstance cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*DtcName* \[in\]
</dt> <dd>

Specifies the DTC instance to retrieve on the host. If you do not specify this parameter, or if you specify a value of "Local", this method gets the local DTC instance for the host.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An array of [**DtcInstance**](dtcinstance.md) embedded instances.

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

[**MSFT\_DtcTask**](msft-dtctask.md)
</dt> </dl>

 

 





