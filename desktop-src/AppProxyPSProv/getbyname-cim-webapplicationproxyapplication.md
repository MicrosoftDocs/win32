---
Description: 'Retrieves information about the published web application that has the specified name.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '2d4e4352-0bf9-47ca-8651-17c4cc658092'
ms.prod: 'windows-server-dev'
ms.technology:
- 'web-app-proxy'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'GetByName method of the CIM\_WebApplicationProxyApplication class'
---

# GetByName method of the CIM\_WebApplicationProxyApplication class

Retrieves information about the published web application that has the specified name.

## Syntax


```mof
uint32 GetByName(
  [in]  string          Name,
  [out] PublishedWebApp cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The name of the published web application.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

When this method returns, if there are multiple results, this parameter contains an array of application names. Otherwise, this parameter contains an array that contains the information about the published application.

</dd> </dl>

## Return value

Returns 0 on success, otherwise returns a WMI error code.

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                 |
| Namespace<br/>                | Root\\Microsoft\\Windows\\WebApplicationProxy<br/>                                          |
| Header<br/>                   | <dl> <dt>Wmp.h</dt> </dl>                  |
| MOF<br/>                      | <dl> <dt>AppProxyPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AppProxyPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_WebApplicationProxyApplication**](cim-webapplicationproxyapplication.md)
</dt> </dl>

 

 




