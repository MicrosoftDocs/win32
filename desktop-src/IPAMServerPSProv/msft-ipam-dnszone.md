---
Description: 'TBD.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '60085b21-a833-47fe-b247-691c07856c9d'
ms.prod: 'windows-server-dev'
ms.technology:
- 'internet-protocol-address-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'MSFT\_IPAM\_DnsZone class'
---

# MSFT\_IPAM\_DnsZone class

TBD

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("IPAMServerPSProvider"), AMENDMENT]
class MSFT_IPAM_DnsZone
{
  string   InstanceID;
  uint16   ZoneType;
  string   ZoneName;
  boolean  IsSigned;
  uint16   DynamicUpdateStatus;
  boolean  ScavengeStaleRecords;
  string   NorefreshInterval;
  string   RefreshInterval;
  string   PreferredServerName;
  string   LastCollectedFromServerName;
  uint16   ZoneOverallHealth;
  datetime ZoneOverallHealthLastUpdateTime;
  string   AccessScopePath;
  boolean  IsInheritedAccessScope;
};
```

## Members

The **MSFT\_IPAM\_DnsZone** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_IPAM\_DnsZone** class has these properties.

<dl> <dt>

**AccessScopePath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Access scope path for this DNS zone.

</dd> <dt>

**DynamicUpdateStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the dynamic update setting for the DNS zone.

The possible values are.

<dt>

<span id="NotApplicable"></span><span id="notapplicable"></span><span id="NOTAPPLICABLE"></span>

**NotApplicable** (0)


</dt> <dd></dd> <dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

**None** (1)


</dt> <dd></dd> <dt>

<span id="NonSecureAndSecure"></span><span id="nonsecureandsecure"></span><span id="NONSECUREANDSECURE"></span>

**NonSecureAndSecure** (2)


</dt> <dd></dd> <dt>

<span id="Secure"></span><span id="secure"></span><span id="SECURE"></span>

**Secure** (3)


</dt> <dd></dd> </dl>

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Opaquely and uniquely identifies an instance of this class within the scope of the instantiating Namespace.

</dd> <dt>

**IsInheritedAccessScope**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether the access scope for this DNS zone is inherited from parent.

</dd> <dt>

**IsSigned**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether the DNS zone is signed using DNSSEC.

</dd> <dt>

**LastCollectedFromServerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The server from which data for this DNS zone was last collected from.

</dd> <dt>

**NorefreshInterval**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The no refresh interval value for the DNS zone. This is valid only if ScavengeStaleRecords is enabled for this zone.

</dd> <dt>

**PreferredServerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Preferred server name for data collection for this DNS zone.

</dd> <dt>

**RefreshInterval**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The refresh interval value for the DNS zone. This is valid only if ScavengeStaleRecords is enabled for this zone.

</dd> <dt>

**ScavengeStaleRecords**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether the DNS zone is enabled for scavenging stale DNS resource records.

</dd> <dt>

**ZoneName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the name of the DNS zone.

</dd> <dt>

**ZoneOverallHealth**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The overall health for this DNS zone. This is valid only for forward lookup zones.

The possible values are.

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

**None** (0)


</dt> <dd></dd> <dt>

<span id="Green"></span><span id="green"></span><span id="GREEN"></span>

**Green** (1)


</dt> <dd></dd> <dt>

<span id="Yellow"></span><span id="yellow"></span><span id="YELLOW"></span>

**Yellow** (2)


</dt> <dd></dd> <dt>

<span id="Red"></span><span id="red"></span><span id="RED"></span>

**Red** (3)


</dt> <dd></dd> <dt>

<span id="NotApplicable"></span><span id="notapplicable"></span><span id="NOTAPPLICABLE"></span>

**NotApplicable** (4)


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (5)


</dt> <dd></dd> <dt>

<span id="Unchecked"></span><span id="unchecked"></span><span id="UNCHECKED"></span>

**Unchecked** (6)


</dt> <dd></dd> </dl>

</dd> <dt>

**ZoneOverallHealthLastUpdateTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The last time overall health for this DNS zone was updated. This is valid only for forward lookup zones.

</dd> <dt>

**ZoneType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the type of DNS zone - forward, IPv4 reverse or IPv6 reverse.

The possible values are.

<dt>

<span id="Forward"></span><span id="forward"></span><span id="FORWARD"></span>

**Forward** (1)


</dt> <dd></dd> <dt>

<span id="IPv4Reverse"></span><span id="ipv4reverse"></span><span id="IPV4REVERSE"></span>

**IPv4Reverse** (2)


</dt> <dd></dd> <dt>

<span id="IPv6Reverse"></span><span id="ipv6reverse"></span><span id="IPV6REVERSE"></span>

**IPv6Reverse** (3)


</dt> <dd></dd> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\IPAM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>IPAMServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IPAMServerPSProvider.dll</dt> </dl> |



 

 




