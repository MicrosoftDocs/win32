---
title: Resource Type Common Properties
description: Common properties for resource types are data values stored in the cluster database that describe the identity and behavior of each resource type in a cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ade5a225-5532-4957-b5f9-c44c75d517b2
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- resource type properties Failover Cluster
- properties Failover Cluster ,resource type (common) properties
- resource types Failover Cluster ,properties
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Resource Type Common Properties

[Common properties](common-properties.md) for [resource types](resource-types.md) are data values stored in the [cluster database](cluster-database.md) that describe the identity and behavior of each resource type in a [*cluster*](c-gly.md#-wolf-cluster-gly).

## In this section

<dl> <dt>

[**AdminExtensions**](resource-types-adminextensions.md)
</dt> <dd>

The [**AdminExtensions**](resource-types-adminextensions.md) property provides the class identifiers (**CLSID**s) for the [Cluster Administrator](cluster-administrator.md) extension DLLs that are associated with the [resource type](resource-types.md). The following table summarizes the attributes of the **AdminExtensions** property.

</dd> <dt>

[**DeadlockTimeout**](deadlocktimeout-restypprop.md)
</dt> <dd>

Specifies the period (in milliseconds) of the deadlock detection heartbeat.

</dd> <dt>

[**DebugControlFunctions**](resource-types-debugcontrolfunctions.md)
</dt> <dd>

This property is not supported.

</dd> <dt>

[**DebugPrefix**](resource-types-debugprefix.md)
</dt> <dd>

This property is not supported.

</dd> <dt>

[**Description**](resource-types-description.md)
</dt> <dd>

Provides comments about the [resource type](resource-types.md). The following table summarizes the attributes of the **Description** property.

</dd> <dt>

[**DllName**](resource-types-dllname.md)
</dt> <dd>

Provides the name of the dynamic-link library (DLL) for the [resource type](resource-types.md). The following table summarizes the attributes of the [**DllName**](resource-types-dllname.md) property.

</dd> <dt>

[**DumpLogQuery**](dumplogquery.md)
</dt> <dd>

Specifies a query that can be used to export logs for resource types.

</dd> <dt>

[**DumpPolicy**](resource-types-dumppolicy.md)
</dt> <dd>

Specifies the dump collection policy for the cluster service.

</dd> <dt>

[**EnabledEventLogs**](enabledeventlogs.md)
</dt> <dd>

Specifies the enabled event logs for a resource type.

</dd> <dt>

[**IsAlivePollInterval**](resource-types-isalivepollinterval.md)
</dt> <dd>

Specifies the recommended interval in milliseconds at which a [Resource Monitor](resource-monitor.md) should poll resources of the particular [resource type](resource-types.md) to determine if they are operational. The polling occurs when the Resource Monitor calls a resource DLL's [**IsAlive**](/windows/previous-versions/ResApi/nc-resapi-pis_alive_routine?branch=master) entry point function. The following table summarizes the attributes of the [**IsAlivePollInterval**](resource-types-isalivepollinterval.md) property.

</dd> <dt>

[**LooksAlivePollInterval**](resource-types-looksalivepollinterval.md)
</dt> <dd>

Specifies the recommended interval in milliseconds at which the [Cluster service](cluster-service.md) should poll [resources](resources.md) of the particular [resource type](resource-types.md) to determine if they appear operational. The polling occurs when the [Resource Monitor](resource-monitor.md) calls a resource DLL's [**LooksAlive**](/windows/previous-versions/ResApi/nc-resapi-plooks_alive_routine?branch=master) entry point function. The following table summarizes the attributes of the [**LooksAlivePollInterval**](resource-types-looksalivepollinterval.md) property.

</dd> <dt>

[**Name**](resource-types-name.md)
</dt> <dd>

Specifies the [display name](display-names.md) of the [resource type](resource-types.md). The display name is the name that appears to administrators in the [Cluster Administrator](cluster-administrator.md) user interface. The following table summarizes the attributes of the **Name** property.

</dd> <dt>

[**PendingTimeout**](pendingtimeout.md)
</dt> <dd>

(TBD).

</dd> </dl>

## Related topics

<dl> <dt>

[Cluster Object Common Properties](common-properties-ref.md)
</dt> <dt>

[Getting Resource Type Information](getting-resource-type-information.md)
</dt> </dl>

 

 




