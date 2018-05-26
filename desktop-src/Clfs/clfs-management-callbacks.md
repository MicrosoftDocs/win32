---
Description: The Common Log File System (CLFS) API defines the following callbacks.
ms.assetid: c7ed5712-2325-4748-beec-6989c815b184
title: CLFS Management Callbacks
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CLFS Management Callbacks

The Common Log File System (CLFS) API defines the following callbacks.



| Callback                                                                     | Description                                                                                                                                         |
|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| [**LOG\_FULL\_HANDLER\_CALLBACK**](/windows/win32/Clfsmgmtw32/?branch=master)<br/> | An application-defined callback function that receives notification that the call to [**HandleLogFull**](/windows/win32/Clfsmgmtw32/nf-clfsmgmtw32-handlelogfull?branch=master) is complete.<br/> |
| [**LOG\_TAIL\_ADVANCE\_CALLBACK**](/windows/win32/Clfsmgmtw32/nc-clfsmgmtw32-plog_tail_advance_callback?branch=master)<br/> | An application-defined callback function that advances a log tail.<br/>                                                                       |
| [**LOG\_UNPINNED\_CALLBACK**](/windows/win32/Clfsmgmtw32/nc-clfsmgmtw32-plog_unpinned_callback?branch=master)<br/>          | An application-defined callback function that receives notification that the log has become unpinned.<br/>                                    |



 

 

 




