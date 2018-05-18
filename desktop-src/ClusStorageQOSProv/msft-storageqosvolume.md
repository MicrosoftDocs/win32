---
title: MSFT\_StorageQoSVolume class
description: Contains per-volume storage QoS metrics and status.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '26d0646c-a98f-4f0b-8aea-75aa1958621f'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-storage-qos'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_StorageQoSVolume class", "MSFT_StorageQoSVolume class, described"]
topic_type:
- apiref
api_name:
- MSFT_StorageQoSVolume
- MSFT_StorageQoSVolume.VolumeId
- MSFT_StorageQoSVolume.Mountpoint
- MSFT_StorageQoSVolume.IOPS
- MSFT_StorageQoSVolume.Latency
- MSFT_StorageQoSVolume.Bandwidth
- MSFT_StorageQoSVolume.Reservation
- MSFT_StorageQoSVolume.Limit
- MSFT_StorageQoSVolume.BandwidthLimit
- MSFT_StorageQoSVolume.TimeStamp
- MSFT_StorageQoSVolume.Interval
- MSFT_StorageQoSVolume.Status
api_location:
- StorageQOS.dll
api_type:
- DllExport
---

# MSFT\_StorageQoSVolume class

Contains per-volume storage QoS metrics and status.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("STORAGEQOS"), AMENDMENT]
class MSFT_StorageQoSVolume
{
  string VolumeId;
  string Mountpoint;
  uint64 IOPS;
  uint64 Latency;
  uint64 Bandwidth;
  uint64 Reservation;
  uint64 Limit;
  uint64 BandwidthLimit;
  uint64 TimeStamp;
  uint64 Interval;
  uint16 Status;
};
```

## Members

The **MSFT\_StorageQoSVolume** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageQoSVolume** class has these properties.

<dl> <dt>

**Bandwidth**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Rolling average of bandwidth on volume in bytes per second.

</dd> <dt>

**BandwidthLimit**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Total bandwidth limit on volume, in bytes per second.

</dd> <dt>

**Interval**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The length of the averaging interval, in FILETIME format.

</dd> <dt>

**IOPS**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The rolling average of normalized IOPS on the volume.

</dd> <dt>

**Latency**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The rolling average, in FILETIME format, of IO latency on the volume.

</dd> <dt>

**Limit**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Total limit on volume, in normalized IOPS.

</dd> <dt>

**Mountpoint**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Volume mount point.

</dd> <dt>

**Reservation**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Total reserve on volume, in normalized IOPS.

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the aggregate reserve for all flows is being met.

<dt>

<span id="OK"></span><span id="ok"></span>

**OK** (0)


</dt> <dd></dd> <dt>

<span id="Insufficient_Throughput"></span><span id="insufficient_throughput"></span><span id="INSUFFICIENT_THROUGHPUT"></span>

**Insufficient Throughput** (1)


</dt> <dd></dd> <dt>

<span id="Lost_Communication"></span><span id="lost_communication"></span><span id="LOST_COMMUNICATION"></span>

**Lost Communication** (3)


</dt> <dd></dd> </dl>

</dd> <dt>

**TimeStamp**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A timestamp, in FILETIME format, indicating the end of the averaging interval.

</dd> <dt>

**VolumeId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The ID of volume reporting aggregated metrics and status.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>StorageQOS.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>StorageQOS.dll</dt> </dl> |



 

 





