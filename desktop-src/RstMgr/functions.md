---
title: Restart Manager Functions
description: The Restart Manager API uses the functions identified in the following table.
ms.assetid: 'ed39695a-1eb6-42fe-87a0-bd690bbce028'
keywords:
- Restart Manager Restart Mgr , reference, functions
ms.topic: article
ms.date: 05/31/2018
---

# Restart Manager Functions

The Restart Manager API uses the functions identified in the following table.



| Function                                           | Description                                                                                                                                                                                  |
|----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**RmAddFilter**](/windows/desktop/api/RestartManager/nf-restartmanager-rmaddfilter)                 | Modifies shutdown or restart actions.                                                                                                                                                        |
| [**RmStartSession**](/windows/desktop/api/RestartManager/nf-restartmanager-rmstartsession)           | Starts a new Restart Manager session.                                                                                                                                                        |
| [**RmJoinSession**](/windows/desktop/api/RestartManager/nf-restartmanager-rmjoinsession)             | Joins the process of an application to an existing Restart Manager session.                                                                                                                  |
| [**RmEndSession**](/windows/desktop/api/RestartManager/nf-restartmanager-rmendsession)               | Ends the Restart Manager session.                                                                                                                                                            |
| [**RmRegisterResources**](/windows/desktop/api/RestartManager/nf-restartmanager-rmregisterresources) | Registers resources, such as filenames, service short names, or [**RM\_UNIQUE\_PROCESS**](/windows/desktop/api/RestartManager/ns-restartmanager-rm_unique_process) structures, to a Restart Manager session.                                   |
| [**RmGetList**](/windows/desktop/api/RestartManager/nf-restartmanager-rmgetlist)                     | Used by installers to get a list of all applications affected by registered resources and their current status.                                                                              |
| [**RmGetFilterList**](/windows/desktop/api/RestartManager/nf-restartmanager-rmgetfilterlist)         | Queries the status of shutdown and restart modifications that have already been applied.                                                                                                     |
| [**RmShutdown**](/windows/desktop/api/RestartManager/nf-restartmanager-rmshutdown)                   | Initiates the shut down of applications and services.                                                                                                                                        |
| [**RmRemoveFilter**](/windows/desktop/api/RestartManager/nf-restartmanager-rmremovefilter)           | Removes shutdown and restart modifications that have already been applied.                                                                                                                   |
| [**RmRestart**](/windows/desktop/api/RestartManager/nf-restartmanager-rmrestart)                     | Restarts applications and services that have been shut down by the [**RmShutdown**](/windows/desktop/api/RestartManager/nf-restartmanager-rmshutdown) function and that have been registered for restart using **RegisterApplicationRestart**. |
| [**RmCancelCurrentTask**](/windows/desktop/api/RestartManager/nf-restartmanager-rmcancelcurrenttask) | Cancels the current [**RmGetList**](/windows/desktop/api/RestartManager/nf-restartmanager-rmgetlist), [**RmShutdown**](/windows/desktop/api/RestartManager/nf-restartmanager-rmshutdown), or [**RmRestart**](/windows/desktop/api/RestartManager/nf-restartmanager-rmrestart) function.                                                            |



 

 

 




