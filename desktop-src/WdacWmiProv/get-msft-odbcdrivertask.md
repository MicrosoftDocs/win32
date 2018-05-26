---
title: Get method of the MSFT\_OdbcDriverTask class
description: Retrieves one or more installed ODBC drivers from the system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f0a93adf-364e-47e5-a87e-6883c0a9dc79
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, MSFT_OdbcDriverTask class
- MSFT_OdbcDriverTask class, Get method
topic_type:
- apiref
api_name:
- MSFT_OdbcDriverTask.Get
api_location:
- WdacWmiProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Get method of the MSFT\_OdbcDriverTask class

Retrieves one or more installed ODBC drivers from the system.

## Syntax


```mof
uint32 Get(
  [in]  string          Name,
  [in]  string          Platform,
  [out] MSFT_OdbcDriver cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

Specifies one or more ODBC drivers by driver name. You can use wildcard characters. The default is to return all ODBC drivers.

</dd> <dt>

*Platform* \[in\]
</dt> <dd>

The platform architecture of the ODBC driver. Possible values are '32-bit', '64-bit' or 'All'. The default is 'All'. This is the platform architecture on the remote machine if this command is executed in a remote CIM session.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The output is an array of CIM objects of type [**MSFT\_OdbcDriver**](msft-odbcdriver.md), each of which represents an ODBC driver.

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

[**MSFT\_OdbcDriverTask**](msft-odbcdrivertask.md)
</dt> <dt>

[**MSFT\_OdbcDriver**](msft-odbcdriver.md)
</dt> </dl>

 

 





