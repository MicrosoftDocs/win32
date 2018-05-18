---
title: AddByTLSA method of the PS\_DnsServerResourceRecord class
description: Adds the record to a specified zone in a DNS server.
audience: developer
ms.assetid: '12a4d092-32c1-4693-a159-6ae61170efbb'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["AddByTLSA method", "AddByTLSA method, PS_DnsServerResourceRecord class", "PS_DnsServerResourceRecord class, AddByTLSA method"]
topic_type:
- apiref
api_name:
- PS_DnsServerResourceRecord.AddByTLSA
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# AddByTLSA method of the PS\_DnsServerResourceRecord class

Adds the record to a specified zone in a DNS server.

## Syntax


```mof
uint32 AddByTLSA(
  [in]  string                  ZoneName,
  [in]  string                  ComputerName,
  [in]  boolean                 PassThru,
  [in]  string                  ZoneScope,
  [in]  string                  VirtualizationInstance,
  [in]  boolean                 TLSA,
  [in]  string                  CertificateUsage,
  [in]  string                  MatchingType,
  [in]  string                  Selector,
  [in]  string                  CertificateAssociationData,
  [in]  string                  Name,
  [in]  boolean                 AgeRecord,
  [in]  boolean                 AllowUpdateAny,
  [in]  datetime                TimeToLive,
  [out] DnsServerResourceRecord cmdletOutput
);
```



## Parameters

<dl> <dt>

*ZoneName* \[in\]
</dt> <dd>

Specifies the name of the zone.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If specified, returns the object or objects on which the operation was done.

</dd> <dt>

*ZoneScope* \[in\]
</dt> <dd>

Name of the zone scope.

</dd> <dt>

*VirtualizationInstance* \[in\]
</dt> <dd>

Unique identifier of the virtualization instance.

</dd> <dt>

*TLSA* \[in\]
</dt> <dd>

DNS Server Resource Record TLSA.

</dd> <dt>

*CertificateUsage* \[in\]
</dt> <dd>

Certificate usage

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


</dt> <dd></dd> </dl> </dd> <dt>

*MatchingType* \[in\]
</dt> <dd>

Matching Type

The possible values are.

<dt>

<span id="ExactMatch"></span><span id="exactmatch"></span><span id="EXACTMATCH"></span>

**ExactMatch** ("ExactMatch")


</dt> <dd></dd> <dt>

<span id="Sha256Hash"></span><span id="sha256hash"></span><span id="SHA256HASH"></span>

**Sha256Hash** ("Sha256Hash")


</dt> <dd></dd> <dt>

<span id="Sha512Hash"></span><span id="sha512hash"></span><span id="SHA512HASH"></span>

**Sha512Hash** ("Sha512Hash")


</dt> <dd></dd> </dl> </dd> <dt>

*Selector* \[in\]
</dt> <dd>

Selector

The possible values are.

<dt>

<span id="FullCertificate"></span><span id="fullcertificate"></span><span id="FULLCERTIFICATE"></span>

**FullCertificate** ("FullCertificate")


</dt> <dd></dd> <dt>

<span id="SubjectPublicKeyInfo"></span><span id="subjectpublickeyinfo"></span><span id="SUBJECTPUBLICKEYINFO"></span>

**SubjectPublicKeyInfo** ("SubjectPublicKeyInfo")


</dt> <dd></dd> </dl> </dd> <dt>

*CertificateAssociationData* \[in\]
</dt> <dd>

The certificate association data.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

The record name.

</dd> <dt>

*AgeRecord* \[in\]
</dt> <dd>

If specified, creates the record with current timestamp so that the record can be scavenged.

</dd> <dt>

*AllowUpdateAny* \[in\]
</dt> <dd>

Allow any authenticated user to update DNS record with same owner name

</dd> <dt>

*TimeToLive* \[in\]
</dt> <dd>

Time To Live, in seconds

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

A [**DnsServerResourceRecord**](dnsserverresourcerecord.md) object containing the following fields:

-   **HostName**
-   **RecordType**
-   **RecordClass**
-   **TimeToLive**
-   **Timestamp**
-   **RecordData**

Note that the **RecordData** field is dependent on **RecordType**.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsServerResourceRecord**](ps-dnsserverresourcerecord.md)
</dt> </dl>

 

 





