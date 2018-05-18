---
title: Security Functions
description: The network management security functions get and set security descriptors for DFS domain-based and stand-alone roots.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '90860842-0f4d-49ad-b835-50305328a050'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-distributed-file-system-(dfs)'
ms.tgt_platform: multiple
keywords: ["Distributed File System Files , security functions", "security functions Files"]
---

# Security Functions

The network management security functions get and set security descriptors for DFS domain-based and stand-alone roots.

The DFS security functions are listed following.



| Function                                                               | Description                                                                                                          |
|------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| [**NetDfsGetSecurity**](netdfsgetsecurity.md)                         | Obtains the security descriptor for the root object of the specified DFS root.                                       |
| [**NetDfsSetSecurity**](netdfssetsecurity.md)                         | Locates the root object for the specified DFS root and sets the supplied security descriptor on it.                  |
| [**NetDfsGetStdContainerSecurity**](netdfsgetstdcontainersecurity.md) | Obtains the security descriptor for the container object of the specified DFS stand-alone root.                      |
| [**NetDfsSetStdContainerSecurity**](netdfssetstdcontainersecurity.md) | Locates the container object for the specified DFS stand-alone root and sets the supplied security descriptor on it. |
| [**NetDfsGetFtContainerSecurity**](netdfsgetftcontainersecurity.md)   | Obtains the security descriptor for the container object of the specified DFS domain root.                           |
| [**NetDfsSetFtContainerSecurity**](netdfssetftcontainersecurity.md)   | Locates the container object for the specified DFS domain root and sets the supplied security descriptor on it.      |



 

 

 




