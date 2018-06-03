---
title: About Control Codes
description: The Failover Cluster API uses control codes to define cluster operations and cluster event notifications.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b8ab57bd-f83e-46c2-9c9c-02107c3881bf
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- control codes Failover Cluster
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# About Control Codes

The Failover Cluster API uses control codes to define cluster operations and cluster event notifications. The API has a large number of built in control codes, and also supports custom controls codes. A Control code is a 32-bit integer that defines a cluster operation or an event notification. The primary way to perform operations on clusters and respond to cluster events, is to pass a control code to a control code function. A control code function initiates an operation on a cluster or notifies a resource DLL of a cluster event.

There are two types of control codes:

-   External control codes, which define control code operations. Applications and resource DLLs can initiate cluster operations by using external control codes.
-   Internal control codes, which define cluster event notifications. The Cluster Service uses control codes to notify resource DLLs about cluster events that affect specific resources and resource types. A resource DLL can respond to those cluster events by supporting the control code of the event.

## In this section

<dl> <dt>

[External Control Codes](external-control-codes.md)
</dt> <dd>

Details about external control codes.

</dd> <dt>

[Internal Control Codes](internal-control-codes.md)
</dt> <dd>

Details about internal control codes.

</dd> <dt>

[Control Code Architecture](control-code-architecture.md)
</dt> <dd>

Describes the structure of control codes. You need this information in order to create custom control codes.

</dd> </dl>

## Related topics

<dl> <dt>

[The Failover Cluster API](the-server-cluster-api.md)
</dt> <dt>

[Using Control Codes](using-control-codes.md)
</dt> <dt>

[Control Code Reference](https://msdn.microsoft.com/library/aa369311)
</dt> </dl>

 

 




