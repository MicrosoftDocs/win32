---
title: Add method of the MSFT\_OdbcDsnTask class
description: Adds an ODBC DSN.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '93055332-e3f1-4857-a46d-5020837bdbea'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Add method", "Add method, MSFT_OdbcDsnTask class", "MSFT_OdbcDsnTask class, Add method"]
topic_type:
- apiref
api_name:
- MSFT_OdbcDsnTask.Add
api_location:
- WdacWmiProv.dll
api_type:
- COM
---

# Add method of the MSFT\_OdbcDsnTask class

Adds an ODBC DSN.

## Syntax


```mof
uint32 Add(
  [in]  string       Name,
  [in]  string       DriverName,
  [in]  string       SetPropertyValue[],
  [in]  boolean      PassThru,
  [in]  string       Platform,
  [in]  string       DsnType,
  [out] MSFT_OdbcDsn cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The name of the ODBC DSN to create. You cannot use wildcard characters.

</dd> <dt>

*DriverName* \[in\]
</dt> <dd>

The name of the ODBC driver for the new ODBC DSN. You cannot use wildcard characters.

</dd> <dt>

*SetPropertyValue* \[in\]
</dt> <dd>

Specifies the property values of the new ODBC DSN. Format as an array of strings where each string is: &lt;key&gt;=&lt;value&gt;.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Passes the object created by this cmdlet through the pipeline. By default, this cmdlet does not pass any objects through the pipeline.

</dd> <dt>

*Platform* \[in\]
</dt> <dd>

The platform architecture of the ODBC DSN you are adding. Possible values are '32-bit' or '64-bit'. The default is '32-bit' on a 32-bit process and '64-bit' on a 64-bit process. This is the platform architecture on the remote machine if this command is executed in a remote CIM session.

</dd> <dt>

*DsnType* \[in\]
</dt> <dd>

The type of the ODBC DSN to add. Possible values are 'User' or 'System'.

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

 

 





