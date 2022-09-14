---
title: Resources on a Remote Desktop Session Host Server
description: Multiple users can log on simultaneously to a single Remote Desktop Session Host (RD Session Host) server, sharing the hardware and software resources of the server.
ms.assetid: ab193a9f-7424-42bf-8cea-28628096edc6
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Resources on a Remote Desktop Session Host Server

In a Remote Desktop Services environment, multiple users can log on simultaneously to a single Remote Desktop Session Host (RD Session Host) server (formerly known as a terminal server). Consequently, the users are sharing the hardware and software resources of the server, which can create the following areas of contention:

-   CPU time. Each user has a desktop environment and can run whatever applications are available to that desktop. However, all applications run by all users are contending for the central CPU resources available on the RD Session Host server. If one user runs a poorly written, CPU-intensive application, other users might experience a visible loss of performance.
-   Disk access. Users contend for access to applications and related program files. In addition, users contend for disk accesses by the server operating system, such as loading DLLs or swapping memory between the paging file and physical memory.
-   Random Access Memory (RAM). Each application run by every user is contending for the RAM resources available on the RD Session Host server. If one user runs a memory-intensive application, other users might experience a loss of performance.
-   Network access. Network access is essential in a Remote Desktop Services environment because all desktop activity—graphical output and mouse/keyboard input—flows over the network links between the client desktop and the server. In addition, the users' applications running on the RD Session Host server contend for access to other network resources.
-   Server hardware. Hardware components such as CD-ROMs, floppy disk drives, serial ports, and parallel ports are often server based, not client based. Sharing these traditionally nonshared components creates new considerations for users and for applications that access these hardware components. For more information, see [Peripheral Hardware Guidelines](peripheral-hardware-guidelines.md).
-   Access to global objects and resources. In a Remote Desktop Services environment, users do not run individual copies of Windows—some of the core modules are cloned, but the remaining modules are shared among the users. Thus, users are competing for access to the registry, the paging file, system services, and other global objects and resources.

Many of the preceding points of contention can be mitigated by sizing the RD Session Host server with sufficient CPU, memory, and disk resources to handle the client demand. For example, a multiple processor configuration can maximize CPU availability. Memory availability can be maximized by installing extra physical memory (the increased memory limits for the Enterprise, Datacenter, or 64-bit editions of Windows Server can help). Finally, disk access performance can be maximized by configuring multiple channels and distributing your operating system and application loads across different physical drives. Properly configuring an RD Session Host server is a critical element of perceived application performance.

Although hardware sizing is an important part of creating a scalable Remote Desktop Services environment, the software considerations are equally important. In fact, fine-tuning an application often can do a lot to reduce resource competition and improve perceived application performance.

For more information about the Remote Desktop Services environment, see the following topics:

-   [Remote Desktop Services Programming Guidelines](terminal-services-programming-guidelines.md)
-   [Detecting the Remote Desktop Services Environment](detecting-the-terminal-services-environment.md)
-   [Detecting Whether the Remote Desktop Services Role Is Installed](detecting-whether-terminal-services-is-installed.md)
-   [Remote Desktop Services Sessions](terminal-services-sessions.md)

 

 




