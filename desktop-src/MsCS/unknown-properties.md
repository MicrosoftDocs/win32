---
title: Unknown Properties
description: An unknown property is a private property that is not defined by the cluster software or by a resource DLL.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '1a4cc421-48b0-4dbe-8a1d-778f40cb77be'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["properties Failover Cluster ,unknown"]
---

# Unknown Properties

An unknown [property](cluster-object-properties.md) is a [private property](private-properties.md) that is not defined by the cluster software or by a [resource DLL](resource-dlls.md). Unknown properties cannot be read-only and cannot be required. Currently, any private property defined for a [group](groups.md), [network](networks.md), [network interface](network-interfaces.md), or [node](nodes.md) is an unknown property. A private property defined for a [resource](resources.md) or [resource type](resource-types.md) outside of the resource DLL that implements the resource type is also an unknown property.

Resource DLLs use the [Cluster Utility Functions](cluster-utility-functions.md) to work with unknown properties, specifically [**ResUtilAddUnknownProperties**](resutiladdunknownproperties.md), [**ResUtilGetAllProperties**](resutilgetallproperties.md), and [**ResUtilSetUnknownProperties**](resutilsetunknownproperties.md).

 

 




