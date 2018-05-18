---
title: PS\_DnsServerResourceRecordDnsKey class
description: DNS Server Resource Record DNSKEY Tasks.
audience: developer
ms.assetid: 'dfec3ba3-1f58-475d-92c4-217a9c0f9cad'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["PS_DnsServerResourceRecordDnsKey class", "PS_DnsServerResourceRecordDnsKey class, described"]
topic_type:
- apiref
api_name:
- PS_DnsServerResourceRecordDnsKey
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
---

# PS\_DnsServerResourceRecordDnsKey class

DNS Server Resource Record DNSKEY Tasks

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class PS_DnsServerResourceRecordDnsKey
{
};
```

## Members

The **PS\_DnsServerResourceRecordDnsKey** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DnsServerResourceRecordDnsKey** class has these methods.



| Method                                              | Description                                    |
|:----------------------------------------------------|:-----------------------------------------------|
| [**Add**](add-ps-dnsserverresourcerecorddnskey.md) | Adds a DNSKEY record to input zone.<br/> |



 

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

 

 





