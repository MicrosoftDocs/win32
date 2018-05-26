---
Description: Manages information about a published web application.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 662d357e-ab6c-416a-9c5f-140205ff9d97
ms.prod: windows-server-dev
ms.technology:
- web-app-proxy
- windows-management-instrumentation
ms.tgt_platform: multiple
title: CIM\_WebApplicationProxyApplication class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_WebApplicationProxyApplication class

Manages information about a published web application.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0"), dynamic, provider("AppProxyPSProvider"), AMENDMENT]
class CIM_WebApplicationProxyApplication
{
};
```

## Members

The **CIM\_WebApplicationProxyApplication** class has these types of members:

-   [Methods](#methods)

### Methods

The **CIM\_WebApplicationProxyApplication** class has these methods.



| Method                                                                  | Description                                                                                       |
|:------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------|
| [**Add**](add-cim-webapplicationproxyapplication.md)                   | Publishes a web application through Web Application Proxy.<br/>                             |
| [**GetByID**](getbyid-cim-webapplicationproxyapplication.md)           | Retrieves information about the published web application that has the specified ID.<br/>   |
| [**GetByName**](getbyname-cim-webapplicationproxyapplication.md)       | Retrieves information about the published web application that has the specified name.<br/> |
| [**RemoveByID**](removebyid-cim-webapplicationproxyapplication.md)     | Removes the web application with the specified ID from Web Application Proxy.<br/>          |
| [**RemoveByName**](removebyname-cim-webapplicationproxyapplication.md) | Removes the web application with the specified name from Web Application Proxy.<br/>        |
| [**SetByID**](setbyid-cim-webapplicationproxyapplication.md)           | Updates the settings of a published application.<br/>                                       |



 

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

 

 




