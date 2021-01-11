---
description: File objects function as the logical interface between kernel and user-mode processes and the file data that resides on the physical disk.
ms.assetid: 53aabb35-4601-42d1-ac73-385473ff91e2
title: File Objects
ms.topic: article
ms.date: 05/31/2018
---

# File Objects

*File objects* function as the logical interface between kernel and user-mode processes and the file data that resides on the physical disk. A file object contains both the data written to the file and the following set of kernel-maintained attributes.



| Information type                                              | Purpose                                                                                                                                                                                         |
|---------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| File name                                                     | Names the corresponding physical file.                                                                                                                                                          |
| Current byte offset                                           | Used in synchronous file I/O (described later in this section) to identify the current starting location of read and write operations.                                                          |
| Share mode                                                    | Specifies whether a second process can open a file for read, write, or delete access while the initial process is still accessing it.                                                           |
| I/O mode                                                      | Specifies whether the initial process opened the file for [synchronous or asynchronous I/O](synchronous-and-asynchronous-i-o.md), cached or uncached I/O, sequential or random I/O, and so on. |
| Pointer to device object                                      | Identifies the physical device the file data resides on.                                                                                                                                        |
| Pointer to the volume parameter block, or [**VPB**](/windows-hardware/drivers/ddi/content/wdm/ns-wdm-_vpb) | Identifies the volume or partition the file data resides on.                                                                                                                                    |
| Pointer to section object pointers                            | Identifies a root structure that describes a [mapped file](/windows/desktop/Memory/file-mapping).                                                                                                                  |
| Pointer to private cache map                                  | Identifies the file data that is currently cached.                                                                                                                                              |



 

These attributes are defined as part of the [**FILE\_OBJECT**](/windows-hardware/drivers/ddi/content/wdm/ns-wdm-_file_object) structure in Ntddk.h. Refer to the definition of this structure in the Windows Driver Kit (WDK) documentation for the data lengths and types of the values.

 

 
