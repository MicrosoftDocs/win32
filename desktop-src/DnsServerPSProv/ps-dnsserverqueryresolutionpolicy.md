---
title: PS\_DnsServerQueryResolutionPolicy class
description: Describes a DNS server query resolution policy.
audience: developer
ms.assetid: 29fae9d8-ff1e-4894-81b1-406730f49a46
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DnsServerQueryResolutionPolicy class
- PS_DnsServerQueryResolutionPolicy class, described
topic_type:
- apiref
api_name:
- PS_DnsServerQueryResolutionPolicy
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PS\_DnsServerQueryResolutionPolicy class

Describes a DNS server query resolution policy.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class PS_DnsServerQueryResolutionPolicy
{
};
```

## Members

The **PS\_DnsServerQueryResolutionPolicy** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DnsServerQueryResolutionPolicy** class has these methods.



| Method                                                                         | Description                                                                  |
|:-------------------------------------------------------------------------------|:-----------------------------------------------------------------------------|
| [**AddByInputObject**](addbyinputobject-ps-dnsserverqueryresolutionpolicy.md) | Adds a query resolution policy to the DNS server by input object.<br/> |
| [**AddByServer**](addbyserver-ps-dnsserverqueryresolutionpolicy.md)           | Adds a query resolution policy to the DNS server by server.<br/>       |
| [**AddByZone**](addbyzone-ps-dnsserverqueryresolutionpolicy.md)               | Adds a query resolution policy to the DNS server by zone.<br/>         |
| [**GetByServer**](getbyserver-ps-dnsserverqueryresolutionpolicy.md)           | Enumerates the name resolution policies by server.<br/>                |
| [**GetByZone**](getbyzone-ps-dnsserverqueryresolutionpolicy.md)               | Enumerates the name resolution Policies by zone.<br/>                  |
| [**RemoveByServer**](removebyserver-ps-dnsserverqueryresolutionpolicy.md)     | Removes the name resolution policy from a DNS server by server.<br/>   |
| [**RemoveByZone**](removebyzone-ps-dnsserverqueryresolutionpolicy.md)         | Removes the name resolution policy from a DNS server by zone.<br/>     |
| [**SetByInputObject**](setbyinputobject-ps-dnsserverqueryresolutionpolicy.md) | Sets the DNS server name resolution policy by input object.<br/>       |
| [**SetByServer**](setbyserver-ps-dnsserverqueryresolutionpolicy.md)           | Sets the DNS server name resolution policy by server.<br/>             |
| [**SetByZone**](setbyzone-ps-dnsserverqueryresolutionpolicy.md)               | Sets the DNS server name resolution policy by zone.<br/>               |



 

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[DnsServerPSProvider Provider](dns-server-classes.md)
</dt> </dl>

 

 





