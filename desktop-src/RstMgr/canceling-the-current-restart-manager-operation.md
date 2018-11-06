---
title: Canceling the Current Restart Manager Operation
description: When a user action directs the installer to perform a different action, the following method can be used to cancel the current Restart Manager operation.
ms.assetid: 87c8cf27-cd77-46fb-8298-cccbf4b1071a
ms.topic: article
ms.date: 05/31/2018
---

# Canceling the Current Restart Manager Operation

When a user action directs the installer to perform a different action, the following method can be used to cancel the current Restart Manager operation.

**To cancel the current Restart Manager operation**

-   The installer can call the [**RMCancelCurrentTask**](/windows/desktop/api/RestartManager/nf-restartmanager-rmcancelcurrenttask) function from another thread to cancel the current [**RmShutdown**](/windows/desktop/api/RestartManager/nf-restartmanager-rmshutdown) or [**RmRestart**](/windows/desktop/api/RestartManager/nf-restartmanager-rmrestart) operation. The Restart Manager may cancel the operation depending on the extent to which the operation has completed when the **RMCancelCurrentTask** function is called.

 

 




