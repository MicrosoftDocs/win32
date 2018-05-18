---
Description: 'Retrieves information about the published web application that has the specified ID.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: 'ce2c3acb-8f9a-46a0-90de-01dc257e2102'
ms.prod: 'windows-server-dev'
ms.technology:
- 'web-app-proxy'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'GetByID method of the CIM\_WebApplicationProxyApplication class'
---

# GetByID method of the CIM\_WebApplicationProxyApplication class

Retrieves information about the published web application that has the specified ID.

## Syntax


```mof
uint32 GetByID(
  [in]  string          ID,
  [out] PublishedWebApp cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ID* \[in\]
</dt> <dd>

The ID of the published web application.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

When this method returns, if there are multiple results, this parameter contains an array of application names. Otherwise, this parameter contains an array that contains the information about the published web application.

</dd> </dl>

## Return value

Returns 0 on success, otherwise returns a WMI error code.

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                 |
| Namespace<br/>                | Root\\Microsoft\\Windows\\WebApplicationProxy<br/>                                          |
| Header<br/>                   | <dl> <dt>Fsrm.h</dt> </dl>                 |
| MOF<br/>                      | <dl> <dt>AppProxyPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AppProxyPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_WebApplicationProxyApplication**](cim-webapplicationproxyapplication.md)
</dt> </dl>

 

 




