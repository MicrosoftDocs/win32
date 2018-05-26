---
title: Failover Cluster Development Guidelines
description: Failover Cluster API programming best practices.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4d3e6312-20b6-4647-8cd2-3a529a94bab7
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- recommendations and cautions Failover Cluster
- cautions Failover Cluster
- best practices Failover Cluster
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Failover Cluster Development Guidelines

The following information applies to all cluster programming tasks.

<dl> <dt>

<span id="Follow_the_standard_order_of_preference_when_selecting_an_API_to_use."></span><span id="follow_the_standard_order_of_preference_when_selecting_an_api_to_use."></span><span id="FOLLOW_THE_STANDARD_ORDER_OF_PREFERENCE_WHEN_SELECTING_AN_API_TO_USE."></span>Follow the standard order of preference when selecting an API to use.
</dt> <dd>

The various subsets of the [Failover Cluster API](the-server-cluster-api.md) sometimes present you with multiple ways to do the same thing. The standard order of preference describes how to choose the best API for your type of application.

</dd> <dt>

<span id="Do_not_use_any_registry_functions_that_are_not_part_of_the_Failover_Cluster_API_on_any_cluster_database_________keys."></span><span id="do_not_use_any_registry_functions_that_are_not_part_of_the_failover_cluster_api_on_any_cluster_database_________keys."></span><span id="DO_NOT_USE_ANY_REGISTRY_FUNCTIONS_THAT_ARE_NOT_PART_OF_THE_FAILOVER_CLUSTER_API_ON_ANY_CLUSTER_DATABASE_________KEYS."></span>Do not use any registry functions that are not part of the Failover Cluster API on any cluster database keys.
</dt> <dd>

They will corrupt the data and make the cluster unusable. Only the Failover Cluster API can work with the cluster database safely. This applies only to keys in the cluster hive (**HKEY\_LOCAL\_MACHINE\\CLUSTER**), not to checkpointed registry keys external to the cluster database.

</dd> <dt>

<span id="Refresh_often_and_use_caution_when_working_with_property_values."></span><span id="refresh_often_and_use_caution_when_working_with_property_values."></span><span id="REFRESH_OFTEN_AND_USE_CAUTION_WHEN_WORKING_WITH_PROPERTY_VALUES."></span>Refresh often and use caution when working with property values.
</dt> <dd>

Keep in mind the possibility that a new value has been written to a property immediately after you read or write the old value (see [Multiple and Simultaneous Property Updates](multiple-and-simultaneous-property-updates.md)). Refresh local property data before relying on a specific value.

</dd> <dt>

<span id="Do_not_mix_LPC_and_RPC_handles_in_the_same_API_call."></span><span id="do_not_mix_lpc_and_rpc_handles_in_the_same_api_call."></span><span id="DO_NOT_MIX_LPC_AND_RPC_HANDLES_IN_THE_SAME_API_CALL."></span>Do not mix LPC and RPC handles in the same API call.
</dt> <dd>

If an API takes more than one cluster object handle as a parameter, be sure that all handles are RPC or that all handles are LPC. Mixing handle types results in an RPC exception and may have other unpredictable results. For more information, see [LPC and RPC Handles](lpc-and-rpc-handles.md).

</dd> <dt>

<span id="Close_handles_after_deleting_objects"></span><span id="close_handles_after_deleting_objects"></span><span id="CLOSE_HANDLES_AFTER_DELETING_OBJECTS"></span>Close handles after deleting objects
</dt> <dd>

The [**DeleteClusterResource**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_delete_cluster_resource?branch=master) and [**DeleteClusterGroup**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_delete_cluster_group?branch=master) functions do not close the handles to the deleted objects. To avoid memory leaks, call [**CloseClusterResource**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_close_cluster_resource?branch=master) and [**CloseClusterGroup**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_close_cluster_group?branch=master) on the handles to the deleted objects.

</dd> <dt>

<span id="Note_which_API_elements_express_string_sizes_as_counts_of_characters_and_which_express_string_sizes_as_________counts_of_bytes."></span><span id="note_which_api_elements_express_string_sizes_as_counts_of_characters_and_which_express_string_sizes_as_________counts_of_bytes."></span><span id="NOTE_WHICH_API_ELEMENTS_EXPRESS_STRING_SIZES_AS_COUNTS_OF_CHARACTERS_AND_WHICH_EXPRESS_STRING_SIZES_AS_________COUNTS_OF_BYTES."></span>Note which API elements express string sizes as counts of characters and which express string sizes as counts of bytes.
</dt> <dd>

For more information see [Data Size Conventions](data-size-conventions.md).

</dd> </dl>

 

 




