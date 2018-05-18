---
title: StatusInformation
description: Contains information about the status of the resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'D487754E-3B54-4DE4-AF5A-2B0CA58EE718'
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

Contains information about the status of the resource.



| Attribute            | Value                                                                   |
|----------------------|-------------------------------------------------------------------------|
| Data type<br/> | Long unsigned integer<br/>                                        |
| Access<br/>    | [Read-only](read-only-properties.md)<br/>                        |
| Structure<br/> | [**CLUSPROP\_ULARGE\_INTEGER**](clusprop-ularge-integer.md)<br/> |
| Minimum<br/>   | 0 (0x0000000000000000)<br/>                                       |
| Maximum<br/>   | 31 (0x000000000000001F)<br/>                                      |
| Default<br/>   | 0<br/>                                                            |



 

## Remarks

This property can contain a bitwise combination of the following values:

<dl> <dt>

<span id="CLUSRES_STATUS_LOCKED_MODE__1_0x001_"></span><span id="clusres_status_locked_mode__1_0x001_"></span><span id="CLUSRES_STATUS_LOCKED_MODE__1_0X001_"></span>**CLUSRES\_STATUS\_LOCKED\_MODE** (1=0x001)
</dt> <dd>

The resource is locked.

</dd> <dt>

<span id="CLUSRES_STATUS_EMBEDDED_FAILURE__2_0x002_"></span><span id="clusres_status_embedded_failure__2_0x002_"></span><span id="CLUSRES_STATUS_EMBEDDED_FAILURE__2_0X002_"></span>**CLUSRES\_STATUS\_EMBEDDED\_FAILURE** (2=0x002)
</dt> <dd>

The resource has an embedded failure.

</dd> <dt>

<span id="CLUSRES_STATUS_FAILED_DUE_TO_INSUFFICIENT_CPU__4_0x004_"></span><span id="clusres_status_failed_due_to_insufficient_cpu__4_0x004_"></span><span id="CLUSRES_STATUS_FAILED_DUE_TO_INSUFFICIENT_CPU__4_0X004_"></span>**CLUSRES\_STATUS\_FAILED\_DUE\_TO\_INSUFFICIENT\_CPU** (4=0x004)
</dt> <dd>

The resource has failed because of insufficient CPU.

</dd> <dt>

<span id="CLUSRES_STATUS_FAILED_DUE_TO_INSUFFICIENT_MEMORY__8_0x008_"></span><span id="clusres_status_failed_due_to_insufficient_memory__8_0x008_"></span><span id="CLUSRES_STATUS_FAILED_DUE_TO_INSUFFICIENT_MEMORY__8_0X008_"></span>**CLUSRES\_STATUS\_FAILED\_DUE\_TO\_INSUFFICIENT\_MEMORY** (8=0x008)
</dt> <dd>

The resource has failed because of insufficient memory.

</dd> <dt>

<span id="CLUSRES_STATUS_FAILED_DUE_TO_INSUFFICIENT_GENERIC_RESOURCES__16_0x010_"></span><span id="clusres_status_failed_due_to_insufficient_generic_resources__16_0x010_"></span><span id="CLUSRES_STATUS_FAILED_DUE_TO_INSUFFICIENT_GENERIC_RESOURCES__16_0X010_"></span>**CLUSRES\_STATUS\_FAILED\_DUE\_TO\_INSUFFICIENT\_GENERIC\_RESOURCES** (16=0x010)
</dt> <dd>

The resource has failed because of insufficient generic resources.

</dd> <dt>

<span id="CLUSRES_STATUS_NETWORK_FAILURE__32_0x020_"></span><span id="clusres_status_network_failure__32_0x020_"></span><span id="CLUSRES_STATUS_NETWORK_FAILURE__32_0X020_"></span>**CLUSRES\_STATUS\_NETWORK\_FAILURE** (32=0x020)
</dt> <dd>

The resource has a network failure.

**Windows Server 2012:** This value is not supported until Windows Server 2012 R2.

</dd> <dt>

<span id="CLUSRES_STATUS_UNMONITORED__64_0x040_"></span><span id="clusres_status_unmonitored__64_0x040_"></span><span id="CLUSRES_STATUS_UNMONITORED__64_0X040_"></span>**CLUSRES\_STATUS\_UNMONITORED** (64=0x040)
</dt> <dd>

The resource is no longer a member of a cluster.

**Windows Server 2012 R2 and Windows Server 2012:** This value is not supported until Windows Server 2016.

</dd> <dt>

<span id="CLUSRES_STATUS_OS_HEARTBEAT__128_0x080_"></span><span id="clusres_status_os_heartbeat__128_0x080_"></span><span id="CLUSRES_STATUS_OS_HEARTBEAT__128_0X080_"></span>**CLUSRES\_STATUS\_OS\_HEARTBEAT** (128=0x080)
</dt> <dd>

The heartbeat is functioning.

**Windows Server 2012 R2 and Windows Server 2012:** This value is not supported until Windows Server 2016.

</dd> <dt>

<span id="CLUSRES_STATUS_APPLICATION_READY__256_0x100_"></span><span id="clusres_status_application_ready__256_0x100_"></span><span id="CLUSRES_STATUS_APPLICATION_READY__256_0X100_"></span>**CLUSRES\_STATUS\_APPLICATION\_READY** (256=0x100)
</dt> <dd>

The application is ready.

**Windows Server 2012 R2 and Windows Server 2012:** This value is not supported until Windows Server 2016.

</dd> </dl>

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Resource Common Properties](resource-common-properties.md)
</dt> </dl>

 

 





