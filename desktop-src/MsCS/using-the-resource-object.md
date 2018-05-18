---
title: Using the Resource Object
description: The Generic Script resource DLL automatically creates an instance of a Resource object for each instance of a scripted resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'd641e062-e7ff-4997-9cbc-018a467f1de3'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["Resource object Failover Cluster , using"]
---

# Using the Resource Object

The Generic Script resource DLL automatically creates an instance of a [**Resource**](resource-object.md) object for each instance of a scripted resource. Your script can use the methods and properties of the **Resource** object to identify the resource, log information about the resource, and manipulate private properties.

Note that the [**Resource**](resource-object.md) object is internally defined and is only available to your script when a resource is brought online.

 

 




