---
title: DnsServerResourceRecordRRSig class
description: DNS Server Resource Record Data RRSIG.
audience: developer
ms.assetid: 56c322e5-7ad0-4b2a-bb50-90f5d6ea3b1e
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerResourceRecordRRSig class
- DnsServerResourceRecordRRSig class, described
topic_type:
- apiref
api_name:
- DnsServerResourceRecordRRSig
- DnsServerResourceRecordRRSig.TypeCovered
- DnsServerResourceRecordRRSig.CryptoAlgorithm
- DnsServerResourceRecordRRSig.LabelCount
- DnsServerResourceRecordRRSig.OriginalTtl
- DnsServerResourceRecordRRSig.SignatureExpiration
- DnsServerResourceRecordRRSig.SignatureInception
- DnsServerResourceRecordRRSig.KeyTag
- DnsServerResourceRecordRRSig.NameSigner
- DnsServerResourceRecordRRSig.Signature
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DnsServerResourceRecordRRSig class

DNS Server Resource Record Data RRSIG.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerResourceRecordRRSig : DnsServerResourceRecordData
{
  String   TypeCovered;
  string   CryptoAlgorithm;
  uint8    LabelCount;
  datetime OriginalTtl;
  datetime SignatureExpiration;
  datetime SignatureInception;
  uint16   KeyTag;
  string   NameSigner;
  string   Signature;
};
```

## Members

The **DnsServerResourceRecordRRSig** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerResourceRecordRRSig** class has these properties.

<dl> <dt>

**CryptoAlgorithm**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Crypto algorithm using which the key was generated.

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

**KeyTag**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The key tag of the associated DnsKey record.

</dd> <dt>

**LabelCount**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Number of labels in the record name associated of this record.

</dd> <dt>

**NameSigner**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The zone name which the record is part of.

</dd> <dt>

**OriginalTtl**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The original TTL value at the time of signing.

</dd> <dt>

**Signature**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

DNSSEC signature of the record set.

</dd> <dt>

**SignatureExpiration**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The signature expiration date and time.

</dd> <dt>

**SignatureInception**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The signature inception date and time.

</dd> <dt>

**TypeCovered**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The record type with which the signature is associated with this record.

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

 

 





