---
title: Modify method of the MicrosoftDNS_AType class
description: The Modify method updates the TTL and IP address of a host Address (A) Resource Record.
ms.assetid: fe01549d-7135-499d-a5a5-cd31ea106f53
keywords:
- Modify method DNS
- Modify method DNS , MicrosoftDNS_AType class
- MicrosoftDNS_AType class DNS , Modify method
topic_type:
- apiref
api_name:
- MicrosoftDNS_AType.Modify
api_location:
- Root\MicrosoftDNS
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Modify method of the MicrosoftDNS\_AType class

The **Modify** method updates the TTL and IP address of a host Address (A) Resource Record.

## Syntax


```mof
void Modify(
  [in, optional] uint32             TTL,
  [in, optional] string             IPAddress,
  [out, ref]     MicrosoftDNS_AType &RR
);
```



## Parameters

<dl> <dt>

*TTL* \[in, optional\]
</dt> <dd>

Time, in seconds, that the RR can be cached by a DNS resolver.

</dd> <dt>

*IPAddress* \[in, optional\]
</dt> <dd>

String representing the IP address of the host.

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

[**MicrosoftDNS\_ResourceRecord**](microsoftdns-resourcerecord.md)
</dt> <dt>

[**CreateInstanceFromPropertyData Method of the MicrosoftDNS\_AType Class**](microsoftdns-atype-createinstancefrompropertydata.md)
</dt> </dl>

 

 





