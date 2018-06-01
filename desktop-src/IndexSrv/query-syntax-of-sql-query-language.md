---
Description: Query Syntax of SQL Query Language
ms.assetid: 76f54565-4f05-4ba8-9179-944ba195a506
title: Query Syntax of SQL Query Language
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Query Syntax of SQL Query Language

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

A typical sequence of statements in the SQL query language consists of the following.

``` syntax
SET Property_Name_Clause | Rank_Method_Clause
...
CREATE VIEW #View_Name
  AS SELECT Select_List
            FROM_Clause
...
SELECT Select_List | *
       FROM_Clause
       [ WHERE_Clause ]
       [ ORDER_BY_Clause ]
```

SQL statements can be submitted individually, or batched together. The following table lists the component statements and clauses in their usual order of use and briefly summarizes each.



| Statement or Clause                                | Description                                                                                                                                              |
|----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| [SET statement](set-statement.md)                 | Maps document-specific properties to column names or selects a ranking method for content searches.                                                      |
| [CREATE VIEW statement](create-view-statement.md) | Associates a subset of properties with a user-defined virtual table name that can then be used to satisfy queries. Several predefined views can be used. |
| [SELECT statement](select-statement.md)           | Retrieves rows by specifying the columns of interest, the scope (the set of documents) for the search, and the search criteria.                          |
| [FROM clause](from-clause.md)                     | Part of the [SELECT](select-statement.md) statement that defines the query scope by specifying the documents on which to perform the search.            |
| [WHERE clause](where-clause.md)                   | Optional part of the [SELECT](select-statement.md) statement that specifies the rows in the virtual table that make up the resulting rowset.            |
| [ORDER BY clause](order-by-clause.md)             | Optional part of the [SELECT](select-statement.md) statement that sorts the rows returned in the rowset according to a specified set of criteria.       |
| [Batched statements](batched-statements.md)       | Allow setting and executing several SQL statements, optionally separated by semicolons, as one command.                                                  |



 

 

 



