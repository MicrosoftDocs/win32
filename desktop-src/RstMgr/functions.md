---
title: Restart Manager Functions
description: The Restart Manager API uses the functions identified in the following table.
ms.assetid: abb78aa5-0487-4e99-85b6-adc38b600c09
keywords:
- Restart Manager Restart Mgr , reference, functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Restart Manager Functions

The Restart Manager API uses the functions identified in the following table.



| Function                                           | Description                                                                                                                                                                                  |
|----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**RmAddFilter**](/windows/win32/RestartManager/nf-restartmanager-rmaddfilter?branch=master)                 | Modifies shutdown or restart actions.                                                                                                                                                        |
| [**RmStartSession**](/windows/win32/RestartManager/nf-restartmanager-rmstartsession?branch=master)           | Starts a new Restart Manager session.                                                                                                                                                        |
| [**RmJoinSession**](/windows/win32/RestartManager/nf-restartmanager-rmjoinsession?branch=master)             | Joins the process of an application to an existing Restart Manager session.                                                                                                                  |
| [**RmEndSession**](/windows/win32/RestartManager/nf-restartmanager-rmendsession?branch=master)               | Ends the Restart Manager session.                                                                                                                                                            |
| [**RmRegisterResources**](/windows/win32/RestartManager/nf-restartmanager-rmregisterresources?branch=master) | Registers resources, such as filenames, service short names, or [**RM\_UNIQUE\_PROCESS**](/windows/win32/RestartManager/ns-restartmanager-_rm_unique_process?branch=master) structures, to a Restart Manager session.                                   |
| [**RmGetList**](/windows/win32/RestartManager/nf-restartmanager-rmgetlist?branch=master)                     | Used by installers to get a list of all applications affected by registered resources and their current status.                                                                              |
| [**RmGetFilterList**](/windows/win32/RestartManager/nf-restartmanager-rmgetfilterlist?branch=master)         | Queries the status of shutdown and restart modifications that have already been applied.                                                                                                     |
| [**RmShutdown**](/windows/win32/RestartManager/nf-restartmanager-rmshutdown?branch=master)                   | Initiates the shut down of applications and services.                                                                                                                                        |
| [**RmRemoveFilter**](/windows/win32/RestartManager/nf-restartmanager-rmremovefilter?branch=master)           | Removes shutdown and restart modifications that have already been applied.                                                                                                                   |
| [**RmRestart**](/windows/win32/RestartManager/nf-restartmanager-rmrestart?branch=master)                     | Restarts applications and services that have been shut down by the [**RmShutdown**](/windows/win32/RestartManager/nf-restartmanager-rmshutdown?branch=master) function and that have been registered for restart using **RegisterApplicationRestart**. |
| [**RmCancelCurrentTask**](/windows/win32/RestartManager/nf-restartmanager-rmcancelcurrenttask?branch=master) | Cancels the current [**RmGetList**](/windows/win32/RestartManager/nf-restartmanager-rmgetlist?branch=master), [**RmShutdown**](/windows/win32/RestartManager/nf-restartmanager-rmshutdown?branch=master), or [**RmRestart**](/windows/win32/RestartManager/nf-restartmanager-rmrestart?branch=master) function.                                                            |



 

 

 




