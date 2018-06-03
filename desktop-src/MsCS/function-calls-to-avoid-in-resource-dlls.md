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
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Function Calls to Avoid in Resource DLLs

Function calls involving the following functions or control codes can cause deadlock when made from resource DLLs. The following table lists these functions along with a usage code. A subsequent table describes the usage codes.



| API element                                                                                          | Usage code              |
|------------------------------------------------------------------------------------------------------|-------------------------|
| [**AddClusterResourceDependency**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_add_cluster_resource_dependency)                                 | Do not use.             |
| [**AddClusterResourceNode**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_add_cluster_resource_node)                                             | Worker thread only.     |
| [**CanResourceBeDependent**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_can_resource_be_dependent)                                             | Worker thread only.     |
| [**ChangeClusterResourceGroup**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_change_cluster_resource_group)                                     | Do not use.             |
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
| [**ClusterGroupEnum**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_group_enum)                                                         | Worker thread only.     |
| [**ClusterGroupOpenEnum**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_group_open_enum)                                                 | Worker thread only.     |
| [**ClusterRegCreateKey**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterregcreatekey)                                                   | Some entry points okay. |
| [**ClusterRegDeleteKey**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterregdeletekey)                                                   | Some entry points okay. |
| [**ClusterRegDeleteValue**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterregdeletevalue)                                               | Some entry points okay. |
| [**ClusterRegSetKeySecurity**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterregsetkeysecurity)                                         | Some entry points okay. |
| [**ClusterRegSetValue**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterregsetvalue)                                                     | Some entry points okay. |
| [**ClusterResourceEnum**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_resource_enum)                                                   | Worker thread only.     |
| [**ClusterResourceOpenEnum**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_resource_open_enum)                                           | Worker thread only.     |
| [**CreateClusterGroup**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_create_cluster_group)                                                     | Do not use.             |
| [**CreateClusterResource**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_create_cluster_resource)                                               | Do not use.             |
| [**DeleteClusterGroup**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_delete_cluster_group)                                                     | Do not use.             |
| [**DeleteClusterResource**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_delete_cluster_resource)                                               | Do not use.             |
| [**DestroyClusterGroup**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_destroy_cluster_group)                                                   | Do not use.             |
| [**FailClusterResource**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_fail_cluster_resource)                                                   | Do not use.             |
| [**GetClusterGroupState**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_get_cluster_group_state)                                                 | Worker thread only.     |
| [**GetClusterResourceNetworkName**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_get_cluster_resource_network_name)                               | Worker thread only.     |
| [**GetClusterResourceState**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_get_cluster_resource_state)                                           | Worker thread only.     |
| [**MoveClusterGroup**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_move_cluster_group)                                                         | Do not use.             |
| [**OfflineClusterGroup**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_offline_cluster_group)                                                   | Do not use.             |
| [**OfflineClusterResource**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_offline_cluster_resource)                                             | Do not use.             |
| [**OnlineClusterGroup**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_online_cluster_group)                                                     | Do not use.             |
| [**OnlineClusterResource**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_online_cluster_resource)                                               | Do not use.             |
| [**RemoveClusterResourceDependency**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_remove_cluster_resource_dependency)                           | Do not use.             |
| [**RemoveClusterResourceNode**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_remove_cluster_resource_node)                                       | Do not use.             |
| [**ResUtilFindDependentDiskResourceDriveLetter**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_find_dependent_disk_resource_drive_letter)   | Do not use.             |
| [**ResUtilGetResourceDependentIPAddressProps**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_get_resource_dependentip_address_props)       | Worker thread only.     |
| [**ResUtilGetEnvironmentWithNetName**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_get_environment_with_net_name)                         | Worker thread only.     |
| [**ResUtilGetResourceDependency**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_get_resource_dependency)                                 | Worker thread only.     |
| [**ResUtilGetResourceDependencyByClass**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_get_resource_dependency_by_class)                   | Worker thread only.     |
| [**ResUtilGetResourceDependencyByName**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_get_resource_dependency_by_name)                     | Worker thread only.     |
| [**ResUtilGetResourceNameDependency**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_get_resource_name_dependency)                         | Worker thread only.     |
| [**ResUtilSetBinaryValue**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_set_binary_value)                                               | Some entry points okay. |
| [**ResUtilSetDwordValue**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_set_dword_value)                                                 | Some entry points okay. |
| [**ResUtilSetExpandSzValue**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_set_expand_sz_value)                                           | Some entry points okay. |
| [**ResUtilSetMultiSzValue**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_set_multi_sz_value)                                             | Some entry points okay. |
| [**ResUtilSetPrivatePropertyList**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_set_private_property_list)                               | Some entry points okay. |
| [**ResUtilSetPropertyParameterBlock**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_set_property_parameter_block)                         | Some entry points okay. |
| [**ResUtilSetPropertyParameterBlockEx**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_set_property_parameter_block_ex)                     | Some entry points okay. |
| [**ResUtilSetPropertyTable**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_set_property_table)                                           | Some entry points okay. |
| [**ResUtilSetPropertyTableEx**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_set_property_table_ex)                                       | Some entry points okay. |
| [**ResUtilSetResourceServiceEnvironment**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_set_resource_service_environment)                 | Worker thread only.     |
| [**ResUtilSetSzValue**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_set_sz_value)                                                       | Some entry points okay. |
| [**ResUtilSetUnknownProperties**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_set_unknown_properties)                                   | Some entry points okay. |
| [**SetClusterGroupName**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_set_cluster_group_name)                                                   | Do not use.             |
| [**SetClusterGroupNodeList**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_set_cluster_group_node_list)                                           | Do not use.             |
| [**SetClusterName**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_setclustername)                                                             | Do not use.             |
| [**SetClusterQuorumResource**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_set_cluster_quorum_resource)                                         | Do not use.             |
| [**SetClusterResourceName**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_set_cluster_resource_name)                                             | Do not use.             |
| [**SetClusterServiceAccountPassword**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_set_cluster_service_account_password)                         | Do not use.             |



 

The following table describes the usage codes presented in the previous table.

### 



| Usage code              | Usage notes                                                                                                                                                                                                                                                                                                                           |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Some entry points okay. | Do not call these functions from the following resource DLL entry point functions: [**Close**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-pclose_routine), [**Offline**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-poffline_routine), [**Online**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-ponline_routine), [**Open**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-popen_routine), [**Terminate**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-pterminate_routine). These functions can be safely called from any other resource DLL entry point function or from a worker thread. |
| Worker thread only.     | These functions should be called only from a worker thread (see [**ClusWorkerCreate**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-pclusapi_clus_worker_create), [**ClusWorkerCheckTerminate**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-pclusapiclusworkercheckterminate), and [**ClusWorkerTerminate**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-pclusapi_clus_worker_terminate)).                                                                                                  |
| Do not use.             | Do not call any of these functions from a resource DLL. Functions in this category modify dependency relationships, add or remove resources from groups, create or delete groups or resources, cause resource or group state changes, or change the node lists of groups or resources.                                                |



 

 

 




