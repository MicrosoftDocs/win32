---
title: Modify method of the MicrosoftDNS_MGType class
description: The Modify method updates a Mail Group (MG) Resource Record.
ms.assetid: c7d42964-19fb-410d-a434-85af20754e20
keywords:
- Modify method DNS
- Modify method DNS , MicrosoftDNS_MGType class
- MicrosoftDNS_MGType class DNS , Modify method
topic_type:
- apiref
api_name:
- MicrosoftDNS_MGType.Modify
api_location:
- Root\MicrosoftDNS
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Modify method of the MicrosoftDNS\_MGType class

The **Modify** method updates a Mail Group (MG) Resource Record.

## Syntax


```mof
void Modify(
  [in, optional] uint32              TTL,
  [in, optional] string              MGMailbox,
  [out, ref]     MicrosoftDNS_MGType &RR
);
```



## Parameters

<dl> <dt>

*TTL* \[in, optional\]
</dt> <dd>

Time, in seconds, that the RR can be cached by a DNS resolver.

</dd> <dt>

*MGMailbox* \[in, optional\]
</dt> <dd>

FQDN specifying a mailbox that is a member of the mail group specified by the record's owner name.

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

[**MicrosoftDNS\_MGType**](microsoftdns-mgtype.md)
</dt> <dt>

[**CreateInstanceFromPropertyData Method of the MicrosoftDNS\_MGType Class**](microsoftdns-mgtype-createinstancefrompropertydata.md)
</dt> <dt>

[**MicrosoftDNS\_ResourceRecord**](microsoftdns-resourcerecord.md)
</dt> </dl>

 

 





