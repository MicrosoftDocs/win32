---
title: Modify method of the MicrosoftDNS_KEYType class
description: The Modify method updates a KEY Resource Record.
ms.assetid: 0ea1e0e5-ccd1-4800-b0c3-27795c36250c
keywords:
- Modify method DNS
- Modify method DNS , MicrosoftDNS_KEYType class
- MicrosoftDNS_KEYType class DNS , Modify method
topic_type:
- apiref
api_name:
- MicrosoftDNS_KEYType.Modify
api_location:
- Root\MicrosoftDNS
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Modify method of the MicrosoftDNS\_KEYType class

The **Modify** method updates a KEY Resource Record.

## Syntax


```mof
void Modify(
  [in, optional] uint32               TTL,
  [in, optional] uint16               Flags,
  [in, optional] uint16               Protocol,
  [in, optional] uint16               Algorithm,
  [in, optional] string               PublicKey,
  [out, ref]     MicrosoftDNS_KEYType &RR
);
```



## Parameters

<dl> <dt>

*TTL* \[in, optional\]
</dt> <dd>

Time, in seconds, that the RR can be cached by a DNS resolver.

</dd> <dt>

*Flags* \[in, optional\]
</dt> <dd>

Flags used to specify mapping, as described in IETF RFC 2535.

</dd> <dt>

*Protocol* \[in, optional\]
</dt> <dd>

Protocol for which the key specified in the RR can be used. The assigned values are shown in the following table.



| Value                                                                                                    | Meaning                  |
|----------------------------------------------------------------------------------------------------------|--------------------------|
| <span id="1"></span><dl> <dt>**1**</dt> </dl>     | TLS<br/>           |
| <span id="2"></span><dl> <dt>**2**</dt> </dl>     | E-Mail<br/>        |
| <span id="3"></span><dl> <dt>**3**</dt> </dl>     | dnssec<br/>        |
| <span id="4"></span><dl> <dt>**4**</dt> </dl>     | IPsec<br/>         |
| <span id="255"></span><dl> <dt>**255**</dt> </dl> | All protocols<br/> |



 

</dd> <dt>

*Algorithm* \[in, optional\]
</dt> <dd>

Algorithm used with the key specified in the resource record. The assigned values are shown in the following table.



| Value                                                                                                | Meaning                                |
|------------------------------------------------------------------------------------------------------|----------------------------------------|
| <span id="1"></span><dl> <dt>**1**</dt> </dl> | RSA/MD5 (RFC 2537)<br/>          |
| <span id="2"></span><dl> <dt>**2**</dt> </dl> | Diffie-Hellman (RFC 2539)<br/>   |
| <span id="3"></span><dl> <dt>**3**</dt> </dl> | DSA (RFC 2536)<br/>              |
| <span id="4"></span><dl> <dt>**4**</dt> </dl> | Elliptic curve cryptography<br/> |



 

</dd> <dt>

*PublicKey* \[in, optional\]
</dt> <dd>

Public key, represented in base 64 as described in Appendix A of RFC 2535.

</dd> <dt>

*RR* \[out, ref\]
</dt> <dd>

Reference to the new object.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

Any parameter not specified is left unchanged in the modified record.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| Namespace<br/>                | Root\\MicrosoftDNS<br/>                                                          |
| MOF<br/>                      | <dl> <dt>Dnsprov.mof</dt> </dl> |



## See also

<dl> <dt>

[**MicrosoftDNS\_KEYType**](microsoftdns-keytype.md)
</dt> <dt>

[**CreateInstanceFromPropertyData Method of the MicrosoftDNS\_KEYType Class**](microsoftdns-keytype-createinstancefrompropertydata.md)
</dt> <dt>

[**MicrosoftDNS\_ResourceRecord**](microsoftdns-resourcerecord.md)
</dt> </dl>

 

 





