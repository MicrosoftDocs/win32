---
title: DFSR WMI Provider Overview
description: The DFSR WMI provider defines classes for configuring and monitoring the DFSR service. Using these classes, you can create your own tools to perform DFSR service administration tasks.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'fa6028ac-5236-4c0e-8097-21ef5bcd7720'
ms.prod: 'windows-server-dev'
ms.technology:
- 'distributed-file-system-replication'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Distributed File System Replication Files , WMI provider", "WMI provider for Distributed File System Replication Files"]
---

# DFSR WMI Provider Overview

A provider is an architectural element of Windows Management Instrumentation (WMI). WMI defines a unified architecture for describing, accessing, and instrumenting objects. Part of this architecture is a large database of WMI classes used to carry out remote management tasks on specific objects.

The DFSR WMI provider defines classes for configuring and monitoring the DFSR service. Using these classes, you can create your own tools to perform DFSR service administration tasks, such as the following:

-   Polling the Active Directory for configuration changes and applying any changes to the DFSR service
-   Applying a fence to a specific file or directory
-   Setting the minimum NTFS journal size
-   Retrieving the number of files scheduled to be replicated to an outbound partner
-   Performing external conflict resolution handling such as forcing a particular version of a file or folder to be replicated
-   Finding the server that originated a file or folder update

The DFSR WMI provider has a set of unique behaviors not found in other providers. For class details, see [DFSR WMI Classes](dfsr-wmi-classes.md).

 

 




