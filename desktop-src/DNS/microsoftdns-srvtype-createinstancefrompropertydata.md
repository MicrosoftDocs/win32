---
title: CreateInstanceFromPropertyData method of the MicrosoftDNS_SRVType class
description: The CreateInstanceFromPropertyData method instantiates a Service (SRV) Resource Record.
ms.assetid: ef55faa8-1109-4c96-98ac-2b01b940fa5c
keywords:
- CreateInstanceFromPropertyData method DNS
- CreateInstanceFromPropertyData method DNS , MicrosoftDNS_SRVType class
- MicrosoftDNS_SRVType class DNS , CreateInstanceFromPropertyData method
topic_type:
- apiref
api_name:
- MicrosoftDNS_SRVType.CreateInstanceFromPropertyData
api_location:
- Root\MicrosoftDNS
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# CreateInstanceFromPropertyData method of the MicrosoftDNS\_SRVType class

The **CreateInstanceFromPropertyData** method instantiates a Service (SRV) Resource Record.

## Syntax


```mof
void CreateInstanceFromPropertyData(
  [in]           string               DnsServerName,
  [in]           string               ContainerName,
  [in]           string               OwnerName,
  [in, optional] uint32               RecordClass = 1,
  [in, optional] uint32               TTL,
  [in]           uint16               Priority,
  [in]           uint16               Weight,
  [in]           uint16               Port,
  [in]           string               SRVDomainName,
  [out, ref]     MicrosoftDNS_SRVType &RR
);
```



## Parameters

<dl> <dt>

*DnsServerName* \[in\]
</dt> <dd>

FQDN or IP address of the DNS Server that contains this RR.

</dd> <dt>

*ContainerName* \[in\]
</dt> <dd>

Name of the Container for the Zone, Cache, or RootHints instance that contains this RR.

</dd> <dt>

*OwnerName* \[in\]
</dt> <dd>

Owner name for the RR.

</dd> <dt>

*RecordClass* \[in, optional\]
</dt> <dd>

Class of the RR. Default value is 1. The following values are valid.



| Value                                                                                                | Meaning                  |
|------------------------------------------------------------------------------------------------------|--------------------------|
| <span id="1"></span><dl> <dt>**1**</dt> </dl> | IN (Internet)<br/> |
| <span id="2"></span><dl> <dt>**2**</dt> </dl> | CS (CSNET)<br/>    |
| <span id="3"></span><dl> <dt>**3**</dt> </dl> | CH (CHAOS)<br/>    |
| <span id="4"></span><dl> <dt>**4**</dt> </dl> | HS (Hesiod)<br/>   |



 

</dd> <dt>

*TTL* \[in, optional\]
</dt> <dd>

Time, in seconds, that the RR can be cached by a DNS resolver.

</dd> <dt>

*Priority* \[in\]
</dt> <dd>

Priority of the target host specified in the owner name. Lower numbers imply higher priorities.

</dd> <dt>

*Weight* \[in\]
</dt> <dd>

Weight of the target host. This is useful when selecting among hosts that have the same priority. The chances of using this host should be proportional to its weight.

</dd> <dt>

*Port* \[in\]
</dt> <dd>

Port used on the target host of a protocol service.

</dd> <dt>

*SRVDomainName* \[in\]
</dt> <dd>

FQDN of the target host. A target of \\.\\ means that the service is decidedly not available at this domain.

</dd> <dt>

*RR* \[out, ref\]
</dt> <dd>

Reference to the new object.

</dd> </dl>

## Return value

This method does not return a value.

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

[**Modify Method of the MicrosoftDNS\_SRVType Class**](microsoftdns-srvtype-modify.md)
</dt> <dt>

[**MicrosoftDNS\_ResourceRecord**](microsoftdns-resourcerecord.md)
</dt> </dl>

 

 





