---
title: Recommended Practices for Resource DLLs
description: The following items should be taken into account when implementing a resource DLL.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 66fd4a96-dac5-4306-827d-9ec09e5b6fc2
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- resource DLLs Failover Cluster ,recommended practices
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Recommended Practices for Resource DLLs

The following items should be taken into account when implementing a resource DLL.

<dl> <dt>

<span id="Avoid_operations_that_cause_deadlocks_in_resource_DLLs."></span><span id="avoid_operations_that_cause_deadlocks_in_resource_dlls."></span><span id="AVOID_OPERATIONS_THAT_CAUSE_DEADLOCKS_IN_RESOURCE_DLLS."></span>Avoid operations that cause deadlocks in resource DLLs.
</dt> <dd>

See [Function Calls to Avoid in Resource DLLs](function-calls-to-avoid-in-resource-dlls.md).

</dd> <dt>

<span id="For_optimal_performance_of_the_cluster_and_maximum_availability_for_your_resources__all_entry_points_________should_return_a_value_in_300_milliseconds_or_less."></span><span id="for_optimal_performance_of_the_cluster_and_maximum_availability_for_your_resources__all_entry_points_________should_return_a_value_in_300_milliseconds_or_less."></span><span id="FOR_OPTIMAL_PERFORMANCE_OF_THE_CLUSTER_AND_MAXIMUM_AVAILABILITY_FOR_YOUR_RESOURCES__ALL_ENTRY_POINTS_________SHOULD_RETURN_A_VALUE_IN_300_MILLISECONDS_OR_LESS."></span>For optimal performance of the cluster and maximum availability for your resources, all entry points should return a value in 300 milliseconds or less.
</dt> <dd>

If your implementation needs more time, create a worker thread to handle the operation asynchronously and return a value immediately. A [resource DLL](resource-dlls.md) is non-reentrant for all entry points except for the [**Terminate**](/windows/previous-versions/ResApi/nc-resapi-pterminate_routine?branch=master) entry point function. Thus, while your DLL is processing an entry point function, your other entry points (except **Terminate**) are blocked. In general, the *Terminate* entry point function can be called concurrently with any entry point function (such as [*IsAlive*](/windows/previous-versions/ResApi/nc-resapi-pis_alive_routine?branch=master), [*LooksAlive*](/windows/previous-versions/ResApi/nc-resapi-plooks_alive_routine?branch=master), [*Offline*](/windows/previous-versions/ResApi/nc-resapi-poffline_routine?branch=master), [*Online*](/windows/previous-versions/ResApi/nc-resapi-ponline_routine?branch=master), [*ResourceControl*](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master), and [*ResourceTypeControl*](/windows/previous-versions/ResApi/nc-resapi-presource_type_control_routine?branch=master)) except for initialization functions (such as [DllMain](implementing-dllmain.md) and [*Startup*](/windows/previous-versions/ResApi/nc-resapi-pstartup_routine?branch=master)) and resource instance management functions (such as [*Open*](/windows/previous-versions/ResApi/nc-resapi-popen_routine?branch=master) and [*Close*](/windows/previous-versions/ResApi/nc-resapi-pclose_routine?branch=master)). Any resources that are accessed by these entry points must be properly guarded.

</dd> <dt>

<span id="The_Cluster_API_will_not_be_available_to_your_DLL_until_the_Cluster_service_has_started."></span><span id="the_cluster_api_will_not_be_available_to_your_dll_until_the_cluster_service_has_started."></span><span id="THE_CLUSTER_API_WILL_NOT_BE_AVAILABLE_TO_YOUR_DLL_UNTIL_THE_CLUSTER_SERVICE_HAS_STARTED."></span>The Cluster API will not be available to your DLL until the Cluster service has started.
</dt> <dd>

Your DLL receives notification that the Cluster service has started through the [CLUSCTL\_RESOURCE\_TYPE\_STARTING\_PHASE2](clusctl-resource-type-starting-phase2.md) control code.

</dd> <dt>

<span id="Starting_in___you_should_author_only_64-bit_resource_DLLs."></span><span id="starting_in___you_should_author_only_64-bit_resource_dlls."></span><span id="STARTING_IN___YOU_SHOULD_AUTHOR_ONLY_64-BIT_RESOURCE_DLLS."></span>Starting in Windows Server 2012, you should author only 64-bit resource DLLs.
</dt> <dd>

32-bit cluster resource DLL support is available for use through Windows Server 2012, but it may be altered or unavailable in subsequent versions.

</dd> </dl>

 

 




