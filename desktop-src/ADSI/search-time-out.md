---
title: Search Time Out
description: A client can also impose a time limit that it will wait for a server to return the result set.
ms.assetid: a31bc8b2-9adf-4dff-a6df-67d6bf304e04
ms.tgt_platform: multiple
keywords:
- Search Time Out ADSI
ms.topic: article
ms.date: 05/31/2018
---

# Search Time Out

A client can also impose a time limit that it will wait for a server to return the result set. The value of the "search time out" option specifies this limit. When the server fails to respond to a query within the specified time period, the client can stop the search and try again later.

The time-out property is useful when a client requests an asynchronous search. In an asynchronous search, the client makes a request and then proceeds with other tasks while waiting for the server to return the results. It is possible that the server can go offline without notifying the client. In this case, the client has no way of recognizing that the server is still processing the query, or if it has ceased to be live. The time-out property provides the client some control in such instances.

For more information about using the search time-out option with a specific search interface, see:

-   [Client Time Limit with IDirectorySearch](client-time-limit-with-idirectorysearch.md)
-   [Searching with ActiveX Data Objects](searching-with-activex-data-objects-ado.md)
-   [Searching with OLE DB](searching-with-ole-db.md)

 

 




