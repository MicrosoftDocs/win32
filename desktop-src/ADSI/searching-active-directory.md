---
title: Searching Active Directory
description: An important function of Active Directory is to resolve data queries for people, as well as configuration data for computers and services.
ms.assetid: 8427d69b-0974-4adc-9732-790e5d31db7a
ms.tgt_platform: multiple
keywords:
- Searching Active Directory ADSI
- ADSI ADSI ,searching Active Directory
- queries ADSI ,searching Active Directory
ms.topic: article
ms.date: 05/31/2018
---

# Searching Active Directory

An important function of Active Directory is to resolve data queries for people, as well as configuration data for computers and services. To write efficient queries for Active Directory, it is helpful to be familiar with the following:

-   Determining the scope of the query: Must the client find properties for objects that might be located anywhere within a forest, or only within one domain, or within a given organizational unit (OU)?
-   Determining the depth of the query: Must the query only search one level or might it cross into other LDAP directories?
-   Performance and handling large result sets: How should the client effectively handle the potential of a large result set?
-   Determining the best queries: What type of queries provide the most efficient results? What type of queries should the developer avoid?
-   Understanding the query syntax: ADSI supports both the LDAP syntax as documented in RFC 2254, as well as a subset of SQL.
-   Choice of interfaces: ADSI provides both OLE DB support as well as a C/C++ interface called [**IDirectorySearch**](/windows/desktop/api/Iads/nn-iads-idirectorysearch). Because ADSI works for multiple namespaces, you can use these interfaces for querying other namespaces such as Exchange, as well as Active Directory. Because the ActiveX Data Object (ADO) is a simple scriptable data access object model on top of OLE DB, the OLE DB interfaces work well for Visual Basic programmers and webpage script writers. The new data access features within Visual Studio and Office applications that take advantage of ADO and OLE DB can now access Active Directory data in the same way that they access data from other OLE DB providers, such as SQL Server. However, if a C/C++ developer must perform a simple directory search, the **IDirectorySearch** interface might be more appropriate than the OLE DB interfaces.

The following topics describe how to search Active Directory to ensure your application issues the most efficient query, given the requirements of the client:

-   [Scope of Query](scope-of-query.md)
-   [Performance and Handling Large Result Sets](performance-and-handling-large-result-sets.md)
-   [Search Filter Syntax](search-filter-syntax.md)
-   [Query Interfaces](query-interfaces.md)
-   [Searching Binary Data](searching-binary-data.md)
-   [Distributed Query](distributed-query.md)

 

 




