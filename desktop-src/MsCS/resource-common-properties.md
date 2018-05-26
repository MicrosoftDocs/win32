---
title: Resource Common Properties
description: Common properties for resources are data values stored in the cluster database that describe the identity and behavior of each resource in a cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b84fe8fe-a49e-4c3c-acbd-f9cfe5ac0782
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- resource properties Failover Cluster
- properties Failover Cluster ,resource (common) properties
- resources Failover Cluster ,properties
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Resource Common Properties

[Common properties](common-properties.md) for [resources](resources.md) are data values stored in the [cluster database](cluster-database.md) that describe the identity and behavior of each resource in a [*cluster*](c-gly.md#-wolf-cluster-gly).

## In this section

<dl> <dt>

[**AdminExtensions**](resources-adminextensions.md)
</dt> <dd>

This property is not supported.

</dd> <dt>

[**DeadlockTimeout**](deadlocktimeout.md)
</dt> <dd>

Specifies the period (in milliseconds) of the deadlock detection heartbeat.

</dd> <dt>

[**DebugPrefix**](resources-debugprefix.md)
</dt> <dd>

This property is not supported.

</dd> <dt>

[**Description**](resources-description.md)
</dt> <dd>

Provides comments about the [resource](resources.md). The following table summarizes the attributes of the **Description** property.

</dd> <dt>

[**DumpServices**](dumpservices.md)
</dt> <dd>

Dump services.

</dd> <dt>

[**IsAlivePollInterval**](resources-isalivepollinterval.md)
</dt> <dd>

Provides the recommended interval in milliseconds at which the [Cluster service](cluster-service.md) should poll the resource to determine if it is operational. The polling occurs when the [Resource Monitor](resource-monitor.md) calls the [resource DLL's](resource-dlls.md) [**IsAlive**](/windows/previous-versions/ResApi/nc-resapi-pis_alive_routine?branch=master) entry point function. The following table summarizes the attributes of the [**IsAlivePollInterval**](resources-isalivepollinterval.md) property.

</dd> <dt>

[**LastOperationStatusCode**](resources-lastoperationstatuscode.md)
</dt> <dd>

Contains the last error that was set by the resource.

</dd> <dt>

[**LooksAlivePollInterval**](resources-looksalivepollinterval.md)
</dt> <dd>

Provides the recommended interval in milliseconds at which the [Cluster service](cluster-service.md) should poll the resource to determine if it appears operational.

</dd> <dt>

[**MaximumMonitors**](maximummonitors.md)
</dt> <dd>

The maximum number of monitors.

</dd> <dt>

[**MonitorProcessId**](monitorprocessid.md)
</dt> <dd>

process id of the resource monitor.

</dd> <dt>

[**Name**](resources-name.md)
</dt> <dd>

Provides the name of the [resource](resources.md). The following table summarizes the attributes of the [**Name**](resources-name.md) property.

</dd> <dt>

[**PendingTimeout**](resources-pendingtimeout.md)
</dt> <dd>

Sets the number of milliseconds that a [Resource Monitor](resource-monitor.md) will wait for a [resource DLL](resource-dlls.md) to update the status of a [resource](resources.md) in an OnlinePending or OfflinePending state before terminating the resource. The following table summarizes the attributes of the **PendingTimeout** property.

</dd> <dt>

[**PersistentState**](resources-persistentstate.md)
</dt> <dd>

Specifies whether the [resource](resources.md) should be brought online or left offline when the [Cluster service](cluster-service.md) is started. The following table summarizes the attributes of the [**PersistentState**](resources-persistentstate.md) property.

</dd> <dt>

[**ResourceSpecificData1**](resources-resourcespecificdata1.md)
</dt> <dd>

Contains a 64-bit value that is specific to the resource.

</dd> <dt>

[**ResourceSpecificData2**](resources-resourcespecificdata2.md)
</dt> <dd>

Contains a 64-bit value that is specific to the resource.

</dd> <dt>

[**ResourceSpecificStatus**](resources-resourcespecificstatus.md)
</dt> <dd>

Provides a resource-specific status message of the [resource](resources.md). The following table summarizes the attributes of the [**ResourceSpecificStatus**](resources-resourcespecificstatus.md) property.

</dd> <dt>

[**RestartAction**](resources-restartaction.md)
</dt> <dd>

Describes the action to be taken by the [cluster service](cluster-service.md) if the [resource](resources.md) [fails](resource-failure.md).

</dd> <dt>

[**RestartDelay**](resources-restartdelay.md)
</dt> <dd>

Indicates the time delay, in milliseconds, before a failed resource is restarted.

</dd> <dt>

[**RestartPeriod**](resources-restartperiod.md)
</dt> <dd>

Defines an interval of time, in milliseconds, during which a specified number of restart attempts can be made on a nonresponsive [resource](resources.md).

</dd> <dt>

[**RestartThreshold**](resources-restartthreshold.md)
</dt> <dd>

Specifies the maximum number of restart attempts that can be made on a [resource](resources.md) within an interval defined by the [**RestartPeriod**](resources-restartperiod.md) property before the [Cluster service](cluster-service.md) initiates the action specified by the [**RestartAction**](resources-restartaction.md) property.

</dd> <dt>

[**RetryPeriodOnFailure**](resources-retryperiodonfailure.md)
</dt> <dd>

Specifies the interval of time (in milliseconds) that a [resource](resources.md) should remain in a failed state before the [Cluster service](cluster-service.md) attempts to restart it. The following table summarizes the attributes of the **RetryPeriodOnFailure** property.

</dd> <dt>

[**SeparateMonitor**](resources-separatemonitor.md)
</dt> <dd>

Indicates whether the [resource](resources.md) requires its own [Resource Monitor](resource-monitor.md). The following table summarizes the attributes of the **SeparateMonitor** property.

</dd> <dt>

[**StatusInformation**](resources-statusinformation.md)
</dt> <dd>

Contains information about the status of the resource.

</dd> <dt>

[**Type**](resources-type.md)
</dt> <dd>

Specifies the display name of the resource. The following table summarizes the attributes of the **Type** property.

</dd> </dl>

## Related topics

<dl> <dt>

[Cluster Object Common Properties](common-properties-ref.md)
</dt> <dt>

[Getting Resource Information](getting-resource-information.md)
</dt> </dl>

 

 




