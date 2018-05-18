---
title: Restart Manager Functions
description: The Restart Manager API uses the functions identified in the following table.
ms.assetid: 'abb78aa5-0487-4e99-85b6-adc38b600c09'
keywords: ["Restart Manager Restart Mgr , reference, functions"]
---

# Restart Manager Functions

The Restart Manager API uses the functions identified in the following table.



| Function                                           | Description                                                                                                                                                                                  |
|----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**RmAddFilter**](rmaddfilter.md)                 | Modifies shutdown or restart actions.                                                                                                                                                        |
| [**RmStartSession**](rmstartsession.md)           | Starts a new Restart Manager session.                                                                                                                                                        |
| [**RmJoinSession**](rmjoinsession.md)             | Joins the process of an application to an existing Restart Manager session.                                                                                                                  |
| [**RmEndSession**](rmendsession.md)               | Ends the Restart Manager session.                                                                                                                                                            |
| [**RmRegisterResources**](rmregisterresources.md) | Registers resources, such as filenames, service short names, or [**RM\_UNIQUE\_PROCESS**](rm-unique-process.md) structures, to a Restart Manager session.                                   |
| [**RmGetList**](rmgetlist.md)                     | Used by installers to get a list of all applications affected by registered resources and their current status.                                                                              |
| [**RmGetFilterList**](rmgetfilterlist.md)         | Queries the status of shutdown and restart modifications that have already been applied.                                                                                                     |
| [**RmShutdown**](rmshutdown.md)                   | Initiates the shut down of applications and services.                                                                                                                                        |
| [**RmRemoveFilter**](rmremovefilter.md)           | Removes shutdown and restart modifications that have already been applied.                                                                                                                   |
| [**RmRestart**](rmrestart.md)                     | Restarts applications and services that have been shut down by the [**RmShutdown**](rmshutdown.md) function and that have been registered for restart using **RegisterApplicationRestart**. |
| [**RmCancelCurrentTask**](rmcancelcurrenttask.md) | Cancels the current [**RmGetList**](rmgetlist.md), [**RmShutdown**](rmshutdown.md), or [**RmRestart**](rmrestart.md) function.                                                            |



 

 

 




