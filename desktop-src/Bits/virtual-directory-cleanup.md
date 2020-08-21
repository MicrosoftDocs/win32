---
title: Virtual Directory Cleanup
description: BITS extends IIS virtual directories to support uploads.
ms.assetid: 8214904e-8a95-4c4b-a1c5-91e84031587f
ms.topic: article
ms.date: 05/31/2018
---

# Virtual Directory Cleanup

BITS extends IIS virtual directories to support uploads. Each virtual directory has a session time-out property (the IIS [BITSSessionTimeout](bits-iis-extension-properties.md) metabase property) that specifies the period of time in which the BITS client must make progress in uploading the file. If no progress is made during that period (the timer is reset when progress is made), BITS closes the session. The default session time-out is 14 days.

BITS adds a work item to the [Task Scheduler](/windows/desktop/TaskSchd/task-scheduler-start-page) for each virtual directory you create and enable. The work item deletes resources associated with the closed sessions. By default, the cleanup occurs every 12 hours. If two virtual directories point to the same physical directory, the cleanup process initiated by one of the directories deletes the resources associated with all closed sessions in the physical directory.

Use the BITS Extension tab or the [Task Scheduler](/windows/desktop/TaskSchd/task-scheduler-start-page) interfaces to change the cleanup schedule as appropriate for your application. You can also call the [**IBITSExtensionSetup::GetCleanupTask**](/windows/desktop/api/Bitscfg/nf-bitscfg-ibitsextensionsetup-getcleanuptask) method to retrieve an interface pointer to the cleanup task associated with the virtual directory.

> [!Note]  
> If the Task Scheduler is disabled after the virtual directory is enabled, the virtual directory cleanup process will not work.

 

 

 