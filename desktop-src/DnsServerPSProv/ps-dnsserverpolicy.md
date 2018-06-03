---
title: PS\_DNSServerPolicy class
description: DNS server policy summary.
audience: developer
ms.assetid: f7441c92-0645-4f96-8c9a-7b60c8e2374f
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DNSServerPolicy class
- PS_DNSServerPolicy class, described
topic_type:
- apiref
api_name:
- PS_DNSServerPolicy
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PS\_DNSServerPolicy class

DNS server policy summary.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class PS_DNSServerPolicy
{
};
```

## Members

The **PS\_DNSServerPolicy** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DNSServerPolicy** class has these methods.



| Method                                        | Description                              |
|:----------------------------------------------|:-----------------------------------------|
| [**Disable**](disable-ps-dnsserverpolicy.md) | Disables a DNS Server policy.<br/> |
| [**Enable**](enable-ps-dnsserverpolicy.md)   | Enables a DNS Server policy.<br/>  |



 

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

 

 





