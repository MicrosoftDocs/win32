---
title: NodeHighestVersion
description: Specifies the highest possible version of the Cluster service with which the node can join or communicate. The following table summarizes the attributes of the NodeHighestVersion property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '915ad936-1bd1-4402-8acc-32a58b8d41d2'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["NodeHighestVersion Failover Cluster ,for nodes", "NodeHighestVersion Failover Cluster"]
topic_type:
- apiref
api_name:
- NodeHighestVersion
api_type:
- NA
---

# NodeHighestVersion

Specifies the highest possible version of the [Cluster service](cluster-service.md) with which the [node](nodes.md) can join or communicate. The following table summarizes the attributes of the **NodeHighestVersion** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read-only](read-only-properties.md)     |
| Structure | [**CLUSPROP\_DWORD**](clusprop-dword.md) |
| Minimum   | 0x000100E0                                |
| Maximum   | 0xFFFFFFF                                 |
| Default   | Varies                                    |



 

## Remarks

The value of **NodeHighestVersion** is set when the Cluster service is installed or upgraded on a node. The upper 16 bits of the value store the version number, while the lower 16 bits describe the build number. For more information on how the Cluster service creates and uses version numbers, see [Version Compatibility](version-compatibility.md).

## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/> |



## See also

<dl> <dt>

[**NodeLowestVersion**](nodes-nodelowestversion.md)
</dt> <dt>

[**CLUSTERVERSIONINFO**](clusterversioninfo.md)
</dt> <dt>

[**GetClusterInformation**](getclusterinformation.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](clusprop-dword.md)
</dt> </dl>

 

 





