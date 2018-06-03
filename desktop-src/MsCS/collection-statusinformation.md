---
title: StatusInformation
description: Contains information about the status of the groupset.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7FCD8E19-DCAA-429D-A21B-9725DE1B29D3
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- StatusInformation Failover Cluster
topic_type:
- apiref
api_name:
- StatusInformation
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# StatusInformation

Contains information about the status of the groupset.



| Attribute            | Value                                                                   |
|----------------------|-------------------------------------------------------------------------|
| Data type<br/> | **ULARGE\_INTEGER**<br/>                                          |
| Access<br/>    | [Read-only](read-only-properties.md)<br/>                        |
| Structure<br/> | [**CLUSPROP\_ULARGE\_INTEGER**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_ularge_integer)<br/> |
| Minimum<br/>   | 0<br/>                                                            |
| Maximum<br/>   | 8<br/>                                                            |
| Default<br/>   | 0<br/>                                                            |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_GROUPSET\_STATUS\_INFORMATION**.

This property can contain a bitwise combination of the following values.

<dl> <dt>

<span id="CLUSGRPGROUPSET_STATUS_GROUPS_PENDING__1_"></span><span id="clusgrpgroupset_status_groups_pending__1_"></span>**CLUSGRPGROUPSET\_STATUS\_GROUPS\_PENDING** (1)
</dt> <dd>

The groups are pending.

</dd> <dt>

<span id="CLUSGRPGROUPSET_STATUS_GROUPS_ONLINE__2_"></span><span id="clusgrpgroupset_status_groups_online__2_"></span>**CLUSGRPGROUPSET\_STATUS\_GROUPS\_ONLINE** (2)
</dt> <dd>

The groups are online.

</dd> <dt>

<span id="CLUSGRPGROUPSET_STATUS_OS_HEARTBEAT__4_"></span><span id="clusgrpgroupset_status_os_heartbeat__4_"></span>**CLUSGRPGROUPSET\_STATUS\_OS\_HEARTBEAT** (4)
</dt> <dd>

the heartbeat is functioning.

</dd> <dt>

<span id="CLUSGRPGROUPSET_STATUS_APPLICATION_READY__8_"></span><span id="clusgrpgroupset_status_application_ready__8_"></span>**CLUSGRPGROUPSET\_STATUS\_APPLICATION\_READY** (8)
</dt> <dd>

The application is ready.

</dd> </dl>

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2016<br/> |



## See also

<dl> <dt>

[Groupset Common Properties](collection-common-properties.md)
</dt> </dl>

 

 





