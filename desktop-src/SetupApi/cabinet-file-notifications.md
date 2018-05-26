---
Description: The following notifications are sent by SetupIterateCabinet. For more information about the format and use of notifications, see Notifications.
ms.assetid: 5a362a93-ebe8-4995-aacc-13ee10d3407a
title: Cabinet File Notifications
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Cabinet File Notifications

The following notifications are sent by [**SetupIterateCabinet**](/windows/win32/Setupapi/nf-setupapi-setupiteratecabineta?branch=master). For more information about the format and use of notifications, see [Notifications](notifications.md).



| Notification                                                        | Description                                                                    |
|---------------------------------------------------------------------|--------------------------------------------------------------------------------|
| [**SPFILENOTIFY\_FILEEXTRACTED**](spfilenotify-fileextracted.md)   | The file has been extracted from the cabinet.                                  |
| [**SPFILENOTIFY\_FILEINCABINET**](spfilenotify-fileincabinet.md)   | A file is encountered in the cabinet, does the application want to extract it? |
| [**SPFILENOTIFY\_NEEDNEWCABINET**](spfilenotify-neednewcabinet.md) | The current file is continued in the next cabinet.                             |



 

 

 



