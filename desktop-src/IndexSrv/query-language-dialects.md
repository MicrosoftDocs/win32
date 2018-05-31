---
title: Query-Language Dialects
description: Query-Language Dialects
ms.assetid: 2cf61134-2096-4de4-b231-d23502293889
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Query-Language Dialects

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Indexing Service accepts queries composed in a language designed especially for Indexing Service. This language has two dialects: Query Dialect 1 is the language used in Index Server 2.0 and earlier versions, and Query Dialect 2 is the language introduced in Indexing Service 3.0. Usually, Dialect 2 is the preferred dialect to use because it is more expressive, flexible, and extensible. The short form of Dialect 2 is compatible with Dialect 1 with a few exceptions. Usually a query submitted as Dialect 2 can employ Dialect 1 syntax.

Microsoft Visual Basic and Microsoft Visual J++ applications and Microsoft Visual Basic Scripting Edition (VBScript) and Microsoft JScript scripts can submit queries in these dialects using the [Query Helper](programming-apis.md#-idxs-query-helper-api) functions. Microsoft Visual C++ applications can submit queries in these dialects using the [OLE DB Helper](programming-apis.md#-idxs-ole-db-helper-api) functions. IDQ+HTX scripts can submit queries in these dialects using the [ISAPI Extensions](programming-apis.md#-idxs-isapi-extensions-api).

This section describes the syntax of the query-language dialects. The topics include:

-   [Description of the EBNF Notation](description-of-the-ebnf-notation.md)
-   [Syntax of Query Language Dialect 1](syntax-of-query-language-dialect-1.md)
-   [Syntax of Query Language Dialect 2](syntax-of-query-language-dialect-2.md)

For details about semantics and use of the query language dialects, see [Indexing Service Query Language](indexing-service-query-language.md). For a description of incompatibilities between the two dialects, see [Incompatibilities of Dialect 2 with Dialect 1](incompatibilities-of-dialect-2-with-dialect-1.md).

 

 




