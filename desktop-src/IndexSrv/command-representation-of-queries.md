---
title: Command Representation of Queries
description: Command Representation of Queries
ms.assetid: 'af5335ce-d8d7-45e2-b663-703632e401c7'
---

# Command Representation of Queries

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

OLE DB uses a tree format to represent commands associated with the [**Command object**](c72d0308-7e30-4250-b85e-557b8c399a3c). For Indexing Service, the command represents a query. A typical query involves the following steps, where the terms in brackets suggest actions familiar to database users:

-   Step 1 \[PROJECT\]: Choose the columns you want to display in the search results table and copy the appropriate values from the files that had hits.
-   Step 2 \[SELECT\]: Define a search on the content and property indexes for some values you specify. The query languages supported allow you to express property-value queries as [*relational queries*](relational-queries.md) or [*pattern-matching queries*](pattern-matching-queries.md) in addition to expressing [*content queries*](content-queries.md). For each part of the search expression, indicate the values that should be searched for in specific properties (including the contents property) for a file. Execute the query.
-   Step 3 \[SORT\]: Sort the results by one or more columns in the specified order.

When creating a machine-readable command structure to represent these steps, Indexing Service uses a [**DBCOMMANDTREE**](dbcommandtree.md) structure, which is an array of zero or more nodes, each describing a part of one of the steps. Nodes include an operation field, a data type identifier field, a data field, and links to other nodes that are children or siblings of this node.

[**DBCOMMANDTREE**](dbcommandtree.md) structures that represent queries as described in Step 2 are known as *select trees*. **DBCOMMANDTREE** structures that represent all three steps are known as *full trees*.

A full tree contains nodes that represent all three steps but in reverse order. Trees are processed upward from the base with final operations occurring at the top. A typical query tree contains a **SELECT** node that creates a results table, a **PROJECT** node that copies values from the results table to the results display table, and a **SORT** node that specifies how the results-display table gets sorted before being available for display.

An example of a full tree is shown in [Example of Command Tree](example-of-command-tree.md).

 

 




