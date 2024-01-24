---
title: Modify method of the MicrosoftDNS_MINFOType class
description: The Modify method updates a Mail Information (MINFO) Resource Record.
ms.assetid: fbec0cd3-f735-44c6-b010-80f35cc33d98
keywords:
- Modify method DNS
- Modify method DNS , MicrosoftDNS_MINFOType class
- MicrosoftDNS_MINFOType class DNS , Modify method
topic_type:
- apiref
api_name:
- MicrosoftDNS_MINFOType.Modify
api_location:
- Root\MicrosoftDNS
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Modify method of the MicrosoftDNS\_MINFOType class

The **Modify** method updates a Mail Information (MINFO) Resource Record.

## Syntax


```mof
void Modify(
  [in, optional] uint32                 TTL,
  [in, optional] string                 ResponsibleMailbox,
  [in, optional] string                 ErrorMailbox,
  [out, ref]     MicrosoftDNS_MINFOType &RR
);
```



## Parameters

<dl> <dt>

*TTL* \[in, optional\]
</dt> <dd>

Time, in seconds, that the RR can be cached by a DNS resolver.

</dd> <dt>

*ResponsibleMailbox* \[in, optional\]
</dt> <dd>

FQDN specifying a mailbox responsible for the mailing list or mailbox specified in the record's Owner Name.

</dd> <dt>

*ErrorMailbox* \[in, optional\]
</dt> <dd>

FQDN specifying a mailbox to receive error messages related to either the mailing list, or to the mailbox specified by the owner name of the MINFO record.

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

[**MicrosoftDNS\_MINFOType**](microsoftdns-minfotype.md)
</dt> <dt>

[**CreateInstanceFromPropertyData Method of the MicrosoftDNS\_MINFOType Class**](microsoftdns-minfotype-createinstancefrompropertydata.md)
</dt> <dt>

[**MicrosoftDNS\_ResourceRecord**](microsoftdns-resourcerecord.md)
</dt> </dl>

 

 





