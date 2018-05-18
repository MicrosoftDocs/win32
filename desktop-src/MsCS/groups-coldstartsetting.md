---
title: ColdStartSetting
description: Specifies the cold start settings for a group cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '511DB0A7-B17F-40D2-B672-B027B57142A0'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["ColdStartSetting Failover Cluster"]
topic_type:
- apiref
api_name:
- ColdStartSetting
api_type:
- NA
---

# ColdStartSetting

Specifies the cold start settings for a group cluster.



| Attribute            | Value                                                |
|----------------------|------------------------------------------------------|
| Data type<br/> | **DWORD**                                            |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>   |
| Structure<br/> | [**CLUSPROP\_DWORD**](clusprop-dword.md)<br/> |
| Minimum<br/>   | **CLUS\_GROUP\_START\_ALWAYS** (0)<br/>        |
| Maximum<br/>   | **CLUS\_GROUP\_START\_ALLOWED** (2)<br/>       |
| Default<br/>   | **CLUS\_GROUP\_START\_ALWAYS** (0)<br/>        |



 

## Remarks

The data for the **ColdStartSetting** property can be set to one of the following values of the [**CLUS\_GROUP\_START\_SETTING**](clus-group-start-setting.md) enumeration.



| Name                                       | Value        | Description                            |
|--------------------------------------------|--------------|----------------------------------------|
| **CLUS\_GROUP\_START\_ALWAYS**<br/>  | 0<br/> | Always start the cluster.<br/>   |
| **CLUS\_GROUP\_DO\_NOT\_START**<br/> | 1<br/> | Do not start the cluster.<br/>   |
| **CLUS\_GROUP\_START\_ALLOWED**<br/> | 2<br/> | The cluster can be started.<br/> |



 

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                            |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Group Common Properties](group-common-properties.md)
</dt> </dl>

 

 





