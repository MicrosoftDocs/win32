---
title: PS\_DnsServerGlobalNameZone class
description: DNS Server Global Name Zone definition.
audience: developer
ms.assetid: c340e712-5638-4020-b126-37465e900297
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DnsServerGlobalNameZone class
- PS_DnsServerGlobalNameZone class, described
topic_type:
- apiref
api_name:
- PS_DnsServerGlobalNameZone
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PS\_DnsServerGlobalNameZone class

DNS Server Global Name Zone definition.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class PS_DnsServerGlobalNameZone
{
};
```

## Members

The **PS\_DnsServerGlobalNameZone** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DnsServerGlobalNameZone** class has these methods.



| Method                                        | Description                                                                                                                                          |
|:----------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Get**](get-ps-dnsserverglobalnamezone.md) | Retrieves Global Name Zone parameters<br/>                                                                                                     |
| [**Set**](set-ps-dnsserverglobalnamezone.md) | Enables or disables support for the GlobalNames zone. The GlobalNames zone supports resolution of single-label DNS names across a forest.<br/> |



 

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

 

 





