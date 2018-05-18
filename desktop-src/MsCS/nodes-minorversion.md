---
title: MinorVersion
description: Specifies the decimal component of the version of the operating system installed on the node. The following table summarizes the attributes of the MinorVersion property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'e7c80ad0-a88a-4d8b-90a8-7891468f911d'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["MinorVersion Failover Cluster ,for nodes", "MinorVersion Failover Cluster"]
topic_type:
- apiref
api_name:
- MinorVersion
api_type:
- NA
---

# MinorVersion

Specifies the decimal component of the version of the operating system installed on the [node](nodes.md). The following table summarizes the attributes of the **MinorVersion** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read-only](read-only-properties.md)     |
| Structure | [**CLUSPROP\_DWORD**](clusprop-dword.md) |
| Minimum   | 0x00000000                                |
| Maximum   | 0xFFFFFFF                                 |
| Default   | Varies                                    |



 

## Remarks

The [**MajorVersion**](nodes-majorversion.md) and **MinorVersion** properties represent a version number in the following form: **MajorVersion**. **MinorVersion**. Further version information is provided by the [**CSDVersion**](nodes-csdversion.md) and [**BuildNumber**](nodes-buildnumber.md) properties.

Note that the [**MajorVersion**](nodes-majorversion.md) and **MinorVersion** properties refer to the version of the system installed on the node, while the [**NodeHighestVersion**](nodes-nodehighestversion.md) property describes the version of the [Cluster service](cluster-service.md) installed on the node.

For information about the values in OS version numbers, see [OSVERSIONINFOEX](https://msdn.microsoft.com/library/windows/desktop/ms724833.aspx).

## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/> |



 

 





