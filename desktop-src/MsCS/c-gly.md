---
title: C
description: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Robots: noindex, nofollow
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '60a760fc-ef79-4a1a-b4ea-8f1927f8f988'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
---

# C

[A](a-gly.md) B C [D](d-gly.md) [E](e-gly.md) [F](f-gly.md) [G](g-gly.md) [H](h-gly.md) [I](i-gly.md) J K [L](l-gly.md) [M](m-gly.md) [N](n-gly.md) [O](o-gly.md) [P](p-gly.md) [Q](q-gly.md) [R](r-gly.md) [S](s-gly.md) [T](t-gly.md) U [V](v-gly.md) [W](w-gly.md) X Y Z

<dl> <dt>

<span id="_wolf_checkpoint_manager_gly"></span><span id="_WOLF_CHECKPOINT_MANAGER_GLY"></span>**Checkpoint Manager**
</dt> <dd>

Software component in the [*Cluster service*](#-wolf-cluster-service-gly) that is responsible for saving data in the log file maintained by the [*quorum resource*](q-gly.md#-wolf-quorum-resource-gly).

</dd> <dt>

<span id="_wolf_cim_gly"></span><span id="_WOLF_CIM_GLY"></span>**CIM**
</dt> <dd>

See [*Common Information Model*](#-wolf-common-information-model-gly).

</dd> <dt>

<span id="_wolf_cim_class_gly"></span><span id="_WOLF_CIM_CLASS_GLY"></span>**CIM class**
</dt> <dd>

See [*WMI class*](w-gly.md#-wolf-wmi-class-gly).

</dd> <dt>

<span id="_wolf_client_application_gly"></span><span id="_WOLF_CLIENT_APPLICATION_GLY"></span>**client application**
</dt> <dd>

Application software that gathers data from the user, prepares it for the server, and issues a request to the server. The client presents data received from the server to the user through its own user interface.

See also [*client-server model*](#-wolf-client-server-model-gly).

</dd> <dt>

<span id="_wolf_client_server_model_gly"></span><span id="_WOLF_CLIENT_SERVER_MODEL_GLY"></span>**client-server model**
</dt> <dd>

Architecture that splits an application into a front-end client component and a back-end server component. The client component gathers data from the user, prepares it for the server, and issues a request to the server. On the back end, the server waits for requests from its clients. When the server receives a request, it processes the request and returns the requested information to the client. The client then presents the data to the user through its own user interface.

</dd> <dt>

<span id="_wolf_cluster_gly"></span><span id="_WOLF_CLUSTER_GLY"></span>**cluster**
</dt> <dd>

[*Windows Clustering*](w-gly.md#-wolf-windows-clustering-gly) defines a cluster as is a group of independent computer systems, referred to as [*nodes*](n-gly.md#-wolf-node-gly), working together as a unified computing resource. *Windows Clustering* provides two different types of clusters: [*failover cluster*](f-gly.md#mscs-failover-cluster-gly) and [*network load balancing clusters*](n-gly.md#-wolf-network-load-balancing-cluster-gly).

</dd> <dt>

<span id="_wolf_cluster_administrator_gly"></span><span id="_WOLF_CLUSTER_ADMINISTRATOR_GLY"></span>**Cluster Administrator**
</dt> <dd>

An application included with [*Windows Clustering*](w-gly.md#-wolf-windows-clustering-gly) that is used to manage and administer a server [*cluster*](#-wolf-cluster-gly). Cluster Administrator can run on any member of the trusted domain regardless of whether the computer is a cluster [*node*](n-gly.md#-wolf-node-gly).

</dd> <dt>

<span id="_wolf_cluster_administrator_extension_gly"></span><span id="_WOLF_CLUSTER_ADMINISTRATOR_EXTENSION_GLY"></span>**Cluster Administrator extension**
</dt> <dd>

A dynamic-link library (DLL) that enables [*Cluster Administrator*](#-wolf-cluster-administrator-gly) to manage a custom [*resource type*](r-gly.md#-wolf-resource-type-gly). A Cluster Administrator extension uses the Cluster Administrator Extension API and is implemented as an in-process COM server.

</dd> <dt>

<span id="_wolf_cluster_automation_server_gly"></span><span id="_WOLF_CLUSTER_AUTOMATION_SERVER_GLY"></span>**Cluster Automation Server**
</dt> <dd>

The library of COM-based interfaces that developers writing in Microsoft Visual Basic and various scripting languages use to create [*cluster management applications*](#-wolf-cluster-management-application-gly) for failover clusters.

</dd> <dt>

<span id="_wolf_cluster_aware_application_gly"></span><span id="_WOLF_CLUSTER_AWARE_APPLICATION_GLY"></span>**cluster-aware application**
</dt> <dd>

An application that runs on a [*node*](n-gly.md#-wolf-node-gly), is managed as a cluster resource, and is designed to be aware of and interact with the server [*cluster*](#-wolf-cluster-gly) environment.

</dd> <dt>

<span id="_wolf_cluster_capable_disk_gly"></span><span id="_WOLF_CLUSTER_CAPABLE_DISK_GLY"></span>**cluster-capable disk**
</dt> <dd>

A disk that satisfies the definition of a [*storage class resource*](s-gly.md#-wolf-storage-class-resource-gly). Because it can be owned by only one [*node*](n-gly.md#-wolf-node-gly) at a time, a cluster-capable disk is not a [*shared disk*](s-gly.md#-wolf-shared-disk-gly).

Also called a [*cluster disk*](#-wolf-cluster-disk-gly).

</dd> <dt>

<span id="_wolf_cluster_database_gly"></span><span id="_WOLF_CLUSTER_DATABASE_GLY"></span>**cluster database**
</dt> <dd>

A database containing property and configuration data for all [*cluster objects*](#-wolf-cluster-object-gly). The cluster database is synchronized across all [*nodes*](n-gly.md#-wolf-node-gly).

</dd> <dt>

<span id="_wolf_cluster_disk_gly"></span><span id="_WOLF_CLUSTER_DISK_GLY"></span>**cluster disk**
</dt> <dd>

A disk that satisfies the definition of a [*storage class resource*](s-gly.md#-wolf-storage-class-resource-gly). Because it can be owned by only one [*node*](n-gly.md#-wolf-node-gly) at a time, a cluster disk is not a [*shared disk*](s-gly.md#-wolf-shared-disk-gly).

Also called a [*cluster-capable disk*](#-wolf-cluster-capable-disk-gly).

</dd> <dt>

<span id="_wolf_cluster_management_application_gly"></span><span id="_WOLF_CLUSTER_MANAGEMENT_APPLICATION_GLY"></span>**cluster management application**
</dt> <dd>

A [*cluster-aware application*](#-wolf-cluster-aware-application-gly) used to manage and administer a server [*cluster*](#-wolf-cluster-gly). [*Cluster Administrator*](#-wolf-cluster-administrator-gly) is an example of such an application.

</dd> <dt>

<span id="_wolf_cluster_network_driver_gly"></span><span id="_WOLF_CLUSTER_NETWORK_DRIVER_GLY"></span>**cluster network driver**
</dt> <dd>

Failover cluster software component that monitors the status of [*network*](n-gly.md#-wolf-network-gly) paths between [*nodes*](n-gly.md#-wolf-node-gly) and detects communication failure by using periodic messages called [*heartbeats*](h-gly.md#-wolf-heartbeat-gly).

</dd> <dt>

<span id="_wolf_cluster_object_gly"></span><span id="_WOLF_CLUSTER_OBJECT_GLY"></span>**cluster object**
</dt> <dd>

A physical or logical unit managed by the [*Cluster service*](#-wolf-cluster-service-gly). The cluster objects are [*nodes*](n-gly.md#-wolf-node-gly), [*networks*](n-gly.md#-wolf-network-gly), [*network interfaces*](n-gly.md#-wolf-network-interface-gly), [*groups*](g-gly.md#-wolf-group-gly), [*resources*](r-gly.md#-wolf-resource-gly), and [*resource types*](r-gly.md#-wolf-resource-type-gly).

Also called [*cluster object*](#-wolf-cluster-object-gly).

</dd> <dt>

<span id="_wolf_cluster_server_gly"></span><span id="_WOLF_CLUSTER_SERVER_GLY"></span>**Cluster Server**
</dt> <dd>

One of the former names for the [*Failover Cluster API*](f-gly.md#mscs-failover-cluster-api-gly).

Other former names or pseudonyms include [*MSCS*](m-gly.md#-wolf-mscs-gly), [*Wolfpack*](w-gly.md#-wolf-wolfpack-gly), [*Server Cluster API*](s-gly.md#-wolf-server-cluster-api-gly), and [*Clustering Service*](#-wolf-clustering-service-gly).

</dd> <dt>

<span id="_wolf_cluster_service_gly"></span><span id="_WOLF_CLUSTER_SERVICE_GLY"></span>**Cluster service**
</dt> <dd>

The essential software component that controls all aspects of failover cluster operation and manages the [*cluster database*](#-wolf-cluster-database-gly). Each [*node*](n-gly.md#-wolf-node-gly) in a failover [*cluster*](#-wolf-cluster-gly) runs one instance of the Cluster service.

</dd> <dt>

<span id="_wolf_cluster_unaware_application_gly"></span><span id="_WOLF_CLUSTER_UNAWARE_APPLICATION_GLY"></span>**cluster-unaware application**
</dt> <dd>

An application that can run on a [*node*](n-gly.md#-wolf-node-gly) and be managed as a cluster [*resource*](r-gly.md#-wolf-resource-gly) but has no inherent knowledge of its environment. Cluster-unaware applications function the same regardless of whether they are running on a node in a failover cluster or on a non-clustered system.

</dd> <dt>

<span id="_wolf_cluster_version_gly"></span><span id="_WOLF_CLUSTER_VERSION_GLY"></span>**cluster version**
</dt> <dd>

Two version numbers that describe the versions of the Cluster service that are compatible with all active nodes. The cluster version is compared to a node's [*node version*](n-gly.md#-wolf-node-version-gly) before the node is allowed to join a cluster. The cluster version changes as nodes join and leave the cluster. The [**GetClusterInformation**](getclusterinformation.md) function retrieves the cluster version.

</dd> <dt>

<span id="_wolf_clustering_service_gly"></span><span id="_WOLF_CLUSTERING_SERVICE_GLY"></span>**Clustering Service**
</dt> <dd>

Obsolete name referring to the collection of software components and APIs that work together to implement [*failover cluster*](f-gly.md#mscs-failover-cluster-gly).

See also [*Cluster Server*](#-wolf-cluster-server-gly), [*MSCS*](m-gly.md#-wolf-mscs-gly), [*Wolfpack*](w-gly.md#-wolf-wolfpack-gly).

</dd> <dt>

<span id="_wolf_common_information_model_gly"></span><span id="_WOLF_COMMON_INFORMATION_MODEL_GLY"></span>**Common Information Model (CIM)**
</dt> <dd>

A conceptual specification supported by the [Desktop Management Task Force](http://dmtf.org/standards/cim) for applying an object-oriented, web-based model to describing management data in an enterprise network.

Used for [*WMI*](w-gly.md#-wolf-windows-management-instrumentation-gly) class specification.

</dd> <dt>

<span id="_wolf_common_property_gly"></span><span id="_WOLF_COMMON_PROPERTY_GLY"></span>**common property**
</dt> <dd>

An attribute possessed by every instance of a [*cluster object*](#-wolf-cluster-object-gly). For example, each [*node*](n-gly.md#-wolf-node-gly) has a [**NodeName**](nodes-nodename.md) property

</dd> <dt>

<span id="_wolf_configuration_object_gly"></span><span id="_WOLF_CONFIGURATION_OBJECT_GLY"></span>**configuration object**
</dt> <dd>

A COM object that implements cluster configuration interfaces in order to manage the creation and configuration of resources. See also [*managed resource*](m-gly.md#-wolf-managed-resource-gly).

</dd> <dt>

<span id="_wolf_control_code_gly"></span><span id="_WOLF_CONTROL_CODE_GLY"></span>**control code**
</dt> <dd>

A 32-bit value defined by the Failover Cluster API used to initiate an operation on a [*cluster object*](#-wolf-cluster-object-gly) or notify a [*resource DLL*](r-gly.md#-wolf-resource-dll-gly) of changes to the [*cluster*](#-wolf-cluster-gly). Control codes are categorized as [*external*](e-gly.md#-wolf-external-control-code-gly) or [*internal*](i-gly.md#-wolf-internal-control-code-gly).

</dd> <dt>

<span id="_wolf_control_code_functions_gly"></span><span id="_WOLF_CONTROL_CODE_FUNCTIONS_GLY"></span>**control code functions**
</dt> <dd>

A set of Failover Cluster API functions that take [*control codes*](#-wolf-control-code-gly) as parameters. Each [*cluster object*](#-wolf-cluster-object-gly) has one control code function and many control codes, allowing a single function to initiate several different operations.

</dd> <dt>

<span id="_wolf_core_network_name_resource_gly"></span><span id="_WOLF_CORE_NETWORK_NAME_RESOURCE_GLY"></span>**core network name resource**
</dt> <dd>

The [*Network Name resource*](n-gly.md#-wolf-network-name-resource-gly) for a Failover [*cluster*](#-wolf-cluster-gly).

</dd> <dt>

<span id="_wolf_custom_resource_type_gly"></span><span id="_WOLF_CUSTOM_RESOURCE_TYPE_GLY"></span>**custom resource type**
</dt> <dd>

A [*resource type*](r-gly.md#-wolf-resource-type-gly) defined by a third-party developer using the Failover Cluster API. Creating a custom resource type involves writing a [*resource DLL*](r-gly.md#-wolf-resource-dll-gly) and a [*Cluster Administrator extension*](#-wolf-cluster-administrator-extension-gly).

</dd> </dl>

 

 




