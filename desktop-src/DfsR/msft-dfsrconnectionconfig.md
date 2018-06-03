---
title: MSFT\_DfsrConnectionConfig class
description: This class provides the configuration settings for a replication group connection. Each connection links a local and remote member, establishing a partnership. Only the connections of the direct partners to the local member have instances of this class.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: fb7372fc-d7fc-48a6-abc6-6fbf125e92e3
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-replication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_DfsrConnectionConfig class Distributed File System Replication
- MSFT_DfsrConnectionConfig class Distributed File System Replication , described
topic_type:
- apiref
api_name:
- MSFT_DfsrConnectionConfig
- MSFT_DfsrConnectionConfig.ConnectionGuid
- MSFT_DfsrConnectionConfig.ConnectionDn
- MSFT_DfsrConnectionConfig.MemberGuid
- MSFT_DfsrConnectionConfig.PartnerGuid
- MSFT_DfsrConnectionConfig.PartnerName
- MSFT_DfsrConnectionConfig.PartnerDn
- MSFT_DfsrConnectionConfig.PartnerDns
- MSFT_DfsrConnectionConfig.ReplicationGroupGuid
- MSFT_DfsrConnectionConfig.Inbound
- MSFT_DfsrConnectionConfig.Enabled
- MSFT_DfsrConnectionConfig.Keywords
- MSFT_DfsrConnectionConfig.RdcEnabled
- MSFT_DfsrConnectionConfig.RdcMinFileSizeInKb
- MSFT_DfsrConnectionConfig.RdcSimilarityDisabled
- MSFT_DfsrConnectionConfig.ScheduleInUtc
- MSFT_DfsrConnectionConfig.Schedule
api_location:
- DfsRWmiV2.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_DfsrConnectionConfig class

This class provides the configuration settings for a replication group connection. Each connection links a local and remote member, establishing a partnership. Only the connections of the direct partners to the local member have instances of this class.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DfsrWMIV2"), AMENDMENT]
class MSFT_DfsrConnectionConfig
{
  string  ConnectionGuid;
  string  ConnectionDn;
  string  MemberGuid;
  string  PartnerGuid;
  string  PartnerName;
  string  PartnerDn;
  string  PartnerDns;
  string  ReplicationGroupGuid;
  boolean Inbound;
  boolean Enabled;
  string  Keywords;
  boolean RdcEnabled;
  uint32  RdcMinFileSizeInKb;
  boolean RdcSimilarityDisabled;
  boolean ScheduleInUtc;
  uint8   Schedule[];
};
```

## Members

The **MSFT\_DfsrConnectionConfig** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_DfsrConnectionConfig** class has these properties.

<dl> <dt>

**ConnectionDn**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Connection Distinguished Name")
</dt> </dl>

The distinguished name of the corresponding [**ms-DFSR-Connection**](https://msdn.microsoft.com/library/ms682382) object in the Active Directory Domain Services.

</dd> <dt>

**ConnectionGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (36), **MinLen** (36), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Connection GUID")
</dt> </dl>

The unique connection identifier.

</dd> <dt>

**Enabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Enabled Connection")
</dt> </dl>

Indicates whether the connection is disabled. If the connection is enabled, then DFSR will use it; otherwise, it is ignored.

</dd> <dt>

**Inbound**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Incoming Connection")
</dt> </dl>

Indicates the direction of the connection between the local member and the partner; it can be inbound (from partner to member) or outbound (member to partner).

</dd> <dt>

**Keywords**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Keywords")
</dt> </dl>

User-defined strings that are used by monitoring and configuration tools and for grouping or identification purposes.

</dd> <dt>

**MemberGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (36), **MinLen** (36), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Member GUID")
</dt> </dl>

The identifier of the local member in this connection.

</dd> <dt>

**PartnerDn**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Partner Distinguished Name")
</dt> </dl>

The distinguished name of the corresponding [**ms-DFSR-Member**](https://msdn.microsoft.com/library/ms682403) object in the Active Directory Domain Services that represents the partner.

</dd> <dt>

**PartnerDns**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Partner DNS")
</dt> </dl>

The partner-qualified DNS name.

</dd> <dt>

**PartnerGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (36), **MinLen** (36), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Partner GUID")
</dt> </dl>

The identifier of the partner object in this connection.

</dd> <dt>

**PartnerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Partner Name")
</dt> </dl>

The partner name. This is typically the unqualified DNS name of the partner computer.

</dd> <dt>

**RdcEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("RDC Enabled")
</dt> </dl>

Indicates whether remote differential compression (RDC) is enabled on this connection.

</dd> <dt>

**RdcMinFileSizeInKb**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("RDC Minimum File Size in KB")
</dt> </dl>

The RDC minimum file size, in kilobytes. RDC is applied only on files that are this size or larger.

</dd> <dt>

**RdcSimilarityDisabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Cross-File RDC Disabled")
</dt> </dl>

Indicates whether cross-file remote differential compression (RDC) is disabled on this connection.

</dd> <dt>

**ReplicationGroupGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (36), **MinLen** (36), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Replication Group GUID")
</dt> </dl>

The unique replication group identifier.

</dd> <dt>

**Schedule**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Octetstring**, [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Schedule")
</dt> </dl>

The replication schedule for this connection.

The data is a series of 336 bytes: 2 bytes for each of the 24 hours per day, 7 days per week. The 2 bytes for each hour are divided into 4 groups of 4 bits. Each 4-bit group can be assigned one of the following values.

<dt>

<span id="BANDWIDTH_LEVEL_OFF"></span><span id="bandwidth_level_off"></span>

<span id="BANDWIDTH_LEVEL_OFF"></span><span id="bandwidth_level_off"></span>**BANDWIDTH\_LEVEL\_OFF** (0x0)


</dt> <dd>

No replication.

</dd> <dt>

<span id="BANDWIDTH_LEVEL_16_KBPS"></span><span id="bandwidth_level_16_kbps"></span>

<span id="BANDWIDTH_LEVEL_16_KBPS"></span><span id="bandwidth_level_16_kbps"></span>**BANDWIDTH\_LEVEL\_16\_KBPS** (0x1)


</dt> <dd>

16 kilobits per second (Kbps).

</dd> <dt>

<span id="BANDWIDTH_LEVEL_64_KBPS"></span><span id="bandwidth_level_64_kbps"></span>

<span id="BANDWIDTH_LEVEL_64_KBPS"></span><span id="bandwidth_level_64_kbps"></span>**BANDWIDTH\_LEVEL\_64\_KBPS** (0x2)


</dt> <dd>

64 Kbps.

</dd> <dt>

<span id="BANDWIDTH_LEVEL_128_KBPS"></span><span id="bandwidth_level_128_kbps"></span>

<span id="BANDWIDTH_LEVEL_128_KBPS"></span><span id="bandwidth_level_128_kbps"></span>**BANDWIDTH\_LEVEL\_128\_KBPS** (0x3)


</dt> <dd>

128 Kbps.

</dd> <dt>

<span id="BANDWIDTH_LEVEL_256_KBPS"></span><span id="bandwidth_level_256_kbps"></span>

<span id="BANDWIDTH_LEVEL_256_KBPS"></span><span id="bandwidth_level_256_kbps"></span>**BANDWIDTH\_LEVEL\_256\_KBPS** (0x4)


</dt> <dd>

256 Kbps.

</dd> <dt>

<span id="BANDWIDTH_LEVEL_512_KBPS"></span><span id="bandwidth_level_512_kbps"></span>

<span id="BANDWIDTH_LEVEL_512_KBPS"></span><span id="bandwidth_level_512_kbps"></span>**BANDWIDTH\_LEVEL\_512\_KBPS** (0x5)


</dt> <dd>

512 Kbps.

</dd> <dt>

<span id="BANDWIDTH_LEVEL_1_MBPS"></span><span id="bandwidth_level_1_mbps"></span>

<span id="BANDWIDTH_LEVEL_1_MBPS"></span><span id="bandwidth_level_1_mbps"></span>**BANDWIDTH\_LEVEL\_1\_MBPS** (0x6)


</dt> <dd>

1 Mbps.

</dd> <dt>

<span id="BANDWIDTH_LEVEL_2_MBPS"></span><span id="bandwidth_level_2_mbps"></span>

<span id="BANDWIDTH_LEVEL_2_MBPS"></span><span id="bandwidth_level_2_mbps"></span>**BANDWIDTH\_LEVEL\_2\_MBPS** (0x7)


</dt> <dd>

2 Mbps.

</dd> <dt>

<span id="BANDWIDTH_LEVEL_4_MBPS"></span><span id="bandwidth_level_4_mbps"></span>

<span id="BANDWIDTH_LEVEL_4_MBPS"></span><span id="bandwidth_level_4_mbps"></span>**BANDWIDTH\_LEVEL\_4\_MBPS** (0x8)


</dt> <dd>

4 Mbps.

</dd> <dt>

<span id="BANDWIDTH_LEVEL_8_MBPS"></span><span id="bandwidth_level_8_mbps"></span>

<span id="BANDWIDTH_LEVEL_8_MBPS"></span><span id="bandwidth_level_8_mbps"></span>**BANDWIDTH\_LEVEL\_8\_MBPS** (0x9)


</dt> <dd>

8 Mbps.

</dd> <dt>

<span id="BANDWIDTH_LEVEL_16_MBPS"></span><span id="bandwidth_level_16_mbps"></span>

<span id="BANDWIDTH_LEVEL_16_MBPS"></span><span id="bandwidth_level_16_mbps"></span>**BANDWIDTH\_LEVEL\_16\_MBPS** (0xA)


</dt> <dd>

16 Mbps.

</dd> <dt>

<span id="BANDWIDTH_LEVEL_32_MBPS"></span><span id="bandwidth_level_32_mbps"></span>

<span id="BANDWIDTH_LEVEL_32_MBPS"></span><span id="bandwidth_level_32_mbps"></span>**BANDWIDTH\_LEVEL\_32\_MBPS** (0xB)


</dt> <dd>

32 Mbps.

</dd> <dt>

<span id="BANDWIDTH_LEVEL_64_MBPS"></span><span id="bandwidth_level_64_mbps"></span>

<span id="BANDWIDTH_LEVEL_64_MBPS"></span><span id="bandwidth_level_64_mbps"></span>**BANDWIDTH\_LEVEL\_64\_MBPS** (0xC)


</dt> <dd>

64 Mbps.

</dd> <dt>

<span id="BANDWIDTH_LEVEL_128_MBPS"></span><span id="bandwidth_level_128_mbps"></span>

<span id="BANDWIDTH_LEVEL_128_MBPS"></span><span id="bandwidth_level_128_mbps"></span>**BANDWIDTH\_LEVEL\_128\_MBPS** (0xD)


</dt> <dd>

128 Mbps.

</dd> <dt>

<span id="BANDWIDTH_LEVEL_256_MBPS"></span><span id="bandwidth_level_256_mbps"></span>

<span id="BANDWIDTH_LEVEL_256_MBPS"></span><span id="bandwidth_level_256_mbps"></span>**BANDWIDTH\_LEVEL\_256\_MBPS** (0xE)


</dt> <dd>

256 Mbps.

</dd> <dt>

<span id="BANDWIDTH_LEVEL_INFINITE"></span><span id="bandwidth_level_infinite"></span>

<span id="BANDWIDTH_LEVEL_INFINITE"></span><span id="bandwidth_level_infinite"></span>**BANDWIDTH\_LEVEL\_INFINITE** (0xF)


</dt> <dd>

Full bandwidth (no throttling.)

</dd> </dl>

</dd> <dt>

**ScheduleInUtc**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Schedule in UTC")
</dt> </dl>

Indicates whether the schedule is to be interpreted as Coordinated Universal Time (UTC) (default) or local time.

</dd> </dl>

## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                        |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dfsr<br/>                                                |
| MOF<br/>                      | <dl> <dt>Dfsrwmiv2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DfsRWmiV2.dll</dt> </dl> |



## See also

<dl> <dt>

[DFSR WMI Classes](dfsr-wmi-classes.md)
</dt> </dl>

 

 





