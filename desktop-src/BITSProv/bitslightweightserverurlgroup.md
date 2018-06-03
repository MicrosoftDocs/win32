---
title: BitsCompactServerUrlGroup class
description: The BitsCompactServerUrlGroup class provides methods to manage URLs and URL groups for the Background Intelligent Transfer Service (BITS) Compact Server.
ms.assetid: c9a49726-b636-49cf-b514-13f53387579e
keywords:
- BitsLightweightServerUrlGroup class
- BitsLightweightServerUrlGroup class, described
topic_type:
- apiref
api_name:
- BitsLightweightServerUrlGroup
- BitsLightweightServerUrlGroup.UrlGroup
api_location:
- Root\microsoft\bits
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# BitsCompactServerUrlGroup class

The **BitsCompactServerUrlGroup** class provides methods to manage URLs and URL groups for the Background Intelligent Transfer Service (BITS) Compact Server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetical order, not MOF order.

## Syntax

``` syntax
class BitsCompactServerUrlGroup
{
  string UrlGroup;
};
```

## Members

The **BitsLightweightServerUrlGroup** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **BitsLightweightServerUrlGroup** class has these methods.



| Method                                                                                       | Description                                                                            |
|:---------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------|
| [**CheckUrl**](checkurl-bitslightweightserverurlgroup.md)                                   | Determines whether a URL exists on a server.<br/>                                |
| [**CreateUrl**](createurl-bitslightweightserverurlgroup.md)                                 | Creates a URL on the host.<br/>                                                  |
| [**CreateUrlGroup**](createurlgroup-bitslightweightserverurlgroup.md)                       | Creates a URL group on the host if the URL group was not available earlier.<br/> |
| [**DeleteUrl**](deleteurl-bitslightweightserverurlgroup.md)                                 | Deletes a URL on the server.<br/>                                                |
| [**DeleteUrlGroup**](bitslightweightserverurlgroup-deleteurlgroup.md)                       | Deletes a URL group on the host if the URL group was available earlier.<br/>     |
| [**GetProperty**](getproperty-bitslightweightserverurlgroup.md)                             | Gets the property that is associated with the URL group.<br/>                    |
| [**GetSslCertificate**](getsslcertificate-bitslightweightserverurlgroup.md)                 | Gets the SSL certificate for a port.<br/>                                        |
| [**GetUrlGroupAuthentication**](geturlgroupauthentication-bitslightweightserverurlgroup.md) | Gets the authentication scheme for a URL group.<br/>                             |
| [**RemoveSslCertificate**](removesslcertificate-bitslightweightserverurlgroup.md)           | Removes the SSL certificate for a port.<br/>                                     |
| [**SetProperty**](setproperty-bitslightweightserverurlgroup.md)                             | Sets the property that is associated with the URL group.<br/>                    |
| [**SetSslCertificate**](setsslcertificate-bitslightweightserverurlgroup.md)                 | Sets the SSL certificate for a port.<br/>                                        |
| [**SetUrlGroupAuthentication**](seturlgroupauthentication-bitslightweightserverurlgroup.md) | Sets the authentication scheme for a URL group.<br/>                             |



 

### Properties

The **BitsLightweightServerUrlGroup** class has these properties.

<dl> <dt>

**UrlGroup**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property specifies the URL group that is associated with the class.

</dd> </dl>

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                           |
| Redistributable<br/>          | Windows Management Framework on Windows Server 2008 with SP2<br/>                     |
| Namespace<br/>                | Root\\microsoft\\bits<br/>                                                            |
| MOF<br/>                      | <dl> <dt>BitsProvider.mof</dt> </dl> |



 

 





