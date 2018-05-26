---
Description: Manages the settings for Web Application Proxy.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7d294634-836f-4145-a598-67f8cafc331c
ms.prod: windows-server-dev
ms.technology:
- web-app-proxy
- windows-management-instrumentation
ms.tgt_platform: multiple
title: CIM\_WebApplicationProxyConfiguration class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_WebApplicationProxyConfiguration class

Manages the settings for Web Application Proxy.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0"), dynamic, provider("AppProxyPSProvider"), AMENDMENT]
class CIM_WebApplicationProxyConfiguration
{
};
```

## Members

The **CIM\_WebApplicationProxyConfiguration** class has these types of members:

-   [Methods](#methods)

### Methods

The **CIM\_WebApplicationProxyConfiguration** class has these methods.



| Method                                                  | Description                                                            |
|:--------------------------------------------------------|:-----------------------------------------------------------------------|
| [**Get**](get-cim-webapplicationproxyconfiguration.md) | Retrieves the global settings for Web Application Proxy.<br/>    |
| [**Set**](set-cim-webapplicationproxyconfiguration.md) | Updates the server configuration for Web Application Proxy.<br/> |



 

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

[Application Proxy WMI Provider Reference](application-proxy-wmi-provider-reference.md)
</dt> </dl>

 

 




