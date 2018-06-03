---
Description: The Common Log File System (CLFS) API defines the following callbacks.
ms.assetid: c7ed5712-2325-4748-beec-6989c815b184
title: CLFS Management Callbacks
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CLFS Management Callbacks

The Common Log File System (CLFS) API defines the following callbacks.



| Callback                                                                     | Description                                                                                                                                         |
|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| [**LOG\_FULL\_HANDLER\_CALLBACK**](/windows/desktop/api/Clfsmgmtw32/)<br/> | An application-defined callback function that receives notification that the call to [**HandleLogFull**](/windows/desktop/api/Clfsmgmtw32/nf-clfsmgmtw32-handlelogfull) is complete.<br/> |
| [**LOG\_TAIL\_ADVANCE\_CALLBACK**](/windows/desktop/api/Clfsmgmtw32/nc-clfsmgmtw32-plog_tail_advance_callback)<br/> | An application-defined callback function that advances a log tail.<br/>                                                                       |
| [**LOG\_UNPINNED\_CALLBACK**](/windows/desktop/api/Clfsmgmtw32/nc-clfsmgmtw32-plog_unpinned_callback)<br/>          | An application-defined callback function that receives notification that the log has become unpinned.<br/>                                    |



 

 

 




