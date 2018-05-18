---
title: PS\_DnsServerDnsSecZoneSetting class
description: DNS Server DnsSec Zone Task Definition.
audience: developer
ms.assetid: '9aa64bb5-00f5-4374-af74-e6f0abf23551'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["PS_DnsServerDnsSecZoneSetting class", "PS_DnsServerDnsSecZoneSetting class, described"]
topic_type:
- apiref
api_name:
- PS_DnsServerDnsSecZoneSetting
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
---

# PS\_DnsServerDnsSecZoneSetting class

DNS Server DnsSec Zone Task Definition.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class PS_DnsServerDnsSecZoneSetting
{
};
```

## Members

The **PS\_DnsServerDnsSecZoneSetting** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DnsServerDnsSecZoneSetting** class has these methods.



| Method                                                                             | Description                                                                        |
|:-----------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|
| [**Get**](get-ps-dnsserverdnsseczonesetting.md)                                   | Returns DNSSEC settings for the input zone.<br/>                             |
| [**GetBySigningMetadata**](getbysigningmetadata-ps-dnsserverdnsseczonesetting.md) | Returns DNSSEC settings for the input zone.<br/>                             |
| [**Set**](set-ps-dnsserverdnsseczonesetting.md)                                   | Specifies the NSEC/NSEC3 and other advanced DNSSEC settings for a zone.<br/> |
| [**SetBySigningMetadata**](setbysigningmetadata-ps-dnsserverdnsseczonesetting.md) | Sets DNSSEC settings for the input zone.<br/>                                |
| [**Test**](test-ps-dnsserverdnsseczonesetting.md)                                 | Validates if the DNSSEC settings configured on the zone are valid.<br/>      |



 

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

 

 





