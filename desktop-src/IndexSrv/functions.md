---
title: Functions
description: Functions
ms.assetid: faec3725-4cc2-4a0c-98a3-68b2774ad99b
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Functions

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Indexing Service provides functions for finding and managing catalogs, determining the catalog file's path, for creating Microsoft OLE DB [**Command**](mdobjcommand) objects to query catalogs using [Query Languages for Indexing Service](query-languages-for-indexing-service.md), and for filtering files.

The following tables list the functions in each category.



| For finding and managing catalogs          | Description                                          |
|--------------------------------------------|------------------------------------------------------|
| [**CIState**](/windows/win32/Ntquery/nf-ntquery-cistate?branch=master)                 | Queries the state of the selected catalog.           |
| [**LocateCatalogs**](/windows/win32/Ntquery/nf-ntquery-locatecatalogsa?branch=master)   | Finds the catalog that indexes a directory.          |
| [**SetCatalogState**](/windows/win32/Ntquery/nf-ntquery-setcatalogstate?branch=master) | Sets the catalog state for backup or other purposes. |



 



| For creating queries using OLE DB command objects          | Description                                                                                                                               |
|------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| [**CICreateCommand**](/windows/win32/Ntquery/nf-ntquery-cicreatecommand?branch=master)                 | Creates a [**Command**](mdobjcommand) object.                                                                                             |
| [**CIMakeICommand**](/windows/win32/Ntquery/nf-ntquery-cimakeicommand?branch=master)                   | Creates a [**Command**](mdobjcommand) object, specifying computers, catalogs, and scopes.                                                 |
| [**CIBuildQueryNode**](/windows/win32/Ntquery/nf-ntquery-cibuildquerynode?branch=master)               | Builds one node of a query restriction tree for a [**Command**](mdobjcommand) object.                                                     |
| [**CIBuildQueryTree**](/windows/win32/Ntquery/nf-ntquery-cibuildquerytree?branch=master)               | Builds a query restriction tree for a [**Command**](mdobjcommand) object.                                                                 |
| [**CIRestrictionToFullTree**](/windows/win32/Ntquery/nf-ntquery-cirestrictiontofulltree?branch=master) | Converts a query restriction tree with columns, sort columns, and grouping columns to a [**DBCOMMANDTREE**](dbcommandtree.md) structure. |
| [**CITextToFullTree**](/windows/win32/Ntquery/nf-ntquery-citexttofulltree?branch=master)               | Creates a full command tree using Query Language 1.                                                                                       |
| [**CITextToFullTreeEx**](/windows/win32/Ntquery/nf-ntquery-citexttofulltreeex?branch=master)           | Creates a full command tree using the Query Language Dialect that you specify.                                                            |
| [**CITextToSelectTree**](/windows/win32/Ntquery/nf-ntquery-citexttoselecttree?branch=master)           | Creates a **SELECT** node for a [**DBCOMMANDTREE**](dbcommandtree.md) structure using Query Language Dialect 1.                          |
| [**CITextToSelectTreeEx**](/windows/win32/Ntquery/nf-ntquery-citexttoselecttreeex?branch=master)       | Creates a **SELECT** node for a [**DBCOMMANDTREE**](dbcommandtree.md) structure using the Query Language Dialect that you specify.       |



 



| For filtering files                                      | Description                                                                                                      |
|----------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| [**LoadIFilter**](/windows/win32/Ntquery/nf-ntquery-loadifilter?branch=master)                       | Retrieves [**IFilter**](/windows/win32/Filter/nn-filter-ifilter?branch=master) from path name for object.                                                  |
| [**BindIFilterFromStorage**](/windows/win32/Ntquery/nf-ntquery-bindifilterfromstorage?branch=master) | Given the [**IStorage**](_stg_istorage) interface pointer, retrieves the appropriate [**IFilter**](/windows/win32/Filter/nn-filter-ifilter?branch=master). |
| [**BindIFilterFromStream**](/windows/win32/Ntquery/nf-ntquery-bindifilterfromstream?branch=master)   | Given the [**IStream**](_stg_istream) interface pointer, retrieves the appropriate [**IFilter**](/windows/win32/Filter/nn-filter-ifilter?branch=master).   |



 

 

 




