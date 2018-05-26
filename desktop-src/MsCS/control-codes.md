---
title: Failover Cluster Control Codes
description: The Cluster API defines a small set of control code functions \ 8212;one for each cluster object \ 8212;as \ 0034;generic \ 0034; interfaces to a wide range of cluster operations.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 47618915-0985-4415-b7d4-5959fb27eb9f
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- control codes Failover Cluster ,described
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Failover Cluster Control Codes

The [Cluster API](cluster-api.md) defines a small set of control code functions—one for each cluster object—as "generic" interfaces to a wide range of cluster operations. [Control codes](about-control-codes.md)—32 bit values used as function parameters—determine the kind of operation a control code function will perform. Together, the control code functions and the control codes support nearly every kind of cluster functionality.

Control codes are 32-bit integers used to describe an operation on a cluster object. Control codes are categorized as internal or external:

-   Applications use [*external control codes*](e-gly.md#-wolf-external-control-code-gly) in [control code functions](control-code-functions.md) to read, validate, and set properties and to perform a variety of other operations on [cluster objects](cluster-objects.md).
-   The [Cluster service](cluster-service.md) uses [*internal control codes*](i-gly.md#-wolf-internal-control-code-gly) to notify [resource DLLs](resource-dlls.md) of changes affecting [resources](resources.md) or [resource types](resource-types.md).

It is important to become familiar with the capabilities of the control codes. Applications and [resource DLLs](resource-dlls.md) should always use control codes, if possible, to perform operations on cluster objects. The control codes are designed to maximize security, protect the [cluster database](cluster-database.md), and ensure resource DLL notification.

## In this section

-   [Cluster Control Codes](cluster-control-codes.md)
-   [Collection Control Codes](collection-control-codes-.md)
-   [Group Control Codes](group-control-codes.md)
-   [Network Control Codes](network-control-codes.md)
-   [Network Interface Control Codes](network-interface-control-codes.md)
-   [Node Control Codes](node-control-codes.md)
-   [Resource Control Codes](resource-control-codes.md)
-   [Resource Type Control Codes](resource-type-control-codes.md)

## Related topics

<dl> <dt>

[Failover Cluster Reference](failover-cluster-reference.md)
</dt> </dl>

 

 




