---
title: StatusInformation
description: Contains information about the status of the group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '0A134761-EC5D-40FF-836C-CE567B418FDA'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["StatusInformation Failover Cluster"]
topic_type:
- apiref
api_name:
- StatusInformation
api_type:
- NA
---

# StatusInformation

Contains information about the status of the group.



| Attribute            | Value                                                                   |
|----------------------|-------------------------------------------------------------------------|
| Data type<br/> | **ULARGE\_INTEGER**<br/>                                          |
| Access<br/>    | [Read-only](read-only-properties.md)<br/>                        |
| Structure<br/> | [**CLUSPROP\_ULARGE\_INTEGER**](clusprop-ularge-integer.md)<br/> |
| Minimum<br/>   | 0 (0x000)<br/>                                                    |
| Maximum<br/>   | 2047 (0x7FF)<br/>                                                 |
| Default<br/>   | 0 (0x000)<br/>                                                    |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_GRP\_STATUS\_INFORMATION**.

This property can contain a bitwise combination of the following values:

<dl> <dt>

<span id="CLUSGRP_STATUS_LOCKED_MODE__1_0x001_"></span><span id="clusgrp_status_locked_mode__1_0x001_"></span><span id="CLUSGRP_STATUS_LOCKED_MODE__1_0X001_"></span>**CLUSGRP\_STATUS\_LOCKED\_MODE** (1=0x001)
</dt> <dd>

The group is locked.

</dd> <dt>

<span id="CLUSGRP_STATUS_PREEMPTED__2_0x002_"></span><span id="clusgrp_status_preempted__2_0x002_"></span><span id="CLUSGRP_STATUS_PREEMPTED__2_0X002_"></span>**CLUSGRP\_STATUS\_PREEMPTED** (2=0x002)
</dt> <dd>

The group has been preempted.

</dd> <dt>

<span id="CLUSGRP_STATUS_WAITING_IN_QUEUE_FOR_MOVE__4_0x004_"></span><span id="clusgrp_status_waiting_in_queue_for_move__4_0x004_"></span><span id="CLUSGRP_STATUS_WAITING_IN_QUEUE_FOR_MOVE__4_0X004_"></span>**CLUSGRP\_STATUS\_WAITING\_IN\_QUEUE\_FOR\_MOVE** (4=0x004)
</dt> <dd>

The group is waiting in the queue for a move.

</dd> <dt>

<span id="CLUSGRP_STATUS_PHYSICAL_RESOURCES_LACKING__8_0x008_"></span><span id="clusgrp_status_physical_resources_lacking__8_0x008_"></span><span id="CLUSGRP_STATUS_PHYSICAL_RESOURCES_LACKING__8_0X008_"></span>**CLUSGRP\_STATUS\_PHYSICAL\_RESOURCES\_LACKING** (8=0x008)
</dt> <dd>

The group is lacking physical resources.

</dd> <dt>

<span id="CLUSGRP_STATUS_WAITING_TO_START__16_0x010_"></span><span id="clusgrp_status_waiting_to_start__16_0x010_"></span><span id="CLUSGRP_STATUS_WAITING_TO_START__16_0X010_"></span>**CLUSGRP\_STATUS\_WAITING\_TO\_START** (16=0x010)
</dt> <dd>

The group is waiting to start.

</dd> <dt>

<span id="CLUSGRP_STATUS_EMBEDDED_FAILURE__32_0x020_"></span><span id="clusgrp_status_embedded_failure__32_0x020_"></span><span id="CLUSGRP_STATUS_EMBEDDED_FAILURE__32_0X020_"></span>**CLUSGRP\_STATUS\_EMBEDDED\_FAILURE** (32=0x020)
</dt> <dd>

The group has an embedded failure.

</dd> <dt>

<span id="CLUSGRP_STATUS_OFFLINE_DUE_TO_ANTIAFFINITY_CONFLICT__64_0x040_"></span><span id="clusgrp_status_offline_due_to_antiaffinity_conflict__64_0x040_"></span><span id="CLUSGRP_STATUS_OFFLINE_DUE_TO_ANTIAFFINITY_CONFLICT__64_0X040_"></span>**CLUSGRP\_STATUS\_OFFLINE\_DUE\_TO\_ANTIAFFINITY\_CONFLICT** (64=0x040)
</dt> <dd>

The group is offline because of an anti-affinity conflict.

</dd> <dt>

<span id="CLUSGRP_STATUS_NETWORK_FAILURE__128_0x080_"></span><span id="clusgrp_status_network_failure__128_0x080_"></span><span id="CLUSGRP_STATUS_NETWORK_FAILURE__128_0X080_"></span>**CLUSGRP\_STATUS\_NETWORK\_FAILURE** (128=0x080)
</dt> <dd>

The group has a network failure.

</dd> <dt>

<span id="CLUSGRP_STATUS_UNMONITORED__256_0x100_"></span><span id="clusgrp_status_unmonitored__256_0x100_"></span><span id="CLUSGRP_STATUS_UNMONITORED__256_0X100_"></span>**CLUSGRP\_STATUS\_UNMONITORED** (256=0x100)
</dt> <dd>

The group is no longer a member of a cluster.

**Windows Server 2012 R2 and Windows Server 2012:** This value is not supported before Windows Server 2016.

</dd> <dt>

<span id="CLUSGRP_STATUS_OS_HEARTBEAT__512_0x200_"></span><span id="clusgrp_status_os_heartbeat__512_0x200_"></span><span id="CLUSGRP_STATUS_OS_HEARTBEAT__512_0X200_"></span>**CLUSGRP\_STATUS\_OS\_HEARTBEAT** (512=0x200)
</dt> <dd>

The heartbeat is functioning.

**Windows Server 2012 R2 and Windows Server 2012:** This value is not supported before Windows Server 2016.

</dd> <dt>

<span id="CLUSGRP_STATUS_APPLICATION_READY__1024_0x400_"></span><span id="clusgrp_status_application_ready__1024_0x400_"></span><span id="CLUSGRP_STATUS_APPLICATION_READY__1024_0X400_"></span>**CLUSGRP\_STATUS\_APPLICATION\_READY** (1024=0x400)
</dt> <dd>

The application is ready

**Windows Server 2012 R2 and Windows Server 2012:** This value is not supported before Windows Server 2016.

</dd> </dl>

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Group Common Properties](group-common-properties.md)
</dt> </dl>

 

 





