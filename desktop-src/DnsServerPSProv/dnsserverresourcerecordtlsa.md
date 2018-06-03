---
title: DnsServerResourceRecordTLSA class
description: Represents a TLSA resource record for a DNS server database.
audience: developer
ms.assetid: aec9af86-d882-4b7d-abe5-9b864b1157e0
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerResourceRecordTLSA class
- DnsServerResourceRecordTLSA class, described
topic_type:
- apiref
api_name:
- DnsServerResourceRecordTLSA
- DnsServerResourceRecordTLSA.CertificateUsage
- DnsServerResourceRecordTLSA.Selector
- DnsServerResourceRecordTLSA.MatchingType
- DnsServerResourceRecordTLSA.CertificateAssociationData
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DnsServerResourceRecordTLSA class

Represents a TLSA resource record for a DNS server database.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerResourceRecordTLSA : DnsServerResourceRecordData
{
  string CertificateUsage;
  string Selector;
  string MatchingType;
  string CertificateAssociationData;
};
```

## Members

The **DnsServerResourceRecordTLSA** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerResourceRecordTLSA** class has these properties.

<dl> <dt>

**CertificateAssociationData**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

the certificate association data.

</dd> <dt>

**CertificateUsage**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Certificate Usage.

The possible values are.

<dt>

<span id="CAConstraint"></span><span id="caconstraint"></span><span id="CACONSTRAINT"></span>

**CAConstraint** ("CAConstraint")


</dt> <dd></dd> <dt>

<span id="ServiceCertificateConstraint"></span><span id="servicecertificateconstraint"></span><span id="SERVICECERTIFICATECONSTRAINT"></span>

**ServiceCertificateConstraint** ("ServiceCertificateConstraint")


</dt> <dd></dd> <dt>

<span id="TrustAnchorAssertion"></span><span id="trustanchorassertion"></span><span id="TRUSTANCHORASSERTION"></span>

**TrustAnchorAssertion** ("TrustAnchorAssertion")


</dt> <dd></dd> <dt>

<span id="DomainIssuedCertificate"></span><span id="domainissuedcertificate"></span><span id="DOMAINISSUEDCERTIFICATE"></span>

**DomainIssuedCertificate** ("DomainIssuedCertificate")


</dt> <dd></dd> </dl>

</dd> <dt>

**MatchingType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The matching type.

<dt>

<span id="ExactMatch"></span><span id="exactmatch"></span><span id="EXACTMATCH"></span>

**ExactMatch** ("ExactMatch")


</dt> <dd></dd> <dt>

<span id="Sha256Hash"></span><span id="sha256hash"></span><span id="SHA256HASH"></span>

**Sha256Hash** ("Sha256Hash")


</dt> <dd></dd> <dt>

<span id="Sha512Hash"></span><span id="sha512hash"></span><span id="SHA512HASH"></span>

**Sha512Hash** ("Sha512Hash")


</dt> <dd></dd> </dl>

</dd> <dt>

**Selector**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The selector.

<dt>

<span id="FullCertificate"></span><span id="fullcertificate"></span><span id="FULLCERTIFICATE"></span>

**FullCertificate** ("FullCertificate")


</dt> <dd></dd> <dt>

<span id="SubjectPublicKeyInfo"></span><span id="subjectpublickeyinfo"></span><span id="SUBJECTPUBLICKEYINFO"></span>

**SubjectPublicKeyInfo** ("SubjectPublicKeyInfo")


</dt> <dd></dd> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**DnsServerResourceRecordData**](dnsserverresourcerecorddata.md)
</dt> </dl>

 

 





