---
title: RemoveByDsnObject method of the MSFT\_OdbcDsnTask class
description: Removes one or more existing DSNs from the system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: cff3f095-5bd9-49eb-acb1-8600199a2205
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoveByDsnObject method
- RemoveByDsnObject method, MSFT_OdbcDsnTask class
- MSFT_OdbcDsnTask class, RemoveByDsnObject method
topic_type:
- apiref
api_name:
- MSFT_OdbcDsnTask.RemoveByDsnObject
api_location:
- WdacWmiProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RemoveByDsnObject method of the MSFT\_OdbcDsnTask class

Removes one or more existing DSNs from the system.

## Syntax


```mof
uint32 RemoveByDsnObject(
  [in]  boolean      PassThru,
  [in]  MSFT_OdbcDsn InputObject[],
  [out] MSFT_OdbcDsn cmdletOutput[]
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

Removes the ODBC DSNs represented by the specified ODBC DSN objects. Enter a variable that contains the objects, or type a command or expression that gets the objects.

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

 

 





