---
title: Set method of the PS\_DnsServerZoneAging class
description: Sets DNS Aging settings for a zone.
audience: developer
ms.assetid: 'c7c6c0bc-5ee1-4fba-a822-c8fe7aaf5de2'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Set method", "Set method, PS_DnsServerZoneAging class", "PS_DnsServerZoneAging class, Set method"]
topic_type:
- apiref
api_name:
- PS_DnsServerZoneAging.Set
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# Set method of the PS\_DnsServerZoneAging class

Sets DNS Aging settings for a zone.

## Syntax


```mof
uint32 Set(
  [in]  boolean            Aging,
  [in]  string             Name,
  [in]  string             ComputerName,
  [in]  string             ScavengeServers[],
  [in]  datetime           RefreshInterval,
  [in]  datetime           NoRefreshInterval,
  [in]  boolean            PassThru,
  [out] DnsServerZoneAging cmdletOutput
);
```



## Parameters

<dl> <dt>

*Aging* \[in\]
</dt> <dd>

Specifies the aging and scavenging behavior of the zone. Zero indicates scavenging is disabled. When scavenging is disabled, the timestamps of records in the zone are not refreshed, and the records are not subjected to scavenging. When set to one, records are subjected to scavenging and their timestamps are refreshed when the server receives the dynamic update request for the records. For Active Directory-integrated zones, this value is set to the DefaultAgingState property of the DNS Server where the zone is created. For standard primary zones, the default value is zero.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Specifies the name of the zone. Only Primary zones

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command

</dd> <dt>

*ScavengeServers* \[in\]
</dt> <dd>

// Array of strings that enumerates the list of IP addresses of DNS servers that are allowed to perform scavenging of stale records of this zone. If the list is not specified, any primary DNS server authoritative for the zone is allowed to scavenge the zone when other prerequisites are met.

</dd> <dt>

*RefreshInterval* \[in\]
</dt> <dd>

Specifies the refresh interval, during which the records with nonzero timestamp are expected to be refreshed to remain in the zone. Records that have not been refreshed by expiration of the Refresh interval could be removed by the next scavenging performed by a server. This value should never be less than the longest refresh period of the records registered in the zone. Values that are too small may lead to removal of valid DNS records. values that are too large prolong the lifetime of stale records. This value is set to the DefaultRefreshInterval property of the DNS server where the zone is created. Range = 0, 8760

</dd> <dt>

*NoRefreshInterval* \[in\]
</dt> <dd>

Specifies the time interval between the last update of a record's timestamp and the earliest moment when the timestamp can be refreshed.

Range = 0, 8760

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**True** to return the object that was modified by the method. By default, this method does not generate any output.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On return, contains an instance of the current object. This parameter returns a value only if *PassThru* is set to **true.**

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

[**PS\_DnsServerZoneAging**](ps-dnsserverzoneaging.md)
</dt> </dl>

 

 





