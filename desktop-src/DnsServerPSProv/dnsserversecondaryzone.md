---
title: DnsServerSecondaryZone class
description: Represents a secondary DNS zone.
audience: developer
ms.assetid: f4a753e7-0b32-4622-9214-7d6823e1738a
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerSecondaryZone class
- DnsServerSecondaryZone class, described
topic_type:
- apiref
api_name:
- DnsServerSecondaryZone
- DnsServerSecondaryZone.DistinguishedName
- DnsServerSecondaryZone.ZoneName
- DnsServerSecondaryZone.ZoneType
- DnsServerSecondaryZone.IsPaused
- DnsServerSecondaryZone.IsDsIntegrated
- DnsServerSecondaryZone.IsAutoCreated
- DnsServerSecondaryZone.IsReverseLookupZone
- DnsServerSecondaryZone.IsReadOnly
- DnsServerSecondaryZone.IsShutdown
- DnsServerSecondaryZone.ZoneFile
- DnsServerSecondaryZone.MasterServers
- DnsServerSecondaryZone.IsWinsEnabled
- DnsServerSecondaryZone.LastSuccessfulSoaCheck
- DnsServerSecondaryZone.LastZoneTransferAttempt
- DnsServerSecondaryZone.LastSuccessfulZoneTransfer
- DnsServerSecondaryZone.LastZoneTransferResult
- DnsServerSecondaryZone.IgnorePolicies
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DnsServerSecondaryZone class

Represents a secondary DNS zone.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerSecondaryZone : DnsServerZone
{
  string   DistinguishedName;
  string   ZoneName;
  string   ZoneType;
  boolean  IsPaused;
  boolean  IsDsIntegrated;
  boolean  IsAutoCreated;
  boolean  IsReverseLookupZone;
  boolean  IsReadOnly;
  boolean  IsShutdown;
  string   ZoneFile;
  string   MasterServers[];
  boolean  IsWinsEnabled;
  datetime LastSuccessfulSoaCheck;
  datetime LastZoneTransferAttempt;
  datetime LastSuccessfulZoneTransfer;
  uint32   LastZoneTransferResult;
  boolean  IgnorePolicies;
};
```

## Members

The **DnsServerSecondaryZone** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerSecondaryZone** class has these properties.

<dl> <dt>

**DistinguishedName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Lightweight Directory Access Protocol (LDAP) name of the domain.

This property is inherited from [**DnsDomain**](dnsdomain.md).

</dd> <dt>

**IgnorePolicies**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**true** if the policies of this zone are to be ignored; otherwise, **false**.

**Windows Server 2012 R2 and Windows Server 2012:** Not supported.

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

**IsWinsEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**true** if WINS is enabled in the zone; otherwise, **false**.

</dd> <dt>

**LastSuccessfulSoaCheck**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time when the last SOA check occurred in the zone.

</dd> <dt>

**LastSuccessfulZoneTransfer**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time when the last successful zone transfer occurred in the zone.

</dd> <dt>

**LastZoneTransferAttempt**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time when last zone transfer occurred in the zone.

</dd> <dt>

**LastZoneTransferResult**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The result of the last successful zone transfer operation.

</dd> <dt>

**MasterServers**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

An array that contains identifiers of the master name servers..

</dd> <dt>

**ZoneFile**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The zone file of the secondary zone.

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
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**DnsServerZone**](dnsserverzone.md)
</dt> <dt>

[DnsServerPSProvider Provider](dns-server-classes.md)
</dt> </dl>

 

 





