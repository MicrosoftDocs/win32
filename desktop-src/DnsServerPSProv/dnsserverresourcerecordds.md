---
title: DnsServerResourceRecordDS class
description: DNS Server Resource Record Data for DS Record Type.
audience: developer
ms.assetid: 8b1dd534-5bd3-4e93-9cf3-92d8851177ed
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerResourceRecordDS class
- DnsServerResourceRecordDS class, described
topic_type:
- apiref
api_name:
- DnsServerResourceRecordDS
- DnsServerResourceRecordDS.KeyTag
- DnsServerResourceRecordDS.CryptoAlgorithm
- DnsServerResourceRecordDS.DigestType
- DnsServerResourceRecordDS.Digest
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DnsServerResourceRecordDS class

DNS Server Resource Record Data for DS Record Type.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerResourceRecordDS : DnsServerResourceRecordData
{
  uint16 KeyTag;
  String CryptoAlgorithm;
  String DigestType;
  String Digest;
};
```

## Members

The **DnsServerResourceRecordDS** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerResourceRecordDS** class has these properties.

<dl> <dt>

**CryptoAlgorithm**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Identifies the public key's cryptographic algorithm of the DnsKey resource record referred by the current DS record.

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

**Digest**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Refers to the digest of the DnsKey resource record.

</dd> <dt>

**DigestType**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the algorithm used to construct the digest.

The possible values are.

<dt>

<span id="Sha1"></span><span id="sha1"></span><span id="SHA1"></span>

**Sha1** ("Sha1")


</dt> <dd></dd> <dt>

<span id="Sha256"></span><span id="sha256"></span><span id="SHA256"></span>

**Sha256** ("Sha256")


</dt> <dd></dd> <dt>

<span id="Sha384"></span><span id="sha384"></span><span id="SHA384"></span>

**Sha384** ("Sha384")


</dt> <dd></dd> </dl>

</dd> <dt>

**KeyTag**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The Key Tag field lists the key tag of the DnsKey Resource Record referred to by the current DS record.

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

 

 





