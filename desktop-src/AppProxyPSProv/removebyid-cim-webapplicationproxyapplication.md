---
Description: 'Removes the web application with the specified ID from Web Application Proxy.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: 'def4d8bf-8c70-4d46-9cbf-60accc7121f7'
ms.prod: 'windows-server-dev'
ms.technology:
- 'web-app-proxy'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'RemoveByID method of the CIM\_WebApplicationProxyApplication class'
---

# RemoveByID method of the CIM\_WebApplicationProxyApplication class

Removes the web application with the specified ID from Web Application Proxy.

## Syntax


```mof
uint32 RemoveByID(
  [in] string ID[]
);
```



## Parameters

<dl> <dt>

*ID* \[in\]
</dt> <dd>

An array that contains the ID of the application to remove.

</dd> </dl>

## Return value

Returns 0 on success, otherwise returns a WMI error code.

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                 |
| Namespace<br/>                | Root\\Microsoft\\Windows\\WebApplicationProxy<br/>                                          |
| MOF<br/>                      | <dl> <dt>AppProxyPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AppProxyPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_WebApplicationProxyApplication**](cim-webapplicationproxyapplication.md)
</dt> </dl>

 

 




