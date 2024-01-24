---
description: The data tier often contains mostly static information&\#8212;information persisted on durable media.
ms.assetid: d2bce8b6-1f88-4e4a-bb08-fc7ee4c039da
title: Optimize Calls Between the COM+ Business Logic and Data
ms.topic: article
ms.date: 05/31/2018
---

# Optimizing Interactions Between the COM+ Business Logic Tier and the Data Tier

The data tier often contains mostly static information—information persisted on durable media. Because this tier encompasses information that is mostly static, it requires a thorough analysis for potential bottlenecks. In addition to the obvious possibility for connection bottlenecks, hot spots can be caused by frequently accessed records, inefficient data access methods, and the need to coordinate access to legacy systems.

## Connecting to the Data Tier

Two considerations play an important role in designing a data tier for a COM+ application: connection pooling and [COM+ just-in-time (JIT) activation](com--just-in-time-activation.md), and the use of DSNs. Components that make connections to the data tier should use [COM+ object pooling](com--object-pooling.md) set on the component.

When creating DSNs, use object constructor strings specified on the component instead of creating a File DSN. File DSNs are slower than a connection using an object constructor string. Object constructor strings can be specified on the component property sheet. For more information, see [COM+ Object Constructor Strings](com--object-constructor-strings.md).

If you are using components to access a SQL Server database, use COM+ object pooling instead of SQL connection pooling.

If your component is using ADO to fetch multiple recordsets, establish multiple connections for the component. When ADO retrieves multiple recordsets, it creates multiple connections in the background if you do not create them. If you create them, you can pool them and have more control over the number of the connections used.

## Related topics

<dl> <dt>

[Optimizing Interactions Between the COM+ Business Logic Tier and the Presentation Tier](optimizing-interactions-between-the-com--business-logic-tier-and-the-presentation-tier.md)
</dt> </dl>

 

 



