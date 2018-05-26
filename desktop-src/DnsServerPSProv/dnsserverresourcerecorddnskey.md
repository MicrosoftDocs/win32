---
title: DnsServerResourceRecordDnsKey class
description: DNS Server Resource Record Data DnsKey.
audience: developer
ms.assetid: dfec3ba3-1f58-475d-92c4-217a9c0f9cad
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerResourceRecordDnsKey class
- DnsServerResourceRecordDnsKey class, described
topic_type:
- apiref
api_name:
- DnsServerResourceRecordDnsKey
- DnsServerResourceRecordDnsKey.KeyTag
- DnsServerResourceRecordDnsKey.SecureEntryPoint
- DnsServerResourceRecordDnsKey.ZoneKey
- DnsServerResourceRecordDnsKey.KeyProtocol
- DnsServerResourceRecordDnsKey.CryptoAlgorithm
- DnsServerResourceRecordDnsKey.Base64Data
- DnsServerResourceRecordDnsKey.Revoked
- DnsServerResourceRecordDnsKey.KeyFlags
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DnsServerResourceRecordDnsKey class

DNS Server Resource Record Data DnsKey.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerResourceRecordDnsKey : DnsServerResourceRecordData
{
  uint16  KeyTag;
  boolean SecureEntryPoint;
  boolean ZoneKey;
  string  KeyProtocol;
  string  CryptoAlgorithm;
  string  Base64Data;
  boolean Revoked;
  uint16  KeyFlags;
};
```

## Members

The **DnsServerResourceRecordDnsKey** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerResourceRecordDnsKey** class has these properties.

<dl> <dt>

**Base64Data**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Holds the public key material. The format depends on the algorithm of the key being stored.

</dd> <dt>

**CryptoAlgorithm**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Identifies the public key's cryptographic algorithm and determines the format of Base64Data property.

The possible values are.

<dt>

<span id="RsaSha1"></span><span id="rsasha1"></span><span id="RSASHA1"></span>

**RsaSha1** ("RsaSha1")


</dt> <dd></dd> <dt>

<span id="RsaSha1NSec3"></span><span id="rsasha1nsec3"></span><span id="RSASHA1NSEC3"></span>

**RsaSha1NSec3** ("RsaSha1NSec3")


</dt> <dd></dd> <dt>

<span id="RsaSha256"></span><span id="rsasha256"></span><span id="RSASHA256"></span>

**RsaSha256** ("RsaSha256")


</dt> <dd></dd> <dt>

<span id="RsaSha512"></span><span id="rsasha512"></span><span id="RSASHA512"></span>

**RsaSha512** ("RsaSha512")


</dt> <dd></dd> <dt>

<span id="ECDsaP256Sha256"></span><span id="ecdsap256sha256"></span><span id="ECDSAP256SHA256"></span>

**ECDsaP256Sha256** ("ECDsaP256Sha256")


</dt> <dd></dd> <dt>

<span id="ECDsaP384Sha384"></span><span id="ecdsap384sha384"></span><span id="ECDSAP384SHA384"></span>

**ECDsaP384Sha384** ("ECDsaP384Sha384")


</dt> <dd></dd> </dl>

</dd> <dt>

**KeyFlags**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Key flag specifies properties of DnsKey resource record.

</dd> <dt>

**KeyProtocol**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Always set to DnsSec.

The possible values are.

<dt>

<span id="DnsSec"></span><span id="dnssec"></span><span id="DNSSEC"></span>

**DnsSec** ("DNSSEC")


</dt> <dd></dd> </dl>

</dd> <dt>

**KeyTag**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The Key Tag field lists the key tag of the DnsKey Resource Record.

</dd> <dt>

**Revoked**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Is set to true if the DnsKey is revoked.

</dd> <dt>

**SecureEntryPoint**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Set to true if the DnsKey is a secure entry point to a signed zone. Set to false otherwise.

</dd> <dt>

**ZoneKey**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Set to true if the DnsKey is a zone key. Set to false otherwise.

</dd> </dl>

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

[**DnsServerResourceRecordData**](dnsserverresourcerecorddata.md)
</dt> <dt>

[DnsServerPSProvider Provider](dns-server-classes.md)
</dt> </dl>

 

 





