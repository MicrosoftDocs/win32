---
title: Application Recovery and Restart
description: Write custom installers to automatically restart an application that has been shut down to complete an update. Save data and configure application recovery before exiting programs.
ms.assetid: 60b057dd-9724-4bc4-b1b0-eea7e8380ecb
keywords:
- restart
- recover
- recovery
- reliability
- software reliability
- application recovery
- application restart
ms.topic: article
ms.date: 05/31/2018
---

# Application Recovery and Restart

## Purpose

An application can use Application Recovery and Restart (ARR) to save data and state information before the application exits due to an unhandled exception or when the application stops responding. The application is also restarted, if requested.

An application can also be restarted if an installer updates a component of the application, or if the computer needs to restart as the result of an update. Note that to support automatic application restart after an installer updates an application, both the application and installer need to be authored appropriately. For details, see [Registering for Application Restart](registering-for-application-restart.md).

## Developer audience

ARR is designed for C and C++ developers.

## Run-time requirements

ARR is available starting with the Windows Vista operating system.

## In this section



| Topic                                                                                                   | Description                                                           |
|---------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| [Using Application Recovery and Restart](using-application-recovery-and-restart.md)<br/>         | Procedural guide for registering for recovery and restart.<br/> |
| [Application Recovery and Restart Reference](application-recovery-and-restart-reference.md)<br/> | Reference information for the ARR API. <br/>                    |



 

 

 





