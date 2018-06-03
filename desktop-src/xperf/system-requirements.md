---
title: System Requirements
description: System Requirements
ms.assetid: 868dcf8e-a9c1-4ed4-af6a-86b06c54de2a
keywords:
- operating system
- system memory
- compatibility
- disk
- processor
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# System Requirements

The following table lists system requirements for installing and running Windows Performance Analyzer.



|                              |                                                                                                                                                                                                                                                                                                                                              |
|------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Operating System <br/> | The minimum versions of the operating system versions are either Windows Vista SP1 or Windows Server 2008.<br/> For Windows XP SP2 and Windows Server 2003 SP1 support, please see the note on regarding XP in the [Installation](installation.md) section of this document.<br/>                                               |
| System Memory <br/>    | A minimum of 1 GB is required to run WPA. 2 GB or more is recommended for trace files larger than 500 MB. Please see the [Sessions](sessions.md) section of this document to understand how memory is allocated.<br/>                                                                                                                 |
| Disk <br/>             | The WPA collection of files is approximately 50 MB. The most important consideration for disk usage is to understand that WPA dumps memory buffers directly to disk. Consequently, the more trace information requested, the larger the resulting files. It is not unusual for trace files to be produced in the gigabyte ranges.<br/> |
| Processor <br/>        | Currently supported processor architectures are x86, IA64 and x64.<br/>                                                                                                                                                                                                                                                                |



 

 

 





