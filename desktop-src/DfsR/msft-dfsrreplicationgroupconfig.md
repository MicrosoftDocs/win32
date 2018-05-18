---
title: MSFT\_DfsrReplicationGroupConfig class
description: An instance of this class is available for each replication group that contains this computer. This class provides read-only access to the replication group configuration parameters.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '8c76ec1f-1139-45c0-97cc-3aacceb8861e'
ms.prod: 'windows-server-dev'
ms.technology:
- 'distributed-file-system-replication'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_DfsrReplicationGroupConfig class Distributed File System Replication", "MSFT_DfsrReplicationGroupConfig class Distributed File System Replication , described"]
topic_type:
- apiref
api_name:
- MSFT_DfsrReplicationGroupConfig
- MSFT_DfsrReplicationGroupConfig.ReplicationGroupGuid
- MSFT_DfsrReplicationGroupConfig.ReplicationGroupName
- MSFT_DfsrReplicationGroupConfig.ReplicationGroupDn
- MSFT_DfsrReplicationGroupConfig.ReplicationGroupType
- MSFT_DfsrReplicationGroupConfig.LastChangeNumber
- MSFT_DfsrReplicationGroupConfig.LastChangeTime
- MSFT_DfsrReplicationGroupConfig.LastChangeSource
- MSFT_DfsrReplicationGroupConfig.TombstoneExpiryInMin
- MSFT_DfsrReplicationGroupConfig.Description
- MSFT_DfsrReplicationGroupConfig.DefaultScheduleInUtc
- MSFT_DfsrReplicationGroupConfig.DefaultSchedule
- MSFT_DfsrReplicationGroupConfig.ContainerComputerName
- MSFT_DfsrReplicationGroupConfig.IsClustered
- MSFT_DfsrReplicationGroupConfig.VcoResourceName
api_location:
- DfsRWmiV2.dll
api_type:
- DllExport
---

# MSFT\_DfsrReplicationGroupConfig class

An instance of this class is available for each replication group that contains this computer. This class provides read-only access to the replication group configuration parameters.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DfsrWMIV2"), AMENDMENT]
class MSFT_DfsrReplicationGroupConfig
{
  string   ReplicationGroupGuid;
  string   ReplicationGroupName;
  string   ReplicationGroupDn;
  uint32   ReplicationGroupType;
  uint32   LastChangeNumber;
  datetime LastChangeTime;
  string   LastChangeSource;
  uint32   TombstoneExpiryInMin;
  string   Description;
  Boolean  DefaultScheduleInUtc;
  uint8    DefaultSchedule[];
  string   ContainerComputerName;
  boolean  IsClustered;
  string   VcoResourceName;
};
```

## Members

The **MSFT\_DfsrReplicationGroupConfig** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_DfsrReplicationGroupConfig** class has these properties.

<dl> <dt>

**ContainerComputerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Replication group AD computer name")
</dt> </dl>

The name of the Active Directory computer object that holds the replication group information. Normally this name is same as the NETBIOS name of the local computer.

</dd> <dt>

**DefaultSchedule**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Octetstring**, [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Default Schedule")
</dt> </dl>

The default replication schedule to be used for any connection in this connection object that does not have a defined schedule.

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

**DefaultScheduleInUtc**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Default Schedule in UTC")
</dt> </dl>

Indicates whether the schedule is to be interpreted as UTC (default) or local time.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Replication Group Description")
</dt> </dl>

The user-specified description of the content or purpose of the current replication group.

</dd> <dt>

**IsClustered**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Is AD computer represent a VCO")
</dt> </dl>

Set to TRUE if the Active Directory server that holds the replicated folder is a virtual computer in a cluster, or FALSE if it is a local computer.

</dd> <dt>

**LastChangeNumber**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MinValue**](https://msdn.microsoft.com/library/aa393650) ("1"), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Last Change Number")
</dt> </dl>

The configuration sequence number. This value is incremented each time the replication group configuration changes.

</dd> <dt>

**LastChangeSource**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Last Change Source")
</dt> </dl>

Information about the originator of the last configuration change. This is the name of the Active Directory server.

</dd> <dt>

**LastChangeTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Last Change Time")
</dt> </dl>

The time stamp of the last configuration change.

</dd> <dt>

**ReplicationGroupDn**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Replication Group Distinguished Name")
</dt> </dl>

The distinguished name of the corresponding [**ms-DFSR-ReplicationGroup**](https://msdn.microsoft.com/library/ms682408) object in the Active Directory.

</dd> <dt>

**ReplicationGroupGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (36), **MinLen** (36), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Replication Group GUID")
</dt> </dl>

The unique identifier of the replication group.

</dd> <dt>

**ReplicationGroupName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Replication Group Name")
</dt> </dl>

The friendly name of the replication group. This name is not required to be unique.

</dd> <dt>

**ReplicationGroupType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Replication Group Type")
</dt> </dl>

The type of the replication group.

<dt>

<span id="OTHER"></span><span id="other"></span>

**OTHER** (0)


</dt> <dd></dd> <dt>

<span id="SYSVOL"></span><span id="sysvol"></span>

**SYSVOL** (1)


</dt> <dd></dd> <dt>

<span id="PROTECTION"></span><span id="protection"></span>

**PROTECTION** (2)


</dt> <dd></dd> <dt>

<span id="DISTRIBUTION"></span><span id="distribution"></span>

**DISTRIBUTION** (3)


</dt> <dd></dd> <dt>

<span id="CLIENT"></span><span id="client"></span>

**CLIENT** (4)


</dt> <dd></dd> <dt>

<span id="PEERNET"></span><span id="peernet"></span>

**PEERNET** (5)


</dt> <dd></dd> </dl>

</dd> <dt>

**TombstoneExpiryInMin**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MinValue**](https://msdn.microsoft.com/library/aa393650) ("60"), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Tombstone Expiration In Minutes")
</dt> </dl>

The maximum lifetime of tombstone objects, in minutes.

</dd> <dt>

**VcoResourceName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Content Set VCO Resource Name")
</dt> </dl>

If the replication group is configured against a virtual computer, this property specifies the Network Name resource of the clustered replication group.

</dd> </dl>

## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                        |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dfsr<br/>                                                |
| MOF<br/>                      | <dl> <dt>Dfsrwmiv2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DfsRWmiV2.dll</dt> </dl> |



## See also

<dl> <dt>

[DFSR WMI Classes](dfsr-wmi-classes.md)
</dt> </dl>

 

 





