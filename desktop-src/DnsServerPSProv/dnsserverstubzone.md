---
title: DnsServerStubZone class
description: Manages a stub zone on a DNS server.
audience: developer
ms.assetid: '903abf0d-06a0-45cd-94ea-d00af191405f'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DnsServerStubZone class", "DnsServerStubZone class, described"]
topic_type:
- apiref
api_name:
- DnsServerStubZone
- DnsServerStubZone.DistinguishedName
- DnsServerStubZone.ZoneName
- DnsServerStubZone.ZoneType
- DnsServerStubZone.IsPaused
- DnsServerStubZone.IsDsIntegrated
- DnsServerStubZone.IsAutoCreated
- DnsServerStubZone.IsReverseLookupZone
- DnsServerStubZone.IsReadOnly
- DnsServerStubZone.IsShutdown
- DnsServerStubZone.DirectoryPartitionName
- DnsServerStubZone.ReplicationScope
- DnsServerStubZone.ZoneFile
- DnsServerStubZone.MasterServers
- DnsServerStubZone.LocalMasters
- DnsServerStubZone.LastSuccessfulSoaCheck
- DnsServerStubZone.LastZoneTransferAttempt
- DnsServerStubZone.LastSuccessfulZoneTransfer
- DnsServerStubZone.LastZoneTransferResult
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
---

# DnsServerStubZone class

Manages a stub zone on a DNS server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerStubZone : DnsServerZone
{
  string   DistinguishedName;
  string   ZoneName;
  string   ZoneType;
  boolean  IsPaused;
  boolean  IsDsIntegrated;
  boolean  IsAutoCreated;
  boolean  IsReverseLookupZone;
  boolean  IsReadOnly;
  boolean  IsShutdown;
  string   DirectoryPartitionName;
  string   ReplicationScope;
  string   ZoneFile;
  string   MasterServers[];
  string   LocalMasters[];
  datetime LastSuccessfulSoaCheck;
  datetime LastZoneTransferAttempt;
  datetime LastSuccessfulZoneTransfer;
  uint32   LastZoneTransferResult;
};
```

## Members

The **DnsServerStubZone** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerStubZone** class has these properties.

<dl> <dt>

**DirectoryPartitionName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The name of the directory partition for the zone.

</dd> <dt>

**DistinguishedName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Lightweight Directory Access Protocol (LDAP) name of the domain.

This property is inherited from [**DnsDomain**](dnsdomain.md).

</dd> <dt>

**IsAutoCreated**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**true** if the zone is automatically created; otherwise, **false**.

This property is inherited from [**DnsServerZone**](dnsserverzone.md).

</dd> <dt>

**IsDsIntegrated**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**true** if the zone is integrated with Active Directory; otherwise, **false**.

This property is inherited from [**DnsServerZone**](dnsserverzone.md).

</dd> <dt>

**IsPaused**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**true** if the zone is paused; otherwise, **false**.

This property is inherited from [**DnsServerZone**](dnsserverzone.md).

</dd> <dt>

**IsReadOnly**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**true** if the zone is read-only; otherwise, **false**.

This property is inherited from [**DnsServerZone**](dnsserverzone.md).

</dd> <dt>

**IsReverseLookupZone**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**true** if the zone is a reverse lookup zone; otherwise, **false**.

This property is inherited from [**DnsServerZone**](dnsserverzone.md).

</dd> <dt>

**IsShutdown**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**true** if the zone is shutdown; otherwise, **false**.

This property is inherited from [**DnsServerZone**](dnsserverzone.md).

</dd> <dt>

**LastSuccessfulSoaCheck**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time of the last SOA check for the zone.

</dd> <dt>

**LastSuccessfulZoneTransfer**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time of the last successful zone transfer for the zone.

</dd> <dt>

**LastZoneTransferAttempt**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time of the last zone transfer for the zone.

</dd> <dt>

**LastZoneTransferResult**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The result of the last successful zone transfer operation

</dd> <dt>

**LocalMasters**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

An array that contains identifiers of the local master name servers for the zone.

</dd> <dt>

**MasterServers**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

An array that contains identifiers of the master name servers for the zone.

</dd> <dt>

**ReplicationScope**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates the replication scope of the zone.

The possible values are.

<dt>

<span id="Forest"></span><span id="forest"></span><span id="FOREST"></span>

**Forest** ("Forest")


</dt> <dd></dd> <dt>

<span id="Domain"></span><span id="domain"></span><span id="DOMAIN"></span>

**Domain** ("Domain")


</dt> <dd></dd> <dt>

<span id="Legacy"></span><span id="legacy"></span><span id="LEGACY"></span>

**Legacy** ("Legacy")


</dt> <dd></dd> <dt>

<span id="Custom"></span><span id="custom"></span><span id="CUSTOM"></span>

**Custom** ("Custom")


</dt> <dd></dd> </dl>

</dd> <dt>

**ZoneFile**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The zone file path.

</dd> <dt>

**ZoneName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The name of the zone.

This property is inherited from [**DnsServerZone**](dnsserverzone.md).

</dd> <dt>

**ZoneType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The zone type.

This property is inherited from [**DnsServerZone**](dnsserverzone.md).

The possible values are.

<dt>

<span id="Cache"></span><span id="cache"></span><span id="CACHE"></span>

**Cache** ("Cache")


</dt> <dd></dd> <dt>

<span id="Primary"></span><span id="primary"></span><span id="PRIMARY"></span>

**Primary** ("Primary")


</dt> <dd></dd> <dt>

<span id="Secondary"></span><span id="secondary"></span><span id="SECONDARY"></span>

**Secondary** ("Secondary")


</dt> <dd></dd> <dt>

<span id="Stub"></span><span id="stub"></span><span id="STUB"></span>

**Stub** ("Stub")


</dt> <dd></dd> <dt>

<span id="Forwarder"></span><span id="forwarder"></span><span id="FORWARDER"></span>

**Forwarder** ("Forwarder")


</dt> <dd></dd> </dl>

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

[**DnsServerZone**](dnsserverzone.md)
</dt> <dt>

[DnsServerPSProvider Provider](dns-server-classes.md)
</dt> </dl>

 

 





