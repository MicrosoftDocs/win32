---
title: Security Functions
description: The network management security functions get and set security descriptors for DFS domain-based and stand-alone roots.
ms.assetid: 90860842-0f4d-49ad-b835-50305328a050
ms.topic: article
ms.date: 05/31/2018
---

# Security Functions

The network management security functions get and set security descriptors for DFS domain-based and stand-alone roots.

The DFS security functions are listed following.

| Function                                                               | Description                                                                                                          |
|------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| [**NetDfsGetSecurity**](/windows/desktop/api/lmdfs/nf-lmdfs-netdfsgetsecurity)                         | Obtains the security descriptor for the root object of the specified DFS root.                                       |
| [**NetDfsSetSecurity**](/windows/desktop/api/lmdfs/nf-lmdfs-netdfssetsecurity)                         | Locates the root object for the specified DFS root and sets the supplied security descriptor on it.                  |
| [**NetDfsGetStdContainerSecurity**](/windows/desktop/api/lmdfs/nf-lmdfs-netdfssetftcontainersecurity) | Obtains the security descriptor for the container object of the specified DFS stand-alone root.                      |
| [**NetDfsSetStdContainerSecurity**](/windows/desktop/api/lmdfs/nf-lmdfs-netdfssetstdcontainersecurity) | Locates the container object for the specified DFS stand-alone root and sets the supplied security descriptor on it. |
| [**NetDfsGetFtContainerSecurity**](/windows/desktop/api/lmdfs/nf-lmdfs-netdfsgetftcontainersecurity)   | Obtains the security descriptor for the container object of the specified DFS domain root.                           |
| [**NetDfsSetFtContainerSecurity**](/windows/desktop/api/lmdfs/nf-lmdfs-netdfssetftcontainersecurity)   | Locates the container object for the specified DFS domain root and sets the supplied security descriptor on it.      |
