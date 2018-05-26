---
title: Application Recovery and Restart Functions
description: Application Recovery and Restart defines the following functions
ms.assetid: 17de24d1-32fe-4b2d-a224-3730af73c892
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Application Recovery and Restart Functions

Application Recovery and Restart defines the following functions:



| Function                                                                               | Description                                                                                |
|----------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| [**ApplicationRecoveryFinished**](applicationrecoveryfinished.md)                     | Indicates that the calling application has completed its data recovery.                    |
| [**ApplicationRecoveryInProgress**](applicationrecoveryinprogress.md)                 | Indicates that the calling application is continuing to recover data.                      |
| [**GetApplicationRecoveryCallback**](getapplicationrecoverycallback.md)               | Retrieves a pointer to the recovery callback routine registered for the specified process. |
| [**GetApplicationRestartSettings**](getapplicationrestartsettings.md)                 | Retrieves the restart information registered for the specified process.                    |
| [**RegisterApplicationRecoveryCallback**](registerapplicationrecoverycallback.md)     | Registers the active instance of an application for recovery.                              |
| [**RegisterApplicationRestart**](registerapplicationrestart.md)                       | Registers the active instance of an application for restart.                               |
| [**UnregisterApplicationRecoveryCallback**](unregisterapplicationrecoverycallback.md) | Removes the active instance of an application from the recovery list.                      |
| [**UnregisterApplicationRestart**](unregisterapplicationrestart.md)                   | Removes the active instance of an application from the restart list.                       |



 

 

 




