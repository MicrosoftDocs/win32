---
title: Query Languages for Indexing Service
description: Query Languages for Indexing Service
ms.assetid: 'cccc0ddf-0100-4742-833a-ca24c8052872'
---

# Query Languages for Indexing Service

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Indexing Service supports two types of query languages: the Indexing Service query language and the Structured Query Language (SQL) query language. An application or script that uses the appropriate application programming interface (API) can use either type of query language to submit the queries to Indexing Service. (The choice of API depends on several factors; see [Programming APIs](programming-apis.md) for a brief discussion.) The following table summarizes the correspondence between query languages and the APIs that support them.



| Query Language                                                                    | Supporting APIs                                                                                                                                                                                                                  |
|-----------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Indexing Service Query Language](indexing-service-query-language.md)<br/> | [ISAPI Extensions](programming-apis.md#-idxs-isapi-extensions-api),<br/> [OLE DB Helper](programming-apis.md#-idxs-ole-db-helper-api),<br/> [Query Helper](programming-apis.md#-idxs-query-helper-api)<br/> |
| [SQL Query Language](sql-query-language.md)<br/>                           | [ActiveX Data Objects](programming-apis.md#-idxs-activex-data-objects-api),<br/> [OLE DB Provider](programming-apis.md#-idxs-ole-db-provider-api)<br/>                                                             |



 

This section describes the Indexing Service query language and its dialects. It also describes the SQL language and its extensions. The topics include the following.

-   [Indexing Service Query Language](indexing-service-query-language.md) is a special language created for Indexing Service, first as Dialect 1 for Index Server 1.0, and now as Dialect 2, an extensible query language introduced with Indexing Service 3.0.
-   [SQL Query Language](sql-query-language.md) is standard SQL with several extensions. It has been available for submitting queries from applications and scripts since Index Server 2.0.
-   [Example Queries](example-queries.md) presents a few examples of queries that compare the two Indexing Service query language dialects and the SQL language.

For a reference to the syntaxes of Dialects 1 and 2 and the SQL language, see [Query Language Syntax](query-language-syntax.md).

[Secure Code Practices](secure-code-practices.md)

 

 





