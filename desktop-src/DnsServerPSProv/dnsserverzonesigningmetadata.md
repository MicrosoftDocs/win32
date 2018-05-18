---
title: DnsServerZoneSigningMetadata class
description: Represents a zone signing metadata object on a DNS server.
audience: developer
ms.assetid: '93103ca4-2c61-4a76-b544-a750a1bfa1e9'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DnsServerZoneSigningMetadata class", "DnsServerZoneSigningMetadata class, described"]
topic_type:
- apiref
api_name:
- DnsServerZoneSigningMetadata
- DnsServerZoneSigningMetadata.DnsSecZoneSetting
- DnsServerZoneSigningMetadata.KeyExtendedInformation
- DnsServerZoneSigningMetadata.DnsSecResourceRecords
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
---

# DnsServerZoneSigningMetadata class

Represents a zone signing metadata object on a DNS server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerZoneSigningMetadata
{
  DnsServerDnsSecZoneSetting             DnsSecZoneSetting;
  DnsServerSigningKeyExtendedInformation KeyExtendedInformation[];
  DnsServerResourceRecord                DnsSecResourceRecords[];
};
```

## Members

The **DnsServerZoneSigningMetadata** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerZoneSigningMetadata** class has these properties.

<dl> <dt>

**DnsSecResourceRecords**
</dt> <dd> <dl> <dt>

Data type: **DnsServerResourceRecord** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerResourceRecord**](dnsserverresourcerecord.md)")
</dt> </dl>

An array that contains the DNSKEY and the RRSIG resource records.

</dd> <dt>

**DnsSecZoneSetting**
</dt> <dd> <dl> <dt>

Data type: **DnsServerDnsSecZoneSetting**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerDnsSecZoneSetting**](dnsserverdnsseczonesetting.md)")
</dt> </dl>

The Domain Name System Security Extensions (DNSSEC) zone setting.

</dd> <dt>

**KeyExtendedInformation**
</dt> <dd> <dl> <dt>

Data type: **DnsServerSigningKeyExtendedInformation** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerSigningKeyExtendedInformation**](dnsserversigningkeyextendedinformation.md)")
</dt> </dl>

An array that contains the extended information for the signing key of the setting.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[DnsServerPSProvider Provider](dns-server-classes.md)
</dt> </dl>

 

 





