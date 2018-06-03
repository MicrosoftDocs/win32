---
title: PS\_DnsServerTrustPoint class
description: DNS Server Trust Point Task Definition.
audience: developer
ms.assetid: 852b08de-3db4-4d38-aeb9-914391d51e8c
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DnsServerTrustPoint class
- PS_DnsServerTrustPoint class, described
topic_type:
- apiref
api_name:
- PS_DnsServerTrustPoint
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PS\_DnsServerTrustPoint class

DNS Server Trust Point Task Definition.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class PS_DnsServerTrustPoint
{
};
```

## Members

The **PS\_DnsServerTrustPoint** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DnsServerTrustPoint** class has these methods.



| Method                                          | Description                                                                       |
|:------------------------------------------------|:----------------------------------------------------------------------------------|
| [**Get**](get-ps-dnsservertrustpoint.md)       | Retrieves Trust points on the server<br/>                                   |
| [**Update**](update-ps-dnsservertrustpoint.md) | Initiates active refresh of all trust points in the trust anchor zone.<br/> |



 

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[DnsServerPSProvider Provider](dns-server-classes.md)
</dt> </dl>

 

 





