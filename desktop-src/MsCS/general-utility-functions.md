---
title: General Utility Functions
description: The general utility functions are used by applications and resource DLLs to perform common tasks such as duplicating strings and validating paths.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 03ba13be-39ea-4352-8218-18f4ed52bd99
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- general utility functions Failover Cluster
- cluster utility functions Failover Cluster ,general utility functions
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# General Utility Functions

The general utility functions are used by applications and [resource DLLs](resource-dlls.md) to perform common tasks such as duplicating strings and validating paths.

## In this section

<dl> <dt>

[*ResUtilCreateDirectoryTree*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_create_directory_tree)
</dt> <dd>

Creates every directory specified in a path, skipping directories that already exist. The **PRESUTIL\_CREATE\_DIRECTORY\_TREE** type defines a pointer to this function.

</dd> <dt>

[*ResUtilDupString*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_dup_string)
</dt> <dd>

Duplicates a null-terminated Unicode string.

</dd> <dt>

[*ResUtilExpandEnvironmentStrings*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_expand_environment_strings)
</dt> <dd>

Expands strings containing unexpanded references to environment variables. The **PRESUTIL\_EXPAND\_ENVIRONMENT\_STRINGS** type defines a pointer to this function.

</dd> <dt>

[*ResUtilGetPropertyFormats*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_get_property_formats)
</dt> <dd>

Returns a property format list describing the format of a specified set of properties. The **PRESUTIL\_GET\_PROPERTY\_FORMATS** type defines a pointer to this function.

</dd> <dt>

[**ResUtilInitializeResourceStatus**](/previous-versions/windows/desktop/api/ResApi/nf-resapi-resutilinitializeresourcestatus)
</dt> <dd>

Initializes a [**RESOURCE\_STATUS**](/previous-versions/windows/desktop/api/ResApi/ns-resapi-resource_status) structure.

</dd> <dt>

[*ResUtilIsPathValid*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_is_path_valid)
</dt> <dd>

Checks whether a path is syntactically valid.

</dd> </dl>

## Related topics

<dl> <dt>

[Failover Cluster Utility Functions](cluster-utility-functions.md)
</dt> </dl>

 

 




