---
Description: Removes the web application with the specified name from Web Application Proxy.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8bc81bd9-e296-4645-abfe-cc40b1e5ca68
ms.prod: windows-server-dev
ms.technology:
- web-app-proxy
- windows-management-instrumentation
ms.tgt_platform: multiple
title: RemoveByName method of the CIM\_WebApplicationProxyApplication class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RemoveByName method of the CIM\_WebApplicationProxyApplication class

Removes the web application with the specified name from Web Application Proxy.

## Syntax


```mof
uint32 RemoveByName(
  [in] string Name
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The name of the application to remove.

</dd> </dl>

## Return value

Returns 0 on success, otherwise returns a WMI error code.

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                 |
| Namespace<br/>                | Root\\Microsoft\\Windows\\WebApplicationProxy<br/>                                          |
| MOF<br/>                      | <dl> <dt>AppProxyPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AppProxyPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_WebApplicationProxyApplication**](cim-webapplicationproxyapplication.md)
</dt> </dl>

 

 




