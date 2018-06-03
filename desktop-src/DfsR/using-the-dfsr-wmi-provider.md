---
title: Using DFSR
description: How to use the DFSR WMI Classes to configure and monitor the DFSR service.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 10892d08-ffdb-44f0-ad02-b22769d60224
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-replication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Distributed File System Replication Files , using
- Distributed File System Replication examples Files
- examples Files
- Distributed File System Replication Files , examples See Distributed File System Replication examples
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using DFSR

The following sections describe how to use the [DFSR WMI Classes](dfsr-wmi-classes.md) to configure and monitor the DFSR service.

To understand the examples in this section, you may need to refer to the [WMI documentation](https://msdn.microsoft.com/library/aa394582), as well as the [Windows Script Host](http://go.microsoft.com/fwlink/p/?linkid=109686) documentation.

Note that it is also possible to perform certain simple tasks using the Windows Management Instrumentation Command-line (WMIC) utility. For example, you can configure the debug log severity by typing the following:

**Wmic /node:"my-machine" /namespace:\\\\root\\microsoftdfs path dfsrmachineconfig set enabledebuglog-true,debuglogseverity=5**

This section also contains detailed scripts to perform the following tasks:

-   [Polling the Active Directory for Configuration Changes](polling-the-active-directory-for-configuration-changes.md)
-   [Displaying and Changing DFSR Local Computer Settings](displaying-and-changing-dfsr-machine-configuration-settings.md)
-   [Getting the ID Record for a File or Folder](getting-the-id-record-for-a-file-or-folder.md)
-   [Getting Replication Backlog Information](getting-replication-backlog-information.md)
-   [Finding the Server that Originated a File or Folder Update](finding-the-server-that-originated-a-file-or-folder-update.md)

 

 




