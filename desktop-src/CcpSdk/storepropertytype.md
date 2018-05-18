---
Description: 'Defines the possible data types for a property.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '6ca1847a-430c-45a8-a87f-137879b2d88e'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: StorePropertyType enumeration
---

# StorePropertyType enumeration

Defines the possible data types for a property.

This enumeration supports the infrastructure and is not intended to be used directly from your code.

## Syntax


```C++
typedef enum  { 
  StorePropertyType_None                 = 0,         // 0x0
  StorePropertyType_Int32                = 65536,     // 0x10000
  StorePropertyType_UInt32               = 131072,    // 0x20000
  StorePropertyType_Int64                = 196608,    // 0x30000
  StorePropertyType_String               = 262144,    // 0x40000
  StorePropertyType_DateTime             = 327680,    // 0x50000
  StorePropertyType_Boolean              = 393216,    // 0x60000
  StorePropertyType_Guid                 = 458752,    // 0x70000
  StorePropertyType_Binary               = 524288,    // 0x80000
  StorePropertyType_Object               = 589824,    // 0x90000
  StorePropertyType_StringList           = 655360,    // 0xA0000
  StorePropertyType_JobPriority          = 1114112,   // 0x110000
  StorePropertyType_JobState             = 1179648,   // 0x120000
  StorePropertyType_JobUnitType          = 1245184,   // 0x130000
  StorePropertyType_CancelRequest        = 1310720,   // 0x140000
  StorePropertyType_FailureReason        = 1376256,   // 0x150000
  StorePropertyType_JobType              = 1441792,   // 0x160000
  StorePropertyType_JobOrderby           = 1507328,   // 0x170000
  StorePropertyType_TaskId               = 1572864,   // 0x180000
  StorePropertyType_PendingReason        = 1638400,   // 0x190000
  StorePropertyType_JobSchedulingPolicy  = 1703936,   // 0x1A0000
  StorePropertyType_TaskType             = 1769472,   // 0x1B0000
  StorePropertyType_TaskState            = 2228224,   // 0x220000
  StorePropertyType_ResourceState        = 3211264,   // 0x310000
  StorePropertyType_ResourceJobPhase     = 3276800,   // 0x320000
  StorePropertyType_NodeState            = 4259840,   // 0x410000
  StorePropertyType_NodeEvent            = 5308416,   // 0x510000
  StorePropertyType_JobEvent             = 5373952,   // 0x520000
  StorePropertyType_AllocationList       = 6356992,   // 0x610000
  StorePropertyType_JobMessageType       = 6422528,   // 0x620000
  StorePropertyType_Error                = 285212672, // 0x11000000
  StorePropertyType_TypeMask             = 536805376 // 0x1FFF0000
} StorePropertyType;
```



## Constants

<dl> <dt>

<span id="StorePropertyType_None"></span><span id="storepropertytype_none"></span><span id="STOREPROPERTYTYPE_NONE"></span>**StorePropertyType\_None**
</dt> <dd>

The property does not contain a type.

</dd> <dt>

<span id="StorePropertyType_Int32"></span><span id="storepropertytype_int32"></span><span id="STOREPROPERTYTYPE_INT32"></span>**StorePropertyType\_Int32**
</dt> <dd>

The property contains a 4-byte signed integer.

</dd> <dt>

<span id="StorePropertyType_UInt32"></span><span id="storepropertytype_uint32"></span><span id="STOREPROPERTYTYPE_UINT32"></span>**StorePropertyType\_UInt32**
</dt> <dd>

The property contains a 4-byte unsigned integer.

</dd> <dt>

<span id="StorePropertyType_Int64"></span><span id="storepropertytype_int64"></span><span id="STOREPROPERTYTYPE_INT64"></span>**StorePropertyType\_Int64**
</dt> <dd>

The property contains an 8-byte signed integer.

</dd> <dt>

<span id="StorePropertyType_String"></span><span id="storepropertytype_string"></span><span id="STOREPROPERTYTYPE_STRING"></span>**StorePropertyType\_String**
</dt> <dd>

The property contains a string.

</dd> <dt>

<span id="StorePropertyType_DateTime"></span><span id="storepropertytype_datetime"></span><span id="STOREPROPERTYTYPE_DATETIME"></span>**StorePropertyType\_DateTime**
</dt> <dd>

The property contains a date and time object.

</dd> <dt>

<span id="StorePropertyType_Boolean"></span><span id="storepropertytype_boolean"></span><span id="STOREPROPERTYTYPE_BOOLEAN"></span>**StorePropertyType\_Boolean**
</dt> <dd>

The property contains a Boolean value (true or false).

</dd> <dt>

<span id="StorePropertyType_Guid"></span><span id="storepropertytype_guid"></span><span id="STOREPROPERTYTYPE_GUID"></span>**StorePropertyType\_Guid**
</dt> <dd>

The property contains a globally unique identifier.

</dd> <dt>

<span id="StorePropertyType_Binary"></span><span id="storepropertytype_binary"></span><span id="STOREPROPERTYTYPE_BINARY"></span>**StorePropertyType\_Binary**
</dt> <dd>

The property contains binary data.

</dd> <dt>

<span id="StorePropertyType_Object"></span><span id="storepropertytype_object"></span><span id="STOREPROPERTYTYPE_OBJECT"></span>**StorePropertyType\_Object**
</dt> <dd>

The property contains an object.

</dd> <dt>

<span id="StorePropertyType_StringList"></span><span id="storepropertytype_stringlist"></span><span id="STOREPROPERTYTYPE_STRINGLIST"></span>**StorePropertyType\_StringList**
</dt> <dd>

The property contains a collection of strings.

</dd> <dt>

<span id="StorePropertyType_JobPriority"></span><span id="storepropertytype_jobpriority"></span><span id="STOREPROPERTYTYPE_JOBPRIORITY"></span>**StorePropertyType\_JobPriority**
</dt> <dd>

The property contains a [**JobPriority**](jobpriority-hpc.md) value.

</dd> <dt>

<span id="StorePropertyType_JobState"></span><span id="storepropertytype_jobstate"></span><span id="STOREPROPERTYTYPE_JOBSTATE"></span>**StorePropertyType\_JobState**
</dt> <dd>

The property contains a [**JobState**](jobstate.md) value.

</dd> <dt>

<span id="StorePropertyType_JobUnitType"></span><span id="storepropertytype_jobunittype"></span><span id="STOREPROPERTYTYPE_JOBUNITTYPE"></span>**StorePropertyType\_JobUnitType**
</dt> <dd>

The property contains a [**JobUnitType**](jobunittype.md) value.

</dd> <dt>

<span id="StorePropertyType_CancelRequest"></span><span id="storepropertytype_cancelrequest"></span><span id="STOREPROPERTYTYPE_CANCELREQUEST"></span>**StorePropertyType\_CancelRequest**
</dt> <dd>

The property contains a [CancelRequest](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.cancelrequest.aspx) value.

</dd> <dt>

<span id="StorePropertyType_FailureReason"></span><span id="storepropertytype_failurereason"></span><span id="STOREPROPERTYTYPE_FAILUREREASON"></span>**StorePropertyType\_FailureReason**
</dt> <dd>

The property contains a [FailureReason](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.failurereason.aspx) value.

</dd> <dt>

<span id="StorePropertyType_JobType"></span><span id="storepropertytype_jobtype"></span><span id="STOREPROPERTYTYPE_JOBTYPE"></span>**StorePropertyType\_JobType**
</dt> <dd>

The property contains a [**JobType**](jobtype.md) value.

</dd> <dt>

<span id="StorePropertyType_JobOrderby"></span><span id="storepropertytype_joborderby"></span><span id="STOREPROPERTYTYPE_JOBORDERBY"></span>**StorePropertyType\_JobOrderby**
</dt> <dd>

The property contains a [JobOrderBy](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.joborderby.aspx) object.

</dd> <dt>

<span id="StorePropertyType_TaskId"></span><span id="storepropertytype_taskid"></span><span id="STOREPROPERTYTYPE_TASKID"></span>**StorePropertyType\_TaskId**
</dt> <dd>

The property contains an [**ITaskId**](itaskid.md) interface.

</dd> <dt>

<span id="StorePropertyType_PendingReason"></span><span id="storepropertytype_pendingreason"></span><span id="STOREPROPERTYTYPE_PENDINGREASON"></span>**StorePropertyType\_PendingReason**
</dt> <dd>

The property contains a [PendingReason](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.pendingreason.aspx) value.

</dd> <dt>

<span id="StorePropertyType_JobSchedulingPolicy"></span><span id="storepropertytype_jobschedulingpolicy"></span><span id="STOREPROPERTYTYPE_JOBSCHEDULINGPOLICY"></span>**StorePropertyType\_JobSchedulingPolicy**
</dt> <dd>

The property contains a **SchedulingMode** value. This value is supported only for HPC Pack 2008 R2.

</dd> <dt>

<span id="StorePropertyType_TaskType"></span><span id="storepropertytype_tasktype"></span><span id="STOREPROPERTYTYPE_TASKTYPE"></span>**StorePropertyType\_TaskType**
</dt> <dd>

The property contains a [**TaskType**](tasktype.md) value. This value is supported only for HPC Pack 2008 R2.

</dd> <dt>

<span id="StorePropertyType_TaskState"></span><span id="storepropertytype_taskstate"></span><span id="STOREPROPERTYTYPE_TASKSTATE"></span>**StorePropertyType\_TaskState**
</dt> <dd>

The property contains a [**TaskState**](taskstate.md) value.

</dd> <dt>

<span id="StorePropertyType_ResourceState"></span><span id="storepropertytype_resourcestate"></span><span id="STOREPROPERTYTYPE_RESOURCESTATE"></span>**StorePropertyType\_ResourceState**
</dt> <dd>

The property contains a [ResourceState](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.resourcestate.aspx) value.

</dd> <dt>

<span id="StorePropertyType_ResourceJobPhase"></span><span id="storepropertytype_resourcejobphase"></span><span id="STOREPROPERTYTYPE_RESOURCEJOBPHASE"></span>**StorePropertyType\_ResourceJobPhase**
</dt> <dd>

The property contains a **ResourceJobPhase** value. This value is supported only for HPC Pack 2008 R2.

</dd> <dt>

<span id="StorePropertyType_NodeState"></span><span id="storepropertytype_nodestate"></span><span id="STOREPROPERTYTYPE_NODESTATE"></span>**StorePropertyType\_NodeState**
</dt> <dd>

The property contains a [**NodeState**](nodestate.md) value.

</dd> <dt>

<span id="StorePropertyType_NodeEvent"></span><span id="storepropertytype_nodeevent"></span><span id="STOREPROPERTYTYPE_NODEEVENT"></span>**StorePropertyType\_NodeEvent**
</dt> <dd>

The property contains a [NodeEvent](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.nodeevent.aspx) value.

</dd> <dt>

<span id="StorePropertyType_JobEvent"></span><span id="storepropertytype_jobevent"></span><span id="STOREPROPERTYTYPE_JOBEVENT"></span>**StorePropertyType\_JobEvent**
</dt> <dd>

The property contains a [JobEvent](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.jobevent.aspx) value.

</dd> <dt>

<span id="StorePropertyType_AllocationList"></span><span id="storepropertytype_allocationlist"></span><span id="STOREPROPERTYTYPE_ALLOCATIONLIST"></span>**StorePropertyType\_AllocationList**
</dt> <dd>

The property contains a collection of [**KeyValuePair**](frlrfSystemCollectionsGenericKeyValuePair2ClassTopic) objects.

</dd> <dt>

<span id="StorePropertyType_JobMessageType"></span><span id="storepropertytype_jobmessagetype"></span><span id="STOREPROPERTYTYPE_JOBMESSAGETYPE"></span>**StorePropertyType\_JobMessageType**
</dt> <dd>

The property contains a **JobMessageType** value. This value is supported only for HPC Pack 2008 R2.

</dd> <dt>

<span id="StorePropertyType_Error"></span><span id="storepropertytype_error"></span><span id="STOREPROPERTYTYPE_ERROR"></span>**StorePropertyType\_Error**
</dt> <dd>

The property contains a [PropertyError](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.propertyerror.aspx) value.

</dd> <dt>

<span id="StorePropertyType_TypeMask"></span><span id="storepropertytype_typemask"></span><span id="STOREPROPERTYTYPE_TYPEMASK"></span>**StorePropertyType\_TypeMask**
</dt> <dd>

A mask that you use to get a type value.

</dd> </dl>

## Requirements



|                         |                                                                                                                   |
|-------------------------|-------------------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.Properties.tlb</dt> </dl> |



## See also

<dl> <dt>

[HPC Enumerations](hpc-enumerations.md)
</dt> </dl>

 

 




