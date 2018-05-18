---
title: Creating a Notification Port
description: Requirements for creating a notification port using the Failover Cluster API.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'e29c67bf-241d-4fb0-9ad2-73bcbeae309d'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["notification ports Failover Cluster ,creating"]
---

# Creating a Notification Port

Applications perform the following steps to create a notification port.

1.  Spawn a separate thread to create and monitor the port.

2.  Call [**CreateClusterNotifyPort**](createclusternotifyport.md). For the initial call, set *hChange* to **INVALID\_HANDLE\_VALUE** so that a new handle will be created. Subsequent calls can specify *hChange* to add more events to the port.

3.  Set the *dwFilter* parameter to one or more events of interest, using the OR operator ( \| ) to specify multiple events. For example, if an application should be informed when there is any change to the [*cluster's*](c-gly.md#-wolf-cluster-gly)[resource types](resource-types.md), it would set *dwFilter* as follows:

    `dwFilter = CLUSTER_CHANGE_RESOURCE_TYPE_ADDED | CLUSTER_CHANGE_RESOURCE_TYPE_DELETED;`

4.  Set the *dwNotifyKey* parameter to a value that identifies the events specified by *dwFilter*. When you retrieve events from the port, all events of type &lt;*dwFilter*&gt; will be "flagged" with a value of &lt;*dwNotifyKey*&gt;. You can use *dwNotifyKey* like an index to differentiate different event types in the same port. For example, the following code fragment creates a notification port for monitoring resource and [cluster database](cluster-database.md) events such that any resource-related event will return a *dwNotifyKey* value of **ResourceEvents**, and any cluster database event will return a *dwNotifyKey* value of **DatabaseEvents**:

    ```C++
    HCHANGE hChange;

    DWORD ResourceEvents = CLUSTER_CHANGE_RESOURCE_ADDED    |
                           CLUSTER_CHANGE_RESOURCE_DELETED  |
                           CLUSTER_CHANGE_RESOURCE_PROPERTY |
                           CLUSTER_CHANGE_RESOURCE_STATE;

    DWORD DatabaseEvents = CLUSTER_CHANGE_REGISTRY_ATTRIBUTES |
                           CLUSTER_CHANGE_REGISTRY_NAME       |
                           CLUSTER_CHANGE_REGISTRY_SUBTREE    |
                           CLUSTER_CHANGE_REGISTRY_VALUE;

    hChange = CreateClusterNotifyPort( (HCHANGE)INVALID_HANDLE_VALUE,
                                       hCluster,
                                       ResourceEvents,   // dwFilter
                                       ResourceEvents ); // dwNotifyKey

    hChange = CreateClusterNotifyPort( hChange,
                                       hCluster,
                                       DatabaseEvents,
                                       DatabaseEvents );
    ```

    

 

 




