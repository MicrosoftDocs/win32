---
Description: DBPROP\_MACHINE
ms.assetid: 05d0bf4f-2947-4384-8c5e-c176c7c6ed80
title: DBPROP\_MACHINE
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DBPROP\_MACHINE

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The DBPROP\_MACHINE property specifies the names of the computer(s) on which a query is to be processed.

### Summary



|                  |                               |
|------------------|-------------------------------|
| **Property Set** | DBPROPSET\_CIFRMWRKCORE\_EXT  |
| **Property ID**  | DBPROP\_MACHINE               |
| **Value Type**   | DBTYPE\_ARRAY \| DBTYPE\_BSTR |
| **Default**      | "." (the local machine)       |



 

### Remarks

If more than one catalog or machine is specified, the DBPROP\_MACHINE, [**DBPROP\_CI\_CATALOG\_NAME**](dbprop-ci-catalog-name.md), [**DBPROP\_CI\_INCLUDE\_SCOPES**](dbprop-ci-include-scopes.md), and [**DBPROP\_CI\_SCOPE\_FLAGS**](dbprop-ci-scope-flags.md) properties must all have the same number of entries, or the count of scopes and flags can be either the count of catalogs and machines or 1.

When more than one machine or catalog is specified, the query is executed on multiple machines and the results are merged on the local machine.

Do not include preceding slashes with machine names. A correct example would be "MyMachine", not "\\\\MyMachine".

The machine name "." refers to the local machine. If the name of the local machine is specified, the query is treated as a remote query.

 

 



