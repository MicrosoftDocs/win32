---
Description: ORDER BY Clause
ms.assetid: 38ef9876-6af9-448c-bdcf-cfa09965e636
title: ORDER BY Clause
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ORDER BY Clause

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **ORDER BY** clause sorts the rows returned in the rowset according to a specified set of criteria. The **ORDER BY** clause is an optional part of the [SELECT statement](select-statement.md).

``` syntax
SELECT Select_List | *
       FROM_Clause
       [WHERE_Clause]
       [ORDER BY Sort_Column [ASC | DESC]
               [,Sort_Column [ASC | DESC]]
                 ... ]
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

<span id="FROM_Clause"></span><span id="from_clause"></span><span id="FROM_CLAUSE"></span>*FROM\_Clause*
</dt> <dd>

Specifies the files on which to perform the search. For details about this parameter, see [FROM Clause](from-clause.md).

</dd> <dt>

<span id="WHERE_Clause"></span><span id="where_clause"></span><span id="WHERE_CLAUSE"></span>*WHERE\_Clause*
</dt> <dd>

Specifies the search condition for selecting rows in the virtual table defined by the *FROM\_Clause* parameter. The matching rows make up the resulting rowset. This clause is optional. For details about this parameter, see [WHERE Clause](where-clause.md).

</dd> <dt>

<span id="Sort_Column"></span><span id="sort_column"></span><span id="SORT_COLUMN"></span>*Sort\_Column*
</dt> <dd>

Specifies the name of the column to be sorted or the ordinal position of the column.

</dd> <dt>

<span id="ASC___DESC"></span><span id="asc___desc"></span>**ASC \| DESC**
</dt> <dd>

Specifies the sorting order, either ascending (**ASC**) or descending (**DESC**). If you do not specify the sort order, the columns are sorted in ascending order. However, if a column is explicitly marked ascending or descending, succeeding columns will use that same sort order until another column in the list is explicitly marked in the other order.

</dd> </dl>

### Examples

Notice the order in the columns in the following example:

-   Col1 is ascending (by default).
-   Col2 is descending (explicitly stated).
-   Col3 and Col4 is descending (implicit, same as last keyword).
-   Col5 is ascending (explicitly stated).


```
SELECT Col1, Col2, Col3, Col4, Col5
  FROM SCOPE()
  WHERE Col1 > 10
  ORDER BY Col1, Col2 DESC, Col3, Col4, Col5 ASC
```



The following example is equivalent to the previous example, but it refers to the columns by their ordinal position.


```
SELECT Col1, Col2, Col3, Col4, Col5
  FROM SCOPE()
  WHERE Col1 > 10
  ORDER BY 1, 2 DESC, 3, 4, 5 ASC
```



## Related topics

<dl> <dt>

[FROM Clause](from-clause.md)
</dt> <dt>

[SELECT Statement](select-statement.md)
</dt> <dt>

[WHERE Clause](where-clause.md)
</dt> </dl>

 

 



