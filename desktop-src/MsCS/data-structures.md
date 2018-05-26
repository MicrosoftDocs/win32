---
title: Data Structures
description: The failover cluster data structures contain cluster information for value lists.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e3ad7c34-0c8a-4f03-8e5c-b57802c493f0
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- data structures Failover Cluster
- structures Failover Cluster ,data
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Data Structures

The failover cluster data structures contain cluster information for [value lists](value-lists.md).

Many of these data structures include other data structures as members:

-   Most structures that describe data of a particular type include a [**CLUSPROP\_VALUE**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_value?branch=master) structure as the first member.
-   The [**CLUSPROP\_VALUE**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_value?branch=master) structure uses a [**CLUSPROP\_SYNTAX**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_syntax?branch=master) union as its first member.
-   Some of the data structures use other data structures to store data values. For example, the [**CLUSPROP\_SCSI\_ADDRESS**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_scsi_address?branch=master) structure uses a [**CLUS\_SCSI\_ADDRESS**](/windows/previous-versions/ClusAPI/ns-clusapi-clus_scsi_address?branch=master) structure to hold the data for a SCSI device.

If a structure contains other structures as members, the description of the structure lists the members of the contained structures explicitly, rather than simply listing the contained structure. For example, ClusAPI.h defines a [**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master) structure as follows:

``` syntax
typedef struct _CLUSPROP_SZ {
  CLUSPROP_VALUE;
  WCHAR           sz[];
} CLUSPROP_SZ, *PCLUSPROP_SZ;
```

To promote clarity, this documentation describes [**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master) as:

``` syntax
typedef struct _CLUSPROP_SZ {
  CLUSPROP_SYNTAX Syntax;
  DWORD           cbLength;
  WCHAR           sz[];
} CLUSPROP_SZ, *PCLUSPROP_SZ;
```

The following diagram shows the relationship between many of the structures used as headers, the structures used to describe data values, and the structures used to hold data for the data values:

![describes relationships between structures](images/wfstruct.png)

## In this section

<dl> <dt>

[**CLUS\_PARTITION\_INFO\_EX2**](/windows/previous-versions/ClusAPI/ns-clusapi-clus_partition_info_ex2?branch=master)
</dt> <dd>

Describes the disk partition information of a [storage class resource](s-gly.md#-wolf-storage-class-resource-gly).

</dd> <dt>

[**CLUSPROP\_PARTITION\_INFO\_EX2**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_partition_info_ex2?branch=master)
</dt> <dd>

A value list entry that contains partition information for a storage class resource. This structure is as a input, and a as a return value for the [CLUSCTL\_RESOURCE\_STORAGE\_GET\_DISK\_INFO\_EX2](clusctl-resource-storage-get-disk-info-ex2.md) control code.

</dd> <dt>

[**CLUS\_CHKDSK\_INFO**](/windows/previous-versions/ClusAPI/ns-clusapi-_clus_chkdsk_info?branch=master)
</dt> <dd>

Represents information about a Chkdsk operation.

</dd> <dt>

[**CLUS\_CSV\_MAINTENANCE\_MODE\_INFO**](/windows/previous-versions/ClusApi/ns-clusapi-clus_csv_maintenance_mode_info?branch=master)
</dt> <dd>

enables or disables the maintenance mode on a cluster shared volume (CSV).

</dd> <dt>

[**CLUS\_CSV\_VOLUME\_INFO**](/windows/previous-versions/ClusAPI/ns-clusapi-_clus_csv_volume_info?branch=master)
</dt> <dd>

Represents information about a cluster shared volume (CSV).

</dd> <dt>

[**CLUS\_CSV\_VOLUME\_NAME**](/windows/previous-versions/ClusAPI/ns-clusapi-_clus_csv_volume_name?branch=master)
</dt> <dd>

Represents the name of a cluster shared volume (CSV).

</dd> <dt>

[**CLUS\_DISK\_NUMBER\_INFO**](/windows/previous-versions/ClusAPI/ns-clusapi-_clus_disk_number_info?branch=master)
</dt> <dd>

Represents information about the disk number of a physical disk.

</dd> <dt>

[**CLUS\_DNN\_LEADER\_STATUS**](/windows/previous-versions/ClusAPI/ns-clusapi-clus_dnn_leader_status?branch=master)
</dt> <dd>

Represents the status of a Distributed Network Name (DNN) resource for a Scale-Out File Server.

</dd> <dt>

[**CLUS\_DNN\_SODAFS\_CLONE\_STATUS**](/windows/previous-versions/ClusAPI/ns-clusapi-clus_dnn_sodafs_clone_status?branch=master)
</dt> <dd>

Represents the status of a Scale-Out File Server clone.

</dd> <dt>

[**CLUS\_FORCE\_QUORUM\_INFO**](/windows/previous-versions/ClusAPI/ns-clusapi-clus_force_quorum_info?branch=master)
</dt> <dd>

Specifies information about the list of [nodes](nodes.md) sufficient to establish quorum in a majority-of-nodes cluster.

</dd> <dt>

[**CLUS\_FTSET\_INFO**](/windows/previous-versions/ClusAPI/ns-clusapi-clus_ftset_info?branch=master)
</dt> <dd>

Contains information about an FT (fault tolerant) set. This structure is used by the [**CLUSPROP\_FTSET\_INFO**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_ftset_info?branch=master) structure to create an entry in a value list.

</dd> <dt>

[**CLUS\_MAINTENANCE\_MODE\_INFO**](/windows/previous-versions/ClusAPI/ns-clusapi-clus_maintenance_mode_info?branch=master)
</dt> <dd>

Enables or disables maintenance mode on a cluster node.

</dd> <dt>

[**CLUS\_MAINTENANCE\_MODE\_INFOEX**](/windows/previous-versions/ClusAPI/ns-clusapi-_clus_maintenance_mode_infoex?branch=master)
</dt> <dd>

Represents the extended maintenance mode settings for a storage class resource.

</dd> <dt>

[**CLUS\_NETNAME\_IP\_INFO\_ENTRY**](/windows/previous-versions/ClusApi/ns-clusapi-clus_netname_ip_info_entry?branch=master)
</dt> <dd>

Represents IP information for a NetName resource.

</dd> <dt>

[**CLUS\_NETNAME\_IP\_INFO\_FOR\_MULTICHANNEL**](/windows/previous-versions/ClusApi/ns-clusapi-clus_netname_ip_info_for_multichannel?branch=master)
</dt> <dd>

Represents IP information for a NetName resource that has Multichannel enabled.

</dd> <dt>

[**CLUS\_NETNAME\_PWD\_INFO**](/windows/previous-versions/ClusAPI/ns-clusapi-clus_netname_pwd_info?branch=master)
</dt> <dd>

Provides information for resetting the security principal associated with a computer name.

</dd> <dt>

[**CLUS\_NETNAME\_VS\_TOKEN\_INFO**](/windows/previous-versions/ClusAPI/ns-clusapi-clus_netname_vs_token_info?branch=master)
</dt> <dd>

Contains the data needed to request a token. It is used as the input parameter of the [CLUSCTL\_RESOURCE\_NETNAME\_GET\_VIRTUAL\_SERVER\_TOKEN](clusctl-resource-netname-get-virtual-server-token.md) control code.

</dd> <dt>

[**CLUS\_PARTITION\_INFO**](/windows/previous-versions/ClusAPI/ns-clusapi-clus_partition_info?branch=master)
</dt> <dd>

Contains data describing a [storage class resource](s-gly.md#-wolf-storage-class-resource-gly) volume and file system. It is used as the data member of a [**CLUSPROP\_PARTITION\_INFO**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_partition_info?branch=master) structure and as the return value of some [control code](control-codes.md) operations.

</dd> <dt>

[**CLUS\_PARTITION\_INFO\_EX**](/windows/previous-versions/ClusAPI/ns-clusapi-clus_partition_info_ex?branch=master)
</dt> <dd>

Describes a [storage class resource](s-gly.md#-wolf-storage-class-resource-gly) volume and file system.

</dd> <dt>

[**CLUS\_PROVIDER\_STATE\_CHANGE\_INFO**](/windows/previous-versions/ClusAPI/ns-clusapi-_clus_provider_state_change_info?branch=master)
</dt> <dd>

Contains data about the state of a [provider](p-gly.md#-wolf-provider-gly) resource.

</dd> <dt>

[**CLUS\_RESOURCE\_CLASS\_INFO**](/windows/previous-versions/ClusAPI/ns-clusapi-clus_resource_class_info?branch=master)
</dt> <dd>

Contains resource class data. It is used as the data member of a [**CLUSPROP\_RESOURCE\_CLASS\_INFO**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_resource_class_info?branch=master) structure and as the return value of some [control code](control-codes.md) operations.

</dd> <dt>

[**CLUS\_SCSI\_ADDRESS**](/windows/previous-versions/ClusAPI/ns-clusapi-clus_scsi_address?branch=master)
</dt> <dd>

Contains [SCSI](s-gly.md#-wolf-small-computer-system-interface-gly) address data. It is used as the data member of a [**CLUSPROP\_SCSI\_ADDRESS**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_scsi_address?branch=master) structure and as the return value of some [control code](control-codes.md) operations.

</dd> <dt>

[**CLUS\_SHARED\_VOLUME\_BACKUP\_MODE**](/windows/previous-versions/ClusAPI/ns-clusapi-_clus_shared_volume_backup_mode?branch=master)
</dt> <dd>

Describes the backup mode for CSV

</dd> <dt>

[**CLUS\_STARTING\_PARAMS**](/windows/previous-versions/ClusAPI/ns-clusapi-clus_starting_params?branch=master)
</dt> <dd>

Indicates whether a [node's](nodes.md) attempt to start the [Cluster service](cluster-service.md) represents an attempt to form or join a [cluster](c-gly.md#-wolf-cluster-gly), and whether the node has attempted to start this version of the Cluster service before. [Resource DLLs](resource-dlls.md) receive the CLUS\_STARTING\_PARAMS structure with the [CLUSCTL\_RESOURCE\_TYPE\_STARTING\_PHASE1](clusctl-resource-type-starting-phase1.md) and [CLUSCTL\_RESOURCE\_TYPE\_STARTING\_PHASE2](clusctl-resource-type-starting-phase2.md) control codes.

</dd> <dt>

[**CLUS\_STORAGE\_GET\_AVAILABLE\_DRIVELETTERS**](/windows/previous-versions/ClusAPI/ns-clusapi-_clus_storage_get_available_driveletters?branch=master)
</dt> <dd>

Contains a bitmask of the driver letters that are available on a node. It is used as the return value of the [CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_GET\_DRIVELETTERS](clusctl-resource-type-storage-get-driveletters.md) control code.

</dd> <dt>

[**CLUS\_STORAGE\_REMAP\_DRIVELETTER**](/windows/previous-versions/ClusAPI/ns-clusapi-_clus_storage_remap_driveletter?branch=master)
</dt> <dd>

Identifies the existing and target drive letter for a disk drive on a node.

</dd> <dt>

[**CLUS\_STORAGE\_SET\_DRIVELETTER**](/windows/previous-versions/ClusAPI/ns-clusapi-_clus_storage_set_driveletter?branch=master)
</dt> <dd>

Supplies drive letter information for a disk partition associated with a storage class resource.

</dd> <dt>

[**CLUSPROP\_BINARY**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_binary?branch=master)
</dt> <dd>

Describes a binary data value.

</dd> <dt>

[**CLUSPROP\_DISK\_NUMBER**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_dword?branch=master)
</dt> <dd>

Describes a numeric value identifying the physical drive of a disk. It is used as an entry in a [value list](value-lists.md) and consists of:

-   A [**CLUSPROP\_VALUE**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_value?branch=master) structure describing the format, type, and length of the numeric data.
-   A **DWORD** value identifying the physical drive of a disk.

For convenience, the [**CLUSPROP\_VALUE**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_value?branch=master) members are listed explicitly:

</dd> <dt>

[**CLUSPROP\_DISK\_SIGNATURE**](/windows/previous-versions/ClusAPI/?branch=master)
</dt> <dd>

Describes the signature that is stored on the disk for identifying it to the operating system. The [**CLUSPROP\_DISK\_SIGNATURE**](/windows/previous-versions/ClusAPI/?branch=master) structure is used as an entry in a [value list](value-lists.md) and consists of:

-   A [**CLUSPROP\_VALUE**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_value?branch=master) structure describing the format, type, and length of the numeric data.
-   A **DWORD** value.

For convenience, the [**CLUSPROP\_VALUE**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_value?branch=master) members are listed explicitly:

</dd> <dt>

[**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master)
</dt> <dd>

Describes numeric data. It is used as an entry in a [value list](value-lists.md) and consists of:

-   A [**CLUSPROP\_VALUE**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_value?branch=master) structure describing the format, type, and length of the numeric data.
-   A **DWORD** value.

For convenience, the [**CLUSPROP\_VALUE**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_value?branch=master) members are listed explicitly:

</dd> <dt>

[**CLUSPROP\_FILETIME**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_filetime?branch=master)
</dt> <dd>

Describes a date and time stamp for a file.

</dd> <dt>

[**CLUSPROP\_FTSET\_INFO**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_ftset_info?branch=master)
</dt> <dd>

Contains information about an FT (fault tolerant) set. It is used as an entry in a [value list](value-lists.md) and consists of a [**CLUSPROP\_VALUE**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_value?branch=master) and a [**CLUS\_FTSET\_INFO**](/windows/previous-versions/ClusAPI/ns-clusapi-clus_ftset_info?branch=master) structure.

</dd> <dt>

[**CLUSPROP\_LARGE\_INTEGER**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_large_integer?branch=master)
</dt> <dd>

Describes a signed large integer. It is used as an entry in a [value list](value-lists.md) and consists of:

-   A [**CLUSPROP\_VALUE**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_value?branch=master) structure indicating the format and type of the integer value.
-   Assigned large integer value.

For convenience, the [**CLUSPROP\_VALUE**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_value?branch=master) members are listed explicitly.

</dd> <dt>

[**CLUSPROP\_LONG**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_long?branch=master)
</dt> <dd>

Describes signed **LONG** data. It is used as an entry in a [value list](value-lists.md) and consists of:

-   A [**CLUSPROP\_VALUE**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_value?branch=master) structure describing the format, type, and length of the numeric data.
-   A **LONG** value.

For convenience, the [**CLUSPROP\_VALUE**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_value?branch=master) members are listed explicitly:

</dd> <dt>

[**CLUSPROP\_MULTI\_SZ**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_sz?branch=master)
</dt> <dd>

Describes multiple **NULL**-terminated Unicode strings. It is used as an entry in a [value list](value-lists.md) and consists of:

-   A [**CLUSPROP\_VALUE**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_value?branch=master) structure describing the format, type, and length of the partition information.
-   A string array.

For convenience, the [**CLUSPROP\_VALUE**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_value?branch=master) members are listed explicitly:

</dd> <dt>

[**CLUSPROP\_PARTITION\_INFO**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_partition_info?branch=master)
</dt> <dd>

Contains information relevant to [storage class resources](s-gly.md#-wolf-storage-class-resource-gly).

</dd> <dt>

[**CLUSPROP\_PARTITION\_INFO\_EX**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_partition_info_ex?branch=master)
</dt> <dd>

The [**CLUSPROP\_PARTITION\_INFO\_EX**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_partition_info_ex?branch=master) structure contains information relevant to [storage class resources](s-gly.md#-wolf-storage-class-resource-gly).

</dd> <dt>

[**CLUSPROP\_PROPERTY\_NAME**](/windows/previous-versions/ClusAPI/?branch=master)
</dt> <dd>

Describes the name of a property. It is used as an entry in a [value list](value-lists.md) and consists of:

-   A [**CLUSPROP\_VALUE**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_value?branch=master) structure describing the format, type, and length of the property name.
-   A null-terminated Unicode string.

For convenience, the [**CLUSPROP\_VALUE**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_value?branch=master) members are listed explicitly:

</dd> <dt>

[**CLUSPROP\_REQUIRED\_DEPENDENCY**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_required_dependency?branch=master)
</dt> <dd>

Describes a [resource](resources.md) that is a required [dependency](resource-dependencies.md) of another resource. This union is used as a value in the [value list](value-lists.md) returned from a [CLUSCTL\_RESOURCE\_GET\_REQUIRED\_DEPENDENCIES](clusctl-resource-get-required-dependencies.md) or [CLUSCTL\_RESOURCE\_TYPE\_GET\_REQUIRED\_DEPENDENCIES](clusctl-resource-type-get-required-dependencies.md) [control code](control-codes.md) operation.

</dd> <dt>

[**CLUSPROP\_RESOURCE\_CLASS**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_resource_class?branch=master)
</dt> <dd>

Describes a resource class. It is used as an entry in a [value list](value-lists.md) and consists of:

-   A [**CLUSPROP\_VALUE**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_value?branch=master) structure describing the format, type, and length of the resource class value.
-   A [**CLUSTER\_RESOURCE\_CLASS**](/windows/previous-versions/ClusAPI/ne-clusapi-cluster_resource_class?branch=master) value describing the resource class. **CLUSTER\_RESOURCE\_CLASS** is an enumeration defined in ClusAPI.h.

For convenience, the [**CLUSPROP\_VALUE**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_value?branch=master) members are listed explicitly:

</dd> <dt>

[**CLUSPROP\_RESOURCE\_CLASS\_INFO**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_resource_class_info?branch=master)
</dt> <dd>

Describes information relating to a resource class. It is used as an entry in a [value list](value-lists.md) and consists of:

-   A [**CLUSPROP\_VALUE**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_value?branch=master) structure indicating the format and type of the resource class information.
-   A [**CLUS\_RESOURCE\_CLASS\_INFO**](/windows/previous-versions/ClusAPI/ns-clusapi-clus_resource_class_info?branch=master) structure describing the resource class and subclass of the resource.

For convenience, the [**CLUSPROP\_VALUE**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_value?branch=master) and [**CLUS\_RESOURCE\_CLASS\_INFO**](/windows/previous-versions/ClusAPI/ns-clusapi-clus_resource_class_info?branch=master) members are listed explicitly.

</dd> <dt>

[**CLUSPROP\_SCSI\_ADDRESS**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_scsi_address?branch=master)
</dt> <dd>

Describes an address for a [SCSI](s-gly.md#-wolf-small-computer-system-interface-gly) device. It is used as an entry in a [value list](value-lists.md) and consists of:

-   A [**CLUSPROP\_VALUE**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_value?branch=master) structure indicating the format and type of the resource class information.
-   A [**CLUS\_SCSI\_ADDRESS**](/windows/previous-versions/ClusAPI/ns-clusapi-clus_scsi_address?branch=master) structure.

For convenience, the [**CLUSPROP\_VALUE**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_value?branch=master) and [**CLUS\_SCSI\_ADDRESS**](/windows/previous-versions/ClusAPI/ns-clusapi-clus_scsi_address?branch=master) members are listed explicitly.

</dd> <dt>

[**CLUSPROP\_SECURITY\_DESCRIPTOR**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_security_descriptor?branch=master)
</dt> <dd>

Describes a security descriptor.

</dd> <dt>

[**CLUSPROP\_SYNTAX**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_syntax?branch=master)
</dt> <dd>

Describes the format and type of a data value. It is used as the **Syntax** member of the [**CLUSPROP\_VALUE**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_value?branch=master) structure.

</dd> <dt>

[**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)
</dt> <dd>

Describes a null-terminated Unicode string. It is used as an entry in a [value list](value-lists.md) and consists of:

-   A [**CLUSPROP\_VALUE**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_value?branch=master) structure indicating the format and type of string.
-   A null-terminated Unicode string.

For convenience, the [**CLUSPROP\_VALUE**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_value?branch=master) members are listed explicitly.

</dd> <dt>

[**CLUSPROP\_ULARGE\_INTEGER**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_ularge_integer?branch=master)
</dt> <dd>

Describes an unsigned large integer. It is used as an entry in a [value list](value-lists.md) and consists of:

-   A [**CLUSPROP\_VALUE**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_value?branch=master) structure indicating the format and type of the integer value.
-   An unsigned large integer value.

For convenience, the [**CLUSPROP\_VALUE**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_value?branch=master) members are listed explicitly.

</dd> <dt>

[**CLUSPROP\_VALUE**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_value?branch=master)
</dt> <dd>

Describes the syntax and length of a data value used in a [value list](value-lists.md). The [**CLUSPROP\_VALUE**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_value?branch=master) structure is used as a generic header in all of the structures that describe data of a particular type, such as [**CLUSPROP\_BINARY**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_binary?branch=master) and [**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master).

</dd> <dt>

[**CLUSPROP\_WORD**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_word?branch=master)
</dt> <dd>

Describes numeric data. It is used as an entry in a [value list](value-lists.md) and consists of:

-   A [**CLUSPROP\_VALUE**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_value?branch=master) structure describing the format, type, and length of the numeric data.
-   A **WORD** value.

For convenience, the [**CLUSPROP\_VALUE**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_value?branch=master) members are listed explicitly:

</dd> <dt>

[**SR\_RESOURCE\_TYPE\_DISK\_INFO**](/windows/previous-versions/ClusAPI/ns-clusapi-_sr_resource_type_disk_info?branch=master)
</dt> <dd>

Describes a set of information that indicates whether a disk is eligible for replication.

</dd> <dt>

[**SR\_RESOURCE\_TYPE\_ELIGIBLE\_DISKS\_RESULT**](/windows/previous-versions/ClusAPI/ns-clusapi-_sr_resource_type_eligible_disks_result?branch=master)
</dt> <dd>

Describes a set of data disks retrieved by a resource type control code operation for storage replication.

</dd> <dt>

[**SR\_RESOURCE\_TYPE\_QUERY\_ELIGIBLE\_LOGDISKS**](/windows/previous-versions/ClusAPI/ns-clusapi-_sr_resource_type_query_eligible_logdisks?branch=master)
</dt> <dd>

Describes a set of retrieved disks that can be used as log disks for the specified data disk.

</dd> <dt>

[**SR\_RESOURCE\_TYPE\_QUERY\_ELIGIBLE\_SOURCE\_DATADISKS**](/windows/previous-versions/ClusAPI/ns-clusapi-_sr_resource_type_eligible_source_datadisks?branch=master)
</dt> <dd>

Describes a set of retrieved data disks that can be used as source sites for replication.

</dd> <dt>

[**SR\_RESOURCE\_TYPE\_QUERY\_ELIGIBLE\_TARGET\_DATADISKS**](/windows/previous-versions/ClusAPI/ns-clusapi-_sr_resource_type_eligible_target_datadisks?branch=master)
</dt> <dd>

Describes a set of retrieved data disks that can be used as target sites for replication.

</dd> <dt>

[**SR\_RESOURCE\_TYPE\_REPLICATED\_DISK**](/windows/previous-versions/ClusAPI/ns-clusapi-_sr_resource_type_replicated_disk?branch=master)
</dt> <dd>

Represents a replicated disk.

</dd> <dt>

[**SR\_RESOURCE\_TYPE\_REPLICATED\_DISKS\_RESULT**](/windows/previous-versions/ClusAPI/ns-clusapi-_sr_resource_type_replicated_disks_result?branch=master)
</dt> <dd>

Describes a retrieved set of replicated disks.

</dd> <dt>

[**SR\_RESOURCE\_TYPE\_REPLICATED\_PARTITION\_ARRAY**](/windows/previous-versions/ClusAPI/ns-clusapi-_sr_resource_type_replicated_partition_array?branch=master)
</dt> <dd>

Lists the all replicated partitions on a disk.

</dd> <dt>

[**SR\_RESOURCE\_TYPE\_REPLICATED\_PARTITION\_INFO**](/windows/previous-versions/ClusAPI/ns-clusapi-_sr_resource_type_replicated_partition_info?branch=master)
</dt> <dd>

Describes a replicated partition.

</dd> </dl>

## Related topics

<dl> <dt>

[Failover Cluster Structures](cluster-structures.md)
</dt> </dl>

 

 




