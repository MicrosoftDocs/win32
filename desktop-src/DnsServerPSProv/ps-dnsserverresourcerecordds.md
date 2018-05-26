---
title: PS\_DnsServerResourceRecordDS class
description: Represents a Delegation Signer (DS) resource record on a Domain Name System (DNS) server.
audience: developer
ms.assetid: 8b1dd534-5bd3-4e93-9cf3-92d8851177ed
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DnsServerResourceRecordDS class
- PS_DnsServerResourceRecordDS class, described
topic_type:
- apiref
api_name:
- PS_DnsServerResourceRecordDS
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PS\_DnsServerResourceRecordDS class

Represents a Delegation Signer (DS) resource record on a Domain Name System (DNS) server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class PS_DnsServerResourceRecordDS
{
};
```

## Members

The **PS\_DnsServerResourceRecordDS** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DnsServerResourceRecordDS** class has these methods.



| Method                                                | Description                                                             |
|:------------------------------------------------------|:------------------------------------------------------------------------|
| [**Add**](add-ps-dnsserverresourcerecordds.md)       | Adds a DS resource record to the input zone of a DNS server.<br/> |
| [**Import**](import-ps-dnsserverresourcerecordds.md) | Imports a DS resource record to the DNS server.<br/>              |



 

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

[DnsServerPSProvider Provider Classes](dns-server-classes.md)
</dt> </dl>

 

 





