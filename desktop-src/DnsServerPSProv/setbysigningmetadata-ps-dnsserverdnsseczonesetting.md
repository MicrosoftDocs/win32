---
title: SetBySigningMetadata method of the PS\_DnsServerDnsSecZoneSetting class
description: Sets DNSSEC settings for the input zone.
audience: developer
ms.assetid: 2de1bbe9-0f9c-43b7-8c62-2a3bebf8c067
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetBySigningMetadata method
- SetBySigningMetadata method, PS_DnsServerDnsSecZoneSetting class
- PS_DnsServerDnsSecZoneSetting class, SetBySigningMetadata method
topic_type:
- apiref
api_name:
- PS_DnsServerDnsSecZoneSetting.SetBySigningMetadata
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SetBySigningMetadata method of the PS\_DnsServerDnsSecZoneSetting class

Sets DNSSEC settings for the input zone.

## Syntax


```mof
uint32 SetBySigningMetadata(
  [in]  string                       ZoneName,
  [in]  string                       ComputerName,
  [in]  DnsServerZoneSigningMetadata InputObject,
  [in]  boolean                      PassThru,
  [out] DnsServerZoneSigningMetadata cmdletOutput
);
```



## Parameters

<dl> <dt>

*ZoneName* \[in\]
</dt> <dd>

Name of the zone on which DNSSEC settings are set.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Optional DNS server name.

</dd> <dt>

*InputObject* \[in\]
</dt> <dd>

Specifies the object containing the DNSSEC settings for the zone

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If specified, returns the object or objects on which the operation was done.

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

 

 





