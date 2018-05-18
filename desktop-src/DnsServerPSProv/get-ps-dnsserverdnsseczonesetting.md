---
title: Get method of the PS\_DnsServerDnsSecZoneSetting class
description: Returns DNSSEC settings for the input zone.
audience: developer
ms.assetid: 'ca5d6d74-a8a5-4319-b47b-e1b7b0dd590c'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Get method", "Get method, PS_DnsServerDnsSecZoneSetting class", "PS_DnsServerDnsSecZoneSetting class, Get method"]
topic_type:
- apiref
api_name:
- PS_DnsServerDnsSecZoneSetting.Get
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# Get method of the PS\_DnsServerDnsSecZoneSetting class

Returns DNSSEC settings for the input zone.

## Syntax


```mof
uint32 Get(
  [in]  string                     ZoneName[],
  [in]  string                     ComputerName,
  [out] DnsServerDnsSecZoneSetting cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ZoneName* \[in\]
</dt> <dd>

Name of the zone on which DnsSec operations are performed.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Optional DNS server name.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DnsServerDnsSecZoneSetting**](dnsserverdnsseczonesetting.md) class.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsServerDnsSecZoneSetting**](ps-dnsserverdnsseczonesetting.md)
</dt> </dl>

 

 





