---
title: Modify method of the MicrosoftDNS_SRVType class
description: The Modify method updates a Service (SRV) Resource Record.
ms.assetid: 626483c9-4b36-4e62-b9ad-dd7bb18f2e1e
keywords:
- Modify method DNS
- Modify method DNS , MicrosoftDNS_SRVType class
- MicrosoftDNS_SRVType class DNS , Modify method
topic_type:
- apiref
api_name:
- MicrosoftDNS_SRVType.Modify
api_location:
- Root\MicrosoftDNS
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Modify method of the MicrosoftDNS\_SRVType class

The **Modify** method updates a Service (SRV) Resource Record.

## Syntax


```mof
void Modify(
  [in, optional] uint32               TTL,
  [in, optional] uint16               Priority,
  [in, optional] uint16               Weight,
  [in, optional] uint16               Port,
  [in, optional] string               SRVDomainName,
  [out, ref]     MicrosoftDNS_SRVType &RR
);
```



## Parameters

<dl> <dt>

*TTL* \[in, optional\]
</dt> <dd>

Time, in seconds, that the RR can be cached by a DNS resolver.

</dd> <dt>

*Priority* \[in, optional\]
</dt> <dd>

Priority of the target host specified in the owner name. Lower numbers imply higher priorities.

</dd> <dt>

*Weight* \[in, optional\]
</dt> <dd>

Weight of the target host. This is useful when selecting among hosts that have the same priority. The chances of using this host should be proportional to its weight.

</dd> <dt>

*Port* \[in, optional\]
</dt> <dd>

Port used on the target host of a protocol service.

</dd> <dt>

*SRVDomainName* \[in, optional\]
</dt> <dd>

FQDN of the target host. A target of \\.\\ means that the service is decidedly not available at this domain.

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

[**MicrosoftDNS\_SRVType**](microsoftdns-srvtype.md)
</dt> <dt>

[**CreateInstanceFromPropertyData Method of the MicrosoftDNS\_SRVType Class**](microsoftdns-srvtype-createinstancefrompropertydata.md)
</dt> <dt>

[**MicrosoftDNS\_ResourceRecord**](microsoftdns-resourcerecord.md)
</dt> </dl>

 

 





