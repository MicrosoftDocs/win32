---
title: Implementing Online
description: A resource is not available until it is online.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '888a973f-2b1f-46d2-abcc-f87e62ffbd4b'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["entry point functions Failover Cluster ,implementing Online", "Online Failover Cluster ,implementing"]
---

# Implementing Online

A [resource](resources.md) is not available until it is online. The [Cluster service](cluster-service.md) calls your [**Online**](online.md) entry point to request that a resource instance be brought from an offline (unavailable) state to an online (available) state. Your implementation of **Online** is thus the first opportunity you have to ensure [*high availability*](h-gly.md#-wolf-high-availability-gly).

Typically, the tasks required to bring a resource online take a long time to complete (hundreds to thousands of milliseconds). Most [**Online**](online.md) implementations create a worker thread to perform these tasks asynchronously.

Whether you implement [**Online**](online.md) synchronously or asynchronously, your online code should perform the following tasks:

**To bring a resource online**

1.  Recommended: Retrieve the current values of the resource's [private properties](private-properties.md) by calling [**ResUtilGetPropertiesToParameterBlock**](resutilgetpropertiestoparameterblock.md).

2.  Required: If the resource is a service

    1.  Call [**ResUtilStopResourceService**](resutilstopresourceservice.md) (if necessary) to stop the service before changing the service options.

    2.  Call [**ResUtilSetResourceServiceEnvironment**](resutilsetresourceserviceenvironment.md).

    3.  Call [**ResUtilSetResourceServiceStartParameters**](resutilsetresourceservicestartparameters.md) to make the service controllable by the [*cluster*](c-gly.md#-wolf-cluster-gly).

3.  Required: Bring the resource to an operational state. For applications, this might be as simple as calling [**CreateProcess**](https://msdn.microsoft.com/library/windows/desktop/ms682425).

**To implement Online**

1.  Required: The [**Online**](online.md) entry point function can be called concurrently with the [*Terminate*](terminate.md) entry point function. Any resources that are accessed by both entry points must be properly guarded.

2.  Recommended: For optimal performance, return a value within 300 milliseconds. If you need more time to perform all of the necessary tasks, have [**Online**](online.md) start a worker thread and return **ERROR\_IO\_PENDING** immediately. See [Implementing Pending Operations](implementing-pending-operations.md).

3.  Optional: If you want to implement asynchronous failure detection, return a handle to an object that can be signaled—such as a semaphore—as the *EventHandle* parameter. For more information see [Detecting Resource Failure](detecting-resource-failure.md).

## Example

See [Resource DLL Examples](https://msdn.microsoft.com/library/aa370474).

 

 




