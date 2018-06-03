---
title: Get method of the MSFT\_OdbcPerfCounterTask class
description: Retrieves the ODBC Connection Pooling PerfMon counters for ODBC Connection Pooling feature.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6cb60092-47bc-42f2-b226-5a265d78b701
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, MSFT_OdbcPerfCounterTask class
- MSFT_OdbcPerfCounterTask class, Get method
topic_type:
- apiref
api_name:
- MSFT_OdbcPerfCounterTask.Get
api_location:
- WdacWmiProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Get method of the MSFT\_OdbcPerfCounterTask class

Retrieves the ODBC Connection Pooling PerfMon counters for ODBC Connection Pooling feature.

## Syntax


```mof
uint32 Get(
  [in]  string               Platform,
  [out] MSFT_OdbcPerfCounter cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*Platform* \[in\]
</dt> <dd>

The platform architecture of the ODBC Connection Pooling PerfMon counters to get. Possible values are '32-bit', '64-bit' or 'All'. The default is 'All'. This is the platform architecture on the remote machine if this command is executed on a remote CIM session.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The output is an array of CIM objects of type [**MSFT\_OdbcPerfCounter**](msft-odbcperfcounter.md), each of which represents an ODBC Performance Counter setting.

</dd> </dl>

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                             |
| Namespace<br/>                | Root\\Microsoft\\Windows\\WDAC<br/>                                                  |
| Header<br/>                   | <dl> <dt>Wbemcli.h</dt> </dl>       |
| MOF<br/>                      | <dl> <dt>WdacWmiProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WdacWmiProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_OdbcPerfCounterTask**](msft-odbcperfcountertask.md)
</dt> <dt>

[**MSFT\_OdbcPerfCounter**](msft-odbcperfcounter.md)
</dt> </dl>

 

 





