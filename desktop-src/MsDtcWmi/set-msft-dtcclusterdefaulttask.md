---
title: Set method of the MSFT\_DtcClusterDefaultTask class
description: Updates cluster the DTC.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 99653eb0-cd5f-4d11-a3ec-ad7e6eab4271
ms.prod: windows-server-dev
ms.technology:
- distributed-transaction-coordinator
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Set method
- Set method, MSFT_DtcClusterDefaultTask class
- MSFT_DtcClusterDefaultTask class, Set method
topic_type:
- apiref
api_name:
- MSFT_DtcClusterDefaultTask.Set
api_location:
- MsDtcWmi.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Set method of the MSFT\_DtcClusterDefaultTask class

Updates cluster the DTC.

## Syntax


```mof
uint32 Set(
  [in]  string DtcResourceName,
  [out] string cmdletOutput
);
```



## Parameters

<dl> <dt>

*DtcResourceName* \[in\]
</dt> <dd>

The new name of the DTC.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The name of the updated cluster DTC.

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

[**MSFT\_DtcClusterDefaultTask**](msft-dtcclusterdefaulttask.md)
</dt> </dl>

 

 





