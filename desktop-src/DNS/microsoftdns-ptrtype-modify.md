---
title: Modify method of the MicrosoftDNS_PTRType class
description: The Modify method updates a Pointer (PTR) Resource Record.
ms.assetid: 801a6bc9-e384-4912-a73a-6b04a1655002
keywords:
- Modify method DNS
- Modify method DNS , MicrosoftDNS_PTRType class
- MicrosoftDNS_PTRType class DNS , Modify method
topic_type:
- apiref
api_name:
- MicrosoftDNS_PTRType.Modify
api_location:
- Root\MicrosoftDNS
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Modify method of the MicrosoftDNS\_PTRType class

The **Modify** method updates a Pointer (PTR) Resource Record.

## Syntax


```mof
void Modify(
  [in, optional] uint32               TTL,
  [in, optional] string               PTRDomainName,
  [out, ref]     MicrosoftDNS_PTRType &RR
);
```



## Parameters

<dl> <dt>

*TTL* \[in, optional\]
</dt> <dd>

Time, in seconds, that the RR can be cached by a DNS resolver.

</dd> <dt>

*PTRDomainName* \[in, optional\]
</dt> <dd>

Domain name address of the PTR record.

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

[**MicrosoftDNS\_PTRType**](microsoftdns-ptrtype.md)
</dt> <dt>

[**CreateInstanceFromPropertyData Method of the MicrosoftDNS\_PTRType Class**](microsoftdns-ptrtype-createinstancefrompropertydata.md)
</dt> <dt>

[**MicrosoftDNS\_ResourceRecord**](microsoftdns-resourcerecord.md)
</dt> </dl>

 

 





