---
title: Modify method of the MicrosoftDNS_MXType class
description: The Modify method updates a Mail Exchanger (MR) Resource Record.
ms.assetid: 40267ac9-0392-4e08-a5d2-145ee9639c39
keywords:
- Modify method DNS
- Modify method DNS , MicrosoftDNS_MXType class
- MicrosoftDNS_MXType class DNS , Modify method
topic_type:
- apiref
api_name:
- MicrosoftDNS_MXType.Modify
api_location:
- Root\MicrosoftDNS
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Modify method of the MicrosoftDNS\_MXType class

The **Modify** method updates a Mail Exchanger (MR) Resource Record.

## Syntax


```mof
void Modify(
  [in, optional] uint32              TTL,
  [in, optional] uint16              Preference,
  [in, optional] string              MailExchange,
  [out, ref]     MicrosoftDNS_MXType &RR
);
```



## Parameters

<dl> <dt>

*TTL* \[in, optional\]
</dt> <dd>

Time, in seconds, that the RR can be cached by a DNS resolver.

</dd> <dt>

*Preference* \[in, optional\]
</dt> <dd>

Preference given to this RR among others at the same owner. Lower values are preferred.

</dd> <dt>

*MailExchange* \[in, optional\]
</dt> <dd>

FQDN specifying a host willing to act as a mail exchange for the owner name.

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

[**MicrosoftDNS\_MXType**](microsoftdns-mxtype.md)
</dt> <dt>

[**CreateInstanceFromPropertyData Method of the MicrosoftDNS\_MXType Class**](microsoftdns-mxtype-createinstancefrompropertydata.md)
</dt> <dt>

[**MicrosoftDNS\_ResourceRecord**](microsoftdns-resourcerecord.md)
</dt> </dl>

 

 





