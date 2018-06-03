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
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Data Structures

The failover cluster data structures contain cluster information for [value lists](value-lists.md).

Many of these data structures include other data structures as members:

-   Most structures that describe data of a particular type include a [**CLUSPROP\_VALUE**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_value) structure as the first member.
-   The [**CLUSPROP\_VALUE**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_value) structure uses a [**CLUSPROP\_SYNTAX**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_syntax) union as its first member.
-   Some of the data structures use other data structures to store data values. For example, the [**CLUSPROP\_SCSI\_ADDRESS**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_scsi_address) structure uses a [**CLUS\_SCSI\_ADDRESS**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clus_scsi_address) structure to hold the data for a SCSI device.

If a structure contains other structures as members, the description of the structure lists the members of the contained structures explicitly, rather than simply listing the contained structure. For example, ClusAPI.h defines a [**CLUSPROP\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/) structure as follows:

``` syntax
typedef struct _CLUSPROP_SZ {
  CLUSPROP_VALUE;
  WCHAR           sz[];
} CLUSPROP_SZ, *PCLUSPROP_SZ;
```

To promote clarity, this documentation describes [**CLUSPROP\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/) as:

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

[**CLUS\_PARTITION\_INFO\_EX2**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clus_partition_info_ex2)
</dt> <dd>

Describes the disk partition information of a [storage class resource](https://www.bing.com/search?q=storage class resource).

</dd> <dt>

[**CLUSPROP\_PARTITION\_INFO\_EX2**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_partition_info_ex2)
</dt> <dd>

A value list entry that contains partition information for a storage class resource. This structure is as a input, and a as a return value for the [CLUSCTL\_RESOURCE\_STORAGE\_GET\_DISK\_INFO\_EX2](clusctl-resource-storage-get-disk-info-ex2.md) control code.

</dd> <dt>

[**CLUS\_CHKDSK\_INFO**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-_clus_chkdsk_info)
</dt> <dd>

Represents information about a Chkdsk operation.

</dd> <dt>

[**CLUS\_CSV\_MAINTENANCE\_MODE\_INFO**](/previous-versions/windows/desktop/api/ClusApi/ns-clusapi-clus_csv_maintenance_mode_info)
</dt> <dd>

enables or disables the maintenance mode on a cluster shared volume (CSV).

</dd> <dt>

[**CLUS\_CSV\_VOLUME\_INFO**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-_clus_csv_volume_info)
</dt> <dd>

Represents information about a cluster shared volume (CSV).

</dd> <dt>

[**CLUS\_CSV\_VOLUME\_NAME**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-_clus_csv_volume_name)
</dt> <dd>

Represents the name of a cluster shared volume (CSV).

</dd> <dt>

[**CLUS\_DISK\_NUMBER\_INFO**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-_clus_disk_number_info)
</dt> <dd>

Represents information about the disk number of a physical disk.

</dd> <dt>

[**CLUS\_DNN\_LEADER\_STATUS**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clus_dnn_leader_status)
</dt> <dd>

Represents the status of a Distributed Network Name (DNN) resource for a Scale-Out File Server.

</dd> <dt>

[**CLUS\_DNN\_SODAFS\_CLONE\_STATUS**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clus_dnn_sodafs_clone_status)
</dt> <dd>

Represents the status of a Scale-Out File Server clone.

</dd> <dt>

[**CLUS\_FORCE\_QUORUM\_INFO**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clus_force_quorum_info)
</dt> <dd>

Specifies information about the list of [nodes](nodes.md) sufficient to establish quorum in a majority-of-nodes cluster.

</dd> <dt>

[**CLUS\_FTSET\_INFO**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clus_ftset_info)
</dt> <dd>

Contains information about an FT (fault tolerant) set. This structure is used by the [**CLUSPROP\_FTSET\_INFO**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_ftset_info) structure to create an entry in a value list.

</dd> <dt>

[**CLUS\_MAINTENANCE\_MODE\_INFO**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clus_maintenance_mode_info)
</dt> <dd>

Enables or disables maintenance mode on a cluster node.

</dd> <dt>

[**CLUS\_MAINTENANCE\_MODE\_INFOEX**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-_clus_maintenance_mode_infoex)
</dt> <dd>

Represents the extended maintenance mode settings for a storage class resource.

</dd> <dt>

[**CLUS\_NETNAME\_IP\_INFO\_ENTRY**](/previous-versions/windows/desktop/api/ClusApi/ns-clusapi-clus_netname_ip_info_entry)
</dt> <dd>

Represents IP information for a NetName resource.

</dd> <dt>

[**CLUS\_NETNAME\_IP\_INFO\_FOR\_MULTICHANNEL**](/previous-versions/windows/desktop/api/ClusApi/ns-clusapi-clus_netname_ip_info_for_multichannel)
</dt> <dd>

Represents IP information for a NetName resource that has Multichannel enabled.

</dd> <dt>

[**CLUS\_NETNAME\_PWD\_INFO**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clus_netname_pwd_info)
</dt> <dd>

Provides information for resetting the security principal associated with a computer name.

</dd> <dt>

[**CLUS\_NETNAME\_VS\_TOKEN\_INFO**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clus_netname_vs_token_info)
</dt> <dd>

Contains the data needed to request a token. It is used as the input parameter of the [CLUSCTL\_RESOURCE\_NETNAME\_GET\_VIRTUAL\_SERVER\_TOKEN](clusctl-resource-netname-get-virtual-server-token.md) control code.

</dd> <dt>

[**CLUS\_PARTITION\_INFO**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clus_partition_info)
</dt> <dd>

Contains data describing a [storage class resource](https://www.bing.com/search?q=storage class resource) volume and file system. It is used as the data member of a [**CLUSPROP\_PARTITION\_INFO**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_partition_info) structure and as the return value of some [control code](control-codes.md) operations.

</dd> <dt>

[**CLUS\_PARTITION\_INFO\_EX**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clus_partition_info_ex)
</dt> <dd>

Describes a [storage class resource](https://www.bing.com/search?q=storage class resource) volume and file system.

</dd> <dt>

[**CLUS\_PROVIDER\_STATE\_CHANGE\_INFO**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-_clus_provider_state_change_info)
</dt> <dd>

Contains data about the state of a [provider](https://www.bing.com/search?q=provider) resource.

</dd> <dt>

[**CLUS\_RESOURCE\_CLASS\_INFO**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clus_resource_class_info)
</dt> <dd>

Contains resource class data. It is used as the data member of a [**CLUSPROP\_RESOURCE\_CLASS\_INFO**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_resource_class_info) structure and as the return value of some [control code](control-codes.md) operations.

</dd> <dt>

[**CLUS\_SCSI\_ADDRESS**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clus_scsi_address)
</dt> <dd>

Contains [SCSI](https://www.bing.com/search?q=SCSI) address data. It is used as the data member of a [**CLUSPROP\_SCSI\_ADDRESS**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_scsi_address) structure and as the return value of some [control code](control-codes.md) operations.

</dd> <dt>

[**CLUS\_SHARED\_VOLUME\_BACKUP\_MODE**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-_clus_shared_volume_backup_mode)
</dt> <dd>

Describes the backup mode for CSV

</dd> <dt>

[**CLUS\_STARTING\_PARAMS**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clus_starting_params)
</dt> <dd>

Indicates whether a [node's](nodes.md) attempt to start the [Cluster service](cluster-service.md) represents an attempt to form or join a [cluster](https://www.bing.com/search?q=cluster), and whether the node has attempted to start this version of the Cluster service before. [Resource DLLs](resource-dlls.md) receive the CLUS\_STARTING\_PARAMS structure with the [CLUSCTL\_RESOURCE\_TYPE\_STARTING\_PHASE1](clusctl-resource-type-starting-phase1.md) and [CLUSCTL\_RESOURCE\_TYPE\_STARTING\_PHASE2](clusctl-resource-type-starting-phase2.md) control codes.

</dd> <dt>

[**CLUS\_STORAGE\_GET\_AVAILABLE\_DRIVELETTERS**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-_clus_storage_get_available_driveletters)
</dt> <dd>

Contains a bitmask of the driver letters that are available on a node. It is used as the return value of the [CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_GET\_DRIVELETTERS](clusctl-resource-type-storage-get-driveletters.md) control code.

</dd> <dt>

[**CLUS\_STORAGE\_REMAP\_DRIVELETTER**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-_clus_storage_remap_driveletter)
</dt> <dd>

Identifies the existing and target drive letter for a disk drive on a node.

</dd> <dt>

[**CLUS\_STORAGE\_SET\_DRIVELETTER**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-_clus_storage_set_driveletter)
</dt> <dd>

Supplies drive letter information for a disk partition associated with a storage class resource.

</dd> <dt>

[**CLUSPROP\_BINARY**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_binary)
</dt> <dd>

Describes a binary data value.

</dd> <dt>

[**CLUSPROP\_DISK\_NUMBER**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_dword)
</dt> <dd>

Describes a numeric value identifying the physical drive of a disk. It is used as an entry in a [value list](value-lists.md) and consists of:

-   A [**CLUSPROP\_VALUE**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_value) structure describing the format, type, and length of the numeric data.
-   A **DWORD** value identifying the physical drive of a disk.

For convenience, the [**CLUSPROP\_VALUE**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_value) members are listed explicitly:

</dd> <dt>

[**CLUSPROP\_DISK\_SIGNATURE**](/previous-versions/windows/desktop/api/ClusAPI/)
</dt> <dd>

Describes the signature that is stored on the disk for identifying it to the operating system. The [**CLUSPROP\_DISK\_SIGNATURE**](/previous-versions/windows/desktop/api/ClusAPI/) structure is used as an entry in a [value list](value-lists.md) and consists of:

-   A [**CLUSPROP\_VALUE**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_value) structure describing the format, type, and length of the numeric data.
-   A **DWORD** value.

For convenience, the [**CLUSPROP\_VALUE**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_value) members are listed explicitly:

</dd> <dt>

[**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/)
</dt> <dd>

Describes numeric data. It is used as an entry in a [value list](value-lists.md) and consists of:

-   A [**CLUSPROP\_VALUE**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_value) structure describing the format, type, and length of the numeric data.
-   A **DWORD** value.

For convenience, the [**CLUSPROP\_VALUE**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_value) members are listed explicitly:

</dd> <dt>

[**CLUSPROP\_FILETIME**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_filetime)
</dt> <dd>

Describes a date and time stamp for a file.

</dd> <dt>

[**CLUSPROP\_FTSET\_INFO**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_ftset_info)
</dt> <dd>

Contains information about an FT (fault tolerant) set. It is used as an entry in a [value list](value-lists.md) and consists of a [**CLUSPROP\_VALUE**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_value) and a [**CLUS\_FTSET\_INFO**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clus_ftset_info) structure.

</dd> <dt>

[**CLUSPROP\_LARGE\_INTEGER**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_large_integer)
</dt> <dd>

Describes a signed large integer. It is used as an entry in a [value list](value-lists.md) and consists of:

-   A [**CLUSPROP\_VALUE**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_value) structure indicating the format and type of the integer value.
-   Assigned large integer value.

For convenience, the [**CLUSPROP\_VALUE**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_value) members are listed explicitly.

</dd> <dt>

[**CLUSPROP\_LONG**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_long)
</dt> <dd>

Describes signed **LONG** data. It is used as an entry in a [value list](value-lists.md) and consists of:

-   A [**CLUSPROP\_VALUE**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_value) structure describing the format, type, and length of the numeric data.
-   A **LONG** value.

For convenience, the [**CLUSPROP\_VALUE**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_value) members are listed explicitly:

</dd> <dt>

[**CLUSPROP\_MULTI\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_sz)
</dt> <dd>

Describes multiple **NULL**-terminated Unicode strings. It is used as an entry in a [value list](value-lists.md) and consists of:

-   A [**CLUSPROP\_VALUE**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_value) structure describing the format, type, and length of the partition information.
-   A string array.

For convenience, the [**CLUSPROP\_VALUE**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_value) members are listed explicitly:

</dd> <dt>

[**CLUSPROP\_PARTITION\_INFO**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_partition_info)
</dt> <dd>

Contains information relevant to [storage class resources](https://www.bing.com/search?q=storage class resources).

</dd> <dt>

[**CLUSPROP\_PARTITION\_INFO\_EX**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_partition_info_ex)
</dt> <dd>

The [**CLUSPROP\_PARTITION\_INFO\_EX**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_partition_info_ex) structure contains information relevant to [storage class resources](https://www.bing.com/search?q=storage class resources).

</dd> <dt>

[**CLUSPROP\_PROPERTY\_NAME**](/previous-versions/windows/desktop/api/ClusAPI/)
</dt> <dd>

Describes the name of a property. It is used as an entry in a [value list](value-lists.md) and consists of:

-   A [**CLUSPROP\_VALUE**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_value) structure describing the format, type, and length of the property name.
-   A null-terminated Unicode string.

For convenience, the [**CLUSPROP\_VALUE**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_value) members are listed explicitly:

</dd> <dt>

[**CLUSPROP\_REQUIRED\_DEPENDENCY**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_required_dependency)
</dt> <dd>

Describes a [resource](resources.md) that is a required [dependency](resource-dependencies.md) of another resource. This union is used as a value in the [value list](value-lists.md) returned from a [CLUSCTL\_RESOURCE\_GET\_REQUIRED\_DEPENDENCIES](clusctl-resource-get-required-dependencies.md) or [CLUSCTL\_RESOURCE\_TYPE\_GET\_REQUIRED\_DEPENDENCIES](clusctl-resource-type-get-required-dependencies.md) [control code](control-codes.md) operation.

</dd> <dt>

[**CLUSPROP\_RESOURCE\_CLASS**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_resource_class)
</dt> <dd>

Describes a resource class. It is used as an entry in a [value list](value-lists.md) and consists of:

-   A [**CLUSPROP\_VALUE**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_value) structure describing the format, type, and length of the resource class value.
-   A [**CLUSTER\_RESOURCE\_CLASS**](/previous-versions/windows/desktop/api/ClusAPI/ne-clusapi-cluster_resource_class) value describing the resource class. **CLUSTER\_RESOURCE\_CLASS** is an enumeration defined in ClusAPI.h.

For convenience, the [**CLUSPROP\_VALUE**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_value) members are listed explicitly:

</dd> <dt>

[**CLUSPROP\_RESOURCE\_CLASS\_INFO**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_resource_class_info)
</dt> <dd>

Describes information relating to a resource class. It is used as an entry in a [value list](value-lists.md) and consists of:

-   A [**CLUSPROP\_VALUE**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_value) structure indicating the format and type of the resource class information.
-   A [**CLUS\_RESOURCE\_CLASS\_INFO**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clus_resource_class_info) structure describing the resource class and subclass of the resource.

For convenience, the [**CLUSPROP\_VALUE**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_value) and [**CLUS\_RESOURCE\_CLASS\_INFO**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clus_resource_class_info) members are listed explicitly.

</dd> <dt>

[**CLUSPROP\_SCSI\_ADDRESS**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_scsi_address)
</dt> <dd>

Describes an address for a [SCSI](https://www.bing.com/search?q=SCSI) device. It is used as an entry in a [value list](value-lists.md) and consists of:

-   A [**CLUSPROP\_VALUE**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_value) structure indicating the format and type of the resource class information.
-   A [**CLUS\_SCSI\_ADDRESS**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clus_scsi_address) structure.

For convenience, the [**CLUSPROP\_VALUE**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_value) and [**CLUS\_SCSI\_ADDRESS**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clus_scsi_address) members are listed explicitly.

</dd> <dt>

[**CLUSPROP\_SECURITY\_DESCRIPTOR**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_security_descriptor)
</dt> <dd>

Describes a security descriptor.

</dd> <dt>

[**CLUSPROP\_SYNTAX**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_syntax)
</dt> <dd>

Describes the format and type of a data value. It is used as the **Syntax** member of the [**CLUSPROP\_VALUE**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_value) structure.

</dd> <dt>

[**CLUSPROP\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/)
</dt> <dd>

Describes a null-terminated Unicode string. It is used as an entry in a [value list](value-lists.md) and consists of:

-   A [**CLUSPROP\_VALUE**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_value) structure indicating the format and type of string.
-   A null-terminated Unicode string.

For convenience, the [**CLUSPROP\_VALUE**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_value) members are listed explicitly.

</dd> <dt>

[**CLUSPROP\_ULARGE\_INTEGER**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_ularge_integer)
</dt> <dd>

Describes an unsigned large integer. It is used as an entry in a [value list](value-lists.md) and consists of:

-   A [**CLUSPROP\_VALUE**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_value) structure indicating the format and type of the integer value.
-   An unsigned large integer value.

For convenience, the [**CLUSPROP\_VALUE**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_value) members are listed explicitly.

</dd> <dt>

[**CLUSPROP\_VALUE**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_value)
</dt> <dd>

Describes the syntax and length of a data value used in a [value list](value-lists.md). The [**CLUSPROP\_VALUE**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_value) structure is used as a generic header in all of the structures that describe data of a particular type, such as [**CLUSPROP\_BINARY**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_binary) and [**CLUSPROP\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/).

</dd> <dt>

[**CLUSPROP\_WORD**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_word)
</dt> <dd>

Describes numeric data. It is used as an entry in a [value list](value-lists.md) and consists of:

-   A [**CLUSPROP\_VALUE**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_value) structure describing the format, type, and length of the numeric data.
-   A **WORD** value.

For convenience, the [**CLUSPROP\_VALUE**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_value) members are listed explicitly:

</dd> <dt>

[**SR\_RESOURCE\_TYPE\_DISK\_INFO**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-_sr_resource_type_disk_info)
</dt> <dd>

Describes a set of information that indicates whether a disk is eligible for replication.

</dd> <dt>

[**SR\_RESOURCE\_TYPE\_ELIGIBLE\_DISKS\_RESULT**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-_sr_resource_type_eligible_disks_result)
</dt> <dd>

Describes a set of data disks retrieved by a resource type control code operation for storage replication.

</dd> <dt>

[**SR\_RESOURCE\_TYPE\_QUERY\_ELIGIBLE\_LOGDISKS**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-_sr_resource_type_query_eligible_logdisks)
</dt> <dd>

Describes a set of retrieved disks that can be used as log disks for the specified data disk.

</dd> <dt>

[**SR\_RESOURCE\_TYPE\_QUERY\_ELIGIBLE\_SOURCE\_DATADISKS**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-_sr_resource_type_eligible_source_datadisks)
</dt> <dd>

Describes a set of retrieved data disks that can be used as source sites for replication.

</dd> <dt>

[**SR\_RESOURCE\_TYPE\_QUERY\_ELIGIBLE\_TARGET\_DATADISKS**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-_sr_resource_type_eligible_target_datadisks)
</dt> <dd>

Describes a set of retrieved data disks that can be used as target sites for replication.

</dd> <dt>

[**SR\_RESOURCE\_TYPE\_REPLICATED\_DISK**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-_sr_resource_type_replicated_disk)
</dt> <dd>

Represents a replicated disk.

</dd> <dt>

[**SR\_RESOURCE\_TYPE\_REPLICATED\_DISKS\_RESULT**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-_sr_resource_type_replicated_disks_result)
</dt> <dd>

Describes a retrieved set of replicated disks.

</dd> <dt>

[**SR\_RESOURCE\_TYPE\_REPLICATED\_PARTITION\_ARRAY**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-_sr_resource_type_replicated_partition_array)
</dt> <dd>

Lists the all replicated partitions on a disk.

</dd> <dt>

[**SR\_RESOURCE\_TYPE\_REPLICATED\_PARTITION\_INFO**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-_sr_resource_type_replicated_partition_info)
</dt> <dd>

Describes a replicated partition.

</dd> </dl>

## Related topics

<dl> <dt>

[Failover Cluster Structures](cluster-structures.md)
</dt> </dl>

 

 




