---
title: Creating and Executing a Query
description: Creating and Executing a Query
ms.assetid: b0206958-21ba-42eb-b631-c196a8a3da86
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Creating and Executing a Query

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The following code segments from the **IssueQuery** function of the sample create and execute a query. The function first declares an [**ICommand**](https://msdn.microsoft.com/windows/desktop/089427ad-5ba3-4613-b89e-8e86420ccc30) interface and uses the [**CIMakeICommand**](/windows/desktop/api/Ntquery/nf-ntquery-cimakeicommand) function of the [OLE DB Helper API](programming-apis.md#-idxs-ole-db-helper-api) to get a pointer to an **ICommand** interface for the specified scope, catalog, and machine properties.


```C++
...
    XInterface<ICommand> xICommand;
    HRESULT hr = CIMakeICommand( xICommand.GetPPointer(),  // result
                                 1,                        // 1 scope
                                 &amp;dwScopeFlags,            // scope flags
                                 &amp;pwcQueryScope,           // scope path
                                 &amp;pwcQueryCatalog,         // catalog
                                 &amp;pwcQueryMachine );       // machine
...
```



The function next declares an [**ICommand**](https://msdn.microsoft.com/windows/desktop/089427ad-5ba3-4613-b89e-8e86420ccc30) interface and queries the **ICommand** interface for a pointer to an [**ICommandTree**](/previous-versions/windows/desktop/api/cmdtree/nn-cmdtree-icommandtree) interface.


```C++
...
    XInterface<ICommandTree> xICommandTree;
    hr = xICommand->QueryInterface( IID_ICommandTree,
                                    xICommandTree.GetQIPointer() );
...
```



Then the function declares a **DBCOMMANDTREE** structure for the command tree of the query and uses the [**CITextToFullTreeEx**](/windows/desktop/api/Ntquery/nf-ntquery-citexttofulltreeex) function to create the command tree structure using previously set query properties.


```C++
...
    DBCOMMANDTREE * pTree;
    hr = CITextToFullTreeEx( pwcQueryRestriction, // the query itself
                             ulDialect,           // query dialect
                             pwcColumns,          // columns to return
                             pwcSort,             // sort order, may be 0
                             0,                   // reserved
                             &amp;pTree,              // resulting tree
                             0,                   // no custom properties
                             0,                   // no custom properties
                             lcid );              // default locale
...
```



The function next uses the [**SetCommandTree**](/previous-versions/windows/desktop/api/cmdtree/nf-cmdtree-icommandtree-setcommandtree) method of the [**ICommandTree**](/previous-versions/windows/desktop/api/cmdtree/nn-cmdtree-icommandtree) interface to set the command tree in the **ICommandTree** interface.


```C++
...
    hr = xICommandTree->SetCommandTree( &amp;pTree,
                                        DBCOMMANDREUSE_NONE,
                                        FALSE );
...
```



The function finally declares an [**IRowset**](https://msdn.microsoft.com/windows/desktop/b14147c4-8b03-49c6-ab5d-00186643a6b4) interface to represent the results of the query and uses it with the [**Execute**](https://msdn.microsoft.com/windows/desktop/95b4c895-a55c-4f01-a641-68a7f9a5f106) method of the [**ICommand**](https://msdn.microsoft.com/windows/desktop/089427ad-5ba3-4613-b89e-8e86420ccc30) interface to execute the query.


```C++
...
    XInterface<IRowset> xIRowset;
    hr = xICommand->Execute( 0,            // no aggregating IUnknown
                             IID_IRowset,  // IID for interface to return
                             0,            // no DBPARAMs
                             0,            // no rows affected
                             xIRowset.GetIUPointer() ); // result
...
```



 

 




