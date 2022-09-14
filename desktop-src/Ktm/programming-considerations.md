---
description: "Learn more about: Programming Considerations For Writing Resource Managers"
ms.assetid: 7f1e61e8-15e1-4a25-b864-eeadcac61108
title: Programming Considerations For Writing Resource Managers
ms.topic: article
ms.date: 05/31/2018
---

# Programming Considerations For Writing Resource Managers

When using the Kernel Transaction Manager API to add transaction support to your applications, consider the following:

-   When you are writing your own resource manager, you should have a good, working knowledge of transaction management techniques and protocols.
-   If you do not write resource managers correctly, you can corrupt your own data with improperly handled recovery operations. You can also pin the tail of transaction log and fill up your file system with transaction logs.
-   If your log size policy is not set to prevent the log from increasing in size, your resource manager will not stop transactions. Your resource manager must stop updating the system so it does not overrun the file system resources.
-   Resource managers should use access control lists (ACLs) to control access to the log files; otherwise, denial of service attacks are possible.
-   Any resource manager or transaction participant that caches data must enlist for pre-prepare notifications. When a pre-prepare notification is received, you must flush all your data, so that any downstream resource managers can enlist before the prepare phase. Any further work in that transaction must not be cached.
-   Do not close an enlistment handle while the transaction is still active; this will cause the transaction to be rolled back.

 

 



