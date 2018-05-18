---
title: External Resource Control Codes
description: The following lists all of the external control codes for resources.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '669e9e2e-8f09-42ed-be99-024464eb89bd'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["resource control codes Failover Cluster ,external", "control codes Failover Cluster ,resource,external", "resources Failover Cluster ,control codes,external"]
---

# External Resource Control Codes

The following lists all of the external control codes for resources.

## In this section

<dl> <dt>

[CLUSCTL\_CLOUD\_WITNESS\_RESOURCE\_UPDATE\_KEY](clusctl-cloud-witness-resource-update-key.md)
</dt> <dd>

TBD.

</dd> <dt>

[CLUSCTL\_CLOUD\_WITNESS\_RESOURCE\_UPDATE\_TOKEN](clusctl-cloud-witness-resource-update-token.md)
</dt> <dd>

Updates the token used to validate a set of credentials for an [Cloud Witness](cloud-witness.md) resource.

</dd> <dt>

[CLUSCTL\_RESOURCE\_ADD\_CRYPTO\_CHECKPOINT](clusctl-resource-add-crypto-checkpoint.md)
</dt> <dd>

Adds a cryptographic key container to the list of keys that are replicated for a [resource](resources.md). Applications use this [control code](about-control-codes.md) as a [**ClusterResourceControl**](clusterresourcecontrol.md) parameter.

</dd> <dt>

[CLUSCTL\_RESOURCE\_ADD\_CRYPTO\_CHECKPOINT\_EX](clusctl-resource-add-crypto-checkpoint-ex.md)
</dt> <dd>

TBD.

</dd> <dt>

[CLUSCTL\_RESOURCE\_ADD\_REGISTRY\_CHECKPOINT](clusctl-resource-add-registry-checkpoint.md)
</dt> <dd>

Adds a registry tree to the list of registry trees that are replicated for a [resource](resources.md). Applications use this [control code](about-control-codes.md) as a parameter in the [**ClusterResourceControl**](clusterresourcecontrol.md) function.

</dd> <dt>

[CLUSCTL\_RESOURCE\_ADD\_REGISTRY\_CHECKPOINT\_32BIT](clusctl-resource-add-registry-checkpoint-32bit.md)
</dt> <dd>

Adds a registry tree using the 32-bit view of the registry to the list of registry trees that are replicated for a [resource](resources.md). Applications use this [control code](about-control-codes.md) as a parameter in the [**ClusterResourceControl**](clusterresourcecontrol.md) function.

</dd> <dt>

[CLUSCTL\_RESOURCE\_ADD\_REGISTRY\_CHECKPOINT\_64BIT](clusctl-resource-add-registry-checkpoint-64bit.md)
</dt> <dd>

Adds a registry tree using the 64-bit view of the registry to the list of registry trees that are replicated for a [resource](resources.md). Applications use this [control code](about-control-codes.md) as a parameter in the [**ClusterResourceControl**](clusterresourcecontrol.md) function.

</dd> <dt>

[CLUSCTL\_RESOURCE\_DELETE\_CRYPTO\_CHECKPOINT](clusctl-resource-delete-crypto-checkpoint.md)
</dt> <dd>

Removes a cryptographic key container from the list of keys that are being replicated for a resource.

</dd> <dt>

[CLUSCTL\_RESOURCE\_DELETE\_REGISTRY\_CHECKPOINT](clusctl-resource-delete-registry-checkpoint.md)
</dt> <dd>

Removes a registry tree from the list of registry trees that are being replicated for a [resource](resources.md). Applications use this [control code](about-control-codes.md) as a [**ClusterResourceControl**](clusterresourcecontrol.md) parameter.

</dd> <dt>

[CLUSCTL\_RESOURCE\_DISABLE\_SHARED\_VOLUME\_DIRECTIO](clusctl-resource-disable-shared-volume-directio.md)
</dt> <dd>

Disables higher performance I/O on the cluster shared volume.

</dd> <dt>

[CLUSCTL\_RESOURCE\_ENABLE\_SHARED\_VOLUME\_DIRECTIO](clusctl-resource-enable-shared-volume-directio.md)
</dt> <dd>

Enables higher performance I/O on the cluster shared volume.

</dd> <dt>

[CLUSCTL\_RESOURCE\_ENUM\_COMMON\_PROPERTIES](clusctl-resource-enum-common-properties.md)
</dt> <dd>

Retrieves a list of the read/write [resource](resources.md) [common property](common-properties.md) names.

</dd> <dt>

[CLUSCTL\_RESOURCE\_ENUM\_PRIVATE\_PROPERTIES](clusctl-resource-enum-private-properties.md)
</dt> <dd>

Retrieves a list of the read/write [private](private-properties.md) and read-only [resource](resources.md) properties.

</dd> <dt>

[CLUSCTL\_RESOURCE\_FILESERVER\_SHARE\_ADD](clusctl-resource-fileserver-share-add.md)
</dt> <dd>

Creates a new file share on a physical disk resource.

</dd> <dt>

[CLUSCTL\_RESOURCE\_FILESERVER\_SHARE\_DEL](clusctl-resource-fileserver-share-del.md)
</dt> <dd>

Deletes a file share on a physical disk resource.

</dd> <dt>

[CLUSCTL\_RESOURCE\_FILESERVER\_SHARE\_MODIFY](clusctl-resource-fileserver-share-modify.md)
</dt> <dd>

Modifies an existing file share on a physical disk resource.

</dd> <dt>

[CLUSCTL\_RESOURCE\_FILESERVER\_SHARE\_REPORT](clusctl-resource-fileserver-share-report.md)
</dt> <dd>

Retrieves the add/delete/change notifications for file shares managed by the File Server [resource](resources.md).

</dd> <dt>

[CLUSCTL\_RESOURCE\_GET\_CHARACTERISTICS](clusctl-resource-get-characteristics.md)
</dt> <dd>

Retrieves the intrinsic characteristics of a [resource](resources.md).

</dd> <dt>

[CLUSCTL\_RESOURCE\_GET\_CLASS\_INFO](clusctl-resource-get-class-info.md)
</dt> <dd>

Retrieves the class and subclass of a [resource](resources.md).

</dd> <dt>

[CLUSCTL\_RESOURCE\_GET\_COMMON\_PROPERTIES](clusctl-resource-get-common-properties.md)
</dt> <dd>

Retrieves the read/write [common properties](common-properties.md) for a [resource](resources.md). Applications use this [control code](about-control-codes.md) as a [**ClusterResourceControl**](clusterresourcecontrol.md) parameter, and [resource DLLs](resource-dlls.md) receive the control code as a [**ResourceControl**](resourcecontrol.md) parameter.

</dd> <dt>

[CLUSCTL\_RESOURCE\_GET\_COMMON\_PROPERTY\_FMTS](clusctl-resource-get-common-property-fmts.md)
</dt> <dd>

Retrieves a [property list](property-lists.md) describing the format of each [resource common property](resource-common-properties.md).

</dd> <dt>

[CLUSCTL\_RESOURCE\_GET\_CRYPTO\_CHECKPOINTS](clusctl-resource-get-crypto-checkpoints.md)
</dt> <dd>

Retrieves a list of all the cryptographic key [checkpoints](checkpointing.md) set for a [resource](resources.md).

</dd> <dt>

[CLUSCTL\_RESOURCE\_GET\_DNS\_NAME](clusctl-resource-get-dns-name.md)
</dt> <dd>

Retrieves the DNS name of the designated resource.

</dd> <dt>

[CLUSCTL\_RESOURCE\_GET\_FAILURE\_INFO](clusctl-resource-get-failure-info.md)
</dt> <dd>

Retrieves information about a resource failure. Applications use this [control code](about-control-codes.md) as a parameter to the [**ClusterResourceControl**](clusterresourcecontrol.md) function.

</dd> <dt>

[CLUSCTL\_RESOURCE\_GET\_FLAGS](clusctl-resource-get-flags.md)
</dt> <dd>

Retrieves the flags that are set for a [resource](resources.md).

</dd> <dt>

[CLUSCTL\_RESOURCE\_GET\_ID](clusctl-resource-get-id.md)
</dt> <dd>

Retrieves the [cluster database](cluster-database.md) subkey identifier for a [resource](resources.md).

</dd> <dt>

[CLUSCTL\_RESOURCE\_GET\_LOADBAL\_PROCESS\_LIST](clusctl-resource-get-loadbal-process-list.md)
</dt> <dd>

Retrieves the load balancing processor list.

</dd> <dt>

[CLUSCTL\_RESOURCE\_GET\_NAME](clusctl-resource-get-name.md)
</dt> <dd>

Retrieves the name of a [resource](resources.md).

</dd> <dt>

[CLUSCTL\_RESOURCE\_GET\_NETWORK\_NAME](clusctl-resource-get-network-name.md)
</dt> <dd>

Retrieves the name [private property](private-properties.md) of a [Network Name](network-name.md) [resource](resources.md). This [control code](about-control-codes.md) is unsupported by the other default [resource types](resource-types.md). Applications can use this control code as a parameter to the [**ClusterResourceControl**](clusterresourcecontrol.md) function.

</dd> <dt>

[CLUSCTL\_RESOURCE\_GET\_PRIVATE\_PROPERTIES](clusctl-resource-get-private-properties.md)
</dt> <dd>

Retrieves the read/write [private properties](private-properties.md) for a [resource](resources.md). Applications use this [control code](about-control-codes.md) as a [**ClusterResourceControl**](clusterresourcecontrol.md) parameter, and [resource DLLs](resource-dlls.md) receive the control code as a [**ResourceControl**](resourcecontrol.md) parameter.

</dd> <dt>

[CLUSCTL\_RESOURCE\_GET\_PRIVATE\_PROPERTY\_FMTS](clusctl-resource-get-private-property-fmts.md)
</dt> <dd>

Retrieves a [property list](property-lists.md) describing the format of each resource [private property](private-properties.md).

</dd> <dt>

[CLUSCTL\_RESOURCE\_GET\_REGISTRY\_CHECKPOINTS](clusctl-resource-get-registry-checkpoints.md)
</dt> <dd>

Retrieves a list of all the registry [checkpoints](checkpointing.md) set for a [resource](resources.md). Applications use this [control code](about-control-codes.md) as a [**ClusterResourceControl**](clusterresourcecontrol.md) parameter.

</dd> <dt>

[CLUSCTL\_RESOURCE\_GET\_REQUIRED\_DEPENDENCIES](clusctl-resource-get-required-dependencies.md)
</dt> <dd>

Retrieves a list of all required [dependencies](resource-dependencies.md) for a [resource](resources.md).

</dd> <dt>

[CLUSCTL\_RESOURCE\_GET\_RESOURCE\_TYPE](clusctl-resource-get-resource-type.md)
</dt> <dd>

Retrieves the [resource type](resource-types.md) name for a [resource](resources.md).

</dd> <dt>

[CLUSCTL\_RESOURCE\_GET\_RO\_COMMON\_PROPERTIES](clusctl-resource-get-ro-common-properties.md)
</dt> <dd>

Retrieves the read-only [common properties](common-properties.md) for a [resource](resources.md).

</dd> <dt>

[CLUSCTL\_RESOURCE\_GET\_RO\_PRIVATE\_PROPERTIES](clusctl-resource-get-ro-private-properties.md)
</dt> <dd>

Retrieves the read-only [private properties](private-properties.md) for a [resource](resources.md).

</dd> <dt>

[CLUSCTL\_RESOURCE\_GET\_STATE\_CHANGE\_TIME](clusctl-resource-get-state-change-time.md)
</dt> <dd>

Retrieves the time of last state change for a resource.

</dd> <dt>

[CLUSCTL\_RESOURCE\_IPADDRESS\_RELEASE\_LEASE](clusctl-resource-ipaddress-release-lease.md)
</dt> <dd>

Releases the DHCP based lease of an IP address associated with a designated resource.

</dd> <dt>

[CLUSCTL\_RESOURCE\_IPADDRESS\_RENEW\_LEASE](clusctl-resource-ipaddress-renew-lease.md)
</dt> <dd>

Renews the DHCP based lease of an IP address associated with a designated resource.

</dd> <dt>

[CLUSCTL\_RESOURCE\_IS\_QUORUM\_BLOCKED](clusctl-resource-is-quorum-blocked.md)
</dt> <dd>

Prevents a resource from being designated as the quorum resource.

</dd> <dt>

[CLUSCTL\_RESOURCE\_NETNAME\_CREDS\_UPDATED](clusctl-resource-netname-creds-updated.md)
</dt> <dd>

Notifies the resource that the credentials for the domain account associated with the resource has changed.. Applications use this [control code](about-control-codes.md) as a parameter to the [**ClusterResourceControl**](clusterresourcecontrol.md) function.

> [!Note]  
> The [CLUSCTL\_RESOURCE\_NETNAME\_CREDS\_UPDATED](clusctl-resource-netname-creds-updated.md) control code is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.

 

</dd> <dt>

[CLUSCTL\_RESOURCE\_NETNAME\_DELETE\_CO](clusctl-resource-netname-delete-co.md)
</dt> <dd>

Deletes the security principal associated with a designated resource. Applications use this [control code](about-control-codes.md) as a parameter to the [**ClusterResourceControl**](clusterresourcecontrol.md) function.

</dd> <dt>

[CLUSCTL\_RESOURCE\_NETNAME\_GET\_VIRTUAL\_SERVER\_TOKEN](clusctl-resource-netname-get-virtual-server-token.md)
</dt> <dd>

Used by custom resources, services, and applications to get a token in the [Network Name](network-name.md)'s logon session.

</dd> <dt>

[CLUSCTL\_RESOURCE\_NETNAME\_REGISTER\_DNS\_RECORDS](clusctl-resource-netname-register-dns-records.md)
</dt> <dd>

Instructs the designated resource to re-register its DNS Host records with the DNS server associated with the designated node.

</dd> <dt>

[CLUSCTL\_RESOURCE\_NETNAME\_REPAIR\_VCO](clusctl-resource-netname-repair-vco.md)
</dt> <dd>

Repairs the password for a security principal on a client based on the client's alternate computer name.

</dd> <dt>

[CLUSCTL\_RESOURCE\_NETNAME\_RESET\_VCO](clusctl-resource-netname-reset-vco.md)
</dt> <dd>

Resets the password for a security principal on a client based on the client's alternate computer name.

Applications use this [control code](about-control-codes.md) as a parameter to the [**ClusterResourceControl**](clusterresourcecontrol.md) function.

</dd> <dt>

[CLUSCTL\_RESOURCE\_NETNAME\_SET\_PWD\_INFO](clusctl-resource-netname-set-pwd-info.md)
</dt> <dd>

Updates information about the security principal associated with a designated resource.

</dd> <dt>

[CLUSCTL\_RESOURCE\_NETNAME\_VALIDATE\_VCO](clusctl-resource-netname-validate-vco.md)
</dt> <dd>

Confirms whether the security principal of the designated resource can be managed by the cluster.

</dd> <dt>

[CLUSCTL\_RESOURCE\_POOL\_GET\_DRIVE\_INFO](clusctl-resource-pool-get-drive-info.md)
</dt> <dd>

Retrieves drive information for a storage pool.

</dd> <dt>

[CLUSCTL\_RESOURCE\_QUERY\_DELETE](clusctl-resource-query-delete.md)
</dt> <dd>

The [CLUSCTL\_RESOURCE\_QUERY\_DELETE](clusctl-resource-query-delete.md) [control code](about-control-codes.md) is reserved for future use.

</dd> <dt>

[CLUSCTL\_RESOURCE\_QUERY\_MAINTENANCE\_MODE](clusctl-resource-query-maintenance-mode.md)
</dt> <dd>

Queries the [maintenance mode](m-gly.md#-mscs-maintenance-mode-gly) state of the specified disk resource.

</dd> <dt>

[CLUSCTL\_RESOURCE\_RLUA\_GET\_VIRTUAL\_SERVER\_TOKEN](clusctl-resource-rlua-get-virtual-server-token.md)
</dt> <dd>

TBD.

</dd> <dt>

[CLUSCTL\_RESOURCE\_RLUA\_SET\_PWD\_INFO](clusctl-resource-rlua-set-pwd-info.md)
</dt> <dd>

TBD.

</dd> <dt>

[CLUSCTL\_RESOURCE\_SET\_COMMON\_PROPERTIES](clusctl-resource-set-common-properties.md)
</dt> <dd>

Updates the read/write [common properties](common-properties.md) for a [resource](resources.md).

</dd> <dt>

[CLUSCTL\_RESOURCE\_SET\_CSV\_MAINTENANCE\_MODE](clusctl-resource-set-csv-maintenance-mode.md)
</dt> <dd>

Enables or disables [maintenance mode](m-gly.md#-mscs-maintenance-mode-gly) for the specified cluster shared volume

</dd> <dt>

[CLUSCTL\_RESOURCE\_SET\_MAINTENANCE\_MODE](clusctl-resource-set-maintenance-mode.md)
</dt> <dd>

Enables or disables [maintenance mode](m-gly.md#-mscs-maintenance-mode-gly) for the specified disk resource.

</dd> <dt>

[CLUSCTL\_RESOURCE\_SET\_PRIVATE\_PROPERTIES](clusctl-resource-set-private-properties.md)
</dt> <dd>

Updates the read/write [private properties](private-properties.md) for a [resource](resources.md).

</dd> <dt>

[CLUSCTL\_RESOURCE\_SET\_SHARED\_VOLUME\_BACKUP\_MODE](clusctl-resource-set-shared-volume-backup-mode.md)
</dt> <dd>

Sets the backup mode for a CSV

</dd> <dt>

[CLUSCTL\_RESOURCE\_STORAGE\_CLUSTER\_DISK](clusctl-resource-storage-cluster-disk.md)
</dt> <dd>

TBD. Applications use this [control code](about-control-codes.md) as a parameter to the [**ClusterResourceControl**](clusterresourcecontrol.md) function.

> [!Note]  
> The [CLUSCTL\_RESOURCE\_STORAGE\_CLUSTER\_DISK](clusctl-resource-storage-cluster-disk.md) control code is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.

 

</dd> <dt>

[CLUSCTL\_RESOURCE\_STORAGE\_GET\_DIRTY](clusctl-resource-storage-get-dirty.md)
</dt> <dd>

Retrieves a list of dirty volumes on the disk resource.

</dd> <dt>

[CLUSCTL\_RESOURCE\_STORAGE\_GET\_DISK\_INFO](clusctl-resource-storage-get-disk-info.md)
</dt> <dd>

Retrieves information about a particular [storage class resource](s-gly.md#-wolf-storage-class-resource-gly).

</dd> <dt>

[CLUSCTL\_RESOURCE\_STORAGE\_GET\_DISK\_INFO\_EX](clusctl-resource-storage-get-disk-info-ex.md)
</dt> <dd>

Retrieves information about a particular [storage class resource](s-gly.md#-wolf-storage-class-resource-gly).

</dd> <dt>

[CLUSCTL\_RESOURCE\_STORAGE\_GET\_DISK\_INFO\_EX2](clusctl-resource-storage-get-disk-info-ex2.md)
</dt> <dd>

Retrieves extended information about a [storage class resource](s-gly.md#-wolf-storage-class-resource-gly).

</dd> <dt>

[CLUSCTL\_RESOURCE\_STORAGE\_GET\_DISK\_NUMBER\_INFO](clusctl-resource-storage-get-disk-number-info.md)
</dt> <dd>

Retrieves the disk number of a physical disk resource in a cluster.

</dd> <dt>

[CLUSCTL\_RESOURCE\_STORAGE\_GET\_DISKID](clusctl-resource-storage-get-diskid.md)
</dt> <dd>

Retrieves the disk ID for a storage class resource.

</dd> <dt>

[CLUSCTL\_RESOURCE\_STORAGE\_GET\_MOUNTPOINTS](clusctl-resource-storage-get-mountpoints.md)
</dt> <dd>

Retrieves a list of path names for the specified partition.

</dd> <dt>

[CLUSCTL\_RESOURCE\_STORAGE\_GET\_SHARED\_VOLUME\_INFO](clusctl-resource-storage-get-shared-volume-info.md)
</dt> <dd>

Retrieves information on the specified shared volume. Applications use this control code as a parameter to the [**ClusterResourceControl**](clusterresourcecontrol.md) function, and [resource DLLs](resource-dlls.md) receive the control code as a parameter to the [*ResourceControl*](resourcecontrol.md) callback function.

</dd> <dt>

[CLUSCTL\_RESOURCE\_STORAGE\_GET\_SHARED\_VOLUME\_PARTITION\_NAMES](clusctl-resource-storage-get-shared-volume-partition-names.md)
</dt> <dd>

Retrieves partition names for a Cluster Shared Volume (CSV).

</dd> <dt>

[CLUSCTL\_RESOURCE\_STORAGE\_GET\_SHARED\_VOLUME\_STATES](clusctl-resource-storage-get-shared-volume-states.md)
</dt> <dd>

Retrieves the status of a Cluster Shared Volume (CSV).

</dd> <dt>

[CLUSCTL\_RESOURCE\_STORAGE\_IS\_PATH\_VALID](clusctl-resource-storage-is-path-valid.md)
</dt> <dd>

Verifies that a specified path exists on a [storage class resource](s-gly.md#-wolf-storage-class-resource-gly).

</dd> <dt>

[CLUSCTL\_RESOURCE\_STORAGE\_IS\_SHARED\_VOLUME](clusctl-resource-storage-is-shared-volume.md)
</dt> <dd>

Verifies that a [storage class resource](s-gly.md#-wolf-storage-class-resource-gly) is a Cluster Shared Volume (CSV).

</dd> <dt>

[CLUSCTL\_RESOURCE\_STORAGE\_SET\_DRIVELETTER](clusctl-resource-storage-set-driveletter.md)
</dt> <dd>

Modifies the drive letter associated with the designated storage-class resource.

</dd> <dt>

[CLUSCTL\_RESOURCE\_UNKNOWN](clusctl-resource-unknown.md)
</dt> <dd>

verifies that [control codes](about-control-codes.md) are being processed on the node where execution of the control is directed.

</dd> <dt>

[CLUSCTL\_RESOURCE\_UPGRADE\_DLL](clusctl-resource-upgrade-dll.md)
</dt> <dd>

Allows a setup application to upgrade a [resource DLL](resource-dlls.md) without stopping the [Cluster service](cluster-service.md). Applications use this [control code](about-control-codes.md) as a [**ClusterResourceControl**](clusterresourcecontrol.md) parameter.

</dd> <dt>

[CLUSCTL\_RESOURCE\_VALIDATE\_COMMON\_PROPERTIES](clusctl-resource-validate-common-properties.md)
</dt> <dd>

Verifies that a [property list](property-lists.md) contains valid [resource](resources.md) [common property](common-properties.md) names and values and that the list is properly formatted.

</dd> <dt>

[CLUSCTL\_RESOURCE\_VALIDATE\_PRIVATE\_PROPERTIES](clusctl-resource-validate-private-properties.md)
</dt> <dd>

Verifies that a [property list](property-lists.md) contains valid [resource](resources.md) private property names and values and that the list is properly formatted.

</dd> <dt>

[CLUSCTL\_RESOURCE\_VM\_CANCEL\_MIGRATION](clusctl-resource-vm-cancel-migration.md)
</dt> <dd>

cancels an ongoing Live Migration of a VM

</dd> <dt>

[CLUSCTL\_RESOURCE\_VM\_CONFIG\_UPDATE](clusctl-resource-vm-config-update.md)
</dt> <dd>

updates the [**VmSwitchPorts**](virtual-machine-configurations-vmswitchports.md) and [**VmPhysicalDisks**](virtual-machine-configurations-vmphysicaldisks.md) properties of the Virtual Machine configuration resource instances.

</dd> <dt>

[CLUSCTL\_RESOURCE\_VM\_SET\_NEXT\_OFFLINE\_ACTION](clusctl-resource-vm-set-next-offline-action.md)
</dt> <dd>

Specifies the offline action for the next [*Offline*](offline.md) operation on the virtual machine (VM) resource instance. This can be used to temporarily change the value of the [**OfflineAction**](virtual-machines-offlineaction.md) property without the overhead of modifying and restoring the resource property. Applications use this control code as a parameter to the [**ClusterResourceControl**](clusterresourcecontrol.md) function, and [resource DLLs](resource-dlls.md) receive the control code as a parameter to the [*ResourceControl*](resourcecontrol.md) callback function.

</dd> <dt>

[CLUSCTL\_RESOURCE\_VM\_START\_MIGRATION](clusctl-resource-vm-start-migration.md)
</dt> <dd>

initiates the live migration of a VM from one node of a cluster to another node of the cluster

</dd> </dl>

## Related topics

<dl> <dt>

[Resource Control Codes](resource-control-codes.md)
</dt> <dt>

[**ClusterResourceControl**](clusterresourcecontrol.md)
</dt> <dt>

[**ResourceControl**](resourcecontrol.md)
</dt> </dl>

 

 




