---
title: ClusProperty.Type property
description: Returns or sets the type of a cluster object property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4cae1bb4-2ca4-4957-b174-1dc07676ce3a
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Type property Failover Cluster
- Type property Failover Cluster , ClusProperty object
- ClusProperty object Failover Cluster , Type property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ClusProperty.Type property

\[The **Type** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns or sets the type of a [cluster object property](cluster-object-properties.md).

This property is read-only.

## Syntax


```VB
ClusProperty.Type
```



## Property value

**Long** describing the type of the cluster object property. MsClus.h defines the following types, enumerated in the [**CLUSTER\_PROPERTY\_TYPE**](/windows/previous-versions/ClusAPI/ne-clusapi-cluster_property_type?branch=master) enumeration

<dt>

<span id="CLUSPROP_TYPE_DISK_NUMBER"></span><span id="clusprop_type_disk_number"></span>

<span id="CLUSPROP_TYPE_DISK_NUMBER"></span><span id="clusprop_type_disk_number"></span>**CLUSPROP\_TYPE\_DISK\_NUMBER** (7)


</dt> <dd>

Describes the number value of a disk resource. A disk number value is represented by a [**CLUSPROP\_DISK\_NUMBER**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_dword?branch=master) structure.

</dd> <dt>

<span id="CLUSPROP_TYPE_DISK_SERIALNUMBER"></span><span id="clusprop_type_disk_serialnumber"></span>

<span id="CLUSPROP_TYPE_DISK_SERIALNUMBER"></span><span id="clusprop_type_disk_serialnumber"></span>**CLUSPROP\_TYPE\_DISK\_SERIALNUMBER** (10)


</dt> <dd>

Describes the serial number of a disk resource.

</dd> <dt>

<span id="CLUSPROP_TYPE_DISK_GUID"></span><span id="clusprop_type_disk_guid"></span>

<span id="CLUSPROP_TYPE_DISK_GUID"></span><span id="clusprop_type_disk_guid"></span>**CLUSPROP\_TYPE\_DISK\_GUID** (11)


</dt> <dd>

Describes the **GUID** of a disk resource.

</dd> <dt>

<span id="CLUSPROP_TYPE_DISK_SIZE"></span><span id="clusprop_type_disk_size"></span>

<span id="CLUSPROP_TYPE_DISK_SIZE"></span><span id="clusprop_type_disk_size"></span>**CLUSPROP\_TYPE\_DISK\_SIZE** (12)


</dt> <dd>

TBD

</dd> <dt>

<span id="CLUSPROP_TYPE_ENDMARK"></span><span id="clusprop_type_endmark"></span>

<span id="CLUSPROP_TYPE_ENDMARK"></span><span id="clusprop_type_endmark"></span>**CLUSPROP\_TYPE\_ENDMARK** (0)


</dt> <dd>

Designates the data value as the last entry in a property or value list.

</dd> <dt>

<span id="CLUSPROP_TYPE_LIST_VALUE"></span><span id="clusprop_type_list_value"></span>

<span id="CLUSPROP_TYPE_LIST_VALUE"></span><span id="clusprop_type_list_value"></span>**CLUSPROP\_TYPE\_LIST\_VALUE** (1)


</dt> <dd>

Describes a data value in a property list. For example, in the property list passed to a [control code function](control-code-functions.md) for a property validation operation, **CLUSPROP\_TYPE\_LIST\_VALUE** is the required type to be included with each property value.

</dd> <dt>

<span id="CLUSPROP_TYPE_NAME"></span><span id="clusprop_type_name"></span>

<span id="CLUSPROP_TYPE_NAME"></span><span id="clusprop_type_name"></span>**CLUSPROP\_TYPE\_NAME** (4)


</dt> <dd>

Describes a data value used as a name, such as a property name. A name value is represented by a [**CLUSPROP\_PROPERTY\_NAME**](/windows/previous-versions/ClusAPI/?branch=master) structure.

</dd> <dt>

<span id="CLUSPROP_TYPE_PARTITION_INFO"></span><span id="clusprop_type_partition_info"></span>

<span id="CLUSPROP_TYPE_PARTITION_INFO"></span><span id="clusprop_type_partition_info"></span>**CLUSPROP\_TYPE\_PARTITION\_INFO** (8)


</dt> <dd>

Describes a collection of information about a disk resource, such as its device name and volume label. Partition data is represented by a [**CLUSPROP\_PARTITION\_INFO**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_partition_info?branch=master) structure.

</dd> <dt>

<span id="CLUSPROP_TYPE_PARTITION_INFO_EX"></span><span id="clusprop_type_partition_info_ex"></span>

<span id="CLUSPROP_TYPE_PARTITION_INFO_EX"></span><span id="clusprop_type_partition_info_ex"></span>**CLUSPROP\_TYPE\_PARTITION\_INFO\_EX** (13)


</dt> <dd>

Describes a collection of information about a disk resource, such as its device name and volume label. Partition data is represented by a [**CLUSPROP\_PARTITION\_INFO\_EX**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_partition_info_ex?branch=master) structure.

</dd> <dt>

<span id="CLUSPROP_TYPE_RESCLASS"></span><span id="clusprop_type_resclass"></span>

<span id="CLUSPROP_TYPE_RESCLASS"></span><span id="clusprop_type_resclass"></span>**CLUSPROP\_TYPE\_RESCLASS** (2)


</dt> <dd>

Describes resource class information. A resource class value is described with a [**CLUSPROP\_RESOURCE\_CLASS**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_resource_class?branch=master) structure. Resource classes are returned when an application calls [**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master) or [**ClusterResourceTypeControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcetypecontrol?branch=master) with one of the following control codes.

[CLUSCTL\_RESOURCE\_GET\_CLASS\_INFO](clusctl-resource-get-class-info.md)

[CLUSCTL\_RESOURCE\_TYPE\_GET\_CLASS\_INFO](clusctl-resource-type-get-class-info.md)

[CLUSCTL\_RESOURCE\_TYPE\_GET\_REQUIRED\_DEPENDENCIES](clusctl-resource-type-get-required-dependencies.md)

</dd> <dt>

<span id="CLUSPROP_TYPE_SCSI_ADDRESS"></span><span id="clusprop_type_scsi_address"></span>

<span id="CLUSPROP_TYPE_SCSI_ADDRESS"></span><span id="clusprop_type_scsi_address"></span>**CLUSPROP\_TYPE\_SCSI\_ADDRESS** (6)


</dt> <dd>

Describes an [**Address**](ip-addresses-address.md) property for an [IP Address](ip-address.md) resource. A SCSI address value is represented by a [**CLUSPROP\_SCSI\_ADDRESS**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_scsi_address?branch=master) structure.

</dd> <dt>

<span id="CLUSPROP_TYPE_SIGNATURE"></span><span id="clusprop_type_signature"></span>

<span id="CLUSPROP_TYPE_SIGNATURE"></span><span id="clusprop_type_signature"></span>**CLUSPROP\_TYPE\_SIGNATURE** (5)


</dt> <dd>

Describes a [**Signature**](physical-disks-signature.md) property for a disk resource. A signature value is represented by a [**CLUSPROP\_DISK\_SIGNATURE**](/windows/previous-versions/ClusAPI/?branch=master) structure.

</dd> <dt>

<span id="CLUSPROP_TYPE_UNKNOWN"></span><span id="clusprop_type_unknown"></span>

<span id="CLUSPROP_TYPE_UNKNOWN"></span><span id="clusprop_type_unknown"></span>**CLUSPROP\_TYPE\_UNKNOWN** (-1)


</dt> <dd>

The property value type is unknown.

</dd> <dt>

<span id="CLUSPROP_TYPE_USER"></span><span id="clusprop_type_user"></span>

<span id="CLUSPROP_TYPE_USER"></span><span id="clusprop_type_user"></span>**CLUSPROP\_TYPE\_USER** (32768)


</dt> <dd>

Describes the beginning of the range for users to define their own types. Associate this type with user-defined private properties.

</dd> </dl>

## Remarks

The **Type** property corresponds to the **wType** member of a [**CLUSPROP\_SYNTAX**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_syntax?branch=master) union.

For information on making constants defined by the Cluster Automation Server type library (MsClus.tlb) available to scripts, see [Creating a Cluster Automation Server Script](creating-a-cluster-automation-server-script.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusProperty is defined as F2E606FE-2631-11D1-89F1-00A0C90D061E<br/>     |



## See also

<dl> <dt>

[**ClusProperty**](clusproperty-object.md)
</dt> <dt>

[**ClusProperty.Format**](clusproperty-format.md)
</dt> <dt>

[**CLUSPROP\_SYNTAX**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_syntax?branch=master)
</dt> <dt>

[**CLUSTER\_PROPERTY\_TYPE**](/windows/previous-versions/ClusAPI/ne-clusapi-cluster_property_type?branch=master)
</dt> </dl>

 

 





