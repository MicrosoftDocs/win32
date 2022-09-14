---
title: MicrosoftDNS_Zone class
description: The MicrosoftDNS\_Zone class describes a DNS Zone. Every instance of the MicrosoftDNS\_Zone class must be assigned to exactly one DNS Server. Zones may be associated with multiple instances of MicrosoftDNS\_Domain or MicrosoftDNS\_ResourceRecord classes.
ms.assetid: 9c59fa61-cca5-4718-ad40-8d2c6ed5fc2d
keywords:
- MicrosoftDNS_Zone class DNS
- MicrosoftDNS_Zone class DNS , described
topic_type:
- apiref
api_name:
- MicrosoftDNS_Zone
- MicrosoftDNS_Zone.PauseZone
- MicrosoftDNS_Zone.ResumeZone
- MicrosoftDNS_Zone.ReloadZone
- MicrosoftDNS_Zone.ForceRefresh
- MicrosoftDNS_Zone.UpdateFromDS
- MicrosoftDNS_Zone.WriteBackZone
- MicrosoftDNS_Zone.AgeAllRecords
- MicrosoftDNS_Zone.CreateZone
- MicrosoftDNS_Zone.ChangeZoneType
- MicrosoftDNS_Zone.ResetSecondaries
- MicrosoftDNS_Zone.GetDistinguishedName
- MicrosoftDNS_Zone.ZoneType
- MicrosoftDNS_Zone.DsIntegrated
- MicrosoftDNS_Zone.AllowUpdate
- MicrosoftDNS_Zone.DataFile
- MicrosoftDNS_Zone.DisableWINSRecordReplication
- MicrosoftDNS_Zone.Notify
- MicrosoftDNS_Zone.SecureSecondaries
- MicrosoftDNS_Zone.Paused
- MicrosoftDNS_Zone.Shutdown
- MicrosoftDNS_Zone.Reverse
- MicrosoftDNS_Zone.AutoCreated
- MicrosoftDNS_Zone.UseWins
- MicrosoftDNS_Zone.UseNBStat
- MicrosoftDNS_Zone.Aging
- MicrosoftDNS_Zone.RefreshInterval
- MicrosoftDNS_Zone.NoRefreshInterval
- MicrosoftDNS_Zone.AvailForScavengeTime
- MicrosoftDNS_Zone.MasterServers
- MicrosoftDNS_Zone.LocalMasterServers
- MicrosoftDNS_Zone.ScavengeServers
- MicrosoftDNS_Zone.SecondaryServers
- MicrosoftDNS_Zone.NotifyServers
- MicrosoftDNS_Zone.ForwarderTimeout
- MicrosoftDNS_Zone.ForwarderSlave
- MicrosoftDNS_Zone.LastSuccessfulSoaCheck
- MicrosoftDNS_Zone.LastSuccessfulXfr
api_location:
- Root\MicrosoftDNS
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# MicrosoftDNS\_Zone class

> [!NOTE]
> This article contains references to the term slave, a term that Microsoft no longer uses. When the term is removed from the software, we’ll remove it from this article.

> [!NOTE]
> This article contains references to the term master server, a term that Microsoft no longer uses. When the term is removed from the software, we’ll remove it from this article.

The **MicrosoftDNS\_Zone** class describes a DNS Zone. Every instance of the **MicrosoftDNS\_Zone** class must be assigned to exactly one DNS Server. Zones may be associated with multiple instances of [**MicrosoftDNS\_Domain**](microsoftdns-domain.md) or [**MicrosoftDNS\_ResourceRecord**](microsoftdns-resourcerecord.md) classes.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
class MicrosoftDNS_Zone : MicrosoftDNS_Domain
{
  uint32  ZoneType;
  boolean DsIntegrated;
  uint32  AllowUpdate;
  string  DataFile;
  boolean DisableWINSRecordReplication;
  uint32  Notify;
  uint32  SecureSecondaries;
  boolean Paused;
  boolean Shutdown;
  boolean Reverse;
  boolean AutoCreated;
  boolean UseWins;
  boolean UseNBStat;
  boolean Aging;
  uint32  RefreshInterval;
  uint32  NoRefreshInterval;
  uint32  AvailForScavengeTime;
  string  MasterServers[];
  string  LocalMasterServers[];
  string  ScavengeServers[];
  string  SecondaryServers[];
  string  NotifyServers[];
  uint32  ForwarderTimeout;
  boolean ForwarderSlave;
  uint32  LastSuccessfulSoaCheck;
  uint32  LastSuccessfulXfr;
};
```

## Members

The **MicrosoftDNS\_Zone** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MicrosoftDNS\_Zone** class has these methods.



| Method                   | Description                                                                                                                                                                                                |
|:-------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **AgeAllRecords**        | Enables aging for some or all non-NS and non-SOA records.<br/>                                                                                                                                       |
| **ChangeZoneType**       | Changes zone types. <br/> Qualifiers: Implemented<br/>                                                                                                                                         |
| **CreateZone**           | Creates a new zone. <br/> Qualifiers: None.<br/>                                                                                                                                               |
| **ForceRefresh**         | Forces an update of the secondary from the Master DNS Server. <br/> Qualifiers: Implemented<br/>                                                                                               |
| **GetDistinguishedName** | Obtains DS distinguished Name for the zone. <br/> Qualifiers: Implemented<br/>                                                                                                                 |
| **PauseZone**            | Pauses the Zone. <br/> Qualifiers: Implemented<br/>                                                                                                                                            |
| **ReloadZone**           | Reloads the Zone. <br/> Qualifiers: Implemented<br/>                                                                                                                                           |
| **ResetSecondaries**     | Resets the secondary ip address array. <br/> Qualifiers: Implemented<br/>                                                                                                                      |
| **ResumeZone**           | Resumes the Zone. <br/> Qualifiers: Implemented<br/>                                                                                                                                           |
| **UpdateFromDS**         | Forces an update of the Zone from the Directory Service (DS). For this method to be valid, the ZoneType must be 0 the Zone must indeed be stored in the DS. <br/> Qualifiers: Implemented<br/> |
| **WriteBackZone**        | Saves Zone data to its zone file. <br/> Qualifiers: Implemented, static<br/>                                                                                                                   |



 

### Properties

The **MicrosoftDNS\_Zone** class has these properties.

<dl> <dt>

**Aging**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the aging and scavenging behavior of the zone. Zero indicates scavenging is disabled. When scavenging is disabled, the timestamps of records in the zone are not refreshed, and the records are not subjected to scavenging. When set to one, records are subjected to scavenging and their timestamps are refreshed when the server receives the dynamic update request for the records. For Active Directory-integrated zones, this value is set to the *DefaultAgingState* property of the DNS Server where the zone is created. For standard primary zones, the default value is zero.

</dd> <dt>

**AllowUpdate**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the Zone accepts dynamic update requests.

</dd> <dt>

**AutoCreated**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the Zone is autocreated.

</dd> <dt>

**AvailForScavengeTime**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the time when the server may attempt scavenging the zone. Even if the zone is configured to enable scavenging the DNS server will not attempt scavenging this zone until after this moment. This value is set to the current time plus the Refresh Interval of the zone whenever the zone is loaded. This parameter is stored locally, and is not replicated to other copies of the zone.

</dd> <dt>

**DataFile**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the name of the zone file.

</dd> <dt>

**DisableWINSRecordReplication**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the WINS record is replicated. If set to TRUE, WINS record replication is disabled.

</dd> <dt>

**DsIntegrated**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies whether the zone is DS integrated.

</dd> <dt>

**ForwarderSlave**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the DNS uses recursion when resolving the names for the specified forward zone. Applicable to Conditional Forwarding zones only.

</dd> <dt>

**ForwarderTimeout**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the time, in seconds, a DNS server forwarding a query for the name under the forward zone waits for resolution from the forwarder before attempting to resolve the query itself. This parameter is applicable to the Forward zones only.

</dd> <dt>

**LastSuccessfulSoaCheck**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of seconds since the beginning of January 1, 1970 GMT, since the SOA serial number for the zone was last checked.

</dd> <dt>

**LastSuccessfulXfr**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of seconds since the beginning of January 1, 1970 GMT, since the zone was last transferred from a master server.

</dd> <dt>

**LocalMasterServers**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Local IP addresses of the master DNS servers for this zone. If set, these masters over-ride the MasterServers found in Active Directory.

</dd> <dt>

**MasterServers**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

IP addresses of the master DNS servers for this zone.

</dd> <dt>

**NoRefreshInterval**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the time interval between the last update of a record's timestamp and the earliest moment when the timestamp can be refreshed.

</dd> <dt>

**Notify**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the master Zone notifies secondaries of any changes in its RRs database. Set to 1 to notify secondaries.

</dd> <dt>

**NotifyServers**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Array of strings enumerating IP addresses of DNS servers to be notified of changes in this zone.

</dd> <dt>

**Paused**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the Zone is paused.

</dd> <dt>

**RefreshInterval**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the refresh interval, during which the records with nonzero timestamp are expected to be refreshed to remain in the zone. Records that have not been refreshed by expiration of the Refresh interval could be removed by the next scavenging performed by a server. This value should never be less than the longest refresh period of the records registered in the zone. Values that are too small may lead to removal of valid DNS records. values that are too large prolong the lifetime of stale records. This value is set to the *DefaultRefreshInterval* property of the DNS server where the zone is created.

</dd> <dt>

**Reverse**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the Zone is reverse (TRUE) or forward (FALSE).

</dd> <dt>

**ScavengeServers**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Array of strings that enumerates the list of IP addresses of DNS servers that are allowed to perform scavenging of stale records of this zone. If the list is not specified, any primary DNS server authoritative for the zone is allowed to scavenge the zone when other prerequisites are met.

</dd> <dt>

**SecondaryServers**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Array of strings enumerating IP addresses of DNS servers allowed to receive this zone through zone replication.

</dd> <dt>

**SecureSecondaries**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether zone transfer is allowed to designated secondaries only. Designated secondaries are DNS Servers whose IP addresses are listed in SecondariesIPAddressesArray.

</dd> <dt>

**Shutdown**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the copy of the Zone is expired. If TRUE, the Zone is expired, or shut down.

</dd> <dt>

**UseNBStat**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This Boolean indicates whether the Zone uses NBStat reverse lookup.

</dd> <dt>

**UseWins**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the Zone uses WINS look up.

</dd> <dt>

**ZoneType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the type of the Zone. Valid values are:

-   DS integrated
-   Primary
-   Secondary

**Windows Server 2003:  **

Additional values:

-   Cache
-   Stub
-   Forwarder

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| Namespace<br/>                | Root\\MicrosoftDNS<br/>                                                          |
| MOF<br/>                      | <dl> <dt>Dnsprov.mof</dt> </dl> |



## See also

<dl> <dt>

[**MicrosoftDNS\_Domain**](microsoftdns-domain.md)
</dt> <dt>

[**AgeAllRecords Method of the MicrosoftDNS\_Zone Class**](microsoftdns-zone-ageallrecords.md)
</dt> <dt>

[**ChangeZoneType Method of the MicrosoftDNS\_Zone Class**](microsoftdns-zone-changezonetype.md)
</dt> <dt>

[**CreateZone Method of the MicrosoftDNS\_Zone Class**](microsoftdns-zone-createzone.md)
</dt> <dt>

[**ForceRefresh Method of the MicrosoftDNS\_Zone Class**](microsoftdns-zone-forcerefresh.md)
</dt> <dt>

[**GetDistinguishedName Method of the MicrosoftDNS\_Zone Class**](microsoftdns-zone-getdistinguishedname.md)
</dt> <dt>

[**PauseZone Method of the MicrosoftDNS\_Zone Class**](microsoftdns-zone-pausezone.md)
</dt> <dt>

[**ReloadZone Method of the MicrosoftDNS\_Zone Class**](microsoftdns-zone-reloadzone.md)
</dt> <dt>

[**ResetSecondaries Method of the MicrosoftDNS\_Zone Class**](microsoftdns-zone-resetsecondaries.md)
</dt> <dt>

[**ResumeZone Method of the MicrosoftDNS\_Zone Class**](microsoftdns-zone-resumezone.md)
</dt> <dt>

[**UpdateFromDS Method of the MicrosoftDNS\_Zone Class**](microsoftdns-zone-updatefromds.md)
</dt> <dt>

[**WriteBackZone Method of the MicrosoftDNS\_Zone Class**](microsoftdns-zone-writebackzone.md)
</dt> </dl>

 

 





