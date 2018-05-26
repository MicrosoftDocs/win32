---
title: DnsServerCache class
description: Represents the settings of a DNS server cache.
audience: developer
ms.assetid: cbe476ad-dfbc-4863-8808-3526a53d4540
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerCache class
- DnsServerCache class, described
topic_type:
- apiref
api_name:
- DnsServerCache
- DnsServerCache.DistinguishedName
- DnsServerCache.ZoneName
- DnsServerCache.ZoneType
- DnsServerCache.IsPaused
- DnsServerCache.IsDsIntegrated
- DnsServerCache.IsAutoCreated
- DnsServerCache.IsReverseLookupZone
- DnsServerCache.IsReadOnly
- DnsServerCache.IsShutdown
- DnsServerCache.MaxTtl
- DnsServerCache.MaxNegativeTtl
- DnsServerCache.MaxKBSize
- DnsServerCache.EnablePollutionProtection
- DnsServerCache.StoreEmptyAuthenticationResponse
- DnsServerCache.LockingPercent
- DnsServerCache.IgnorePolicies
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DnsServerCache class

Represents the settings of a DNS server cache.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerCache : DnsServerZone
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
  datetime MaxTtl;
  datetime MaxNegativeTtl;
  uint32   MaxKBSize;
  boolean  EnablePollutionProtection;
  boolean  StoreEmptyAuthenticationResponse;
  uint32   LockingPercent;
  boolean  IgnorePolicies;
};
```

## Members

The **DnsServerCache** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerCache** class has these properties.

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

**EnablePollutionProtection**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**True** to enable protection against cache pollution; otherwise, **false**.

</dd> <dt>

**IgnorePolicies**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**True** to ignore the policies of the cache; otherwise, **false**.

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

**LockingPercent**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The percentage of the maximum TTL for the cache, after which DNS cache locking is enabled. Cache locking allows you to control whether information in the DNS cache can be overwritten.

</dd> <dt>

**MaxKBSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The maximum size of the cache, in bytes.

</dd> <dt>

**MaxNegativeTtl**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The maximum TTL duration in which the cache can cache negative responses.

</dd> <dt>

**MaxTtl**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A timespan that specifies the time to live (TTL) of the cache.

</dd> <dt>

**StoreEmptyAuthenticationResponse**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**True** to store empty authentication responses in the cache; otherwise, **false**.

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

 

 





