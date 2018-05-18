---
title: ReadySetting
description: Indicates what condition is used to indicate a group set is ready.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'D18E2572-F23A-4EE9-8727-23092B9BE92C'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["ReadySetting Failover Cluster"]
topic_type:
- apiref
api_name:
- ReadySetting
api_type:
- NA
---

# ReadySetting

Indicates what condition is used to indicate a group set is ready.



| Attribute            | Value                                                           |
|----------------------|-----------------------------------------------------------------|
| Data type<br/> | **DWORD**<br/>                                            |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>              |
| Structure<br/> | [**CLUSPROP\_DWORD**](clusprop-dword.md)<br/>            |
| Minimum<br/>   | **GROUPSET\_READY\_SETTING\_DELAY** (1)<br/>              |
| Maximum<br/>   | **GROUPSET\_READY\_SETTING\_APPLICATION\_READY** (4)<br/> |
| Default<br/>   | **GROUPSET\_READY\_SETTING\_ONLINE** (2)<br/>             |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_GROUPSET\_READY\_SETTING**.

The possible values for this property are:

-   **GROUPSET\_READY\_SETTING\_DELAY** (1)
-   **GROUPSET\_READY\_SETTING\_ONLINE** (2)
-   **GROUPSET\_READY\_SETTING\_OS\_HEARTBEAT** (3)
-   **GROUPSET\_READY\_SETTING\_APPLICATION\_READY** (4)

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2016<br/> |



## See also

<dl> <dt>

[Collection Common Properties](collection-common-properties.md)
</dt> </dl>

 

 





