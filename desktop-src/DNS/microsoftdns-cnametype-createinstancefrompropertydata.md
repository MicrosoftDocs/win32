---
title: CreateInstanceFromPropertyData method of the MicrosoftDNS_CNAMEType class
description: The CreateInstanceFromPropertyData method instantiates a Canonical Name (CNAME) Resource Record.
ms.assetid: b5a5e14a-fb30-4cdf-90d0-7ef446350ac6
keywords:
- CreateInstanceFromPropertyData method DNS
- CreateInstanceFromPropertyData method DNS , MicrosoftDNS_CNAMEType class
- MicrosoftDNS_CNAMEType class DNS , CreateInstanceFromPropertyData method
topic_type:
- apiref
api_name:
- MicrosoftDNS_CNAMEType.CreateInstanceFromPropertyData
api_location:
- Root\MicrosoftDNS
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# CreateInstanceFromPropertyData method of the MicrosoftDNS\_CNAMEType class

The **CreateInstanceFromPropertyData** method instantiates a Canonical Name (CNAME) Resource Record.

## Syntax


```mof
void CreateInstanceFromPropertyData(
  [in]           string                 DnsServerName,
  [in]           string                 ContainerName,
  [in]           string                 OwnerName,
  [in, optional] uint32                 RecordClass = 1,
  [in, optional] uint32                 TTL,
  [in]           string                 PrimaryName,
  [out, ref]     MicrosoftDNS_CNAMEType &RR
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

*PrimaryName* \[in\]
</dt> <dd>

Primary name of the CNAME RR.

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

[**MicrosoftDNS\_CNAMEType**](microsoftdns-cnametype.md)
</dt> <dt>

[**Modify Method of the MicrosoftDNS\_CNAMEType Class**](microsoftdns-cnametype-modify.md)
</dt> <dt>

[**MicrosoftDNS\_ResourceRecord**](microsoftdns-resourcerecord.md)
</dt> </dl>

 

 





