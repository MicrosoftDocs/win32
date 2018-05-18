---
title: Resource Utility Functions
description: The resource utility functions allow applications and resource DLLs to manage multiple cluster resources.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '42eb7c1b-6bd6-4997-b33e-ed16470c8475'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["resource utility functions Failover Cluster", "cluster utility functions Failover Cluster ,resource utility functions", "resources Failover Cluster ,utility functions"]
---

# Resource Utility Functions

The resource utility functions allow applications and [resource DLLs](resource-dlls.md) to manage multiple [cluster resources](resources.md).

## In this section

<dl> <dt>

[*ResUtilEnumResources*](resutilenumresources.md)
</dt> <dd>

Enumerates all of the [resources](resources.md) in the local [cluster](c-gly.md#-wolf-cluster-gly) and initiates a user-defined operation for each resource. The **PRESUTIL\_ENUM\_RESOURCES** type defines a pointer to this function.

</dd> <dt>

[*ResUtilEnumResourcesEx*](resutilenumresourcesex.md)
</dt> <dd>

Enumerates all of the [resources](resources.md) in a specified [cluster](c-gly.md#-wolf-cluster-gly) and initiates a user-defined operation for each resource. The **PRESUTIL\_ENUM\_RESOURCES\_EX** type defines a pointer to this function.

</dd> <dt>

[*ResUtilEnumResourcesEx2*](resutilenumresourcesex2.md)
</dt> <dd>

Enumerates all of the [resources](resources.md) in a specified [cluster](c-gly.md#-wolf-cluster-gly) and initiates a user-defined operation for each resource. The **PRESUTIL\_ENUM\_RESOURCES\_EX2** type defines a pointer to this function.

</dd> <dt>

[*ResUtilFindDependentDiskResourceDriveLetter*](resutilfinddependentdiskresourcedriveletter.md)
</dt> <dd>

Retrieves the drive letter associated with a [Physical Disk](physical-disk.md) [dependency](resource-dependencies.md) of a [resource](resources.md). The **PRESUTIL\_FIND\_DEPENDENT\_DISK\_RESOURCE\_DRIVE\_LETTER** type defines a pointer to this function.

</dd> <dt>

[*ResUtilFindFileTimeProperty*](resutilfindfiletimeproperty.md)
</dt> <dd>

TBD. The **PRESUTIL\_FIND\_FILETIME\_PROPERTY** type defines a pointer to this function.

</dd> <dt>

[**ResUtilGetClusterRoleState**](resutilgetclusterrolestate.md)
</dt> <dd>

Determines whether or not a specific role has been assigned to a cluster.

</dd> <dt>

[*ResUtilGetCoreClusterResources*](resutilgetcoreclusterresources.md)
</dt> <dd>

Returns handles to the [core](core-resources.md) [Network Name](network-name.md), [IP Address](ip-address.md) and [quorum](quorum-resource.md) resources. The **PRESUTIL\_GET\_CORE\_CLUSTER\_RESOURCES** type defines a pointer to this function.

</dd> <dt>

[*ResUtilGetCoreClusterResourcesEx*](resutilgetcoreclusterresourcesex.md)
</dt> <dd>

Returns handles to the [core](core-resources.md), [Network Name](network-name.md), [IP Address](ip-address.md), and [quorum](quorum-resource.md) resources. The **PRESUTIL\_GET\_CORE\_CLUSTER\_RESOURCES\_EX** type defines a pointer to this function.

</dd> <dt>

[*ResUtilGetFileTimeProperty*](resutilgetfiletimeproperty.md)
</dt> <dd>

TBD. The **PRESUTIL\_GET\_FILETIME\_PROPERTY** type defines a pointer to this function.

</dd> <dt>

[*ResUtilGetLongProperty*](resutilgetlongproperty.md)
</dt> <dd>

TBD. The **PRESUTIL\_GET\_LONG\_PROPERTY** type defines a pointer to this function.

</dd> <dt>

[*ResUtilGetQwordValue*](resutilgetqwordvalue.md)
</dt> <dd>

TBD

</dd> <dt>

[*ResUtilGetResourceDependency*](resutilgetresourcedependency.md)
</dt> <dd>

Enumerates the [dependencies](resource-dependencies.md) of a specified [resource](resources.md) and returns a handle to a dependency of a specified type. The **PRESUTIL\_GET\_RESOURCE\_DEPENDENCY** type defines a pointer to this function.

</dd> <dt>

[*ResUtilGetResourceDependencyByClass*](resutilgetresourcedependencybyclass.md)
</dt> <dd>

Enumerates the [dependencies](resource-dependencies.md) of a specified [resource](resources.md) in a specified [cluster](c-gly.md#-wolf-cluster-gly) and returns a handle to a dependency that matches a specified resource class. The **PRESUTIL\_GET\_RESOURCE\_DEPENDENCY\_BY\_CLASS** type defines a pointer to this function.

</dd> <dt>

[*ResUtilGetResourceDependencyByClassEx*](resutilgetresourcedependencybyclassex.md)
</dt> <dd>

Enumerates the [dependencies](resource-dependencies.md) of a specified [resource](resources.md) in a specified [cluster](c-gly.md#-wolf-cluster-gly) and returns a handle to a dependency that matches a specified resource class. The **PRESUTIL\_GET\_RESOURCE\_DEPENDENCY\_BY\_CLASS\_EX** type defines a pointer to this function.

</dd> <dt>

[*ResUtilGetResourceDependencyByName*](resutilgetresourcedependencybyname.md)
</dt> <dd>

Enumerates the [dependencies](resource-dependencies.md) of a specified [resource](resources.md) in a specified [cluster](c-gly.md#-wolf-cluster-gly) and returns a handle to a dependency of a specified type. The **PRESUTIL\_GET\_RESOURCE\_DEPENDENCY\_BY\_NAME** type defines a pointer to this function.

</dd> <dt>

[**ResUtilGetResourceDependencyByNameEx**](resutilgetresourcedependencybynameex.md)
</dt> <dd>

Enumerates the [dependencies](resource-dependencies.md) of a specified [resource](resources.md) in a specified [cluster](c-gly.md#-wolf-cluster-gly) and returns a handle to a dependency of a specified type. The **PRESUTIL\_GET\_RESOURCE\_DEPENDENCY\_BY\_NAME\_EX** type defines a pointer to this function.

</dd> <dt>

[*ResUtilGetResourceDependencyEx*](resutilgetresourcedependencyex.md)
</dt> <dd>

Enumerates the [dependencies](resource-dependencies.md) of a specified [resource](resources.md) and returns a handle to a dependency of a specified type. The **PRESUTIL\_GET\_RESOURCE\_DEPENDENCY\_EX** type defines a pointer to this function.

</dd> <dt>

[*ResUtilGetResourceDependentIPAddressProps*](resutilgetresourcedependentipaddressprops.md)
</dt> <dd>

Retrieves the [private properties](private-properties.md) of the first IP Address [dependency](resource-dependencies.md) found for a specified [resource](resources.md). The **PRESUTIL\_GET\_RESOURCE\_DEPENDENTIP\_ADDRESS\_PROPS** type defines a pointer to this function.

</dd> <dt>

[*ResUtilGetResourceName*](resutilgetresourcename.md)
</dt> <dd>

Returns the name of a [resource](resources.md). The **PRESUTIL\_GET\_RESOURCE\_NAME** type defines a pointer to this function.

</dd> <dt>

[*ResUtilGetResourceNameDependency*](resutilgetresourcenamedependency.md)
</dt> <dd>

Enumerates the [dependencies](resource-dependencies.md) of a specified [resource](resources.md) in the local [cluster](c-gly.md#-wolf-cluster-gly) and returns a handle to a dependency of a specified [resource type](resource-types.md). The **PRESUTIL\_GET\_RESOURCE\_NAME\_DEPENDENCY** type defines a pointer to this function.

</dd> <dt>

[*ResUtilGetResourceNameDependencyEx*](resutilgetresourcenamedependencyex.md)
</dt> <dd>

Enumerates the [dependencies](resource-dependencies.md) of a specified [resource](resources.md) in the local [cluster](c-gly.md#-wolf-cluster-gly) and returns a handle to a dependency of a specified [resource type](resource-types.md). The **PRESUTIL\_GET\_RESOURCE\_NAME\_DEPENDENCY\_EX** type defines a pointer to this function.

</dd> <dt>

[*ResUtilIsResourceClassEqual*](resutilisresourceclassequal.md)
</dt> <dd>

Tests whether the resource class of a specified [resource](resources.md) is equal to a specified resource class. The **PRESUTIL\_IS\_RESOURCE\_CLASS\_EQUAL** type defines a pointer to this function.

</dd> <dt>

[**ResUtilLeftPaxosIsLessThanRight**](resutilleftpaxosislessthanright.md)
</dt> <dd>

Indicates whether a specified Paxos tag contains older cluster configuration information than another specified Paxos tag.

</dd> <dt>

[**ResUtilPaxosComparer**](resutilpaxoscomparer.md)
</dt> <dd>

Compares two Paxos tags and indicates whether they have the same values.

</dd> <dt>

[*ResUtilResourcesEqual*](resutilresourcesequal.md)
</dt> <dd>

Tests whether two resource handles represent the same [resource](resources.md). The **PRESUTIL\_RESOURCES\_EQUAL** type defines a pointer to this function.

</dd> <dt>

[*ResUtilResourceTypesEqual*](resutilresourcetypesequal.md)
</dt> <dd>

Tests whether a [resource type](resource-types.md) matches the resource type name of a specified [resource](resources.md). The **PRESUTIL\_RESOURCE\_TYPES\_EQUAL** type defines a pointer to this function.

</dd> <dt>

[*ResUtilSetQwordValue*](resutilsetqwordvalue.md)
</dt> <dd>

TBD. The **PRESUTIL\_SET\_QWORD\_VALUE** type defines a pointer to this function.

</dd> </dl>

## Related topics

<dl> <dt>

[Failover Cluster Utility Functions](cluster-utility-functions.md)
</dt> </dl>

 

 




