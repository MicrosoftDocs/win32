---
title: CreateInstanceFromPropertyData method of the MicrosoftDNS_WINSType class
description: The CreateInstanceFromPropertyData method instantiates a Windows Internet Name Service (WINS) Resource Record.
ms.assetid: 0b41a6a5-0bb1-467b-9089-2c721d521887
keywords:
- CreateInstanceFromPropertyData method DNS
- CreateInstanceFromPropertyData method DNS , MicrosoftDNS_WINSType class
- MicrosoftDNS_WINSType class DNS , CreateInstanceFromPropertyData method
topic_type:
- apiref
api_name:
- MicrosoftDNS_WINSType.CreateInstanceFromPropertyData
api_location:
- Root\MicrosoftDNS
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# CreateInstanceFromPropertyData method of the MicrosoftDNS\_WINSType class

The **CreateInstanceFromPropertyData** method instantiates a Windows Internet Name Service (WINS) Resource Record.

## Syntax


```mof
void CreateInstanceFromPropertyData(
  [in]           string                DnsServerName,
  [in]           string                ContainerName,
  [in]           string                OwnerName,
  [in, optional] uint32                RecordClass = 1,
  [in, optional] uint32                TTL,
  [in]           uint32                MappingFlag,
  [in]           uint32                LookupTimeout,
  [in]           uint32                CacheTimeout,
  [in]           string                WinsServers,
  [out, ref]     MicrosoftDNS_WINSType &RR
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

*MappingFlag* \[in\]
</dt> <dd>

WINS mapping flag that specifies whether the record must be included into the zone replication. It may have only two values: 0x80000000 and 0x00010000 corresponding to the replication and no-replication (local record) flags, respectively. The following values are valid.



| Value                                                                                                                                               | Meaning                                       |
|-----------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| <span id="0x80000000"></span><span id="0X80000000"></span><dl> <dt>**0x80000000**</dt> </dl> | Replication flag<br/>                   |
| <span id="0x00010000"></span><span id="0X00010000"></span><dl> <dt>**0x00010000**</dt> </dl> | No-replication (local record) flag<br/> |



 

</dd> <dt>

*LookupTimeout* \[in\]
</dt> <dd>

Time, in seconds, that a DNS Server attempts resolution using WINS Look up.

</dd> <dt>

*CacheTimeout* \[in\]
</dt> <dd>

Time, in seconds, that a DNS Server using WINS Look up may cache the WINS server's response.

</dd> <dt>

*WinsServers* \[in\]
</dt> <dd>

List of comma-separated IP addresses of WINS servers used in WINS Look ups.

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

[**MicrosoftDNS\_WINSType**](microsoftdns-winstype.md)
</dt> <dt>

[**Modify Method of the MicrosoftDNS\_WINSType Class**](microsoftdns-winstype-modify.md)
</dt> <dt>

[**MicrosoftDNS\_ResourceRecord**](microsoftdns-resourcerecord.md)
</dt> </dl>

 

 





