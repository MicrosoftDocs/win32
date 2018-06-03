---
title: PS\_DnsServerTrustAnchor class
description: DNS Server Trust Anchor Task Definition.
audience: developer
ms.assetid: 646e0b50-8322-4ec0-88b3-68e6cfb6c581
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DnsServerTrustAnchor class
- PS_DnsServerTrustAnchor class, described
topic_type:
- apiref
api_name:
- PS_DnsServerTrustAnchor
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PS\_DnsServerTrustAnchor class

DNS Server Trust Anchor Task Definition.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class PS_DnsServerTrustAnchor
{
};
```

## Members

The **PS\_DnsServerTrustAnchor** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DnsServerTrustAnchor** class has these methods.



| Method                                                                     | Description                                                                                                                                                                                                                                  |
|:---------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddByDnsKey**](addbydnskey-ps-dnsservertrustanchor.md)                 | Adds a trust anchor DNSKEY record. If there is no trust anchor zone present, the cmdlet should create one. If neither SecureEntryPoint nor ZoneSigningKey are specified, then the cmdlet creates a trust anchor with SEP bit set.<br/> |
| [**AddByDS**](addbyds-ps-dnsservertrustanchor.md)                         | Adds a trust anchor DNSKEY record. If there is no trust anchor zone present, the cmdlet should create one. If neither SecureEntryPoint nor ZoneSigningKey are specified, then the cmdlet creates a trust anchor with SEP bit set.<br/> |
| [**AddByRoot**](addbyroot-ps-dnsservertrustanchor.md)                     | Adds a trust anchor DNSKEY record.<br/>                                                                                                                                                                                                |
| [**Get**](get-ps-dnsservertrustanchor.md)                                 | Retrieves TAs on the server<br/>                                                                                                                                                                                                       |
| [**ImportByDSSet**](importbydsset-ps-dnsservertrustanchor.md)             | Imports DNS server Trust anchors from specified files<br/>                                                                                                                                                                             |
| [**ImportByKeySet**](importbykeyset-ps-dnsservertrustanchor.md)           | Imports DNS server Trust anchors from specified files<br/>                                                                                                                                                                             |
| [**RemoveByInputObject**](removebyinputobject-ps-dnsservertrustanchor.md) | Deletes the specified trust anchor.<br/>                                                                                                                                                                                               |
| [**RemoveByName**](removebyname-ps-dnsservertrustanchor.md)               | Deletes the specified trust anchor.<br/>                                                                                                                                                                                               |



 

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

 

 





