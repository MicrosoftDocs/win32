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
| [**ApplicationRecoveryFinished**](/windows/win32/Winbase/nf-winbase-applicationrecoveryfinished?branch=master)                     | Indicates that the calling application has completed its data recovery.                    |
| [**ApplicationRecoveryInProgress**](/windows/win32/Winbase/nf-winbase-applicationrecoveryinprogress?branch=master)                 | Indicates that the calling application is continuing to recover data.                      |
| [**GetApplicationRecoveryCallback**](/windows/win32/Winbase/nf-winbase-getapplicationrecoverycallback?branch=master)               | Retrieves a pointer to the recovery callback routine registered for the specified process. |
| [**GetApplicationRestartSettings**](/windows/win32/Winbase/nf-winbase-getapplicationrestartsettings?branch=master)                 | Retrieves the restart information registered for the specified process.                    |
| [**RegisterApplicationRecoveryCallback**](/windows/win32/Winbase/nf-winbase-registerapplicationrecoverycallback?branch=master)     | Registers the active instance of an application for recovery.                              |
| [**RegisterApplicationRestart**](/windows/win32/Winbase/nf-winbase-registerapplicationrestart?branch=master)                       | Registers the active instance of an application for restart.                               |
| [**UnregisterApplicationRecoveryCallback**](/windows/win32/Winbase/nf-winbase-unregisterapplicationrecoverycallback?branch=master) | Removes the active instance of an application from the recovery list.                      |
| [**UnregisterApplicationRestart**](/windows/win32/Winbase/nf-winbase-unregisterapplicationrestart?branch=master)                   | Removes the active instance of an application from the restart list.                       |



 

 

 




