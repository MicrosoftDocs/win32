---
title: SELECT Statement
description: SELECT Statement
ms.assetid: '8791d086-ddb1-47fa-894e-a8099d0e632c'
---

# SELECT Statement

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **SELECT** statement retrieves rows by specifying the columns of interest, the scope (the set of files) for the search, and the search criteria. If the results must be ordered, you can add an additional [ORDER BY clause](order-by-clause.md) to return the rows in ascending or descending order.

``` syntax
<b>SELECT</b> Select_List | *
       FROM_Clause
       [WHERE_Clause]
       [ORDER_BY_Clause]
```

### Parameters

<dl> <dt>

<span id="Select_List"></span><span id="select_list"></span><span id="SELECT_LIST"></span>*Select\_List*
</dt> <dd>

Specifies the list of column aliases (properties) making up the table (rowset) that is returned as a result of the query. A column alias can be either a well known Indexing Service friendly name or a new friendly name (regular\_identifier) as defined by a [SET PROPERTYNAME](set-propertyname.md) statement.

> [!Note]  
> Do not use "true" SQL expressions, such as: "SIZE + 500", and LENGTH(DocAuthor), in the *Select\_List* parameter. These expressions are not supported.

 

</dd> <dt>

<span id="___asterisk_"></span><span id="___ASTERISK_"></span>*\** (asterisk)
</dt> <dd>

Specifies all columns. This option is valid only when the *FROM\_Clause* parameter references a predefined view or a temporary view.

</dd> <dt>

<span id="FROM_Clause"></span><span id="from_clause"></span><span id="FROM_CLAUSE"></span>*FROM\_Clause*
</dt> <dd>

Specifies the files on which to perform the search. For details about this parameter, see [FROM Clause](from-clause.md).

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

If the *Select\_List* parameter specifies a column more than once, only one instance of that column appears in the result set.

SQL-92 specifies both the ALL and DISTINCT set quantifiers. Because Indexing Service retrieves all rows including duplicate rows, the ALL set quantifier is assumed and does not have to be specified. DISTINCT is not supported.

### Examples

The following query returns the author, size, title, and the last time the file was modified for all files in the physical root directory that contain the phrase "Indexing Service".


```
SELECT DocAuthor, size, DocTitle, write
  FROM SCOPE()
  WHERE CONTAINS(Contents, '"Indexing Service"')
```



Suppose \#MyDocView has been defined with a [CREATE VIEW statement](create-view-statement.md) containing the properties DocAuthor, FileName, size, and access. Use of an asterisk selects all the properties in that view. The following statement returns DocAuthor, FileName, size, and access values for all rows where the file size is greater than 100000.


```
SELECT * FROM #MyDocView
  WHERE size > 100000
```



## Related topics

<dl> <dt>

[CREATE VIEW Statement](create-view-statement.md)
</dt> <dt>

[FROM Clause](from-clause.md)
</dt> <dt>

[ORDER BY Clause](order-by-clause.md)
</dt> <dt>

[WHERE Clause](where-clause.md)
</dt> </dl>

 

 




