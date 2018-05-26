---
title: Failover Cluster Macros
description: The Failover Cluster API provides the following macros, which you can use to work with data structures and property lists.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b8c636d1-ae4d-4a70-bab8-2b161e6ca0a8
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- macros Failover Cluster
- structures Failover Cluster , macros
- property lists Failover Cluster ,macros
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Failover Cluster Macros

The Failover Cluster API provides the following macros, which you can use to work with [data structures](data-structures.md) and [property lists](property-lists.md).

## In this section

<dl> <dt>

[**ALIGN\_CLUSPROP**](/windows/previous-versions/ClusAPI/nf-clusapi-align_clusprop?branch=master)
</dt> <dd>

Aligns structures properly within [value lists](value-lists.md).

</dd> <dt>

[**CLRES\_V1\_FUNCTION\_TABLE**](/windows/previous-versions/ResApi/nf-resapi-clres_v1_function_table?branch=master)
</dt> <dd>

Initializes a function table for version 1.0 of the [Resource API](resource-api.md).

</dd> <dt>

[**CLRES\_V2\_FUNCTION\_TABLE\_SET**](/windows/previous-versions/ResApi/nf-resapi-clres_v2_function_table_set?branch=master)
</dt> <dd>

Initializes a function table for version 2.0 of the [Resource API](resource-api.md).

</dd> <dt>

[**CLRES\_V3\_FUNCTION\_TABLE\_SET**](/windows/previous-versions/ResApi/nf-resapi-clres_v3_function_table_set?branch=master)
</dt> <dd>

Initializes a function table for version 3.0 of the [Resource API](resource-api.md).

</dd> <dt>

[**CLRES\_V4\_FUNCTION\_TABLE\_SET**](/windows/previous-versions/ResApi/nf-resapi-clres_v4_function_table_set?branch=master)
</dt> <dd>

Initializes a function table for version 4.0 of the [Resource API](resource-api.md).

</dd> <dt>

[**CLUSCTL\_GET\_ACCESS\_MODE**](/windows/previous-versions/ClusAPI/nf-clusapi-clusctl_get_access_mode?branch=master)
</dt> <dd>

Extracts the access code from a control code. For more information on the various codes that comprise a control code, see [Control Code Architecture](control-code-architecture.md).

</dd> <dt>

[**CLUSCTL\_GET\_CONTROL\_FUNCTION**](/windows/previous-versions/ClusAPI/nf-clusapi-clusctl_get_control_function?branch=master)
</dt> <dd>

Extracts the operation code from a control code. For more information on the various codes that comprise a control code, see [Control Code Architecture](control-code-architecture.md).

</dd> <dt>

[**CLUSCTL\_GET\_CONTROL\_OBJECT**](/windows/previous-versions/ClusAPI/nf-clusapi-clusctl_get_control_object?branch=master)
</dt> <dd>

Extracts the object code from a control code. For more information on the various codes that comprise a control code, see [Control Code Architecture](control-code-architecture.md).

</dd> <dt>

[**CLUSCTL\_GET\_USER**](/windows/previous-versions/ClusAPI/nf-clusapi-clusctl_get_user?branch=master)
</dt> <dd>

Retrieves the user bit from a control code. For more information, see [Control Code Architecture](control-code-architecture.md).

</dd> <dt>

[**CLUSCTL\_USER\_CODE**](/windows/previous-versions/ClusAPI/nf-clusapi-clusctl_user_code?branch=master)
</dt> <dd>

Generates a correctly formatted user-defined control code. For more information on the bit layout of control codes, see [Control Code Architecture](control-code-architecture.md).

</dd> <dt>

[**CLUSPROP\_BINARY\_DECLARE**](/windows/previous-versions/ClusAPI/nf-clusapi-clusprop_binary_declare?branch=master)
</dt> <dd>

Creates a [**CLUSPROP\_BINARY**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_binary?branch=master) structure with the **rgb** member set to a size determined by the caller.

</dd> <dt>

[**CLUSPROP\_PROPERTY\_NAME\_DECLARE**](/windows/previous-versions/ClusAPI/nf-clusapi-clusprop_property_name_declare?branch=master)
</dt> <dd>

Creates a [**CLUSPROP\_PROPERTY\_NAME**](/windows/previous-versions/ClusAPI/?branch=master) structure with the **sz** member set to a size determined by the caller.

</dd> <dt>

[**CLUSPROP\_SZ\_DECLARE**](/windows/previous-versions/ClusAPI/nf-clusapi-clusprop_sz_declare?branch=master)
</dt> <dd>

Creates a [**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master) structure with the **sz** member set to a size determined by the caller.

</dd> <dt>

[**CLUSTER\_GET\_MAJOR\_VERSION**](/windows/previous-versions/ClusAPI/nf-clusapi-cluster_get_major_version?branch=master)
</dt> <dd>

Extracts the major version portion of a [Cluster service](cluster-service.md) version number.

</dd> <dt>

[**CLUSTER\_GET\_MINOR\_VERSION**](/windows/previous-versions/ClusAPI/nf-clusapi-cluster_get_minor_version?branch=master)
</dt> <dd>

Extracts the minor version portion of a [Cluster service](cluster-service.md) version number.

</dd> <dt>

[**CLUSTER\_GET\_UPGRADE\_VERSION**](/windows/previous-versions/ClusAPI/nf-clusapi-cluster_get_upgrade_version?branch=master)
</dt> <dd>

Extracts the upgrade version portion of a [Cluster service](cluster-service.md) version number.

</dd> <dt>

[**CLUSTER\_MAKE\_VERSION**](/windows/previous-versions/ClusAPI/nf-clusapi-cluster_make_version?branch=master)
</dt> <dd>

Creates a Cluster service version number.

</dd> </dl>

## Related topics

<dl> <dt>

[Failover Cluster Reference](failover-cluster-reference.md)
</dt> </dl>

 

 




