---
title: MajorVersion
description: Specifies the integer component of the version of the operating system installed on the node. The following table summarizes the attributes of the MajorVersion property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9bd16289-e98a-4a8b-92cc-ee37d6f9f059
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- MajorVersion Failover Cluster ,for nodes
- MajorVersion Failover Cluster
topic_type:
- apiref
api_name:
- MajorVersion
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MajorVersion

Specifies the integer component of the version of the operating system installed on the [node](nodes.md). The following table summarizes the attributes of the **MajorVersion** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read-only](read-only-properties.md)     |
| Structure | [**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master) |
| Minimum   | 0x00000004                                |
| Maximum   | 0xFFFFFFF                                 |
| Default   | Varies                                    |



 

## Remarks

The **MajorVersion** and [**MinorVersion**](nodes-minorversion.md) properties represent a version number of the following form: **MajorVersion**.**MinorVersion**. Further version information is provided by the [**CSDVersion**](nodes-csdversion.md) and [**BuildNumber**](nodes-buildnumber.md) properties.

Note that the **MajorVersion** and [**MinorVersion**](nodes-minorversion.md) properties refer to the version of the operating system installed on the node, while the [**NodeHighestVersion**](nodes-nodehighestversion.md) property describes the version of the [Cluster service](cluster-service.md) installed on the node.

For information about the values in OS version numbers, see [OSVERSIONINFOEX](https://msdn.microsoft.com/library/windows/desktop/ms724833.aspx).

## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/> |



 

 





