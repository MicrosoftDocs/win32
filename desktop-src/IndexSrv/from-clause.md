---
title: FROM Clause
description: FROM Clause
ms.assetid: '758a5f63-c4ee-4524-92d8-3b135a365540'
---

# FROM Clause

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **FROM** clause defines the query scope by specifying the files on which to perform the search. The **FROM** clause is a required part of the **SELECT** statement.

``` syntax
SELECT Select_List | *
       FROM {[Server_Name.][Catalog_Name..]Predefined_View_Name |
             [Server_Name.][Catalog_Name..]View_Name |
             [Server_Name.][Catalog_Name..]SCOPE('Scope_Arguments']) |
             (TABLE [Server_Name.][Catalog_Name..]SCOPE(['Scope_Arguments'])
             UNION ALL TABLE [Server_Name.][Catalog_Name..]SCOPE(['Scope_Arguments'])
             [UNION ALL TABLE [Server_Name.][Catalog_Name..]SCOPE(['Scope_Arguments']) 
             ...])}
       [WHERE_Clause]
       [ORDER_BY_Clause]
```

### Parameters

<dl> <dt>

<span id="Select_List"></span><span id="select_list"></span><span id="SELECT_LIST"></span>*Select\_List*
</dt> <dd>

Specifies the list of column aliases (properties) making up the table (rowset) that is returned as a result of the query.

</dd> <dt>

<span id="___asterisk_"></span><span id="___ASTERISK_"></span>*\** (asterisk)
</dt> <dd>

Specifies all columns. This option is valid only when the *FROM\_Clause* parameter references a predefined view or a temporary view.

</dd> <dt>

<span id="Server_Name"></span><span id="server_name"></span><span id="SERVER_NAME"></span>*Server\_Name*
</dt> <dd>

Specifies the name of the server on which the query will be run. A *Server\_Name* parameter can't be specified for a query that uses a temporary view because a temporary view is specified only for the current catalog. A *Server\_Name* parameter can be specified for a query that uses a predefined view.

</dd> <dt>

<span id="Catalog_Name"></span><span id="catalog_name"></span><span id="CATALOG_NAME"></span>*Catalog\_Name*
</dt> <dd>

Specifies the catalog to use. A catalog is the highest-level unit of organization in Indexing Service. Each catalog is a completely self-contained unit containing an index and cached properties for one or more scopes (virtual or physical directories). If a query does not specify the *Catalog\_Name* parameter, the default catalog "system" is used.

</dd> <dt>

<span id="Scope_Arguments"></span><span id="scope_arguments"></span><span id="SCOPE_ARGUMENTS"></span>*Scope\_Arguments*
</dt> <dd>

The **SCOPE** function, which is the main component of the **FROM** clause, can take zero or more comma-separated *Scope\_Arguments* parameters.

If *Scope\_Arguments* is an empty list (for example, **FROM SCOPE()**), this specifies that the physical root is to be used as the default path.

If not empty, *Scope\_Arguments* specifies the paths or virtual roots to be searched and how they will be traversed. Each *Scope\_Argument* must be enclosed in single quotes. The syntax of each *Scope\_Argument* is:


```
'[<i>Traversal_Type</i>] ("<i>Path</i>"[, "<i>Path</i>", ...])'
```



*Traversal\_Type* can be either of these options:

<dl> <dt>

<span id="DEEP_TRAVERSAL_OF"></span><span id="deep_traversal_of"></span>**DEEP TRAVERSAL OF**
</dt> <dd>

Searches the paths specified plus all directories beneath them.

</dd> <dt>

<span id="SHALLOW_TRAVERSAL_OF"></span><span id="shallow_traversal_of"></span>**SHALLOW TRAVERSAL OF**
</dt> <dd>

Searches the specified paths only.

You can group a set of directories or virtual roots for deep or shallow traversal. See the following Examples section.

If you do not specify *Traversal\_Type*, the default option is **DEEP TRAVERSAL OF**.

*Path* can be specified either as physical directories, such as "d:\\reports\\year\\97", or as virtual roots, like "/annual/corporate". A scope definition can include multiple physical paths and multiple virtual roots. Enclose each *Path* parameter with double quotes (to accommodate spaces in paths). If you specify more than one path, they must be separated by commas.

</dd> </dl> </dd> <dt>

<span id="Predefined_View_Name"></span><span id="predefined_view_name"></span><span id="PREDEFINED_VIEW_NAME"></span>*Predefined\_View\_Name*
</dt> <dd>

Specifies one of a set of [Indexing Service predefined views](indexing-service-predefined-views.md) or [Site Server predefined views](site-server-predefined-views.md) of often-queried properties.

</dd> <dt>

<span id="View_Name"></span><span id="view_name"></span><span id="VIEW_NAME"></span>*View\_Name*
</dt> <dd>

Specifies a nonpersistent view defined with the **CREATE VIEW** statement.

Although the **SCOPE** function restricts the lifetime of the virtual-table definition to the current query, you can use a **CREATE VIEW** statement to define combinations of properties and scope for use in subsequent queries. For more information, see the [CREATE VIEW Statement](create-view-statement.md).

</dd> <dt>

<span id="WHERE_Clause"></span><span id="where_clause"></span><span id="WHERE_CLAUSE"></span>*WHERE\_Clause*
</dt> <dd>

Specifies the search condition for selecting rows in the virtual table defined by the *FROM\_Clause* parameter. The matching rows make up the resulting rowset. This clause is optional. For details about this parameter, see [WHERE Clause](where-clause.md).

</dd> <dt>

<span id="ORDER_BY_Clause"></span><span id="order_by_clause"></span><span id="ORDER_BY_CLAUSE"></span>*ORDER\_BY\_Clause*
</dt> <dd>

Specifies the ordering of the resulting rowset. This clause is optional. For details about this parameter, see [ORDER BY Clause](order-by-clause.md).

</dd> </dl>

### Remarks

When using one or more periods (.) to separate the *Server\_Name*, *Catalog\_Name*, **SCOPE()**, *Predefined\_View\_Name*, and *View\_Name* parameters, do not include any spaces.

If some, but not all, of the paths you specify do not exist, these invalid paths are ignored and the query is made using only the valid paths. If all the paths you specify are invalid, then the result set is always empty.

### Examples

The following example defines a deep traversal search (default scope). It searches for the word smith in the DocAuthor property for all files, starting from the physical root directories in the catalog.


```
SELECT DocAuthor, DocTitle
  FROM SCOPE()
  WHERE CONTAINS(DocAuthor, 'smith')
```



The following example defines a shallow traversal of \\Contracts\\open on drive D (the top directory only) and all the subdirectories at /reports/year 97 from a specific catalog called Contracts.


```
SELECT DocAuthor, size,  DocTitle,  write
  FROM Contracts..SCOPE(' SHALLOW TRAVERSAL OF "D:\Contracts\open" ',
             ' DEEP TRAVERSAL OF "/Reports/Year 97" ')
  WHERE CONTAINS(DocTitle, '"Contract Expenses"')
```



Because **DEEP TRAVERSAL OF** is the default traversal selection, its inclusion is optional. You may want to use it to increase readability of the statement. Notice that single quoted strings are used to associate traversal type to a specific path or set of paths.

The following example statements are equivalent, but the **FROM** clause in the latter is more verbose than in the former. In the second example, extra parentheses are added around the paths to enhance readability. Also, the examples demonstrate the syntax for querying a remote server.


```
SELECT DocAuthor, size,  DocTitle,  write
  FROM SpecServer.Specs..SCOPE(' "D:\Word97\specs", "E:\DAPI\specs"  ' )
  WHERE CONTAINS(Contents, '"content search"')
SELECT DocAuthor, size,  DocTitle,  write
  FROM SpecServer.Specs..SCOPE(' DEEP TRAVERSAL OF ( "D:\Word97\specs",    "E:\DAPI\specs" ) ')
  WHERE CONTAINS(Contents, '"content search"')
```



The following example demonstrates a query against multiple catalogs. It returns results for matches that contain the phrase "content search" from the Specs catalog and the default catalog.


```
SELECT DocAuthor, size,  DocTitle,  write
  FROM (TABLE Specs..SCOPE()
        UNION ALL TABLE SCOPE())
  WHERE CONTAINS(Contents, '"content search"')
```



The following example specifies a *Server\_Name* but not a *Catalog\_Name*, which defaults to "System".


```
SELECT DocAuthor, FileName
  FROM MyServer...SCOPE()
```



The preceding example is therefore equivalent to the following example.


```
SELECT DocAuthor, FileName
  FROM MyServer.System..SCOPE()
```



If the *Server\_Name* or *Catalog\_Name* parameter contains any non-alphanumeric characters, the name must be double-quoted as in the following example.


```
SELECT DocAuthor, FileName
  FROM "My-Server".System..SCOPE()
```



## Related topics

<dl> <dt>

[ORDER BY Clause](order-by-clause.md)
</dt> <dt>

[SELECT Statement](select-statement.md)
</dt> <dt>

[WHERE Clause](where-clause.md)
</dt> </dl>

 

 




