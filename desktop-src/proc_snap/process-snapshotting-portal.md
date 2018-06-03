---
title: Process Snapshotting
description: .
ms.assetid: 1dc6fe86-3f5a-4810-8e93-a0fe309c54ee
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Process Snapshotting

## Purpose

Process snapshotting enables you to capture process state, in part or whole. It is similar to the [Tool Help](https://msdn.microsoft.com/library/windows/desktop/ms686837) API, but with one important advantage: it can efficiently capture the virtual address contents of a process using the Windows internal POSIX fork clone capability. The process snapshot can be dumped into a file using the [**MiniDumpWriteDump**](https://msdn.microsoft.com/library/windows/desktop/ms680360) function. For more information, see [Generate Dump File from a Process Snapshot](export-a-process-snapshot-to-a-file.md).

## Developer audience

Process Snapshotting is designed for use by C/C++ developers.

## Run-time requirements

Process Snapshotting is included in Windows 8.1 and Windows Server 2012 R2 operating systems.

## In this section



| Topic                                                                                            | Description                                                        |
|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| [Overview of Process Snapshotting](overview-of-process-snapshotting.md)<br/>              | General information about Process Snapshotting.<br/>         |
| [Generate Dump File from a Process Snapshot](export-a-process-snapshot-to-a-file.md)<br/> | You can generate a process snapshot dump file.<br/>          |
| [Process Snapshotting Reference](process-snapshotting-reference.md)<br/>                  | Reference information for the Process Snapshotting API.<br/> |



 

 

 





