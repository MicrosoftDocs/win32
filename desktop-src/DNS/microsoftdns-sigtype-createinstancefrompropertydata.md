---
title: CreateInstanceFromPropertyData method of the MicrosoftDNS_SIGType class
description: The CreateInstanceFromPropertyData method instantiates a Signature (SIG) Resource Record.
ms.assetid: 8e83e56f-d2b3-4b71-be70-7d2640d49845
keywords:
- CreateInstanceFromPropertyData method DNS
- CreateInstanceFromPropertyData method DNS , MicrosoftDNS_SIGType class
- MicrosoftDNS_SIGType class DNS , CreateInstanceFromPropertyData method
topic_type:
- apiref
api_name:
- MicrosoftDNS_SIGType.CreateInstanceFromPropertyData
api_location:
- Root\MicrosoftDNS
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# CreateInstanceFromPropertyData method of the MicrosoftDNS\_SIGType class

The **CreateInstanceFromPropertyData** method instantiates a Signature (SIG) Resource Record.

## Syntax


```mof
void CreateInstanceFromPropertyData(
  [in]           string               DnsServerName,
  [in]           string               ContainerName,
  [in]           string               OwnerName,
  [in, optional] uint32               RecordClass = 1,
  [in, optional] uint32               TTL,
  [in]           uint16               TypeCovered,
  [in]           uint16               Algorithm,
  [in]           uint16               Labels,
  [in]           uint32               OriginalTTL,
  [in]           uint32               SignatureExpiration,
  [in]           uint32               SignatureInception,
  [in]           uint16               KeyTag,
  [in]           string               SignerName,
  [in]           string               Signature,
  [out, ref]     MicrosoftDNS_SIGType &RR
);
```



## Parameters

<dl> <dt>

*DnsServerName* \[in\]
</dt> <dd>

FQDN or IP address of the DNS Server that contains this RR.

</dd> <dt>

*ContainerName* \[in\]
</dt> <dd>

Name of the Container for the Zone, Cache, or RootHints instance that contains this RR.

</dd> <dt>

*OwnerName* \[in\]
</dt> <dd>

Owner name for the RR.

</dd> <dt>

*RecordClass* \[in, optional\]
</dt> <dd>

Class of the RR. Default value is 1. The following values are valid.



| Value                                                                                                | Meaning                  |
|------------------------------------------------------------------------------------------------------|--------------------------|
| <span id="1"></span><dl> <dt>**1**</dt> </dl> | IN (Internet)<br/> |
| <span id="2"></span><dl> <dt>**2**</dt> </dl> | CS (CSNET)<br/>    |
| <span id="3"></span><dl> <dt>**3**</dt> </dl> | CH (CHAOS)<br/>    |
| <span id="4"></span><dl> <dt>**4**</dt> </dl> | HS (Hesiod)<br/>   |



 

</dd> <dt>

*TTL* \[in, optional\]
</dt> <dd>

Time, in seconds, that the RR can be cached by a DNS resolver.

</dd> <dt>

*TypeCovered* \[in\]
</dt> <dd>

Type of RR covered by this SIG.

</dd> <dt>

*Algorithm* \[in\]
</dt> <dd>

Algorithm used with the key specified in the resource record. The assigned values are shown in the following table.



| Value                                                                                                | Meaning                                |
|------------------------------------------------------------------------------------------------------|----------------------------------------|
| <span id="1"></span><dl> <dt>**1**</dt> </dl> | RSA/MD5 (RFC 2537)<br/>          |
| <span id="2"></span><dl> <dt>**2**</dt> </dl> | Diffie-Hellman (RFC 2539)<br/>   |
| <span id="3"></span><dl> <dt>**3**</dt> </dl> | DSA (RFC 2536)<br/>              |
| <span id="4"></span><dl> <dt>**4**</dt> </dl> | Elliptic curve cryptography<br/> |



 

</dd> <dt>

*Labels* \[in\]
</dt> <dd>

Unsigned count of labels in the original SIG RR owner name. The count does not include the NULL label for the root, nor any initial wildcards.

</dd> <dt>

*OriginalTTL* \[in\]
</dt> <dd>

TTL of the RR set signed by the SIG.

</dd> <dt>

*SignatureExpiration* \[in\]
</dt> <dd>

Signature expiration date, expressed in seconds since the beginning of January 1, 1970, Greenwich Mean Time (GMT), excluding leap seconds.

</dd> <dt>

*SignatureInception* \[in\]
</dt> <dd>

Date and time at which the Signature becomes valid, expressed in seconds since the beginning of January 1, 1970, Greenwich Mean Time (GMT), excluding leap seconds.

</dd> <dt>

*KeyTag* \[in\]
</dt> <dd>

Method used to choose a key that verifies an SIG. See RFC 2535, Appendix C for the method used to calculate a KeyTag.

</dd> <dt>

*SignerName* \[in\]
</dt> <dd>

Domain name of the signer that generated the SIG RR.

</dd> <dt>

*Signature* \[in\]
</dt> <dd>

Signature, represented in base 64, formatted as defined in RFC 2535, Appendix A.

</dd> <dt>

*RR* \[out, ref\]
</dt> <dd>

Reference to the new object.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| Namespace<br/>                | Root\\MicrosoftDNS<br/>                                                          |
| MOF<br/>                      | <dl> <dt>Dnsprov.mof</dt> </dl> |



## See also

<dl> <dt>

[**MicrosoftDNS\_SIGType**](microsoftdns-sigtype.md)
</dt> <dt>

[**Modify Method of the MicrosoftDNS\_SIGType Class**](microsoftdns-sigtype-modify.md)
</dt> <dt>

[**MicrosoftDNS\_ResourceRecord**](microsoftdns-resourcerecord.md)
</dt> </dl>

 

 





