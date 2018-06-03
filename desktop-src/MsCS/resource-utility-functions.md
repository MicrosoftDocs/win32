---
title: Resource Utility Functions
description: The resource utility functions allow applications and resource DLLs to manage multiple cluster resources.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 42eb7c1b-6bd6-4997-b33e-ed16470c8475
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- resource utility functions Failover Cluster
- cluster utility functions Failover Cluster ,resource utility functions
- resources Failover Cluster ,utility functions
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Resource Utility Functions

The resource utility functions allow applications and [resource DLLs](resource-dlls.md) to manage multiple [cluster resources](resources.md).

## In this section

<dl> <dt>

[*ResUtilEnumResources*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_enum_resources)
</dt> <dd>

Enumerates all of the [resources](resources.md) in the local [cluster](https://www.bing.com/search?q=cluster) and initiates a user-defined operation for each resource. The **PRESUTIL\_ENUM\_RESOURCES** type defines a pointer to this function.

</dd> <dt>

[*ResUtilEnumResourcesEx*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_enum_resources_ex)
</dt> <dd>

Enumerates all of the [resources](resources.md) in a specified [cluster](https://www.bing.com/search?q=cluster) and initiates a user-defined operation for each resource. The **PRESUTIL\_ENUM\_RESOURCES\_EX** type defines a pointer to this function.

</dd> <dt>

[*ResUtilEnumResourcesEx2*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_enum_resources_ex2)
</dt> <dd>

Enumerates all of the [resources](resources.md) in a specified [cluster](https://www.bing.com/search?q=cluster) and initiates a user-defined operation for each resource. The **PRESUTIL\_ENUM\_RESOURCES\_EX2** type defines a pointer to this function.

</dd> <dt>

[*ResUtilFindDependentDiskResourceDriveLetter*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_find_dependent_disk_resource_drive_letter)
</dt> <dd>

Retrieves the drive letter associated with a [Physical Disk](physical-disk.md) [dependency](resource-dependencies.md) of a [resource](resources.md). The **PRESUTIL\_FIND\_DEPENDENT\_DISK\_RESOURCE\_DRIVE\_LETTER** type defines a pointer to this function.

</dd> <dt>

[*ResUtilFindFileTimeProperty*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_find_filetime_property)
</dt> <dd>

TBD. The **PRESUTIL\_FIND\_FILETIME\_PROPERTY** type defines a pointer to this function.

</dd> <dt>

[**ResUtilGetClusterRoleState**](/previous-versions/windows/desktop/api/ResApi/nf-resapi-resutilgetclusterrolestate)
</dt> <dd>

Determines whether or not a specific role has been assigned to a cluster.

</dd> <dt>

[*ResUtilGetCoreClusterResources*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_get_core_cluster_resources)
</dt> <dd>

Returns handles to the [core](core-resources.md) [Network Name](network-name.md), [IP Address](ip-address.md) and [quorum](quorum-resource.md) resources. The **PRESUTIL\_GET\_CORE\_CLUSTER\_RESOURCES** type defines a pointer to this function.

</dd> <dt>

[*ResUtilGetCoreClusterResourcesEx*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_get_core_cluster_resources_ex)
</dt> <dd>

Returns handles to the [core](core-resources.md), [Network Name](network-name.md), [IP Address](ip-address.md), and [quorum](quorum-resource.md) resources. The **PRESUTIL\_GET\_CORE\_CLUSTER\_RESOURCES\_EX** type defines a pointer to this function.

</dd> <dt>

[*ResUtilGetFileTimeProperty*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_get_filetime_property)
</dt> <dd>

TBD. The **PRESUTIL\_GET\_FILETIME\_PROPERTY** type defines a pointer to this function.

</dd> <dt>

[*ResUtilGetLongProperty*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_get_long_property)
</dt> <dd>

TBD. The **PRESUTIL\_GET\_LONG\_PROPERTY** type defines a pointer to this function.

</dd> <dt>

[*ResUtilGetQwordValue*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_get_qword_value)
</dt> <dd>

TBD

</dd> <dt>

[*ResUtilGetResourceDependency*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_get_resource_dependency)
</dt> <dd>

Enumerates the [dependencies](resource-dependencies.md) of a specified [resource](resources.md) and returns a handle to a dependency of a specified type. The **PRESUTIL\_GET\_RESOURCE\_DEPENDENCY** type defines a pointer to this function.

</dd> <dt>

[*ResUtilGetResourceDependencyByClass*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_get_resource_dependency_by_class)
</dt> <dd>

Enumerates the [dependencies](resource-dependencies.md) of a specified [resource](resources.md) in a specified [cluster](https://www.bing.com/search?q=cluster) and returns a handle to a dependency that matches a specified resource class. The **PRESUTIL\_GET\_RESOURCE\_DEPENDENCY\_BY\_CLASS** type defines a pointer to this function.

</dd> <dt>

[*ResUtilGetResourceDependencyByClassEx*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_get_resource_dependency_by_class_ex)
</dt> <dd>

Enumerates the [dependencies](resource-dependencies.md) of a specified [resource](resources.md) in a specified [cluster](https://www.bing.com/search?q=cluster) and returns a handle to a dependency that matches a specified resource class. The **PRESUTIL\_GET\_RESOURCE\_DEPENDENCY\_BY\_CLASS\_EX** type defines a pointer to this function.

</dd> <dt>

[*ResUtilGetResourceDependencyByName*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_get_resource_dependency_by_name)
</dt> <dd>

Enumerates the [dependencies](resource-dependencies.md) of a specified [resource](resources.md) in a specified [cluster](https://www.bing.com/search?q=cluster) and returns a handle to a dependency of a specified type. The **PRESUTIL\_GET\_RESOURCE\_DEPENDENCY\_BY\_NAME** type defines a pointer to this function.

</dd> <dt>

[**ResUtilGetResourceDependencyByNameEx**](/previous-versions/windows/desktop/api/ResApi/nf-resapi-resutilgetresourcedependencybyname)
</dt> <dd>

Enumerates the [dependencies](resource-dependencies.md) of a specified [resource](resources.md) in a specified [cluster](https://www.bing.com/search?q=cluster) and returns a handle to a dependency of a specified type. The **PRESUTIL\_GET\_RESOURCE\_DEPENDENCY\_BY\_NAME\_EX** type defines a pointer to this function.

</dd> <dt>

[*ResUtilGetResourceDependencyEx*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_get_resource_dependency_ex)
</dt> <dd>

Enumerates the [dependencies](resource-dependencies.md) of a specified [resource](resources.md) and returns a handle to a dependency of a specified type. The **PRESUTIL\_GET\_RESOURCE\_DEPENDENCY\_EX** type defines a pointer to this function.

</dd> <dt>

[*ResUtilGetResourceDependentIPAddressProps*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_get_resource_dependentip_address_props)
</dt> <dd>

Retrieves the [private properties](private-properties.md) of the first IP Address [dependency](resource-dependencies.md) found for a specified [resource](resources.md). The **PRESUTIL\_GET\_RESOURCE\_DEPENDENTIP\_ADDRESS\_PROPS** type defines a pointer to this function.

</dd> <dt>

[*ResUtilGetResourceName*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_get_resource_name)
</dt> <dd>

Returns the name of a [resource](resources.md). The **PRESUTIL\_GET\_RESOURCE\_NAME** type defines a pointer to this function.

</dd> <dt>

[*ResUtilGetResourceNameDependency*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_get_resource_name_dependency)
</dt> <dd>

Enumerates the [dependencies](resource-dependencies.md) of a specified [resource](resources.md) in the local [cluster](https://www.bing.com/search?q=cluster) and returns a handle to a dependency of a specified [resource type](resource-types.md). The **PRESUTIL\_GET\_RESOURCE\_NAME\_DEPENDENCY** type defines a pointer to this function.

</dd> <dt>

[*ResUtilGetResourceNameDependencyEx*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_get_resource_name_dependency_ex)
</dt> <dd>

Enumerates the [dependencies](resource-dependencies.md) of a specified [resource](resources.md) in the local [cluster](https://www.bing.com/search?q=cluster) and returns a handle to a dependency of a specified [resource type](resource-types.md). The **PRESUTIL\_GET\_RESOURCE\_NAME\_DEPENDENCY\_EX** type defines a pointer to this function.

</dd> <dt>

[*ResUtilIsResourceClassEqual*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_is_resource_class_equal)
</dt> <dd>

Tests whether the resource class of a specified [resource](resources.md) is equal to a specified resource class. The **PRESUTIL\_IS\_RESOURCE\_CLASS\_EQUAL** type defines a pointer to this function.

</dd> <dt>

[**ResUtilLeftPaxosIsLessThanRight**](/previous-versions/windows/desktop/api/ResApi/nf-resapi-resutilleftpaxosislessthanright)
</dt> <dd>

Indicates whether a specified Paxos tag contains older cluster configuration information than another specified Paxos tag.

</dd> <dt>

[**ResUtilPaxosComparer**](/previous-versions/windows/desktop/api/ResApi/nf-resapi-resutilpaxoscomparer)
</dt> <dd>

Compares two Paxos tags and indicates whether they have the same values.

</dd> <dt>

[*ResUtilResourcesEqual*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_resources_equal)
</dt> <dd>

Tests whether two resource handles represent the same [resource](resources.md). The **PRESUTIL\_RESOURCES\_EQUAL** type defines a pointer to this function.

</dd> <dt>

[*ResUtilResourceTypesEqual*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_resource_types_equal)
</dt> <dd>

Tests whether a [resource type](resource-types.md) matches the resource type name of a specified [resource](resources.md). The **PRESUTIL\_RESOURCE\_TYPES\_EQUAL** type defines a pointer to this function.

</dd> <dt>

[*ResUtilSetQwordValue*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_set_qword_value)
</dt> <dd>

TBD. The **PRESUTIL\_SET\_QWORD\_VALUE** type defines a pointer to this function.

</dd> </dl>

## Related topics

<dl> <dt>

[Failover Cluster Utility Functions](cluster-utility-functions.md)
</dt> </dl>

 

 




