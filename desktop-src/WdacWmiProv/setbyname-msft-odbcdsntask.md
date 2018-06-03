---
title: SetByName method of the MSFT\_OdbcDsnTask class
description: Modifies one or more ODBC DSNs.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 144bad20-2805-4f5d-9d81-90487ef335ad
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetByName method
- SetByName method, MSFT_OdbcDsnTask class
- MSFT_OdbcDsnTask class, SetByName method
topic_type:
- apiref
api_name:
- MSFT_OdbcDsnTask.SetByName
api_location:
- WdacWmiProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetByName method of the MSFT\_OdbcDsnTask class

Modifies one or more ODBC DSNs.

## Syntax


```mof
uint32 SetByName(
  [in]  boolean      PassThru,
  [in]  string       SetPropertyValue[],
  [in]  string       RemovePropertyValue[],
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

*SetPropertyValue* \[in\]
</dt> <dd>

Specifies the property values of the ODBC DSN that you are modifying or adding. Format as an array of strings where each string is: &lt;key&gt;=&lt;value&gt;.

</dd> <dt>

*RemovePropertyValue* \[in\]
</dt> <dd>

Specifies the property values of the ODBC DSN to be deleted. This is an array of keys to be removed.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

The name of the ODBC DSN to set. You can use wildcard characters.

</dd> <dt>

*DriverName* \[in\]
</dt> <dd>

This cmdlet will set the ODBC DSN using this driver only. You can use wildcard characters. The default is to set all ODBC DSNs.

</dd> <dt>

*Platform* \[in\]
</dt> <dd>

The platform architecture of the ODBC DSN to set. Possible values are '32-bit', '64-bit' or 'All'. The default is '32-bit' on a 32-bit process and '64-bit' on a 64-bit process. This is the platform architecture on the remote machine if this command is executed in a remote CIM session.

</dd> <dt>

*DsnType* \[in\]
</dt> <dd>

The type of the ODBC DSN to set. Possible values are 'User', 'System' or 'All'.

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

 

 





