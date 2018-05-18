---
title: DisableByInputObject method of the MSFT\_OdbcPerfCounterTask class
description: Disables the ODBC Connection Pooling PerfMon counters for ODBC Connection Pooling feature.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '481c84c7-0bf7-492b-b7eb-27227938dbcc'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DisableByInputObject method", "DisableByInputObject method, MSFT_OdbcPerfCounterTask class", "MSFT_OdbcPerfCounterTask class, DisableByInputObject method"]
topic_type:
- apiref
api_name:
- MSFT_OdbcPerfCounterTask.DisableByInputObject
api_location:
- WdacWmiProv.dll
api_type:
- COM
---

# DisableByInputObject method of the MSFT\_OdbcPerfCounterTask class

Disables the ODBC Connection Pooling PerfMon counters for ODBC Connection Pooling feature.

## Syntax


```mof
uint32 DisableByInputObject(
  [in]  boolean              PassThru,
  [in]  MSFT_OdbcPerfCounter InputObject[],
  [out] MSFT_OdbcPerfCounter cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*PassThru* \[in\]
</dt> <dd>

Passes the object created by this cmdlet through the pipeline. By default, this cmdlet does not pass any objects through the pipeline.

</dd> <dt>

*InputObject* \[in\]
</dt> <dd>

Disables the ODBC Connection Pooling PerfMon counters represented by the specified [**MSFT\_OdbcPerfCounter**](msft-odbcperfcounter.md) instances. Enter a variable that contains the objects, or type a command or expression that gets the objects.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The output is an array of CIM objects of type [**MSFT\_OdbcPerfCounter**](msft-odbcperfcounter.md), each of which represents an ODBC Performance Counter setting.

</dd> </dl>

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                             |
| Namespace<br/>                | Root\\Microsoft\\Windows\\WDAC<br/>                                                  |
| MOF<br/>                      | <dl> <dt>WdacWmiProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WdacWmiProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_OdbcPerfCounterTask**](msft-odbcperfcountertask.md)
</dt> <dt>

[**MSFT\_OdbcPerfCounter**](msft-odbcperfcounter.md)
</dt> </dl>

 

 





