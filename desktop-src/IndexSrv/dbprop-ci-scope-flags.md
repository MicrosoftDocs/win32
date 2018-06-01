---
Description: DBPROP\_CI\_SCOPE\_FLAGS
ms.assetid: 5ff75464-55d3-4d27-9046-37a765cc99a0
title: DBPROP\_CI\_SCOPE\_FLAGS
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DBPROP\_CI\_SCOPE\_FLAGS

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **DBPROP\_CI\_SCOPE\_FLAGS** property specifies attributes of the scopes specified for [**DBPROP\_CI\_INCLUDE\_SCOPES**](dbprop-ci-include-scopes.md).

### Summary



|                  |                                      |
|------------------|--------------------------------------|
| **Property Set** | DBPROPSET\_FSCIFRMWRK\_EXT           |
| **Property ID**  | DBPROP\_CI\_SCOPE\_FLAGS             |
| **Value Type**   | DBTYPE\_UI4                          |
| **Default**      | QUERY\_DEEP \| QUERY\_PHYSICAL\_PATH |



 

<dl> <dt>

<span id="QUERY_SHALLOW"></span><span id="query_shallow"></span>QUERY\_SHALLOW
</dt> <dd>

Only files in the scope directory are included in the results. Cannot be combined with QUERY\_DEEP.

</dd> <dt>

<span id="QUERY_DEEP"></span><span id="query_deep"></span>QUERY\_DEEP
</dt> <dd>

Files in the scope directory and all subdirectories are included in the results. Cannot be combined with QUERY\_SHALLOW.

</dd> <dt>

<span id="QUERY_PHYSICAL_PATH"></span><span id="query_physical_path"></span>QUERY\_PHYSICAL\_PATH
</dt> <dd>

The scope is a physical directory. Cannot be combined with QUERY\_VIRTUAL\_PATH.

</dd> <dt>

<span id="QUERY_VIRTUAL_PATH"></span><span id="query_virtual_path"></span>QUERY\_VIRTUAL\_PATH
</dt> <dd>

The scope is a virtual IIS directory. Cannot be combined with QUERY\_PHYSICAL\_PATH.

</dd> </dl>

### Remarks

When you set a flag using these values, perform the logical **OR** operation of one of QUERY\_SHALLOW or QUERY\_DEEP with one of QUERY\_PHYSICAL\_PATH or QUERY\_VIRTUAL\_PATH.

If more than one catalog or machine is specified, the [**DBPROP\_MACHINE**](dbprop-machine.md), [**DBPROP\_CI\_CATALOG\_NAME**](dbprop-ci-catalog-name.md), [**DBPROP\_CI\_INCLUDE\_SCOPES**](dbprop-ci-include-scopes.md), and [**DBPROP\_CI\_SCOPE\_FLAGS**](https://www.bing.com/search?q=**DBPROP\_CI\_SCOPE\_FLAGS**) properties must all have the same number of entries. The exception is that if more than one catalog or machine is specified, the count of scopes and flags can be either the count of catalogs and machines or 1.

When more than one machine or catalog is specified, the query is executed on multiple machines and the results are merged on the local machine.

This property corresponds to the *CiFlags* variable in the [Internet Data Query Files](internet-data-query-files.md) of Indexing Service.

 

 



