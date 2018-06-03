---
title: Closing a Notification Port
description: Applications close a notification port by calling CloseClusterNotifyPort.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 90e6dafe-68ea-4327-bde4-034cd86b4b64
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- notification ports Failover Cluster , closing
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Closing a Notification Port

Applications close a notification port by calling [**CloseClusterNotifyPort**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_close_cluster_notify_port).

Note the potential for a race condition if multiple threads access the same notification port. For example, one thread could be calling [**CloseClusterNotifyPort**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_close_cluster_notify_port) to close the notification port while another thread, which has called [**GetClusterNotify**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_get_cluster_notify), is waiting to retrieve information from the same port.

Prevent this problem by having the thread that is calling [**GetClusterNotify**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_get_cluster_notify) check for a CLUSTER\_CHANGE\_HANDLE\_CLOSE event.

 

 




