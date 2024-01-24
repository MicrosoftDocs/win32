---
title: Modify method of the MicrosoftDNS_AFSDBType class
description: The Modify method updates an Andrew File System Database Server (AFSDB) Resource Record.
ms.assetid: 9b98a3cf-cc2b-4497-921b-eaca4d13d6a1
keywords:
- Modify method DNS
- Modify method DNS , MicrosoftDNS_AFSDBType class
- MicrosoftDNS_AFSDBType class DNS , Modify method
topic_type:
- apiref
api_name:
- MicrosoftDNS_AFSDBType.Modify
api_location:
- Root\MicrosoftDNS
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Modify method of the MicrosoftDNS\_AFSDBType class

The **Modify** method updates an Andrew File System Database Server (AFSDB) Resource Record.

## Syntax


```mof
void Modify(
  [in, optional] uint32                 TTL,
  [in, optional] uint16                 Subtype,
  [in, optional] string                 ServerName,
  [out, ref]     MicrosoftDNS_AFSDBType &RR
);
```



## Parameters

<dl> <dt>

*TTL* \[in, optional\]
</dt> <dd>

Time, in seconds, that the RR can be cached by a DNS resolver.

</dd> <dt>

*Subtype* \[in, optional\]
</dt> <dd>

Subtype of the host AFS server. For subtype 1 (value=1), the host has an AFS version 3.0 Volume Location Server for the named AFS cell. In the case of subtype 2 (value=2), the host has an authenticated name server holding the cell-root directory node for the named DCE/NCA cell.

</dd> <dt>

*ServerName* \[in, optional\]
</dt> <dd>

FQDN specifying a host that has a server for the AFS cell specified in the owner name.

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

[**MicrosoftDNS\_AFSDBType**](microsoftdns-afsdbtype.md)
</dt> <dt>

[**CreateInstanceFromPropertyData Method of the MicrosoftDNS\_AFSDBType Class**](microsoftdns-afsdbtype-createinstancefrompropertydata.md)
</dt> <dt>

[**MicrosoftDNS\_ResourceRecord**](microsoftdns-resourcerecord.md)
</dt> </dl>

 

 





