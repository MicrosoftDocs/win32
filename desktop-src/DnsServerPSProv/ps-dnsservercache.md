---
title: PS\_DnsServerCache class
description: Retrieves DNS server cache settings.
audience: developer
ms.assetid: cbe476ad-dfbc-4863-8808-3526a53d4540
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DnsServerCache class
- PS_DnsServerCache class, described
topic_type:
- apiref
api_name:
- PS_DnsServerCache
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PS\_DnsServerCache class

Retrieves DNS server cache settings.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class PS_DnsServerCache
{
};
```

## Members

The **PS\_DnsServerCache** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DnsServerCache** class has these methods.



| Method                                   | Description                                              |
|:-----------------------------------------|:---------------------------------------------------------|
| [**Clear**](clear-ps-dnsservercache.md) | Clears the settings of a DNS server cache.<br/>    |
| [**Get**](get-ps-dnsservercache.md)     | Retrieves the settings of a DNS server cache.<br/> |
| [**Set**](set-ps-dnsservercache.md)     | Updates the settings of a DNS server cache.<br/>   |
| [**Show**](show-ps-dnsservercache.md)   | Dumps a DNS server cache.<br/>                     |



 

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

 

 





