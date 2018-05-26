---
Description: RSM performs several tasks at startup time.
ms.assetid: 0df87a69-39c7-4fdd-a710-1b5e269aca14
title: RSM Startup
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# RSM Startup

\[[Removable Storage Manager](removable-storage-manager.md) is no longer available as of Windows 7 and Windows Server 2008 R2.\]

RSM performs several tasks at startup time. During some of the tasks, RSM is unavailable for commands. At other times during startup, RSM may accept commands; however, the execution of the command may be delayed while RSM completes initialization. The following steps outline the process followed by RSM during startup. It is important to note that the process is the same when the service is restarted or the computer has been restarted.

1.  Build or reconfigure the RSM database based on the current device configuration.
2.  Mark all not completed work-items in the work queue as canceled.
3.  Start a thread to process requests for each library in the system.
4.  Each thread checks its configuration and performs a default inventory for its library. The inventory may result work items to identify media being placed on the library's work queue.
5.  Start accepting requests.
6.  Complete the default inventory work.

> [!Note]  
> Inventory will empty the drives if possible. If the drives are currently in use, RSM leaves the media in the drive and examines the media in the drive at a later time. Also, note that the inventory performed is the default inventory for the specified device which can be set to FULL, FAST, or NONE.

 

 

 



