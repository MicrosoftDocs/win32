---
title: RemoveByName method of the MSFT\_OdbcDsnTask class
description: Removes one or more existing DSNs from the system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 73e6d214-33da-41eb-8d74-0ed2a872ea60
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoveByName method
- RemoveByName method, MSFT_OdbcDsnTask class
- MSFT_OdbcDsnTask class, RemoveByName method
topic_type:
- apiref
api_name:
- MSFT_OdbcDsnTask.RemoveByName
api_location:
- WdacWmiProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RemoveByName method of the MSFT\_OdbcDsnTask class

Removes one or more existing DSNs from the system.

## Syntax


```mof
uint32 RemoveByName(
  [in]  boolean      PassThru,
  [in]  string       Name,
  [in]  string       DriverName,
  [in]  string       Platform,
  [in]  string       DsnType,
  [out] MSFT_OdbcDsn cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*PassThru* \[in\]
</dt> <dd>

Passes the object created by this cmdlet through the pipeline. By default, this cmdlet does not pass any objects through the pipeline.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Specifies one or more ODBC DSNs to remove. You can use wildcard characters.

</dd> <dt>

*DriverName* \[in\]
</dt> <dd>

This cmdlet will remove the ODBC DSN using this driver only. You can use wildcard characters. The default is to remove all ODBC DSNs.

</dd> <dt>

*Platform* \[in\]
</dt> <dd>

The platform architecture of the ODBC DSN to remove. Possible values are '32-bit', '64-bit' or 'All'. The default is '32-bit' on a 32-bit process and '64-bit' on a 64-bit process. This is the platform architecture on the remote machine if this command is executed in a remote CIM session.

</dd> <dt>

*DsnType* \[in\]
</dt> <dd>

The type of the ODBC DSN to remove. Possible values are 'User', 'System' or 'All'.

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
| MOF<br/>                      | <dl> <dt>WdacWmiProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WdacWmiProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_OdbcDsnTask**](msft-odbcdsntask.md)
</dt> <dt>

[**MSFT\_OdbcDsn**](msft-odbcdsn.md)
</dt> </dl>

 

 





