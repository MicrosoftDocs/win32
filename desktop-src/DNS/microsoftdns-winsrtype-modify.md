---
title: Modify method of the MicrosoftDNS_WINSRType class
description: The Modify method updates a WINS Reverse Look up (WINSR) Resource Record.
ms.assetid: 28be0045-5b0d-4434-a2a9-b56191f1e213
keywords:
- Modify method DNS
- Modify method DNS , MicrosoftDNS_WINSRType class
- MicrosoftDNS_WINSRType class DNS , Modify method
topic_type:
- apiref
api_name:
- MicrosoftDNS_WINSRType.Modify
api_location:
- Root\MicrosoftDNS
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Modify method of the MicrosoftDNS\_WINSRType class

The **Modify** method updates a WINS Reverse Look up (WINSR) Resource Record.

## Syntax


```mof
void Modify(
  [in, optional] uint32                 TTL,
  [in, optional] uint32                 MappingFlag,
  [in, optional] uint32                 LookupTimeout,
  [in, optional] uint32                 CacheTimeout,
  [in, optional] string                 ResultDomain,
  [out, ref]     MicrosoftDNS_WINSRType &RR
);
```



## Parameters

<dl> <dt>

*TTL* \[in, optional\]
</dt> <dd>

Time, in seconds, that the RR can be cached by a DNS resolver.

</dd> <dt>

*MappingFlag* \[in, optional\]
</dt> <dd>

WINSR mapping flag that specifies whether the record must be included into the zone replication. It may have only two values: 0x80000000 and 0x00010000 corresponding to the replication and no-replication (local record) flags, respectively.

</dd> <dt>

*LookupTimeout* \[in, optional\]
</dt> <dd>

Time out, in seconds, for a DNS Server using WINS Reverse Look up.

</dd> <dt>

*CacheTimeout* \[in, optional\]
</dt> <dd>

Time, in seconds, a DNS Server using WINS Look up may cache the WINS server's response.

</dd> <dt>

*ResultDomain* \[in, optional\]
</dt> <dd>

Domain name to append to returned NetBIOS names.

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

[**MicrosoftDNS\_WINSRType**](microsoftdns-winsrtype.md)
</dt> <dt>

[**CreateInstanceFromPropertyData Method of the MicrosoftDNS\_WINSRType Class**](microsoftdns-winsrtype-createinstancefrompropertydata.md)
</dt> <dt>

[**MicrosoftDNS\_ResourceRecord**](microsoftdns-resourcerecord.md)
</dt> </dl>

 

 





