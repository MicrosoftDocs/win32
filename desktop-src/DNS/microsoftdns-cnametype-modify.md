---
title: Modify method of the MicrosoftDNS_CNAMEType class
description: The Modify method updates a Canonical Name (CNAME) Resource Record.
ms.assetid: 7e550026-d901-44a0-86ac-520682232ccb
keywords:
- Modify method DNS
- Modify method DNS , MicrosoftDNS_CNAMEType class
- MicrosoftDNS_CNAMEType class DNS , Modify method
topic_type:
- apiref
api_name:
- MicrosoftDNS_CNAMEType.Modify
api_location:
- Root\MicrosoftDNS
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Modify method of the MicrosoftDNS\_CNAMEType class

The **Modify** method updates a Canonical Name (CNAME) Resource Record.

## Syntax


```mof
void Modify(
  [in, optional] uint32                 TTL,
  [in, optional] string                 PrimaryName,
  [out, ref]     MicrosoftDNS_CNAMEType &RR
);
```



## Parameters

<dl> <dt>

*TTL* \[in, optional\]
</dt> <dd>

Time, in seconds, that the RR can be cached by a DNS resolver.

</dd> <dt>

*PrimaryName* \[in, optional\]
</dt> <dd>

String representing the primary name for the CNAME record.

</dd> <dt>

*RR* \[out, ref\]
</dt> <dd>

Reference to the modified object.

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

[**MicrosoftDNS\_CNAMEType**](microsoftdns-cnametype.md)
</dt> <dt>

[**CreateInstanceFromPropertyData Method of the MicrosoftDNS\_CNAMEType Class**](microsoftdns-cnametype-createinstancefrompropertydata.md)
</dt> <dt>

[**MicrosoftDNS\_ResourceRecord**](microsoftdns-resourcerecord.md)
</dt> </dl>

 

 





