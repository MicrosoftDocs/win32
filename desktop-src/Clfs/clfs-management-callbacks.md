---
Description: 'The Common Log File System (CLFS) API defines the following callbacks.'
ms.assetid: 'c7ed5712-2325-4748-beec-6989c815b184'
title: CLFS Management Callbacks
---

# CLFS Management Callbacks

The Common Log File System (CLFS) API defines the following callbacks.



| Callback                                                                     | Description                                                                                                                                         |
|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| [**LOG\_FULL\_HANDLER\_CALLBACK**](log-full-handler-callback.md)<br/> | An application-defined callback function that receives notification that the call to [**HandleLogFull**](handlelogfull.md) is complete.<br/> |
| [**LOG\_TAIL\_ADVANCE\_CALLBACK**](log-tail-advance-callback.md)<br/> | An application-defined callback function that advances a log tail.<br/>                                                                       |
| [**LOG\_UNPINNED\_CALLBACK**](log-unpinned-callback.md)<br/>          | An application-defined callback function that receives notification that the log has become unpinned.<br/>                                    |



 

 

 




