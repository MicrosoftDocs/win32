---
title: Application Recovery and Restart Functions
description: Application Recovery and Restart defines the following functions
ms.assetid: 17de24d1-32fe-4b2d-a224-3730af73c892
ms.topic: article
ms.date: 05/31/2018
---

# Application Recovery and Restart Functions

Application Recovery and Restart defines the following functions:



| Function                                                                               | Description                                                                                |
|----------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| [**ApplicationRecoveryFinished**](https://msdn.microsoft.com/library/Aa373328(v=VS.85).aspx)                     | Indicates that the calling application has completed its data recovery.                    |
| [**ApplicationRecoveryInProgress**](https://msdn.microsoft.com/library/Aa373329(v=VS.85).aspx)                 | Indicates that the calling application is continuing to recover data.                      |
| [**GetApplicationRecoveryCallback**](https://msdn.microsoft.com/library/Aa373343(v=VS.85).aspx)               | Retrieves a pointer to the recovery callback routine registered for the specified process. |
| [**GetApplicationRestartSettings**](https://msdn.microsoft.com/library/Aa373344(v=VS.85).aspx)                 | Retrieves the restart information registered for the specified process.                    |
| [**RegisterApplicationRecoveryCallback**](https://msdn.microsoft.com/library/Aa373345(v=VS.85).aspx)     | Registers the active instance of an application for recovery.                              |
| [**RegisterApplicationRestart**](https://msdn.microsoft.com/library/Aa373347(v=VS.85).aspx)                       | Registers the active instance of an application for restart.                               |
| [**UnregisterApplicationRecoveryCallback**](https://msdn.microsoft.com/library/Aa373348(v=VS.85).aspx) | Removes the active instance of an application from the recovery list.                      |
| [**UnregisterApplicationRestart**](https://msdn.microsoft.com/library/Aa373349(v=VS.85).aspx)                   | Removes the active instance of an application from the restart list.                       |



 

 

 




