---
title: Private Properties of a Cluster Object
description: A private property is an attribute possessed by an individual instance of a cluster object. Other instances may or may not possess the same property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a1dee11c-f1fe-4509-a40a-a58c4b8999ef
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- properties Failover Cluster ,private
- properties Failover Cluster ,private,described
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Private Properties of a Cluster Object

A private [property](cluster-object-properties.md) is an attribute possessed by an individual instance of a [cluster object](cluster-objects.md). Other instances may or may not possess the same property.

Private properties are defined by the cluster software and by [resource DLLs](resource-dlls.md). End users and developers can create private properties for objects as needed. Private properties that are not created by the cluster or by a resource DLL are classified as unknown properties.

Private properties are further categorized as required or optional. If an object has a required private property, the property must have valid data before the object can be used. This may be a matter of verifying that the default value of the property is valid, or it may require an explicit assignment. For example, the [**Address**](ip-addresses-address.md) property for [IP Addresses](ip-address.md) [resources](resources.md) is required. The resource cannot be brought online unless a valid IP address is stored in the **Address** property.

Optional private properties do not require a value.

The private properties for any cluster object reside in the [cluster database](cluster-database.md) under a **Parameters** key that is related to the identifier of the object. The following syntax illustrates a parameters key where *Object* refers to the name of the object and *ObjectID* refers to the object's identifier:

**HKEY\_LOCAL\_MACHINE**\\**Cluster**\\*Object*\\*ObjectID*\\**Parameters**

 

 




