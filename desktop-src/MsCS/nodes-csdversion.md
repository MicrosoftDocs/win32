---
title: CSDVersion
description: Specifies the name of the most recent service pack installed on the node (if any). The following table summarizes the attributes of the CSDVersion property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 54338636-e4bf-4cb9-84bd-5a04143ccd90
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CSDVersion Failover Cluster ,for nodes
- CSDVersion Failover Cluster
topic_type:
- apiref
api_name:
- CSDVersion
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CSDVersion

Specifies the name of the most recent service pack installed on the [node](nodes.md) (if any). The following table summarizes the attributes of the **CSDVersion** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | Null-terminated Unicode string                                   |
| Access    | [Read-only](read-only-properties.md)                            |
| Structure | [**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)                              |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | **NULL**                                                         |



 

## Remarks

The version of the operating system installed on a node is fully described by the following properties:

-   [**MajorVersion**](nodes-majorversion.md)
-   [**MinorVersion**](nodes-minorversion.md)
-   [**BuildNumber**](nodes-buildnumber.md)

For information about the values in OS version numbers, see [OSVERSIONINFOEX](https://msdn.microsoft.com/library/windows/desktop/ms724833.aspx).

## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/> |



 

 





