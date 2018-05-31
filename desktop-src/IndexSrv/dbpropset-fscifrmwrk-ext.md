---
title: DBPROPSET\_FSCIFRMWRK\_EXT
description: DBPROPSET\_FSCIFRMWRK\_EXT
ms.assetid: b53486be-b9c0-435b-b002-16c815b1b5f2
keywords:
- DBPROPSET_FSCIFRMWRK_EXT
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DBPROPSET\_FSCIFRMWRK\_EXT

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The DBPROPSET\_FSCIFRMWRK\_EXT property set contains file system properties that represent the catalog name and the scopes indexed by that catalog.

``` syntax
#define DBPROPSET_FSCIFRMWRK_EXT \
    { 0xA9BD1526, 0x6A80, 0x11D0, \
        { 0x8C, 0x9D, 0x00, 0x20, 0xAF, 0x1D, 0x74, 0x0E } }
```

### Remarks

The DBPROPSET\_FSCIFRMWRK\_EXT property set contains the following property constants:

<dl> <dt>

<span id="DBPROP_CI_CATALOG_NAME"></span><span id="dbprop_ci_catalog_name"></span>DBPROP\_CI\_CATALOG\_NAME
</dt> <dd>

Property ID 2. PIDContent Index catalog name.

</dd> <dt>

<span id="DBPROP_CI_INCLUDE_SCOPES"></span><span id="dbprop_ci_include_scopes"></span>DBPROP\_CI\_INCLUDE\_SCOPES
</dt> <dd>

Property ID 3. Directories indexed by a catalog.

</dd> <dt>

<span id="DBPROP_CI_SCOPE_FLAGS"></span><span id="dbprop_ci_scope_flags"></span>DBPROP\_CI\_SCOPE\_FLAGS
</dt> <dd>

Property ID 4. A combination of [QUERY\_\* scope constants](query-scope-constants.md).

</dd> <dt>

<span id="DBPROP_CI_EXCLUDE_SCOPES"></span><span id="dbprop_ci_exclude_scopes"></span>DBPROP\_CI\_EXCLUDE\_SCOPES
</dt> <dd>

Property ID 5. Directories excluded from indexing by a catalog.

</dd> <dt>

<span id="DBPROP_CI_SECURITY_ID"></span><span id="dbprop_ci_security_id"></span>DBPROP\_CI\_SECURITY\_ID
</dt> <dd>

Property ID 6. Security ID of query. Reserved for future use.

</dd> <dt>

<span id="DBPROP_CI_QUERY_TYPE"></span><span id="dbprop_ci_query_type"></span>DBPROP\_CI\_QUERY\_TYPE
</dt> <dd>

Property ID 7. Type of query. Reserved for future use.

</dd> </dl>

## Related topics

<dl> <dt>

[OLE DB Provider for Indexing Service](ole-db-provider-for-indexing-service.md)
</dt> <dt>

[QUERY\_\* Scope Constants](query-scope-constants.md)
</dt> </dl>

 

 




