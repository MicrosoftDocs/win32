---
title: Get method of the MSFT\_OdbcDsnTask class
description: Retrieves one or more ODBC DSNs from the system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5f73c113-7e03-4e7e-8c3c-0ba702aa42f8
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, MSFT_OdbcDsnTask class
- MSFT_OdbcDsnTask class, Get method
topic_type:
- apiref
api_name:
- MSFT_OdbcDsnTask.Get
api_location:
- WdacWmiProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Get method of the MSFT\_OdbcDsnTask class

Retrieves one or more ODBC DSNs from the system.

## Syntax


```mof
uint32 Get(
  [in]  string       Name,
  [in]  string       DriverName,
  [in]  string       Platform,
  [in]  string       DsnType,
  [out] MSFT_OdbcDsn cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

Specifies one or more ODBC DSNs by DSN name. You can use wildcard characters. The default is to return all ODBC DSNs.

</dd> <dt>

*DriverName* \[in\]
</dt> <dd>

Gets only ODBC DSNs that are using the specified ODBC driver. You can use wildcard characters. The default is to return all ODBC DSNs.

</dd> <dt>

*Platform* \[in\]
</dt> <dd>

The platform architecture of the ODBC DSN to retrieve. Possible values are '32-bit', '64-bit' or 'All'. The default is 'All'. This is the platform architecture on the remote machine if this command is executed in a remote CIM session.

</dd> <dt>

*DsnType* \[in\]
</dt> <dd>

The type of the ODBC DSN to retrieve. Possible values are 'User', 'System' or 'All'. The default is 'All'.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The output is an array of CIM objects of type [**MSFT\_OdbcDsn**](msft-odbcdsn.md), each of which represents an ODBC DSN.

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

[**MSFT\_OdbcDsnTask**](msft-odbcdsntask.md)
</dt> <dt>

[**MSFT\_OdbcDsn**](msft-odbcdsn.md)
</dt> </dl>

 

 





