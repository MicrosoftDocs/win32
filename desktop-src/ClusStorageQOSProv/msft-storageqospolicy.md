---
title: MSFT\_StorageQoSPolicy class
description: Defines a storage QOS policy.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f3f1f113-8f27-4acc-ae5f-66e555d5073a
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-storage-qos
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_StorageQoSPolicy class
- MSFT_StorageQoSPolicy class, described
topic_type:
- apiref
api_name:
- MSFT_StorageQoSPolicy
- MSFT_StorageQoSPolicy.PolicyId
- MSFT_StorageQoSPolicy.Name
- MSFT_StorageQoSPolicy.ThroughputLimit
- MSFT_StorageQoSPolicy.ThroughputReservation
- MSFT_StorageQoSPolicy.BandwidthLimit
- MSFT_StorageQoSPolicy.ParentPolicy
- MSFT_StorageQoSPolicy.PolicyType
- MSFT_StorageQoSPolicy.Status
api_location:
- StorageQOS.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_StorageQoSPolicy class

Defines a storage QOS policy.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("STORAGEQOS"), AMENDMENT]
class MSFT_StorageQoSPolicy
{
  string PolicyId;
  string Name;
  uint64 ThroughputLimit;
  uint64 ThroughputReservation;
  uint64 BandwidthLimit;
  string ParentPolicy;
  uint16 PolicyType;
  uint16 Status;
};
```

## Members

The **MSFT\_StorageQoSPolicy** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_StorageQoSPolicy** class has these methods.



| Method                                                       | Description                                           |
|:-------------------------------------------------------------|:------------------------------------------------------|
| [**DeletePolicy**](deletepolicy-msft-storageqospolicy.md)   | Deletes a policy.<br/>                          |
| [**SetAttributes**](setattributes-msft-storageqospolicy.md) | Sets the attributes of an existing policy.<br/> |



 

### Properties

The **MSFT\_StorageQoSPolicy** class has these properties.

<dl> <dt>

**BandwidthLimit**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

Bandwidth limit in bytes per second.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The name of the policy.

</dd> <dt>

**ParentPolicy**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The parent of the policy.

</dd> <dt>

**PolicyId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A UUID uniquely identifying the policy.

</dd> <dt>

**PolicyType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the throughput limits/reservations are shared among all initiators (SingleInstance), or are per-initiator (MultiInstance).

<dt>

<span id="Single_Instance"></span><span id="single_instance"></span><span id="SINGLE_INSTANCE"></span>

**Single Instance** (0)


</dt> <dd></dd> <dt>

<span id="Multi_Instance"></span><span id="multi_instance"></span><span id="MULTI_INSTANCE"></span>

**Multi Instance** (1)


</dt> <dd></dd> </dl>

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether reserve for policy is being met.

<dt>

<span id="OK"></span><span id="ok"></span>

**OK** (0)


</dt> <dd></dd> <dt>

<span id="Insufficient_Throughput"></span><span id="insufficient_throughput"></span><span id="INSUFFICIENT_THROUGHPUT"></span>

**Insufficient Throughput** (1)


</dt> <dd></dd> </dl>

</dd> <dt>

**ThroughputLimit**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

Throughput limit in normalized IOPS.

</dd> <dt>

**ThroughputReservation**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

Throughput reserve in normalized IOPS.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>StorageQOS.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>StorageQOS.dll</dt> </dl> |



 

 





