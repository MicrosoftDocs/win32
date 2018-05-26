---
title: SetByName method of the MSFT\_OdbcDriverTask class
description: Configure driver\\\\s properties for one or more installed ODBC drivers.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f31d8841-4869-4cf1-8fe9-ca18e47f5cc8
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetByName method
- SetByName method, MSFT_OdbcDriverTask class
- MSFT_OdbcDriverTask class, SetByName method
topic_type:
- apiref
api_name:
- MSFT_OdbcDriverTask.SetByName
api_location:
- WdacWmiProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SetByName method of the MSFT\_OdbcDriverTask class

Configure driver\\\\'s properties for one or more installed ODBC drivers.

## Syntax


```mof
uint32 SetByName(
  [in]  boolean         PassThru,
  [in]  string          SetPropertyValue[],
  [in]  string          RemovePropertyValue[],
  [in]  string          Name,
  [in]  string          Platform,
  [out] MSFT_OdbcDriver cmdletOutput[]
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

Specifies the property values of the ODBC driver to be modified or added. Format as an array of strings where each string is: &lt;key&gt;=&lt;value&gt;.

</dd> <dt>

*RemovePropertyValue* \[in\]
</dt> <dd>

Specifies the property values of the ODBC driver to be deleted. This is an array of keys to be removed.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Specifies one or more ODBC drivers by driver name. You can use wildcard characters.

</dd> <dt>

*Platform* \[in\]
</dt> <dd>

The platform architecture of the ODBC driver. Possible values are '32-bit', '64-bit' or 'All'. The default is '32-bit' on a 32-bit process and '64-bit' on a 64-bit process. This is the platform architecture on the remote machine if this command is executed in a remote CIM session.

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
| MOF<br/>                      | <dl> <dt>WdacWmiProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WdacWmiProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_OdbcDriverTask**](msft-odbcdrivertask.md)
</dt> <dt>

[**MSFT\_OdbcDriver**](msft-odbcdriver.md)
</dt> </dl>

 

 





