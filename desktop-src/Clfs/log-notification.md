---
Description: 'If a client of the log manager has called the RegisterManageableLogClient function to register as an asynchronous client, the client can read log notifications, which are received as callbacks.'
ms.assetid: 'f40919a3-140a-4fae-9412-bb3c2b2a5067'
title: Log Notification
---

# Log Notification

If a client of the log manager has called the [**RegisterManageableLogClient**](registermanageablelogclient.md) function to register as an asynchronous client, the client can read log notifications, which are received as callbacks.

Log notifications allow your application to receive status messages indicating the status of a call to the [**HandleLogFull**](handlelogfull.md) function, that a log is unpinned, or that the application's log tail must be moved.

Callbacks are most useful if an application maintains a dedicated thread for the callbacks. The application must keep the context it received when it registered so that the application can unregister the log client. Notifications can be serviced from any thread.

 

 



