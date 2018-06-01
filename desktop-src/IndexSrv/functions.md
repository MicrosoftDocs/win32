---
title: Functions
description: Functions
ms.assetid: faec3725-4cc2-4a0c-98a3-68b2774ad99b
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Functions

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Indexing Service provides functions for finding and managing catalogs, determining the catalog file's path, for creating Microsoft OLE DB [**Command**](https://www.bing.com/search?q=**Command**) objects to query catalogs using [Query Languages for Indexing Service](query-languages-for-indexing-service.md), and for filtering files.

The following tables list the functions in each category.



| For finding and managing catalogs          | Description                                          |
|--------------------------------------------|------------------------------------------------------|
| [**CIState**](/windows/desktop/api/Ntquery/nf-ntquery-cistate)                 | Queries the state of the selected catalog.           |
| [**LocateCatalogs**](/windows/desktop/api/Ntquery/nf-ntquery-locatecatalogsa)   | Finds the catalog that indexes a directory.          |
| [**SetCatalogState**](/windows/desktop/api/Ntquery/nf-ntquery-setcatalogstate) | Sets the catalog state for backup or other purposes. |



 



| For creating queries using OLE DB command objects          | Description                                                                                                                               |
|------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| [**CICreateCommand**](/windows/desktop/api/Ntquery/nf-ntquery-cicreatecommand)                 | Creates a [**Command**](https://www.bing.com/search?q=**Command**) object.                                                                                             |
| [**CIMakeICommand**](/windows/desktop/api/Ntquery/nf-ntquery-cimakeicommand)                   | Creates a [**Command**](https://www.bing.com/search?q=**Command**) object, specifying computers, catalogs, and scopes.                                                 |
| [**CIBuildQueryNode**](/windows/desktop/api/Ntquery/nf-ntquery-cibuildquerynode)               | Builds one node of a query restriction tree for a [**Command**](https://www.bing.com/search?q=**Command**) object.                                                     |
| [**CIBuildQueryTree**](/windows/desktop/api/Ntquery/nf-ntquery-cibuildquerytree)               | Builds a query restriction tree for a [**Command**](https://www.bing.com/search?q=**Command**) object.                                                                 |
| [**CIRestrictionToFullTree**](/windows/desktop/api/Ntquery/nf-ntquery-cirestrictiontofulltree) | Converts a query restriction tree with columns, sort columns, and grouping columns to a [**DBCOMMANDTREE**](dbcommandtree.md) structure. |
| [**CITextToFullTree**](/windows/desktop/api/Ntquery/nf-ntquery-citexttofulltree)               | Creates a full command tree using Query Language 1.                                                                                       |
| [**CITextToFullTreeEx**](/windows/desktop/api/Ntquery/nf-ntquery-citexttofulltreeex)           | Creates a full command tree using the Query Language Dialect that you specify.                                                            |
| [**CITextToSelectTree**](/windows/desktop/api/Ntquery/nf-ntquery-citexttoselecttree)           | Creates a **SELECT** node for a [**DBCOMMANDTREE**](dbcommandtree.md) structure using Query Language Dialect 1.                          |
| [**CITextToSelectTreeEx**](/windows/desktop/api/Ntquery/nf-ntquery-citexttoselecttreeex)       | Creates a **SELECT** node for a [**DBCOMMANDTREE**](dbcommandtree.md) structure using the Query Language Dialect that you specify.       |



 



| For filtering files                                      | Description                                                                                                      |
|----------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| [**LoadIFilter**](/windows/desktop/api/Ntquery/nf-ntquery-loadifilter)                       | Retrieves [**IFilter**](/windows/desktop/api/Filter/nn-filter-ifilter) from path name for object.                                                  |
| [**BindIFilterFromStorage**](/windows/desktop/api/Ntquery/nf-ntquery-bindifilterfromstorage) | Given the [**IStorage**](https://www.bing.com/search?q=**IStorage**) interface pointer, retrieves the appropriate [**IFilter**](/windows/desktop/api/Filter/nn-filter-ifilter). |
| [**BindIFilterFromStream**](/windows/desktop/api/Ntquery/nf-ntquery-bindifilterfromstream)   | Given the [**IStream**](https://www.bing.com/search?q=**IStream**) interface pointer, retrieves the appropriate [**IFilter**](/windows/desktop/api/Filter/nn-filter-ifilter).   |



 

 

 




