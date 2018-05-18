---
title: MSFT\_WvrHealth class
description: Represents the health of Storage Replica Objects.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '50490694-9325-41f0-a16c-b47e1bf6542c'
ms.prod: 'windows-server-dev'
ms.technology:
- 'storage-replica'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_WvrHealth class", "MSFT_WvrHealth class, described"]
topic_type:
- apiref
api_name:
- MSFT_WvrHealth
- MSFT_WvrHealth.ObjectType
- MSFT_WvrHealth.SourceObjectId
- MSFT_WvrHealth.DiskId
- MSFT_WvrHealth.ReplicationGroupId
- MSFT_WvrHealth.HealthStatus
- MSFT_WvrHealth.FaultReasonParameters
- MSFT_WvrHealth.FaultReason
- MSFT_WvrHealth.FaultTypeId
- MSFT_WvrHealth.ActionId
- MSFT_WvrHealth.ActionString
- MSFT_WvrHealth.ActionStringParameters
api_location:
- wvrcimprov.dll
api_type:
- DllExport
---

# MSFT\_WvrHealth class

Represents the health of Storage Replica Objects.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("wvrcimprov"), AMENDMENT]
class MSFT_WvrHealth
{
  uint16 ObjectType;
  string SourceObjectId;
  string DiskId;
  string ReplicationGroupId;
  uint16 HealthStatus;
  string FaultReasonParameters[];
  string FaultReason;
  string FaultTypeId;
  string ActionId;
  string ActionString;
  string ActionStringParameters[];
};
```

## Members

The **MSFT\_WvrHealth** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_WvrHealth** class has these properties.

<dl> <dt>

**ActionId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the action ID associated with the **FaultId** for this health object.

</dd> <dt>

**ActionString**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the action ID string. This string can be used as is and will be localized in the server locale.

</dd> <dt>

**ActionStringParameters**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the parameters for the action ID string.

</dd> <dt>

**DiskId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the disk identifier in case of objects of type **Replica**, **ReplicaLog** or **PartitionDb**.

</dd> <dt>

**FaultReason**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies a string that contains the fault reason. This string can be used as-is and will be localized in the server locale.

</dd> <dt>

**FaultReasonParameters**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the parameters for the reason string associated with the **FaultTypeId**.

</dd> <dt>

**FaultTypeId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the ID for the fault type associated with the health object.

</dd> <dt>

**HealthStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the health of the object.

<dt>

<span id="Healthy"></span><span id="healthy"></span><span id="HEALTHY"></span>

**Healthy** (0)


</dt> <dd></dd> <dt>

<span id="Warning"></span><span id="warning"></span><span id="WARNING"></span>

**Warning** (1)


</dt> <dd></dd> <dt>

<span id="Unhealthy"></span><span id="unhealthy"></span><span id="UNHEALTHY"></span>

**Unhealthy** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**ObjectType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Represents the object type this health object is associated with.

<dt>

<span id="ReplicationGroup"></span><span id="replicationgroup"></span><span id="REPLICATIONGROUP"></span>

**ReplicationGroup** (0)


</dt> <dd></dd> <dt>

<span id="Replica"></span><span id="replica"></span><span id="REPLICA"></span>

**Replica** (1)


</dt> <dd></dd> <dt>

<span id="ReplicaLog"></span><span id="replicalog"></span><span id="REPLICALOG"></span>

**ReplicaLog** (2)


</dt> <dd></dd> <dt>

<span id="PartitionDb"></span><span id="partitiondb"></span><span id="PARTITIONDB"></span>

**PartitionDb** (3)


</dt> <dd></dd> </dl>

</dd> <dt>

**ReplicationGroupId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the unique id of the replication group that owns the health object.

</dd> <dt>

**SourceObjectId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

Indicates the object that this health object belongs to.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\StorageReplica<br/>                                       |
| MOF<br/>                      | <dl> <dt>Wvrcimprov.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wvrcimprov.dll</dt> </dl> |



 

 





