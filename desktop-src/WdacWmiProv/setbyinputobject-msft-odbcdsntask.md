---
title: SetByInputObject method of the MSFT\_OdbcDsnTask class
description: Modifies one or more ODBC DSNs.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '935a8cb2-3e5c-481e-8cb9-50073de50766'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["SetByInputObject method", "SetByInputObject method, MSFT_OdbcDsnTask class", "MSFT_OdbcDsnTask class, SetByInputObject method"]
topic_type:
- apiref
api_name:
- MSFT_OdbcDsnTask.SetByInputObject
api_location:
- WdacWmiProv.dll
api_type:
- COM
---

# SetByInputObject method of the MSFT\_OdbcDsnTask class

Modifies one or more ODBC DSNs.

## Syntax


```mof
uint32 SetByInputObject(
  [in]  boolean      PassThru,
  [in]  string       SetPropertyValue[],
  [in]  string       RemovePropertyValue[],
  [in]  MSFT_OdbcDsn InputObject[],
  [out] MSFT_OdbcDsn cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*PassThru* \[in\]
</dt> <dd>

Passes the object created by this cmdlet through the pipeline. By default, this cmdlet does not pass any objects through the pipeline.

</dd> <dt>

*SetPropertyValue* \[in\]
</dt> <dd>

Specifies the property values of the ODBC DSN that you are modifying or adding. Format as an array of strings where each string is: &lt;key&gt;=&lt;value&gt;.

</dd> <dt>

*RemovePropertyValue* \[in\]
</dt> <dd>

Specifies the property values of the ODBC DSN to be deleted. This is an array of keys to be removed.

</dd> <dt>

*InputObject* \[in\]
</dt> <dd>

Modifies the ODBC DSNs represented by the specified ODBC DSN objects. Enter a variable that contains the objects, or type a command or expression that gets the objects.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The output is an array of CIM objects of type [**MSFT\_OdbcDsn**](msft-odbcdsn.md), each of which represents an ODBC DSN.

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

[**MSFT\_OdbcDsnTask**](msft-odbcdsntask.md)
</dt> <dt>

[**MSFT\_OdbcDsn**](msft-odbcdsn.md)
</dt> </dl>

 

 





