---
title: P
description: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Robots: noindex, nofollow
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d1052185-c938-4054-9308-8c6213f029ec
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# P

[A](a-gly.md) B [C](c-gly.md) [D](d-gly.md) [E](e-gly.md) [F](f-gly.md) [G](g-gly.md) [H](h-gly.md) [I](i-gly.md) J K [L](l-gly.md) [M](m-gly.md) [N](n-gly.md) [O](o-gly.md) P [Q](q-gly.md) [R](r-gly.md) [S](s-gly.md) [T](t-gly.md) U [V](v-gly.md) [W](w-gly.md) X Y Z

<dl> <dt>

<span id="_wolf_parameter_block_gly"></span><span id="_WOLF_PARAMETER_BLOCK_GLY"></span>**parameter block**
</dt> <dd>

A buffer that contains the data for one or more properties, or a pointer to the data. Entries in a [*property table*](#-wolf-property-table-gly) contain an offset to a parameter block.

</dd> <dt>

<span id="_wolf_partitioned_gly"></span><span id="_WOLF_PARTITIONED_GLY"></span>**partitioned**
</dt> <dd>

A state in which one or more of the [*nodes*](https://www.bing.com/search?q=*nodes*) in a server [*cluster*](https://www.bing.com/search?q=*cluster*) cannot communicate with the other nodes.

</dd> <dt>

<span id="_wolf_paused_gly"></span><span id="_WOLF_PAUSED_GLY"></span>**paused**
</dt> <dd>

State that applies to a [*node*](https://www.bing.com/search?q=*node*) that is a fully [*active*](https://www.bing.com/search?q=*active*) member in the server [*cluster*](https://www.bing.com/search?q=*cluster*) but cannot host [*groups*](https://www.bing.com/search?q=*groups*). The paused state is provided for an administrator to perform maintenance.

</dd> <dt>

<span id="_wolf_pending_gly"></span><span id="_WOLF_PENDING_GLY"></span>**pending**
</dt> <dd>

State that refers to a [*resource*](https://www.bing.com/search?q=*resource*) being brought [*online*](https://www.bing.com/search?q=*online*) or taken [*offline*](https://www.bing.com/search?q=*offline*).

</dd> <dt>

<span id="_wolf_persistent_arbitration_gly"></span><span id="_WOLF_PERSISTENT_ARBITRATION_GLY"></span>**persistent arbitration**
</dt> <dd>

The process by which a [*node*](https://www.bing.com/search?q=*node*) gains control of the [*quorum resource*](https://www.bing.com/search?q=*quorum resource*) and defends its control. The [*SCSI*](https://www.bing.com/search?q=*SCSI*) reserve and release functions can be used to implement this type of arbitration support.

</dd> <dt>

<span id="_wolf_physical_disk_resource_gly"></span><span id="_WOLF_PHYSICAL_DISK_RESOURCE_GLY"></span>**Physical Disk resource**
</dt> <dd>

A [*cluster-capable disk*](https://www.bing.com/search?q=*cluster-capable disk*) being managed as a cluster [*resource*](https://www.bing.com/search?q=*resource*) by the Physical Disk [*resource type*](https://www.bing.com/search?q=*resource type*)

.

</dd> <dt>

<span id="_wolf_possible_owner_gly"></span><span id="_WOLF_POSSIBLE_OWNER_GLY"></span>**possible owner**
</dt> <dd>

A [*node*](https://www.bing.com/search?q=*node*) on which a resource is capable of running. Each [*resource*](https://www.bing.com/search?q=*resource*) is associated with a list of possible owners. Resources will [*fail over*](https://www.bing.com/search?q=*fail over*) only to nodes that are listed as possible owners.

</dd> <dt>

<span id="_wolf_preferred_owner_gly"></span><span id="_WOLF_PREFERRED_OWNER_GLY"></span>**preferred owner**
</dt> <dd>

A [*node*](https://www.bing.com/search?q=*node*) on which a [*group*](https://www.bing.com/search?q=*group*) prefers to run. Each group is associated with a list of preferred owners sorted in order of preference. During [*failover*](https://www.bing.com/search?q=*failover*), the group is moved to the next preferred node in the preferred owner list.

</dd> <dt>

<span id="_wolf_print_spooler_resource_gly"></span><span id="_WOLF_PRINT_SPOOLER_RESOURCE_GLY"></span>**Print Spooler resource**
</dt> <dd>

A print spooler being managed as a cluster [*resource*](https://www.bing.com/search?q=*resource*) by the Print Spooler [*resource type*](https://www.bing.com/search?q=*resource type*)

.

</dd> <dt>

<span id="_wolf_private_property_gly"></span><span id="_WOLF_PRIVATE_PROPERTY_GLY"></span>**private property**
</dt> <dd>

An attribute possessed by an individual instance of a [*cluster object*](https://www.bing.com/search?q=*cluster object*). Other instances may or may not possess the same [*property*](#-wolf-property-gly).

</dd> <dt>

<span id="_wolf_property_gly"></span><span id="_WOLF_PROPERTY_GLY"></span>**property**
</dt> <dd>

An attribute associated with a [*cluster object*](https://www.bing.com/search?q=*cluster object*) that describes an identity or behavior for the object. A property can consist of multiple property values, each of which can consist of multiple data values. For example, if a property consists of multiple **DWORD** arrays, each array is considered a property value, and each array element is considered a data value.

</dd> <dt>

<span id="_wolf_property_access_gly"></span><span id="_WOLF_PROPERTY_ACCESS_GLY"></span>**property access**
</dt> <dd>

A characteristic of a property that determines the user's ability to change the property. A property's access can be read/write or read-only.

</dd> <dt>

<span id="_wolf_property_list_gly"></span><span id="_WOLF_PROPERTY_LIST_GLY"></span>**property list**
</dt> <dd>

A collection of information used to describe multiple properties in [*control code*](https://www.bing.com/search?q=*control code*) operations. Each entry in a property list consists of a [*value list*](https://www.bing.com/search?q=*value list*) containing a property name and one or more [*property values*](#-wolf-property-value-gly). Each property value, in turn, consists of one or more [*data values*](https://www.bing.com/search?q=*data values*).

</dd> <dt>

<span id="_wolf_property_scope_gly"></span><span id="_WOLF_PROPERTY_SCOPE_GLY"></span>**property scope**
</dt> <dd>

A characteristic of a [*property*](#-wolf-property-gly) that determines which objects the property applies to. A property can be [*common*](https://www.bing.com/search?q=*common*) or [*private*](#-wolf-private-property-gly) in scope.

</dd> <dt>

<span id="_wolf_property_status_gly"></span><span id="_WOLF_PROPERTY_STATUS_GLY"></span>**property status**
</dt> <dd>

A characteristic of a [*private property*](#-wolf-private-property-gly) that determines whether the property must have a value. Private properties can have a status of required (must have a valid value) or optional (does not need a value).

</dd> <dt>

<span id="_wolf_property_table_gly"></span><span id="_WOLF_PROPERTY_TABLE_GLY"></span>**property table**
</dt> <dd>

An array of [**RESUTIL\_PROPERTY\_ITEM**](/previous-versions/windows/desktop/api/ResApi/ns-resapi-resutil_property_item) structures used to store multiple properties.

</dd> <dt>

<span id="_wolf_property_value_gly"></span><span id="_WOLF_PROPERTY_VALUE_GLY"></span>**property value**
</dt> <dd>

One of the values associated with a multivalue property. A [*cluster object*](https://www.bing.com/search?q=*cluster object*) property consists of one or more property values, each consisting of one or more [*data values*](https://www.bing.com/search?q=*data values*). For example, if a property consists of multiple **DWORD** arrays, each array is considered a property value, and each array element is considered a data value.

</dd> <dt>

<span id="_wolf_provider_gly"></span><span id="_WOLF_PROVIDER_GLY"></span>**provider**
</dt> <dd>

A provider is a resource with one or more dependent resources. For example, the netname resource depends on the IP1 or IP2 resources. In that case, IP1 and IP2 are both providers in relation to netname.

</dd> </dl>

 

 




