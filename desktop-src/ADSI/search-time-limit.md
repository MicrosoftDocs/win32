---
title: Search Time Limit
description: When you request a search on a server that is under a heavy workload, you may want to instruct the server to restrict the search to a specified time limit.
ms.assetid: 199ac73b-3624-4cd5-a1ee-6db418cd77ba
ms.tgt_platform: multiple
keywords:
- Search Time Limit ADSI
ms.topic: article
ms.date: 05/31/2018
---

# Search Time Limit

When you request a search on a server that is under a heavy workload, you may want to instruct the server to restrict the search to a specified time limit. For example, to execute an application to generate a weekly report on a server that is running near capacity, and to avoid maximizing the CPU time and preventing other jobs from running, you can set the search time to a small value and rerun the application later if it fails to generate the report.

Some servers can impose their own administrative time limit. In these cases, if you specify a search time limit value greater than the administrative time limit, the server ignores your specification and use its internal administrative time limit instead.

For more information about using the search time limit option with a specific search interface, see:

-   [Server Time Limit with IDirectorySearch](server-time-limit-with-idirectorysearch.md)
-   [Searching with ActiveX Data Objects](searching-with-activex-data-objects-ado.md)
-   [Searching with OLE DB](searching-with-ole-db.md)

 

 




