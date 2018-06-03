---
title: External Resource Type Control Codes
description: The following lists all of the external resource type control codes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a46de248-deac-4ec4-b4d3-f2b845f8057c
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- resource type control codes Failover Cluster ,external
- control codes Failover Cluster ,resource type,external
- resource types Failover Cluster ,control codes,external
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# External Resource Type Control Codes

The following lists all of the external resource type control codes.

## In this section

<dl> <dt>

[CLUSCTL\_CLOUD\_WITNESS\_RESOURCE\_TYPE\_VALIDATE\_CREDENTIALS](clusctl-cloud-witness-resource-type-validate-credentials.md)
</dt> <dd>

Retrieves the token and credentials used to validate a cluster node's access to a storage account for a [Cloud Witness](cloud-witness.md) resource. Applications use this [control code](about-control-codes.md) as a [**ClusterResourceTypeControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcetypecontrol) parameter, and [resource DLLs](resource-dlls.md) receive the control code as a parameter to the [**ResourceTypeControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_type_control_routine) function.

</dd> <dt>

[CLUSCTL\_CLOUD\_WITNESS\_RESOURCE\_TYPE\_VALIDATE\_CREDENTIALS\_WITH\_KEY](clusctl-cloud-witness-resource-type-validate-credentials-with-key.md)
</dt> <dd>

TBD

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_ENUM\_COMMON\_PROPERTIES](clusctl-resource-type-enum-common-properties.md)
</dt> <dd>

Retrieves a list of the read/write [resource type](resource-types.md) [common property](common-properties.md) names.

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_ENUM\_PRIVATE\_PROPERTIES](clusctl-resource-type-enum-private-properties.md)
</dt> <dd>

Retrieves a list of the read/write and read-only [resource type](resource-types.md) [private properties](private-properties.md).

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_GEN\_APP\_VALIDATE\_DIRECTORY](clusctl-resource-type-gen-app-validate-directory.md)
</dt> <dd>

Confirms that, for resources of type "Generic Application", the supplied directory exists.

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_GEN\_APP\_VALIDATE\_PATH](clusctl-resource-type-gen-app-validate-path.md)
</dt> <dd>

Confirms that, for resources of type "Generic Application", the server can access the file using the supplied path.

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_GEN\_SCRIPT\_VALIDATE\_PATH](clusctl-resource-type-gen-script-validate-path.md)
</dt> <dd>

Confirms that, for resources of type "Generic Script", the server can access the file using the supplied path.

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_GET\_ARB\_TIMEOUT](clusctl-resource-type-get-arb-timeout.md)
</dt> <dd>

Allows a [quorum resource](quorum-resource.md) DLL to specify a new arbitration timeout value.

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_GET\_CHARACTERISTICS](clusctl-resource-type-get-characteristics.md)
</dt> <dd>

Retrieves the intrinsic characteristics of a [resource type](resource-types.md). Applications use this [control code](about-control-codes.md) as a [**ClusterResourceTypeControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcetypecontrol) parameter, and [resource DLLs](resource-dlls.md) receive the control code as a parameter to the [**ResourceTypeControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_type_control_routine) function.

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_GET\_CLASS\_INFO](clusctl-resource-type-get-class-info.md)
</dt> <dd>

Retrieves the class and subclass of a [resource type](resource-types.md).

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_GET\_COMMON\_PROPERTIES](clusctl-resource-type-get-common-properties.md)
</dt> <dd>

Retrieves the read/write [common properties](common-properties.md) for a [resource type](resource-types.md).

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_GET\_COMMON\_PROPERTY\_FMTS](clusctl-resource-type-get-common-property-fmts.md)
</dt> <dd>

Reserved for future use.

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_GET\_COMMON\_RESOURCE\_PROPERTY\_FMTS](clusctl-resource-type-get-common-resource-property-fmts.md)
</dt> <dd>

Retrieves a [property list](property-lists.md) describing the format of each [resource common property](resource-common-properties.md).

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_GET\_CRYPTO\_CHECKPOINTS](clusctl-resource-type-get-crypto-checkpoints.md)
</dt> <dd>

The [CLUSCTL\_RESOURCE\_TYPE\_GET\_CRYPTO\_CHECKPOINTS](clusctl-resource-type-get-crypto-checkpoints.md) [control code](about-control-codes.md) is reserved for future use.

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_GET\_FLAGS](clusctl-resource-type-get-flags.md)
</dt> <dd>

Retrieves the flags that are set for a [resource type](resource-types.md).

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_GET\_PRIVATE\_PROPERTIES](clusctl-resource-type-get-private-properties.md)
</dt> <dd>

Retrieves the read/write [private properties](private-properties.md) for a [resource type](resource-types.md).

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_GET\_PRIVATE\_PROPERTY\_FMTS](clusctl-resource-type-get-private-property-fmts.md)
</dt> <dd>

Retrieves a [property list](property-lists.md) describing the format of each resource type [private property](private-properties.md).

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_GET\_PRIVATE\_RESOURCE\_PROPERTY\_FMTS](clusctl-resource-type-get-private-resource-property-fmts.md)
</dt> <dd>

Returns a [property list](property-lists.md) describing the format of each resource [private property](private-properties.md). Applications use this [control code](about-control-codes.md) as a parameter.

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_GET\_REGISTRY\_CHECKPOINTS](clusctl-resource-type-get-registry-checkpoints.md)
</dt> <dd>

The [CLUSCTL\_RESOURCE\_TYPE\_GET\_REGISTRY\_CHECKPOINTS](clusctl-resource-type-get-registry-checkpoints.md) [control code](about-control-codes.md) is reserved for future use.

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_GET\_REQUIRED\_DEPENDENCIES](clusctl-resource-type-get-required-dependencies.md)
</dt> <dd>

Retrieves a list of all required [dependencies](resource-dependencies.md) for a [resource type](resource-types.md).

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_GET\_RO\_COMMON\_PROPERTIES](clusctl-resource-type-get-ro-common-properties.md)
</dt> <dd>

Retrieves the read-only [common properties](common-properties.md) for a [resource type](resource-types.md).

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_GET\_RO\_PRIVATE\_PROPERTIES](clusctl-resource-type-get-ro-private-properties.md)
</dt> <dd>

Retrieves the read-only [private properties](private-properties.md) for a [resource type](resource-types.md).

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_NETNAME\_GET\_OU\_FOR\_VCO](clusctl-resource-type-netname-get-ou-for-vco.md)
</dt> <dd>

TBD.

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_NETNAME\_VALIDATE\_NETNAME](clusctl-resource-type-netname-validate-netname.md)
</dt> <dd>

The [CLUSCTL\_RESOURCE\_TYPE\_NETNAME\_VALIDATE\_NETNAME](clusctl-resource-type-netname-validate-netname.md) [control code](about-control-codes.md) TBD. Applications use this control code as a parameter to [**ClusterResourceTypeControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcetypecontrol) function, and [resource DLLs](resource-dlls.md) receive the control code as a parameter to the [**ResourceTypeControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_type_control_routine) callback function.

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_QUERY\_DELETE](clusctl-resource-type-query-delete.md)
</dt> <dd>

The [CLUSCTL\_RESOURCE\_TYPE\_QUERY\_DELETE](clusctl-resource-type-query-delete.md) [control code](about-control-codes.md) is reserved for future use.

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_REPLICATION\_GET\_ELIGIBLE\_LOGDISKS](clusctl-resource-type-replication-get-eligible-logdisks.md)
</dt> <dd>

Gets the eligible log disks for a data disk.

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_REPLICATION\_GET\_ELIGIBLE\_SOURCE\_DATADISKS](clusctl-resource-type-replication-get-eligible-source-datadisks.md)
</dt> <dd>

Gets the source disks that can be added to the same replication group as the specified source disk.

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_REPLICATION\_GET\_ELIGIBLE\_TARGET\_DATADISKS](clusctl-resource-type-replication-get-eligible-target-datadisks.md)
</dt> <dd>

Gets the eligible replication destination disks for the source disk.

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_REPLICATION\_GET\_LOG\_VOLUME](clusctl-resource-type-replication-get-log-volume.md)
</dt> <dd>

Gets the log volume from a physical disk resource that is in a replication relationship.

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_REPLICATION\_GET\_REPLICA\_VOLUMES](clusctl-resource-type-replication-get-replica-volumes.md)
</dt> <dd>

Gets all volumes that can be used for replication on the source disk and the destination disk.

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_REPLICATION\_GET\_REPLICATED\_DISKS](clusctl-resource-type-replication-get-replicated-disks.md)
</dt> <dd>

Retrieves the replicated disks in a cluster.

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_REPLICATION\_GET\_REPLICATED\_PARTITION\_INFO](clusctl-resource-type-replication-get-replicated-partition-info.md)
</dt> <dd>

Gets the replicated partitions on a disk.

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_REPLICATION\_GET\_RESOURCE\_GROUP](clusctl-resource-type-replication-get-resource-group.md)
</dt> <dd>

Gets all cluster resource groups that are eligible for replication.

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_SET\_COMMON\_PROPERTIES](clusctl-resource-type-set-common-properties.md)
</dt> <dd>

Updates the read/write [common properties](common-properties.md) for a [resource type](resource-types.md).

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_SET\_PRIVATE\_PROPERTIES](clusctl-resource-type-set-private-properties.md)
</dt> <dd>

Updates the read/write [private properties](private-properties.md) for a [resource type](resource-types.md).

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_GET\_AVAILABLE\_DISKS](clusctl-resource-type-storage-get-available-disks.md)
</dt> <dd>

Retrieves information about storage class devices supported by a [resource type](resource-types.md).

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_GET\_AVAILABLE\_DISKS\_EX](clusctl-resource-type-storage-get-available-disks-ex.md)
</dt> <dd>

Retrieves information about storage class devices supported by a [resource type](resource-types.md).

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_GET\_AVAILABLE\_DISKS\_EX2\_INT](clusctl-resource-type-storage-get-available-disks-ex2-int.md)
</dt> <dd>

Retrieves information about storage class devices supported by a [resource type](resource-types.md).

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_GET\_DISKID](clusctl-resource-type-storage-get-diskid.md)
</dt> <dd>

Queries the ID of a disk on the designated node.

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_GET\_DRIVELETTERS](clusctl-resource-type-storage-get-driveletters.md)
</dt> <dd>

Queries a bitmask of the driver letters that are not in use on the designated node.

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_GET\_RESOURCEID](clusctl-resource-type-storage-get-resourceid.md)
</dt> <dd>

Retrieves the resource ID string for a storage resource.

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_IS\_CLUSTERABLE](clusctl-resource-type-storage-is-clusterable.md)
</dt> <dd>

Confirms whether a disk on the designated node can be placed under cluster control.

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_IS\_CSV\_FILE](clusctl-resource-type-storage-is-csv-file.md)
</dt> <dd>

queries whether a file is stored on a CSV that is accessible to all nodes in the cluster

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_REMAP\_DRIVELETTER](clusctl-resource-type-storage-remap-driveletter.md)
</dt> <dd>

Modifies the drive letter of a disk on the designated node.

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_REMOVE\_VM\_OWNERSHIP](clusctl-resource-type-storage-remove-vm-ownership.md)
</dt> <dd>

The [CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_REMOVE\_VM\_OWNERSHIP](clusctl-resource-type-storage-remove-vm-ownership.md) [control code](about-control-codes.md) TBD. Applications use this control code as a parameter to [**ClusterResourceTypeControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcetypecontrol) function, and [resource DLLs](resource-dlls.md) receive the control code as a parameter to the [**ResourceTypeControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_type_control_routine) callback function.

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_SYNC\_CLUSDISK\_DB](clusctl-resource-type-storage-sync-clusdisk-db.md)
</dt> <dd>

The [CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_SYNC\_CLUSDISK\_DB](clusctl-resource-type-storage-sync-clusdisk-db.md) [control code](about-control-codes.md) TBD. Applications use this control code as a parameter to [**ClusterResourceTypeControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcetypecontrol) function, and [resource DLLs](resource-dlls.md) receive the control code as a parameter to the [**ResourceTypeControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_type_control_routine) callback function.

To perform this operation, call the [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) function with the following parameters.

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_UNKNOWN](clusctl-resource-type-unknown.md)
</dt> <dd>

verifies that [control codes](about-control-codes.md) are being processed on the node where execution of the control is directed.

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_VALIDATE\_COMMON\_PROPERTIES](clusctl-resource-type-validate-common-properties.md)
</dt> <dd>

Verifies that a [property list](property-lists.md) contains valid [resource type](resource-types.md) [common property](common-properties.md) names and values and that the list is properly formatted.

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_VALIDATE\_PRIVATE\_PROPERTIES](clusctl-resource-type-validate-private-properties.md)
</dt> <dd>

Verifies that a [property list](property-lists.md) contains valid [resource type](resource-types.md) property names and values and that the list is properly formatted.

</dd> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_WITNESS\_VALIDATE\_PATH](clusctl-resource-type-witness-validate-path.md)
</dt> <dd>

Confirms that the server can access the file share path for the designated resource type.

</dd> </dl>

## Related topics

<dl> <dt>

[Resource Type Control Codes](resource-type-control-codes.md)
</dt> <dt>

[**ClusterResourceTypeControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcetypecontrol)
</dt> <dt>

[**ResourceTypeControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_type_control_routine)
</dt> </dl>

 

 




