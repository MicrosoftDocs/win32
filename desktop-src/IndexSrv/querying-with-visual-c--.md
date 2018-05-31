---
title: Querying with Visual C++
description: Querying with Visual C++
ms.assetid: 98ec7a2a-b868-42c9-93c6-26701feecccf
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Querying with Visual C++

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

With Visual C++, the [OLE DB Helper API](programming-apis.md#-idxs-ole-db-helper-api), and optionally the [OLE DB Provider API](programming-apis.md#-idxs-ole-db-provider-api), you can construct, execute, and retrieve the results of queries.

The [Simple Sample](simple-sample.md) (QSample) illustrates use of the OLE DB Helper API and the OLE DB Provider API to construct and execute a query with Indexing Service. Using the OLE DB Helper API simplifies construction of a command tree for a query. The Simple Sample uses the [CIMakeICommand](/windows/desktop/api/Ntquery/nf-ntquery-cimakeicommand), [CITextToFullTreeEx](/windows/desktop/api/Ntquery/nf-ntquery-citexttofulltreeex), [LocateCatalogs](/windows/desktop/api/Ntquery/nf-ntquery-locatecatalogsa), and [CIState](/windows/desktop/api/Ntquery/nf-ntquery-cistate) functions in addition to the [ICommandTree](icommandtree.md), [ICommand](089427ad-5ba3-4613-b89e-8e86420ccc30), [IAccessor](a39058b6-ecfa-418b-80a3-66eea4a7bf89), and [IRowset](b14147c4-8b03-49c6-ab5d-00186643a6b4) interfaces. For more complex examples that use the OLE DB Provider exclusively and that require using a data source object and a session object to construct a command tree, see the [AdvQuery Sample](advquery-sample.md).

The following topics discuss selected code segments for the Simple Sample (from the QSample.cxx file) that perform actions specific to Indexing Service. For instructions about how to install the complete code of the Simple Sample, refer to [Installing the Samples](installing-the-samples.md).

-   [Defining a Template for Managing Ownership of Interfaces](defining-a-template-for-managing-ownership-of-interfaces.md)
-   [Creating and Executing a Query](creating-and-executing-a-query.md)
-   [Getting the Query Results for Display](getting-the-query-results-for-display.md)
-   [Looking Up a Machine and Catalog for a Scope](looking-up-a-machine-and-catalog-for-a-scope.md)
-   [Displaying the Status of a Catalog](displaying-the-status-of-a-catalog.md)

 

 




