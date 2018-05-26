---
title: Function Calls to Avoid in Resource DLLs
description: Function calls involving the following functions or control codes can cause deadlock when made from resource DLLs. The following table lists these functions along with a usage code. A subsequent table describes the usage codes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0eaa4aea-8d9a-4552-b43a-fafa23a3e736
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- resource DLLs Failover Cluster ,function calls to avoid
- entry point functions Failover Cluster ,function calls to avoid in resource DLLs
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Function Calls to Avoid in Resource DLLs

Function calls involving the following functions or control codes can cause deadlock when made from resource DLLs. The following table lists these functions along with a usage code. A subsequent table describes the usage codes.



| API element                                                                                          | Usage code              |
|------------------------------------------------------------------------------------------------------|-------------------------|
| [**AddClusterResourceDependency**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_add_cluster_resource_dependency?branch=master)                                 | Do not use.             |
| [**AddClusterResourceNode**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_add_cluster_resource_node?branch=master)                                             | Worker thread only.     |
| [**CanResourceBeDependent**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_can_resource_be_dependent?branch=master)                                             | Worker thread only.     |
| [**ChangeClusterResourceGroup**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_change_cluster_resource_group?branch=master)                                     | Do not use.             |
| [CLUSCTL\_GROUP\_ENUM\_COMMON\_PROPERTIES](clusctl-group-enum-common-properties.md)                 | Worker thread only.     |
| [CLUSCTL\_GROUP\_ENUM\_PRIVATE\_PROPERTIES](clusctl-group-enum-private-properties.md)               | Worker thread only.     |
| [CLUSCTL\_GROUP\_GET\_CHARACTERISTICS](clusctl-group-get-characteristics.md)                        | Worker thread only.     |
| [CLUSCTL\_GROUP\_GET\_COMMON\_PROPERTIES](clusctl-group-get-common-properties.md)                   | Worker thread only.     |
| [CLUSCTL\_GROUP\_GET\_COMMON\_PROPERTY\_FMTS](clusctl-group-get-common-property-fmts.md)            | Worker thread only.     |
| [CLUSCTL\_GROUP\_GET\_FLAGS](clusctl-group-get-flags.md)                                            | Worker thread only.     |
| [CLUSCTL\_GROUP\_GET\_ID](clusctl-group-get-id.md)                                                  | Worker thread only.     |
| [CLUSCTL\_GROUP\_GET\_NAME](clusctl-group-get-name.md)                                              | Worker thread only.     |
| [CLUSCTL\_GROUP\_GET\_PRIVATE\_PROPERTIES](clusctl-group-get-private-properties.md)                 | Worker thread only.     |
| [CLUSCTL\_GROUP\_GET\_PRIVATE\_PROPERTY\_FMTS](clusctl-group-get-private-property-fmts.md)          | Worker thread only.     |
| [CLUSCTL\_GROUP\_GET\_RO\_COMMON\_PROPERTIES](clusctl-group-get-ro-common-properties.md)            | Worker thread only.     |
| [CLUSCTL\_GROUP\_GET\_RO\_PRIVATE\_PROPERTIES](clusctl-group-get-ro-private-properties.md)          | Worker thread only.     |
| [CLUSCTL\_GROUP\_QUERY\_DELETE](clusctl-group-query-delete.md)                                      | Worker thread only.     |
| [CLUSCTL\_GROUP\_SET\_COMMON\_PROPERTIES](clusctl-group-set-common-properties.md)                   | Worker thread only.     |
| [CLUSCTL\_GROUP\_SET\_PRIVATE\_PROPERTIES](clusctl-group-set-private-properties.md)                 | Worker thread only.     |
| [CLUSCTL\_GROUP\_UNKNOWN](clusctl-group-unknown.md)                                                 | Worker thread only.     |
| [CLUSCTL\_GROUP\_VALIDATE\_COMMON\_PROPERTIES](clusctl-group-validate-common-properties.md)         | Worker thread only.     |
| [CLUSCTL\_GROUP\_VALIDATE\_PRIVATE\_PROPERTIES](clusctl-group-validate-private-properties.md)       | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_ADD\_DEPENDENCY](clusctl-resource-add-dependency.md)                            | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_ADD\_OWNER](clusctl-resource-add-owner.md)                                      | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_CLUSTER\_NAME\_CHANGED](clusctl-resource-cluster-name-changed.md)               | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_CLUSTER\_VERSION\_CHANGED](clusctl-resource-cluster-version-changed.md)         | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_DELETE](clusctl-resource-delete.md)                                             | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_ENUM\_COMMON\_PROPERTIES](clusctl-resource-enum-common-properties.md)           | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_ENUM\_PRIVATE\_PROPERTIES](clusctl-resource-enum-private-properties.md)         | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_EVICT\_NODE](clusctl-resource-evict-node.md)                                    | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_GET\_CHARACTERISTICS](clusctl-resource-get-characteristics.md)                  | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_GET\_CLASS\_INFO](clusctl-resource-get-class-info.md)                           | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_GET\_COMMON\_PROPERTIES](clusctl-resource-get-common-properties.md)             | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_GET\_FLAGS](clusctl-resource-get-flags.md)                                      | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_GET\_ID](clusctl-resource-get-id.md)                                            | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_GET\_NAME](clusctl-resource-get-name.md)                                        | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_GET\_NETWORK\_NAME](clusctl-resource-get-network-name.md)                       | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_GET\_PRIVATE\_PROPERTIES](clusctl-resource-get-private-properties.md)           | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_GET\_REQUIRED\_DEPENDENCIES](clusctl-resource-get-required-dependencies.md)     | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_GET\_RESOURCE\_TYPE](clusctl-resource-get-resource-type.md)                     | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_GET\_RO\_COMMON\_PROPERTIES](clusctl-resource-get-ro-common-properties.md)      | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_GET\_RO\_PRIVATE\_PROPERTIES](clusctl-resource-get-ro-private-properties.md)    | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_INSTALL\_NODE](clusctl-resource-install-node.md)                                | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_REMOVE\_DEPENDENCY](clusctl-resource-remove-dependency.md)                      | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_REMOVE\_OWNER](clusctl-resource-remove-owner.md)                                | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_SET\_COMMON\_PROPERTIES](clusctl-resource-set-common-properties.md)             | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_SET\_NAME](clusctl-resource-set-name.md)                                        | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_SET\_PRIVATE\_PROPERTIES](clusctl-resource-set-private-properties.md)           | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_STORAGE\_GET\_DISK\_INFO](clusctl-resource-storage-get-disk-info.md)            | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_STORAGE\_GET\_DISK\_INFO\_EX](clusctl-resource-storage-get-disk-info-ex.md)     | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_STORAGE\_GET\_MOUNTPOINTS](clusctl-resource-storage-get-mountpoints.md)         | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_STORAGE\_IS\_PATH\_VALID](clusctl-resource-storage-is-path-valid.md)            | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_UNKNOWN](clusctl-resource-unknown.md)                                           | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_VALIDATE\_COMMON\_PROPERTIES](clusctl-resource-validate-common-properties.md)   | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_VALIDATE\_PRIVATE\_PROPERTIES](clusctl-resource-validate-private-properties.md) | Worker thread only.     |
| [**ClusterGroupEnum**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_group_enum?branch=master)                                                         | Worker thread only.     |
| [**ClusterGroupOpenEnum**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_group_open_enum?branch=master)                                                 | Worker thread only.     |
| [**ClusterRegCreateKey**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterregcreatekey?branch=master)                                                   | Some entry points okay. |
| [**ClusterRegDeleteKey**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterregdeletekey?branch=master)                                                   | Some entry points okay. |
| [**ClusterRegDeleteValue**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterregdeletevalue?branch=master)                                               | Some entry points okay. |
| [**ClusterRegSetKeySecurity**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterregsetkeysecurity?branch=master)                                         | Some entry points okay. |
| [**ClusterRegSetValue**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterregsetvalue?branch=master)                                                     | Some entry points okay. |
| [**ClusterResourceEnum**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_resource_enum?branch=master)                                                   | Worker thread only.     |
| [**ClusterResourceOpenEnum**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_resource_open_enum?branch=master)                                           | Worker thread only.     |
| [**CreateClusterGroup**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_create_cluster_group?branch=master)                                                     | Do not use.             |
| [**CreateClusterResource**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_create_cluster_resource?branch=master)                                               | Do not use.             |
| [**DeleteClusterGroup**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_delete_cluster_group?branch=master)                                                     | Do not use.             |
| [**DeleteClusterResource**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_delete_cluster_resource?branch=master)                                               | Do not use.             |
| [**DestroyClusterGroup**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_destroy_cluster_group?branch=master)                                                   | Do not use.             |
| [**FailClusterResource**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_fail_cluster_resource?branch=master)                                                   | Do not use.             |
| [**GetClusterGroupState**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_get_cluster_group_state?branch=master)                                                 | Worker thread only.     |
| [**GetClusterResourceNetworkName**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_get_cluster_resource_network_name?branch=master)                               | Worker thread only.     |
| [**GetClusterResourceState**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_get_cluster_resource_state?branch=master)                                           | Worker thread only.     |
| [**MoveClusterGroup**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_move_cluster_group?branch=master)                                                         | Do not use.             |
| [**OfflineClusterGroup**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_offline_cluster_group?branch=master)                                                   | Do not use.             |
| [**OfflineClusterResource**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_offline_cluster_resource?branch=master)                                             | Do not use.             |
| [**OnlineClusterGroup**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_online_cluster_group?branch=master)                                                     | Do not use.             |
| [**OnlineClusterResource**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_online_cluster_resource?branch=master)                                               | Do not use.             |
| [**RemoveClusterResourceDependency**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_remove_cluster_resource_dependency?branch=master)                           | Do not use.             |
| [**RemoveClusterResourceNode**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_remove_cluster_resource_node?branch=master)                                       | Do not use.             |
| [**ResUtilFindDependentDiskResourceDriveLetter**](/windows/previous-versions/ResApi/nc-resapi-presutil_find_dependent_disk_resource_drive_letter?branch=master)   | Do not use.             |
| [**ResUtilGetResourceDependentIPAddressProps**](/windows/previous-versions/ResApi/nc-resapi-presutil_get_resource_dependentip_address_props?branch=master)       | Worker thread only.     |
| [**ResUtilGetEnvironmentWithNetName**](/windows/previous-versions/ResApi/nc-resapi-presutil_get_environment_with_net_name?branch=master)                         | Worker thread only.     |
| [**ResUtilGetResourceDependency**](/windows/previous-versions/ResApi/nc-resapi-presutil_get_resource_dependency?branch=master)                                 | Worker thread only.     |
| [**ResUtilGetResourceDependencyByClass**](/windows/previous-versions/ResApi/nc-resapi-presutil_get_resource_dependency_by_class?branch=master)                   | Worker thread only.     |
| [**ResUtilGetResourceDependencyByName**](/windows/previous-versions/ResApi/nc-resapi-presutil_get_resource_dependency_by_name?branch=master)                     | Worker thread only.     |
| [**ResUtilGetResourceNameDependency**](/windows/previous-versions/ResApi/nc-resapi-presutil_get_resource_name_dependency?branch=master)                         | Worker thread only.     |
| [**ResUtilSetBinaryValue**](/windows/previous-versions/ResApi/nc-resapi-presutil_set_binary_value?branch=master)                                               | Some entry points okay. |
| [**ResUtilSetDwordValue**](/windows/previous-versions/ResApi/nc-resapi-presutil_set_dword_value?branch=master)                                                 | Some entry points okay. |
| [**ResUtilSetExpandSzValue**](/windows/previous-versions/ResApi/nc-resapi-presutil_set_expand_sz_value?branch=master)                                           | Some entry points okay. |
| [**ResUtilSetMultiSzValue**](/windows/previous-versions/ResApi/nc-resapi-presutil_set_multi_sz_value?branch=master)                                             | Some entry points okay. |
| [**ResUtilSetPrivatePropertyList**](/windows/previous-versions/ResApi/nc-resapi-presutil_set_private_property_list?branch=master)                               | Some entry points okay. |
| [**ResUtilSetPropertyParameterBlock**](/windows/previous-versions/ResApi/nc-resapi-presutil_set_property_parameter_block?branch=master)                         | Some entry points okay. |
| [**ResUtilSetPropertyParameterBlockEx**](/windows/previous-versions/ResApi/nc-resapi-presutil_set_property_parameter_block_ex?branch=master)                     | Some entry points okay. |
| [**ResUtilSetPropertyTable**](/windows/previous-versions/ResApi/nc-resapi-presutil_set_property_table?branch=master)                                           | Some entry points okay. |
| [**ResUtilSetPropertyTableEx**](/windows/previous-versions/ResApi/nc-resapi-presutil_set_property_table_ex?branch=master)                                       | Some entry points okay. |
| [**ResUtilSetResourceServiceEnvironment**](/windows/previous-versions/ResApi/nc-resapi-presutil_set_resource_service_environment?branch=master)                 | Worker thread only.     |
| [**ResUtilSetSzValue**](/windows/previous-versions/ResApi/nc-resapi-presutil_set_sz_value?branch=master)                                                       | Some entry points okay. |
| [**ResUtilSetUnknownProperties**](/windows/previous-versions/ResApi/nc-resapi-presutil_set_unknown_properties?branch=master)                                   | Some entry points okay. |
| [**SetClusterGroupName**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_set_cluster_group_name?branch=master)                                                   | Do not use.             |
| [**SetClusterGroupNodeList**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_set_cluster_group_node_list?branch=master)                                           | Do not use.             |
| [**SetClusterName**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_setclustername?branch=master)                                                             | Do not use.             |
| [**SetClusterQuorumResource**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_set_cluster_quorum_resource?branch=master)                                         | Do not use.             |
| [**SetClusterResourceName**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_set_cluster_resource_name?branch=master)                                             | Do not use.             |
| [**SetClusterServiceAccountPassword**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_set_cluster_service_account_password?branch=master)                         | Do not use.             |



 

The following table describes the usage codes presented in the previous table.

### 



| Usage code              | Usage notes                                                                                                                                                                                                                                                                                                                           |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Some entry points okay. | Do not call these functions from the following resource DLL entry point functions: [**Close**](/windows/previous-versions/ResApi/nc-resapi-pclose_routine?branch=master), [**Offline**](/windows/previous-versions/ResApi/nc-resapi-poffline_routine?branch=master), [**Online**](/windows/previous-versions/ResApi/nc-resapi-ponline_routine?branch=master), [**Open**](/windows/previous-versions/ResApi/nc-resapi-popen_routine?branch=master), [**Terminate**](/windows/previous-versions/ResApi/nc-resapi-pterminate_routine?branch=master). These functions can be safely called from any other resource DLL entry point function or from a worker thread. |
| Worker thread only.     | These functions should be called only from a worker thread (see [**ClusWorkerCreate**](/windows/previous-versions/ResApi/nc-resapi-pclusapi_clus_worker_create?branch=master), [**ClusWorkerCheckTerminate**](/windows/previous-versions/ResApi/nc-resapi-pclusapiclusworkercheckterminate?branch=master), and [**ClusWorkerTerminate**](/windows/previous-versions/ResApi/nc-resapi-pclusapi_clus_worker_terminate?branch=master)).                                                                                                  |
| Do not use.             | Do not call any of these functions from a resource DLL. Functions in this category modify dependency relationships, add or remove resources from groups, create or delete groups or resources, cause resource or group state changes, or change the node lists of groups or resources.                                                |



 

 

 




