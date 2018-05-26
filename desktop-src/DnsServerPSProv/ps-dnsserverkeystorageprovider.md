---
title: PS\_DnsServerKeyStorageProvider class
description: DNS Server Key Storage Provider Task Definition.
audience: developer
ms.assetid: 05d5b845-268b-46a3-bdec-1539d0d712c8
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DnsServerKeyStorageProvider class
- PS_DnsServerKeyStorageProvider class, described
topic_type:
- apiref
api_name:
- PS_DnsServerKeyStorageProvider
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PS\_DnsServerKeyStorageProvider class

DNS Server Key Storage Provider Task Definition.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class PS_DnsServerKeyStorageProvider
{
};
```

## Members

The **PS\_DnsServerKeyStorageProvider** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DnsServerKeyStorageProvider** class has these methods.



| Method                                              | Description                                                                       |
|:----------------------------------------------------|:----------------------------------------------------------------------------------|
| [**Show**](show-ps-dnsserverkeystorageprovider.md) | Returns the list of key storage providers available on the DNS server.<br/> |



 

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

 

 





