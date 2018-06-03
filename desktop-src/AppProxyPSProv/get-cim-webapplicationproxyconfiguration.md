---
Description: Retrieves the server configuration for Web Application Proxy.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9f9937a3-520a-4ed8-8fac-a0193ff9a6b2
ms.prod: windows-server-dev
ms.technology:
- web-app-proxy
- windows-management-instrumentation
ms.tgt_platform: multiple
title: Get method of the CIM\_WebApplicationProxyConfiguration class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Get method of the CIM\_WebApplicationProxyConfiguration class

Retrieves the server configuration for Web Application Proxy.

## Syntax


```mof
uint32 Get(
  [out] AppProxyGlobalConfiguration cmdletOutput
);
```



## Parameters

<dl> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

When this method returns, the server configuration for Web Application Proxy.

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

[**CIM\_WebApplicationProxyConfiguration**](cim-webapplicationproxyconfiguration.md)
</dt> </dl>

 

 




