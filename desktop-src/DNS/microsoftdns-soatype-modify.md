---
title: Modify method of the MicrosoftDNS_SOAType class
description: The Modify method updates a Start Of Authority (SOA) Resource Record.
ms.assetid: 531b770d-9ac9-43da-8595-fbc175b51b23
keywords:
- Modify method DNS
- Modify method DNS , MicrosoftDNS_SOAType class
- MicrosoftDNS_SOAType class DNS , Modify method
topic_type:
- apiref
api_name:
- MicrosoftDNS_SOAType.Modify
api_location:
- Root\MicrosoftDNS
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Modify method of the MicrosoftDNS\_SOAType class

The **Modify** method updates a Start Of Authority (SOA) Resource Record.

## Syntax


```mof
void Modify(
  [in, optional] uint32               TTL,
  [in, optional] uint32               SerialNumber,
  [in, optional] string               PrimaryServer,
  [in, optional] string               ResponsibleParty,
  [in, optional] uint32               RefreshInterval,
  [in, optional] uint32               RetryDelay,
  [in, optional] uint32               ExpireLimit,
  [in, optional] uint32               MinimumTTL,
  [out, ref]     MicrosoftDNS_SOAType &RR
);
```



## Parameters

<dl> <dt>

*TTL* \[in, optional\]
</dt> <dd>

Time, in seconds, that the RR can be cached by a DNS resolver.

</dd> <dt>

*SerialNumber* \[in, optional\]
</dt> <dd>

SOA serial number representing the number of times the zone has been updated, used by [*secondary servers*](s-gly.md) to determine whether zone transfer is necessary.

</dd> <dt>

*PrimaryServer* \[in, optional\]
</dt> <dd>

Name of the primary server.

</dd> <dt>

*ResponsibleParty* \[in, optional\]
</dt> <dd>

Mailbox address of the responsible party, in the form of alias.domain, such as xyz.microsoft.com. Note the use of a period rather than an at symbol (@).

</dd> <dt>

*RefreshInterval* \[in, optional\]
</dt> <dd>

Time, in seconds, before the zone containing this record should be refreshed.

</dd> <dt>

*RetryDelay* \[in, optional\]
</dt> <dd>

Time, in seconds, the DNS Server should delay between name resolution attempts.

</dd> <dt>

*ExpireLimit* \[in, optional\]
</dt> <dd>

Time, in seconds, that secondary servers should wait for a response from the primary server before discarding their copies of the zone file as invalid.

</dd> <dt>

*MinimumTTL* \[in, optional\]
</dt> <dd>

TTL time, in seconds, applied to resource records in the zone that do not specify their own TTL.

</dd> <dt>

*RR* \[out, ref\]
</dt> <dd>

Reference to the modified object

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

[**MicrosoftDNS\_SOAType**](microsoftdns-soatype.md)
</dt> <dt>

[**MicrosoftDNS\_ResourceRecord**](microsoftdns-resourcerecord.md)
</dt> </dl>

 

 





