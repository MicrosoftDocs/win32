---
title: Canceling the Current Restart Manager Operation
description: When a user action directs the installer to perform a different action, the following method can be used to cancel the current Restart Manager operation.
ms.assetid: 87c8cf27-cd77-46fb-8298-cccbf4b1071a
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Canceling the Current Restart Manager Operation

When a user action directs the installer to perform a different action, the following method can be used to cancel the current Restart Manager operation.

**To cancel the current Restart Manager operation**

-   The installer can call the [**RMCancelCurrentTask**](/windows/win32/RestartManager/nf-restartmanager-rmcancelcurrenttask?branch=master) function from another thread to cancel the current [**RmShutdown**](/windows/win32/RestartManager/nf-restartmanager-rmshutdown?branch=master) or [**RmRestart**](/windows/win32/RestartManager/nf-restartmanager-rmrestart?branch=master) operation. The Restart Manager may cancel the operation depending on the extent to which the operation has completed when the **RMCancelCurrentTask** function is called.

 

 




