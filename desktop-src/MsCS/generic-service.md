---
title: Generic Service
description: The Generic Service resource type manages services as cluster resources.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '50366c38-d9f7-4faa-8a97-6e0a0547320f'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["resource types Failover Cluster ,Generic Service", "Generic Service resource type Failover Cluster"]
---

# Generic Service

The Generic Service [resource type](resource-types.md) manages services as cluster [resources](resources.md). Similar to the [Generic Application](generic-application.md) resource type, the Generic Service resource type provides only the most basic functionality. For example, the failure of a Generic Service [resource](resources.md) is determined by a query of the Service Control Manager (SCM). If the service is running, it is presumed to be [*online*](o-gly.md#-wolf-online-gly). To provide greater functionality, you can define a custom resource type (for information, see [Creating Resource Types](creating-resource-types.md)).

A generic service resource type is usually used to manage a stateless service as a cluster resource, which can be failed over. However, generic services don't provide much state information other than their online state, so if they have an issue that doesn't cause the resource to go offline, it is more difficult to detect a service failure.

Generic services should only be used when all of the following conditions are true; otherwise, you should create a [resource DLL](resource-dlls.md).

-   The resource is not a device. The generic resource types are not designed to manage hardware.
-   The resource is stateless.
-   The resource is not dependent on other resources.
-   The resource does not have unique attributes that should be managed with private properties.
-   The resource does not have special functionality that should be exposed through control codes.
-   The resource can be started and stopped easily without using special procedures.

The following table summarizes the characteristics of the Generic Service resource type.



| Characteristic                                        | Description                                                                                                                |
|-------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| Required [dependencies](resource-dependencies.md)    | None                                                                                                                       |
| Required [private properties](private-properties.md) | [**ServiceName**](generic-services-servicename.md)                                                                        |
| Optional private properties                           | [**StartupParameters**](generic-services-startupparameters.md), [**UseNetworkName**](generic-services-usenetworkname.md) |



 

## Related topics

<dl> <dt>

[Resource Types](resource-types.md)
</dt> </dl>

 

 




