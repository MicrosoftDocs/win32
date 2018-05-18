---
title: Functions
description: Functions
ms.assetid: 'faec3725-4cc2-4a0c-98a3-68b2774ad99b'
---

# Functions

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Indexing Service provides functions for finding and managing catalogs, determining the catalog file's path, for creating Microsoft OLE DB [**Command**](mdobjcommand) objects to query catalogs using [Query Languages for Indexing Service](query-languages-for-indexing-service.md), and for filtering files.

The following tables list the functions in each category.



| For finding and managing catalogs          | Description                                          |
|--------------------------------------------|------------------------------------------------------|
| [**CIState**](cistate.md)                 | Queries the state of the selected catalog.           |
| [**LocateCatalogs**](locatecatalogs.md)   | Finds the catalog that indexes a directory.          |
| [**SetCatalogState**](setcatalogstate.md) | Sets the catalog state for backup or other purposes. |



 



| For creating queries using OLE DB command objects          | Description                                                                                                                               |
|------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| [**CICreateCommand**](cicreatecommand.md)                 | Creates a [**Command**](mdobjcommand) object.                                                                                             |
| [**CIMakeICommand**](cimakeicommand.md)                   | Creates a [**Command**](mdobjcommand) object, specifying computers, catalogs, and scopes.                                                 |
| [**CIBuildQueryNode**](cibuildquerynode.md)               | Builds one node of a query restriction tree for a [**Command**](mdobjcommand) object.                                                     |
| [**CIBuildQueryTree**](cibuildquerytree.md)               | Builds a query restriction tree for a [**Command**](mdobjcommand) object.                                                                 |
| [**CIRestrictionToFullTree**](cirestrictiontofulltree.md) | Converts a query restriction tree with columns, sort columns, and grouping columns to a [**DBCOMMANDTREE**](dbcommandtree.md) structure. |
| [**CITextToFullTree**](citexttofulltree.md)               | Creates a full command tree using Query Language 1.                                                                                       |
| [**CITextToFullTreeEx**](citexttofulltreeex.md)           | Creates a full command tree using the Query Language Dialect that you specify.                                                            |
| [**CITextToSelectTree**](citexttoselecttree.md)           | Creates a **SELECT** node for a [**DBCOMMANDTREE**](dbcommandtree.md) structure using Query Language Dialect 1.                          |
| [**CITextToSelectTreeEx**](citexttoselecttreeex.md)       | Creates a **SELECT** node for a [**DBCOMMANDTREE**](dbcommandtree.md) structure using the Query Language Dialect that you specify.       |



 



| For filtering files                                      | Description                                                                                                      |
|----------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| [**LoadIFilter**](loadifilter.md)                       | Retrieves [**IFilter**](ifilter.md) from path name for object.                                                  |
| [**BindIFilterFromStorage**](bindifilterfromstorage.md) | Given the [**IStorage**](_stg_istorage) interface pointer, retrieves the appropriate [**IFilter**](ifilter.md). |
| [**BindIFilterFromStream**](bindifilterfromstream.md)   | Given the [**IStream**](_stg_istream) interface pointer, retrieves the appropriate [**IFilter**](ifilter.md).   |



 

 

 




