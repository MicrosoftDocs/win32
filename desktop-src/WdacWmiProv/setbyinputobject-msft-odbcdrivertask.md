---
title: SetByInputObject method of the MSFT\_OdbcDriverTask class
description: Configure driver\\\\'s properties for one or more installed ODBC drivers.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 839c096b-ef6f-4562-8931-f0a16c98aa77
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetByInputObject method
- SetByInputObject method, MSFT_OdbcDriverTask class
- MSFT_OdbcDriverTask class, SetByInputObject method
topic_type:
- apiref
api_name:
- MSFT_OdbcDriverTask.SetByInputObject
api_location:
- WdacWmiProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetByInputObject method of the MSFT\_OdbcDriverTask class

Configure driver\\\\'s properties for one or more installed ODBC drivers.

## Syntax


```mof
uint32 SetByInputObject(
  [in]  boolean         PassThru,
  [in]  string          SetPropertyValue[],
  [in]  string          RemovePropertyValue[],
  [in]  MSFT_OdbcDriver InputObject[],
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

*InputObject* \[in\]
</dt> <dd>

Modifies the ODBC driver represented by the specified ODBC driver objects. Enter a variable that contains the objects, or type a command or expression that gets the objects.

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

 

 





