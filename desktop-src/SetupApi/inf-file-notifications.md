---
Description: The following notifications are used with the SetupInstallFile, SetupInstallFileEx, and SetupInstallFromInfSection functions. For more information about the format and use of notifications, see Notifications.
ms.assetid: 095cf4c9-3cb9-4b95-a8a2-9312c134e721
title: INF File Notifications
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# INF File Notifications

The following notifications are used with the [**SetupInstallFile**](/windows/win32/Setupapi/nf-setupapi-setupinstallfilea?branch=master), [**SetupInstallFileEx**](/windows/win32/Setupapi/nf-setupapi-setupinstallfileexa?branch=master), and [**SetupInstallFromInfSection**](/windows/win32/Setupapi/nf-setupapi-setupinstallfrominfsectiona?branch=master) functions. For more information about the format and use of notifications, see [Notifications](notifications.md).



| Notification                                                      | Description                                                                            |
|-------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| [**SPFILENOTIFY\_FILEOPDELAYED**](spfilenotify-fileopdelayed.md) | The file is in use, and the current operation is delayed until the system is rebooted. |
| [**SPFILENOTIFY\_LANGMISMATCH**](spfilenotify-langmismatch.md)   | The language of the current file does not match the system language.                   |
| [**SPFILENOTIFY\_TARGETEXISTS**](spfilenotify-targetexists.md)   | A copy of the specified file already exists on the target.                             |
| [**SPFILENOTIFY\_TARGETNEWER**](spfilenotify-targetnewer.md)     | A newer version of the specified file exists on the target.                            |



 

> [!Note]  
> Because [**SetupInstallFromInfSection**](/windows/win32/Setupapi/nf-setupapi-setupinstallfrominfsectiona?branch=master) creates and commits an internal file queue, it also uses the [File Queue Notifications](file-queue-notifications.md).

 

 

 



