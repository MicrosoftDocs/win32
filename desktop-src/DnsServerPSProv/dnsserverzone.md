---
title: DnsServerZone class
description: Represents a DNS zone.
audience: developer
ms.assetid: 15d91109-9165-46bf-aad1-b95d0b4729e7
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerZone class
- DnsServerZone class, described
topic_type:
- apiref
api_name:
- DnsServerZone
- DnsServerZone.DistinguishedName
- DnsServerZone.ZoneName
- DnsServerZone.ZoneType
- DnsServerZone.IsPaused
- DnsServerZone.IsDsIntegrated
- DnsServerZone.IsAutoCreated
- DnsServerZone.IsReverseLookupZone
- DnsServerZone.IsReadOnly
- DnsServerZone.IsShutdown
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DnsServerZone class

Represents a DNS zone.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerZone : DnsDomain
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
};
```

## Members

The **DnsServerZone** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerZone** class has these properties.

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

**IsAutoCreated**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**true** if the zone is automatically created; otherwise, **false**.

</dd> <dt>

**IsDsIntegrated**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**true** if the zone is integrated with Active Directory; otherwise, **false**.

</dd> <dt>

**IsPaused**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**true** if the zone is paused; otherwise, **false**.

</dd> <dt>

**IsReadOnly**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**true** if the zone is read-only; otherwise, **false**.

</dd> <dt>

**IsReverseLookupZone**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**true** if the zone is a reverse lookup zone; otherwise, **false**.

</dd> <dt>

**IsShutdown**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**true** if the zone is shutdown; otherwise, **false**.

</dd> <dt>

**ZoneName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The name of the zone.

</dd> <dt>

**ZoneType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The zone type.

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

[**DnsDomain**](dnsdomain.md)
</dt> <dt>

[DnsServerPSProvider Provider](dns-server-classes.md)
</dt> </dl>

 

 





