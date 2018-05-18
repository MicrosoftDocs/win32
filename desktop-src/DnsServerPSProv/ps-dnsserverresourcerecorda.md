---
title: PS\_DnsServerResourceRecordA class
description: Represents a type A resource record on a DNS server.
audience: developer
ms.assetid: '1321dbe2-bdd4-4dc8-9269-fbf005cdcb33'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["PS_DnsServerResourceRecordA class", "PS_DnsServerResourceRecordA class, described"]
topic_type:
- apiref
api_name:
- PS_DnsServerResourceRecordA
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
---

# PS\_DnsServerResourceRecordA class

Represents a type A resource record on a DNS server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class PS_DnsServerResourceRecordA
{
};
```

## Members

The **PS\_DnsServerResourceRecordA** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DnsServerResourceRecordA** class has these methods.



| Method                                         | Description                                             |
|:-----------------------------------------------|:--------------------------------------------------------|
| [**Add**](add-ps-dnsserverresourcerecorda.md) | Adds type A resource record to a DNS server.<br/> |



 

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[DnsServerPSProvider Provider](dns-server-classes.md)
</dt> </dl>

 

 





