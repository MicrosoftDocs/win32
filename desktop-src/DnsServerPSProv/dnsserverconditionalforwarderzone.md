---
title: DnsServerConditionalForwarderZone class
description: Represents a DNS conditional forwarder on a DNS server.
audience: developer
ms.assetid: cc32f883-7ffc-4767-8722-90feaf58bb4f
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerConditionalForwarderZone class
- DnsServerConditionalForwarderZone class, described
topic_type:
- apiref
api_name:
- DnsServerConditionalForwarderZone
- DnsServerConditionalForwarderZone.DistinguishedName
- DnsServerConditionalForwarderZone.ZoneName
- DnsServerConditionalForwarderZone.ZoneType
- DnsServerConditionalForwarderZone.IsPaused
- DnsServerConditionalForwarderZone.IsDsIntegrated
- DnsServerConditionalForwarderZone.IsAutoCreated
- DnsServerConditionalForwarderZone.IsReverseLookupZone
- DnsServerConditionalForwarderZone.IsReadOnly
- DnsServerConditionalForwarderZone.IsShutdown
- DnsServerConditionalForwarderZone.DirectoryPartitionName
- DnsServerConditionalForwarderZone.ReplicationScope
- DnsServerConditionalForwarderZone.MasterServers
- DnsServerConditionalForwarderZone.UseRecursion
- DnsServerConditionalForwarderZone.ForwarderTimeout
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DnsServerConditionalForwarderZone class

Represents a DNS conditional forwarder on a DNS server.

> [!Note]  
> Conditional forwarders are stored internally as zones.

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerConditionalForwarderZone : DnsServerZone
{
  string  DistinguishedName;
  string  ZoneName;
  string  ZoneType;
  boolean IsPaused;
  boolean IsDsIntegrated;
  boolean IsAutoCreated;
  boolean IsReverseLookupZone;
  boolean IsReadOnly;
  boolean IsShutdown;
  string  DirectoryPartitionName;
  string  ReplicationScope;
  string  MasterServers[];
  boolean UseRecursion;
  uint32  ForwarderTimeout;
};
```

## Members

The **DnsServerConditionalForwarderZone** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerConditionalForwarderZone** class has these properties.

<dl> <dt>

**DirectoryPartitionName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The name of the directory partition that contains the conditional forwarder zone.

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

**ForwarderTimeout**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The timeout of the forwarder, in seconds.

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

**MasterServers**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

An array that contains the IP addresses of the master servers of the zone. You can use both IPv4 and IPv6 addresses. You must specify at least one master server.

</dd> <dt>

**ReplicationScope**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The replication scope for the conditional forwarder.

The possible values are.

<dt>

<span id="Forest"></span><span id="forest"></span><span id="FOREST"></span>

<span id="Forest"></span><span id="forest"></span><span id="FOREST"></span>**Forest** ("Forest")


</dt> <dd>

Replicate the conditional forwarder to all DNS servers that run on domain controllers in the forest.

</dd> <dt>

<span id="Domain"></span><span id="domain"></span><span id="DOMAIN"></span>

<span id="Domain"></span><span id="domain"></span><span id="DOMAIN"></span>**Domain** ("Domain")


</dt> <dd>

Replicate the conditional forwarder to all DNS servers that run on domain controllers in the domain.

</dd> <dt>

<span id="Legacy"></span><span id="legacy"></span><span id="LEGACY"></span>

<span id="Legacy"></span><span id="legacy"></span><span id="LEGACY"></span>**Legacy** ("Legacy")


</dt> <dd>

Replicate the conditional forwarder to all domain controllers in the domain.

</dd> <dt>

<span id="Custom"></span><span id="custom"></span><span id="CUSTOM"></span>

<span id="Custom"></span><span id="custom"></span><span id="CUSTOM"></span>**Custom** ("Custom")


</dt> <dd>

Replicate the conditional forwarder to all DNS servers running on domain controllers enlisted in a custom directory partition.

</dd> </dl>

</dd> <dt>

**UseRecursion**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**True** enable recursion in the zone; otherwise, **false**.

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

 

 





