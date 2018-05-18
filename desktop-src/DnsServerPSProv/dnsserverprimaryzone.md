---
title: DnsServerPrimaryZone class
description: DNS Primary Zone.
audience: developer
ms.assetid: '94c84eed-1872-46a4-b7aa-f40a82faf6b7'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DnsServerPrimaryZone class", "DnsServerPrimaryZone class, described"]
topic_type:
- apiref
api_name:
- DnsServerPrimaryZone
- DnsServerPrimaryZone.DistinguishedName
- DnsServerPrimaryZone.ZoneName
- DnsServerPrimaryZone.ZoneType
- DnsServerPrimaryZone.IsPaused
- DnsServerPrimaryZone.IsDsIntegrated
- DnsServerPrimaryZone.IsAutoCreated
- DnsServerPrimaryZone.IsReverseLookupZone
- DnsServerPrimaryZone.IsReadOnly
- DnsServerPrimaryZone.IsShutdown
- DnsServerPrimaryZone.DirectoryPartitionName
- DnsServerPrimaryZone.ReplicationScope
- DnsServerPrimaryZone.ZoneFile
- DnsServerPrimaryZone.Notify
- DnsServerPrimaryZone.NotifyServers
- DnsServerPrimaryZone.SecureSecondaries
- DnsServerPrimaryZone.SecondaryServers
- DnsServerPrimaryZone.DynamicUpdate
- DnsServerPrimaryZone.IsWinsEnabled
- DnsServerPrimaryZone.IsSigned
- DnsServerPrimaryZone.AllowedDcForNsRecordsAutoCreation
- DnsServerPrimaryZone.IsPluginEnabled
- DnsServerPrimaryZone.IgnorePolicies
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
---

# DnsServerPrimaryZone class

DNS Primary Zone.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerPrimaryZone : DnsServerZone
{
  string  DistinguishedName;
  string  ZoneName;
  string  ZoneType;
  boolean IsPaused;
  boolean IsDsIntegrated;
  boolean IsAutoCreated;
  boolean IsReverseLookupZone;
  boolean IsReadOnly;
  boolean IsShutdown;
  string  DirectoryPartitionName;
  string  ReplicationScope;
  string  ZoneFile;
  string  Notify;
  string  NotifyServers[];
  string  SecureSecondaries;
  string  SecondaryServers[];
  string  DynamicUpdate;
  boolean IsWinsEnabled;
  boolean IsSigned;
  string  AllowedDcForNsRecordsAutoCreation[];
  boolean IsPluginEnabled;
  boolean IgnorePolicies;
};
```

## Members

The **DnsServerPrimaryZone** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerPrimaryZone** class has these properties.

<dl> <dt>

**AllowedDcForNsRecordsAutoCreation**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the Domain Controllers which can register the NS records for this zone.

</dd> <dt>

**DirectoryPartitionName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Directory Partition Name

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

**DynamicUpdate**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Dynamic update

The possible values are.

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

**None** ("None")


</dt> <dd></dd> <dt>

<span id="Secure"></span><span id="secure"></span><span id="SECURE"></span>

**Secure** ("Secure")


</dt> <dd></dd> <dt>

<span id="NonsecureAndSecure"></span><span id="nonsecureandsecure"></span><span id="NONSECUREANDSECURE"></span>

**NonsecureAndSecure** ("NonsecureAndSecure")


</dt> <dd></dd> </dl>

</dd> <dt>

**IgnorePolicies**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**true** if the policies of this zone are to be ignored; otherwise, **false**.

**Windows Server 2012 R2 and Windows Server 2012:** Not supported.

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

**IsPluginEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Experimental**
</dt> </dl>

Not supported.

**Windows Server 2012 R2:  true** if the zone is plugin enabled.

**Windows Server 2012:** Not supported.

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

**IsSigned**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specified if the zone is signed.

</dd> <dt>

**IsWinsEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specified if WINS is enabled on the zone.

</dd> <dt>

**Notify**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Notify secondary servers

The possible values are.

<dt>

<span id="NoNotify"></span><span id="nonotify"></span><span id="NONOTIFY"></span>

**NoNotify** ("NoNotify")


</dt> <dd></dd> <dt>

<span id="Notify"></span><span id="notify"></span><span id="NOTIFY"></span>

**Notify** ("Notify")


</dt> <dd></dd> <dt>

<span id="NotifyServers"></span><span id="notifyservers"></span><span id="NOTIFYSERVERS"></span>

**NotifyServers** ("NotifyServers")


</dt> <dd></dd> </dl>

</dd> <dt>

**NotifyServers**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

Secondary servers

</dd> <dt>

**ReplicationScope**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Replication Scope

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

**SecondaryServers**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

Zone transfer servers

</dd> <dt>

**SecureSecondaries**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Zone transfer

The possible values are.

<dt>

<span id="NoTransfer"></span><span id="notransfer"></span><span id="NOTRANSFER"></span>

**NoTransfer** ("NoTransfer")


</dt> <dd></dd> <dt>

<span id="TransferAnyServer"></span><span id="transferanyserver"></span><span id="TRANSFERANYSERVER"></span>

**TransferAnyServer** ("TransferAnyServer")


</dt> <dd></dd> <dt>

<span id="TransferToZoneNameServer"></span><span id="transfertozonenameserver"></span><span id="TRANSFERTOZONENAMESERVER"></span>

**TransferToZoneNameServer** ("TransferToZoneNameServer")


</dt> <dd></dd> <dt>

<span id="TransferToSecureServers"></span><span id="transfertosecureservers"></span><span id="TRANSFERTOSECURESERVERS"></span>

**TransferToSecureServers** ("TransferToSecureServers")


</dt> <dd></dd> </dl>

</dd> <dt>

**ZoneFile**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Zone file path

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

 

 





