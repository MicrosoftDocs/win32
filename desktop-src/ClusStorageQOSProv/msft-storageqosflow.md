---
title: MSFT\_StorageQoSFlow class
description: Contains per-flow storage QoS metrics.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 82ae09b1-1dfd-426e-8dd8-70fc5c3ddffb
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-storage-qos
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_StorageQoSFlow class
- MSFT_StorageQoSFlow class, described
topic_type:
- apiref
api_name:
- MSFT_StorageQoSFlow
- MSFT_StorageQoSFlow.FlowId
- MSFT_StorageQoSFlow.PolicyId
- MSFT_StorageQoSFlow.InitiatorId
- MSFT_StorageQoSFlow.Reservation
- MSFT_StorageQoSFlow.Limit
- MSFT_StorageQoSFlow.BandwidthLimit
- MSFT_StorageQoSFlow.FilePath
- MSFT_StorageQoSFlow.VolumeId
- MSFT_StorageQoSFlow.InitiatorName
- MSFT_StorageQoSFlow.InitiatorNodeName
- MSFT_StorageQoSFlow.InitiatorIOPS
- MSFT_StorageQoSFlow.InitiatorLatency
- MSFT_StorageQoSFlow.InitiatorBandwidth
- MSFT_StorageQoSFlow.StorageNodeName
- MSFT_StorageQoSFlow.StorageNodeIOPS
- MSFT_StorageQoSFlow.StorageNodeLatency
- MSFT_StorageQoSFlow.StorageNodeBandwidth
- MSFT_StorageQoSFlow.TimeStamp
- MSFT_StorageQoSFlow.Interval
- MSFT_StorageQoSFlow.Status
api_location:
- StorageQOS.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_StorageQoSFlow class

Contains per-flow storage QoS metrics.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("STORAGEQOS"), AMENDMENT]
class MSFT_StorageQoSFlow
{
  string FlowId;
  string PolicyId;
  string InitiatorId;
  uint64 Reservation;
  uint64 Limit;
  uint64 BandwidthLimit;
  string FilePath;
  string VolumeId;
  string InitiatorName;
  string InitiatorNodeName;
  uint64 InitiatorIOPS;
  uint64 InitiatorLatency;
  uint64 InitiatorBandwidth;
  string StorageNodeName;
  uint64 StorageNodeIOPS;
  uint64 StorageNodeLatency;
  uint64 StorageNodeBandwidth;
  uint64 TimeStamp;
  uint64 Interval;
  uint16 Status;
};
```

## Members

The **MSFT\_StorageQoSFlow** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageQoSFlow** class has these properties.

<dl> <dt>

**BandwidthLimit**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Bandwidth limit being applied to flow, in bytes per second.

</dd> <dt>

**FilePath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The path on volume of the file being accessed.

</dd> <dt>

**FlowId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A UUID uniquely identifying the flow.

</dd> <dt>

**InitiatorBandwidth**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Rolling average of bandwidth in bytes per second at the initiator.

</dd> <dt>

**InitiatorId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A UUID uniquely identifying the initiator of the flow.

</dd> <dt>

**InitiatorIOPS**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The rolling average of the normalized IOPS at the initiator.

</dd> <dt>

**InitiatorLatency**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The rolling average, in microseconds, of latency at the initiator.

</dd> <dt>

**InitiatorName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of initiator.

</dd> <dt>

**InitiatorNodeName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The hostname of the node initiating the flow.

</dd> <dt>

**Interval**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The length of averaging interval, in FILETIME format.

</dd> <dt>

**Limit**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The limit being applied to the flow.

</dd> <dt>

**PolicyId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A UUID uniquely identifying the policy being applied to this flow.

</dd> <dt>

**Reservation**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Normalized IOPS Limit being applied to flow.

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the reserve for flow is being met.

<dt>

<span id="OK"></span><span id="ok"></span>

**OK** (0)


</dt> <dd></dd> <dt>

<span id="Insufficient_Throughput"></span><span id="insufficient_throughput"></span><span id="INSUFFICIENT_THROUGHPUT"></span>

**Insufficient Throughput** (1)


</dt> <dd></dd> <dt>

<span id="Unknown_Policy_ID"></span><span id="unknown_policy_id"></span><span id="UNKNOWN_POLICY_ID"></span>

**Unknown Policy ID** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**StorageNodeBandwidth**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Rolling average of bandwidth in bytes per second at the initiator.

</dd> <dt>

**StorageNodeIOPS**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The rolling average of normalized IOPS at the storage node.

</dd> <dt>

**StorageNodeLatency**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The rolling average, in FILETIME format, of IO latency at the storage node.

</dd> <dt>

**StorageNodeName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The hostname of the storage node servicing the flow.

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

The ID of volume being accessed by the flow.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>StorageQOS.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>StorageQOS.dll</dt> </dl> |



 

 





