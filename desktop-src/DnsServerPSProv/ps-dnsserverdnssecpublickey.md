---
title: PS\_DnsServerDnsSecPublicKey class
description: Describes the public keys of DNSSEC signed zones.
audience: developer
ms.assetid: 'e1d10eb9-0e41-4a5e-92ec-f8589ffeed2e'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["PS_DnsServerDnsSecPublicKey class", "PS_DnsServerDnsSecPublicKey class, described"]
topic_type:
- apiref
api_name:
- PS_DnsServerDnsSecPublicKey
api_location:
- DNSServerPSProvider.dll
api_type:
- DllExport
---

# PS\_DnsServerDnsSecPublicKey class

Describes the public keys of DNSSEC signed zones.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class PS_DnsServerDnsSecPublicKey
{
};
```

## Members

The **PS\_DnsServerDnsSecPublicKey** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DnsServerDnsSecPublicKey** class has these methods.



| Method                                                               | Description                                                          |
|:---------------------------------------------------------------------|:---------------------------------------------------------------------|
| [**ExportByDnsKey**](exportbydnskey-ps-dnsserverdnssecpublickey.md) | Exports DS or DNSKEY information of a DNSSEC signed zone.<br/> |
| [**ExportByDsKey**](exportbydskey-ps-dnsserverdnssecpublickey.md)   | Exports DS or DNSKEY information of a DNSSEC signed zone.<br/> |



 

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DNSServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[DnsServerPSProvider Provider](dns-server-classes.md)
</dt> </dl>

 

 





