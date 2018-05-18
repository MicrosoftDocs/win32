---
title: Creating Resource Types
description: One of the most common programming tasks for failover clusters is to create a resource type that allows an application, service, or device to be managed as a highly available cluster resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'de3569ef-ee74-457e-b672-00e22ee8154c'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["resource types Failover Cluster ,creating"]
---

# Creating Resource Types

One of the most common programming tasks for failover clusters is to create a [resource type](resource-types.md) that allows an application, service, or device to be managed as a highly available [cluster resource](resources.md). This section of the documentation contains topics that describe how to create a resource type, and how to perform related tasks such as debugging and deploying resource types.

## When to create a resource DLL

[Resource DLLs](resource-dlls.md) provide more advanced resource availability for failover clusters than the generic resource types. The resource management tasks performed by resource DLLs are more specialized and can be configured to manage hardware, software, and services. You should use a resource DLL if any of these conditions are true:

-   The resource is a device.
-   The resource depends on other resources.
-   The resource manages critical transaction-based data.
-   The resource is stateful.
-   The resource requires special initialization, shutdown, or emergency termination procedures.
-   The resource has unique attributes that should be managed as private properties.
-   The resource has special functionality that should be exposed through user-defined [control codes](about-control-codes.md).

## When to use the generic application or generic resource type

The [generic application](generic-application.md) and [generic service](generic-service.md) resources types provide basic implementations of the resource DLL entry point functions. These implementations start and stop resources by starting and terminating a process, and look for resource failure by verifying whether the process still exists. Because generic resource types provide more basic implementations than resource DLLs, they should only be when all of these conditions are true:

-   The resource is not a device. The generic resource types are not designed to manage hardware.
-   The resource is stateless.
-   The resource is not dependent on other resources.
-   The resource does not have unique attributes that should be managed with private properties.
-   The resource does not have special functionality that should be exposed through control codes.
-   The resource can be started and stopped easily without using special procedures.

## In this section

<dl> <dt>

[Implementing Resource DLLs](implementing-resource-dlls.md)
</dt> <dd>

Create a resource DLL that defines resource types for failover clusters by using specialized resource management tasks.

</dd> <dt>

[Using the Generic Script Resource Type](using-the-generic-script-resource-type.md)
</dt> <dd>

The generic script resource type can be used with applications that can be controlled by a script interface such as an ActiveX object, or WMI.

</dd> <dt>

[Implementing Extension DLLs](implementing-extension-dlls.md)
</dt> <dd>

An extension DLL allows administrators to mange resource types with the Failover Cluster Administrator user interface.

</dd> <dt>

[Debugging Resource DLLs](debugging-resource-dlls.md)
</dt> <dd>

Debug a resource DLL.

</dd> <dt>

[Debugging Extension DLLs](debugging-extension-dlls.md)
</dt> <dd>

Debug an extension DLL for a resource type.

</dd> <dt>

[Manually Deploying Resource Types](deploying-resource-types.md)
</dt> <dd>

Manually deploy resource types in order to design and test the resource type.

</dd> <dt>

[Creating Setup Applications that Deploy Resource Types](creating-cluster-aware-setup-applications.md)
</dt> <dd>

Create a setup application that deploys resource types by installing files, registering the resource types, and initializing groups.

</dd> </dl>

## Related topics

<dl> <dt>

[Using the Failover Cluster APIs](using-the-server-cluster-api.md)
</dt> </dl>

 

 




