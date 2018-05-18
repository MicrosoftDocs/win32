---
title: SGML-Style Syntax
description: SGML-Style Syntax
ms.assetid: '46bb0535-5835-4779-b9c1-66eba5860407'
---

# SGML-Style Syntax

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Dialect 2 introduces an SGML-style syntax that employs tags to interpret query terms and modify query operators. The query tags, indicated by braces (the "{" and "}" symbols), are used to open and close query expressions. In many cases, a query expression can have an implied closing tag. The query tags can also include attributes to define additional variations of the tag. This permits easy construction of complex queries.

The general syntax of a query tag is the following.

**{query-tag attribute1=***value1***, attribute2=***value2***, ...}** *query expression* **{/query-tag}**

The syntax is similar to that of SGML, except that Dialect 2 uses braces instead of angle brackets (the latter are the "&lt;" and "&gt;" symbols) to delineate tags. This prevents confusion of tags with the relational operators "less than" and "greater than".

 

 




