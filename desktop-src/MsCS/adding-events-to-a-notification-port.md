---
title: Adding Events to a Notification Port
description: After the port has been created (see Creating a Notification Port), applications can add other event types to the port by calling RegisterClusterNotify.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '654f571d-ff7d-40d4-a52c-01fcbd1573ad'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["notification ports Failover Cluster , adding events", "events Failover Cluster", "events Failover Cluster , adding to a notification port"]
---

# Adding Events to a Notification Port

After the port has been created (see [Creating a Notification Port](creating-a-notification-port.md)), applications can add other event types to the port by calling [**RegisterClusterNotify**](registerclusternotify.md). Like [**CreateClusterNotifyPort**](createclusternotifyport.md), **RegisterClusterNotify** allows you to specify the type of events (*dwFilter*) and associate those events with a key (*dwNotifyKey*). **RegisterClusterNotify** also allows you to specify an object handle in the *hObject* parameter, enabling you to receive event notifications on a per-handle basis.

The following code fragment adds resource-specific events to an existing notification port. Any events of a type defined by *ResourceEvents* that involve *hMyResource* will generate notifications identified by a *dwNotifyKey* of *dwMyResource*:


```C++
HCLUSTER hCluster;
HRESOURCE hMyResource;
DWORD_PTR dwMyResource;
DWORD dwResult;

hMyResource = OpenClusterResource( hCluster, L"MyResource" );
dwMyResource = (DWORD)hMyResource;
dwResult = RegisterClusterNotify( hChange,
                                  ResourceEvents,
                                  hMyResource,
                                  dwMyResource );
```



 

 




