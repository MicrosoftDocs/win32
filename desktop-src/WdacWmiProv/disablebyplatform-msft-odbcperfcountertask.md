---
title: DisableByPlatform method of the MSFT\_OdbcPerfCounterTask class
description: Disables the ODBC Connection Pooling PerfMon counters for ODBC Connection Pooling feature.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e4356529-f78a-415b-b9e1-dd0237ecc332
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DisableByPlatform method
- DisableByPlatform method, MSFT_OdbcPerfCounterTask class
- MSFT_OdbcPerfCounterTask class, DisableByPlatform method
topic_type:
- apiref
api_name:
- MSFT_OdbcPerfCounterTask.DisableByPlatform
api_location:
- WdacWmiProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DisableByPlatform method of the MSFT\_OdbcPerfCounterTask class

Disables the ODBC Connection Pooling PerfMon counters for ODBC Connection Pooling feature.

## Syntax


```mof
uint32 DisableByPlatform(
  [in]  boolean              PassThru,
  [in]  string               Platform,
  [out] MSFT_OdbcPerfCounter cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*PassThru* \[in\]
</dt> <dd>

Passes the object created by this cmdlet through the pipeline. By default, this cmdlet does not pass any objects through the pipeline.

</dd> <dt>

*Platform* \[in\]
</dt> <dd>

The platform architecture of the ODBC Connection Pooling PerfMon counters to disable. Possible values are '32-bit', '64-bit' or 'All'. The default is '32-bit' on a 32-bit process and '64-bit' on a 64-bit process. This is the platform architecture on the remote machine if this command is executed on a remote CIM session.

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
| MOF<br/>                      | <dl> <dt>WdacWmiProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WdacWmiProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_OdbcPerfCounterTask**](msft-odbcperfcountertask.md)
</dt> <dt>

[**MSFT\_OdbcPerfCounter**](msft-odbcperfcounter.md)
</dt> </dl>

 

 





