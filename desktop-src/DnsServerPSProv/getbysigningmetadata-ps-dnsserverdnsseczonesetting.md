---
title: GetBySigningMetadata method of the PS\_DnsServerDnsSecZoneSetting class
description: Returns DNSSEC settings for the input zone.
audience: developer
ms.assetid: 9aa64bb5-00f5-4374-af74-e6f0abf23551
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetBySigningMetadata method
- GetBySigningMetadata method, PS_DnsServerDnsSecZoneSetting class
- PS_DnsServerDnsSecZoneSetting class, GetBySigningMetadata method
topic_type:
- apiref
api_name:
- PS_DnsServerDnsSecZoneSetting.GetBySigningMetadata
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetBySigningMetadata method of the PS\_DnsServerDnsSecZoneSetting class

Returns DNSSEC settings for the input zone.

## Syntax


```mof
uint32 GetBySigningMetadata(
  [in]  string                       ZoneName[],
  [in]  string                       ComputerName,
  [in]  boolean                      SigningMetadata,
  [in]  boolean                      IncludeKSKMetadata,
  [out] DnsServerZoneSigningMetadata cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ZoneName* \[in\]
</dt> <dd>

Name of the zone on which DNSSEC operations are performed.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Optional DNS server name.

</dd> <dt>

*SigningMetadata* \[in\]
</dt> <dd>

SigningMetaData

</dd> <dt>

*IncludeKSKMetadata* \[in\]
</dt> <dd>

Include KSK metadata

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DnsServerZoneSigningMetadata**](dnsserverzonesigningmetadata.md) class.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsServerDnsSecZoneSetting**](ps-dnsserverdnsseczonesetting.md)
</dt> </dl>

 

 





