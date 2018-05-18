---
title: CREATE VIEW Statement
description: CREATE VIEW Statement
ms.assetid: 'af55851e-576a-498c-9f49-06b954cd862d'
---

# CREATE VIEW Statement

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **CREATE VIEW** statement defines and stores (for the duration of a session with Indexing Service) a set of frequently used properties. The name associated with this set of properties can be used with subsequent [SELECT](select-statement.md) statements.

``` syntax
CREATE VIEW #View_Name
  AS SELECT Select_List
            FROM_Clause
```

### Parameters

<dl> <dt>

<span id="View_Name"></span><span id="view_name"></span><span id="VIEW_NAME"></span>*View\_Name*
</dt> <dd>

Specifies the name for the view. The view name must be preceded by a number sign (\#) to indicate that it is a temporary definition.

</dd> <dt>

<span id="Select_List"></span><span id="select_list"></span><span id="SELECT_LIST"></span>*Select\_List*
</dt> <dd>

Specifies the list of column aliases (properties) making up the table (rowset) that is returned as a result of the query.

</dd> <dt>

<span id="FROM_Clause"></span><span id="from_clause"></span><span id="FROM_CLAUSE"></span>*FROM\_Clause*
</dt> <dd>

Specifies the files on which to perform the search. For details about this parameter, see [FROM Clause](from-clause.md).

</dd> </dl>

### Remarks

You can create a temporary view or use one of several predefined views supplied with the SQL extensions. Predefined views include the following.

-   [Indexing Service Predefined Views](indexing-service-predefined-views.md)
-   [Site Server Predefined Views](site-server-predefined-views.md)

Creating a view allows you to use **SELECT \*** queries, which normally cannot be performed in Indexing Service. Without a view, you would have to specify the full list of columns each time you want to run such a query.

> [!Note]  
> It is possible to issue a [SELECT statement](select-statement.md) against a view where the *Select\_List* is a subset of the columns in the view definition.

 

After you have associated a name with a view definition by means of the **CREATE VIEW** statement, you cannot associate it with another view definition. For example, if you execute the following two **CREATE VIEW** statements in succession, the second **CREATE VIEW** statement is an attempt to redefine the view, and it will fail.


```
CREATE VIEW #MyView1 AS SELECT DocAuthor FROM SCOPE()
CREATE VIEW #MyView1 AS SELECT FileName FROM SCOPE()
```



The view name, along with its view definition, is implicitly associated with the catalog active at the time you define the view. If you switch catalogs, that view will not be found and you must redefine it. Consider the following pseudocode flow.

&lt;default catalog is cat1&gt;


```
CREATE VIEW #MyView1 AS SELECT DocAuthor, size FROM SCOPE()
```



&lt;set current catalog to cat2&gt;


```
SELECT * FROM #MyView1
```



The preceding **SELECT** statement will result in an error since \#MyView1 has not been defined for cat2.

&lt;set current catalog back to cat1&gt;


```
SELECT * FROM #MyView1
```



The preceding **SELECT** statement will return hits if there are files within the specified scope.

Because there is no support for a **DROP VIEW** statement, once a view is created, it persists for the duration of the Indexing Service session.

### Examples

Suppose you often query using the following properties and scope:

-   DocAuthor, FileName, size, and last file access date.
-   Query a scope of /specs/database/integration (deep traversal) and /current/specs (shallow traversal).

The following **CREATE VIEW** statement stores that information in a view and eliminates the need to reenter it for **SELECT \*** queries.


```
CREATE VIEW #MySpecView  AS SELECT DocAuthor, FileName, size, access  FROM SCOPE(' DEEP TRAVERSAL OF "/specs/database/integration" ',  SHALLOW TRAVERSAL OF "/current/specs" ')
```



As a result, all future queries can be expressed in a simpler manner. For example, you can issue the following queries:


```
SELECT * FROM #MySpecView
  WHERE size > 100000
SELECT * FROM #MySpecView
  WHERE CONTAINS (' "index search" ')
SELECT FileName, size FROM #MySpecView
  WHERE FREETEXT ('how do I search with Indexing Service')
  AND FileName LIKE 'm%.doc'
```



## Related topics

<dl> <dt>

[Batched Statements](batched-statements.md)
</dt> <dt>

[Indexing Service Predefined Views](indexing-service-predefined-views.md)
</dt> <dt>

[Site Server Predefined Views](site-server-predefined-views.md)
</dt> </dl>

 

 




