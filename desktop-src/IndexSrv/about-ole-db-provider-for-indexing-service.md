---
title: About OLE DB Provider for Indexing Service
description: About OLE DB Provider for Indexing Service
ms.assetid: '5ea90c4e-0d8b-4e99-ac30-8997bcb66c3c'
---

# About OLE DB Provider for Indexing Service

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

OLE DB is a set of Microsoft ActiveX interfaces that abstract how an application retrieves data from data sources and how it presents such information in table form to clients. In OLE DB, a component can be a data *consumer* (retrieving data from a data source) or a data *provider* (supplying data to a data consumer). The same component can take on both roles at different times in its process.

In order to manage the roles of data consumer and data provider, OLE DB provides an object model that includes data source objects (DSOs) and session objects. The [data source object constant](data-source-object-constant.md) (CLSID\_INDEX\_SERVER\_DSO) identifies Indexing Service as a data source object. Once connected to this specific DSO, a client can create a session object that, in turn, can create command objects to execute queries against the data source and rowset objects to hold the results of a query. In addition, accessors map the text in a command to the columns in the retrieved rowset object for retrieving query results.

This section gives an overview of the OLE DB Provider for Indexing Service. It includes the following topics:

-   [OLE DB Objects Used by Indexing Service](ole-db-objects-used-by-indexing-service.md)
-   [Command Representation of Queries](command-representation-of-queries.md)
-   [Command Trees](command-trees.md)
-   [Command Properties](command-properties.md)
-   [Memory Allocation](memory-allocation.md)

For more information about OLE DB objects, see the [OLE DB Programmer's Reference](3c5e2dd5-35e5-4a93-ac3a-3818bb43bbf8) in the Platform Software Development Kit (SDK). For an example of how to connect the Indexing Service data source provider, see [Using OLE DB Provider for Indexing Service](using-ole-db-provider-for-indexing-service.md). For sample applications that show how to use these objects, see the [Querying Samples](querying-samples.md) in the samples directory of the Platform SDK.

 

 




