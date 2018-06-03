---
title: Application Recovery and Restart Functions
description: Application Recovery and Restart defines the following functions
ms.assetid: 17de24d1-32fe-4b2d-a224-3730af73c892
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Application Recovery and Restart Functions

Application Recovery and Restart defines the following functions:



| Function                                                                               | Description                                                                                |
|----------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| [**ApplicationRecoveryFinished**](/windows/desktop/api/Winbase/nf-winbase-applicationrecoveryfinished)                     | Indicates that the calling application has completed its data recovery.                    |
| [**ApplicationRecoveryInProgress**](/windows/desktop/api/Winbase/nf-winbase-applicationrecoveryinprogress)                 | Indicates that the calling application is continuing to recover data.                      |
| [**GetApplicationRecoveryCallback**](/windows/desktop/api/Winbase/nf-winbase-getapplicationrecoverycallback)               | Retrieves a pointer to the recovery callback routine registered for the specified process. |
| [**GetApplicationRestartSettings**](/windows/desktop/api/Winbase/nf-winbase-getapplicationrestartsettings)                 | Retrieves the restart information registered for the specified process.                    |
| [**RegisterApplicationRecoveryCallback**](/windows/desktop/api/Winbase/nf-winbase-registerapplicationrecoverycallback)     | Registers the active instance of an application for recovery.                              |
| [**RegisterApplicationRestart**](/windows/desktop/api/Winbase/nf-winbase-registerapplicationrestart)                       | Registers the active instance of an application for restart.                               |
| [**UnregisterApplicationRecoveryCallback**](/windows/desktop/api/Winbase/nf-winbase-unregisterapplicationrecoverycallback) | Removes the active instance of an application from the recovery list.                      |
| [**UnregisterApplicationRestart**](/windows/desktop/api/Winbase/nf-winbase-unregisterapplicationrestart)                   | Removes the active instance of an application from the restart list.                       |



 

 

 




