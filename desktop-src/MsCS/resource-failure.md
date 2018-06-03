---
title: Resource Failure
description: Whether you are creating a resource DLL or trying to maximize the availability of a resource, it is important to understand how the Cluster service detects and responds to resource failure and how you can affect that process.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f18644d1-63ec-4920-b703-a3f149684508
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- resource failure Failover Cluster
- resources Failover Cluster ,failure
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Resource Failure

Whether you are creating a [resource DLL](resource-dlls.md) or trying to maximize the availability of a [resource](resources.md), it is important to understand how the [Cluster service](cluster-service.md) detects and responds to resource failure and how you can affect that process.

-   At intervals determined by a resource's [**LooksAlivePollInterval**](resources-looksalivepollinterval.md) property, the [Cluster service](cluster-service.md) checks to see if the [resource](resources.md) appears operational. The Cluster service invokes the [Resource Monitor](resource-monitor.md) to call the [**LooksAlive**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-plooks_alive_routine) entry point function of the [resource DLL](resource-dlls.md) managing the resource. This function implements resource-specific procedures to detect whether the resource is working properly and then communicates the results back through the Resource Monitor to the Cluster service. If **LooksAlive** reports failure, the Cluster service immediately calls the [**IsAlive**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-pis_alive_routine) entry point function. Note that **LooksAlive** is not called for all resources. A resource DLL can be implemented in a way that prevents **LooksAlive** checks. For more information see [**Open**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-popen_routine).
-   At intervals determined by a resource's [**IsAlivePollInterval**](resources-isalivepollinterval.md) property, the Cluster service checks to see if the resource is still operational. The Cluster service invokes the Resource Monitor to call the [**IsAlive**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-pis_alive_routine) entry point function of the resource DLL managing the resource. This function implements resource-specific procedures to detect whether the resource is working properly and then communicates the results back through the Resource Monitor to the Cluster service. If **IsAlive** reports failure, the resource is considered failed.
-   A resource DLL can be designed to report failure at any time, even in the intervals between [**IsAlive**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-pis_alive_routine) checks. For more information see Open.
-   When a resource has failed, and the [**RestartAction**](resources-restartaction.md) property is set to allow a restart, the Cluster service attempts to restart the resource on the same node. The resource's [**RestartThreshold**](resources-restartthreshold.md) property determines the maximum number of restart attempts that can occur within a time period specified by the [**RestartPeriod**](resources-restartperiod.md) property. If the Cluster service exceeds the maximum number of restart attempts within the specified time period, and the resource is still not operational, the Cluster service may attempt failover (see next bullet).
-   When a resource has failed and restart attempts on the same node have failed, its [**RestartAction**](resources-restartaction.md) property determines whether the [group](groups.md) to which the resource belongs will be failed over to another [node](nodes.md) (see [Failover](failover.md)).
-   If a failed resource does not fail over successfully, it remains in a failed state for an interval determined by the [**RetryPeriodOnFailure**](resources-retryperiodonfailure.md) property. Then, if [**RestartAction**](resources-restartaction.md) is set to allow restarts, the Cluster service makes a final attempt to bring the resource online. If this does not succeed, the failed resource remains in its failed state until the problem is corrected manually.

You can control a resource's failure detection procedures by adjusting the [**RestartPeriod**](resources-restartperiod.md), [**LooksAlivePollInterval**](resources-looksalivepollinterval.md), [**IsAlivePollInterval**](resources-isalivepollinterval.md), [**RetryPeriodOnFailure**](resources-retryperiodonfailure.md), and [**RestartAction**](resources-restartaction.md) properties. Developers of [custom resource types](custom-resource-types.md) can implement [**LooksAlive**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-plooks_alive_routine) and [**IsAlive**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-pis_alive_routine) with failure detection procedures specific to the resource being supported. For information, see [Implementing LooksAlive](implementing-looksalive.md) and [Implementing IsAlive](implementing-isalive.md).

> [!Note]  
> Both [resources](resources.md) and [resource types](resource-types.md) have the [**IsAlivePollInterval**](resources-isalivepollinterval.md) and [**LooksAlivePollInterval**](resources-looksalivepollinterval.md) properties. Resource type properties apply to all resources of that type in the [*cluster*](https://www.bing.com/search?q=*cluster*). Resource properties apply to an individual resource and can override resource type properties. For example, the [Physical Disk](physical-disk.md) resource type's **IsAlivePollInterval** property might be set to 300 milliseconds. All Physical Disk resources in the cluster would default to this property value. However, an administrator could set an individual Physical Disk resource's **IsAlivePollInterval** property to 500 milliseconds, overriding the property value of the resource type.

 

 

 




