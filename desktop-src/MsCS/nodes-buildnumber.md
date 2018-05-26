---
title: BuildNumber
description: Specifies the build number of the version of the operating system installed on a node. The following table summarizes the attributes of the BuildNumber property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6e9d369e-c74a-4b8f-9af3-3a739f50239c
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- BuildNumber Failover Cluster ,for nodes
- BuildNumber Failover Cluster
topic_type:
- apiref
api_name:
- BuildNumber
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# BuildNumber

Specifies the build number of the version of the operating system installed on a [node](nodes.md). The following table summarizes the attributes of the **BuildNumber** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read-only](read-only-properties.md)     |
| Structure | [**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master) |
| Minimum   | 0x00000000                                |
| Maximum   | 0xFFFFFFF                                 |
| Default   | Varies                                    |



 

## Remarks

The version of the operating system installed on a node is fully described by the following properties:

-   [**MajorVersion**](nodes-majorversion.md)
-   [**MinorVersion**](nodes-minorversion.md)
-   [**CSDVersion**](nodes-csdversion.md)

For information about the values in OS version numbers, see [OSVERSIONINFOEX](https://msdn.microsoft.com/library/windows/desktop/ms724833.aspx).

## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/> |



 

 





