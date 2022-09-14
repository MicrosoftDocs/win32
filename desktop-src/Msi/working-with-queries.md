---
description: Because the installer uses a relational database, there are functions for making Structured Query Language (SQL) queries to the database. The following procedure describes how to use SQL to query a database.
ms.assetid: 1b8fd935-4964-4875-801b-cc6765b16924
title: Working with Queries
ms.topic: article
ms.date: 05/31/2018
---

# Working with Queries

Because the installer uses a relational database, there are functions for making Structured Query Language (SQL) queries to the database. The following procedure describes how to use SQL to query a database.

**To query a database with SQL**

1.  Open the [**View**](view-object.md) object, with the appropriate SQL statement, by calling the [**MsiDatabaseOpenView**](/windows/desktop/api/Msiquery/nf-msiquery-msidatabaseopenviewa) function.

    A [**View**](view-object.md) object is the logical table created by applying a query to a set of tables. SQL queries must adhere to the [SQL syntax](sql-syntax.md) provided by the installer. This SQL statement can contain parameter markers that are not specified until the **View** object runs.

2.  Run the [**View**](view-object.md) object by calling the [**MsiViewExecute**](/windows/desktop/api/Msiquery/nf-msiquery-msiviewexecute) function.
3.  Retrieve the next record from a [**View**](view-object.md) object by calling the [**MsiViewFetch**](/windows/desktop/api/Msiquery/nf-msiquery-msiviewfetch) function.
4.  Modify the [**View**](view-object.md) object by calling the [**MsiViewModify**](/windows/desktop/api/Msiquery/nf-msiquery-msiviewmodify) function.

    You can also validate data with [**MsiViewModify**](/windows/desktop/api/Msiquery/nf-msiquery-msiviewmodify) by passing the appropriate flags. If **MsiViewModify** returns ERROR\_INVALID\_DATA from a validation request, the underlying data is corrupt.

5.  Obtain detailed error information on the [**View**](view-object.md) object by calling the [**MsiViewGetError**](/windows/desktop/api/Msiquery/nf-msiquery-msiviewgeterrora) function.
6.  Close the [**View**](view-object.md) object by calling the [**MsiViewClose**](/windows/desktop/api/Msiquery/nf-msiquery-msiviewclose) function.

For more information, see [Examples of Database Queries Using SQL and Script](examples-of-database-queries-using-sql-and-script.md).

 

 



