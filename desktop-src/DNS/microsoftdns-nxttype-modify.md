---
title: Modify method of the MicrosoftDNS_NXTType class
description: The Modify method updates a Next (NXT) Resource Record.
ms.assetid: 5a21b843-0761-4022-b00a-9dbcd6814454
keywords:
- Modify method DNS
- Modify method DNS , MicrosoftDNS_NXTType class
- MicrosoftDNS_NXTType class DNS , Modify method
topic_type:
- apiref
api_name:
- MicrosoftDNS_NXTType.Modify
api_location:
- Root\MicrosoftDNS
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Modify method of the MicrosoftDNS\_NXTType class

The **Modify** method updates a Next (NXT) Resource Record.

## Syntax


```mof
void Modify(
  [in, optional] uint32               TTL,
  [in]           string               NextDomainName,
  [in]           string               Types,
  [out, ref]     MicrosoftDNS_NXTType &RR
);
```



## Parameters

<dl> <dt>

*TTL* \[in, optional\]
</dt> <dd>

Time, in seconds, that the RR can be cached by a DNS resolver.

</dd> <dt>

*NextDomainName* \[in\]
</dt> <dd>

Next domain name.

</dd> <dt>

*Types* \[in\]
</dt> <dd>

Space-separated list of the RR-type mnemonics for the owner name of the NXT Resource Record.

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

[**MicrosoftDNS\_NXTType**](microsoftdns-nxttype.md)
</dt> <dt>

[**CreateInstanceFromPropertyData Method of the MicrosoftDNS\_NXTType Class**](microsoftdns-nxttype-createinstancefrompropertydata.md)
</dt> <dt>

[**MicrosoftDNS\_ResourceRecord**](microsoftdns-resourcerecord.md)
</dt> </dl>

 

 





