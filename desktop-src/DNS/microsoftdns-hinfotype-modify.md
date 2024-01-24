---
title: Modify method of the MicrosoftDNS_HINFOType class
description: The Modify method updates a Host Information (HINFO) Resource Record.
ms.assetid: 8f8148f3-804f-4f99-8e79-606cd3cea660
keywords:
- Modify method DNS
- Modify method DNS , MicrosoftDNS_HINFOType class
- MicrosoftDNS_HINFOType class DNS , Modify method
topic_type:
- apiref
api_name:
- MicrosoftDNS_HINFOType.Modify
api_location:
- Root\MicrosoftDNS
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Modify method of the MicrosoftDNS\_HINFOType class

The **Modify** method updates a Host Information (HINFO) Resource Record.

## Syntax


```mof
void Modify(
  [in, optional] uint32                 TTL,
  [in, optional] string                 CPU,
  [in, optional] string                 OS,
  [out, ref]     MicrosoftDNS_HINFOType &RR
);
```



## Parameters

<dl> <dt>

*TTL* \[in, optional\]
</dt> <dd>

Time, in seconds, that the RR can be cached by a DNS resolver.

</dd> <dt>

*CPU* \[in, optional\]
</dt> <dd>

CPU type of the record owner.

</dd> <dt>

*OS* \[in, optional\]
</dt> <dd>

Operating system of the record owner.

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

[**MicrosoftDNS\_HINFOType**](microsoftdns-hinfotype.md)
</dt> <dt>

[**CreateInstanceFromPropertyData Method of the MicrosoftDNS\_HINFOType Class**](microsoftdns-hinfotype-createinstancefrompropertydata.md)
</dt> <dt>

[**MicrosoftDNS\_ResourceRecord**](microsoftdns-resourcerecord.md)
</dt> </dl>

 

 





