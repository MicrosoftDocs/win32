---
title: WHERE Clause
description: WHERE Clause
ms.assetid: 1eabd5e6-afa3-4c08-b602-262271cb9099
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WHERE Clause

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **WHERE** clause specifies the search condition for selecting rows in the virtual table defined by the [FROM](from-clause.md) clause. The matching rows constitute the resulting rowset. The **WHERE** clause is an optional part of the [SELECT](select-statement.md) statement. However, if the **WHERE** clause is absent, the resulting rowset can be extremely large because all rows of the virtual table defined by the **FROM** clause are returned in the resulting rowset.

``` syntax
SELECT Select_List | *
       FROM_Clause
       [WHERE Search_Conditions]
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

<span id="FROM_Clause"></span><span id="from_clause"></span><span id="FROM_CLAUSE"></span>*FROM\_Clause*
</dt> <dd>

Specifies the files on which to perform the search. For details about this parameter, see [FROM Clause](from-clause.md).

</dd> <dt>

<span id="Search_Conditions"></span><span id="search_conditions"></span><span id="SEARCH_CONDITIONS"></span>*Search\_Conditions*
</dt> <dd>

One or more predicates combined with **AND**, **OR**, and **NOT**. It specifies the conditions that rows must satisfy to belong to the resulting rowset. The rowset only includes rows in which all the predicates evaluate to **TRUE**.

</dd> <dt>

<span id="ORDER_BY_Clause"></span><span id="order_by_clause"></span><span id="ORDER_BY_CLAUSE"></span>*ORDER\_BY\_Clause*
</dt> <dd>

Specifies the ordering of the resulting rowset. This clause is optional. For details about this parameter, see [ORDER BY Clause](order-by-clause.md).

</dd> </dl>

### Remarks

The composition of search conditions has two parts: Boolean operators and predicates.

Boolean operators are **AND**, **OR**, and **NOT**. When using these operators together, precedence rules determine the order of evaluation of the conditions. When the search condition consists of statements enclosed in parentheses, expressions in parentheses are evaluated first. After the parenthetical expressions are evaluated, the following rules apply:

-   **NOT** is evaluated before **AND**. **NOT** can only occur after **AND** (as in **AND NOT**; the combination **OR NOT** is not allowed).
-   **AND** is evaluated before **OR**.
-   **AND** expressions are associative and can be applied in any order. For example, A **AND** B **AND** C, is the same as (A **AND** B) **AND** C, which is the same as A **AND** (B **AND** C).
-   **OR** expressions are associative and can be applied in any order.

> [!Note]  
> It is not valid to place **NOT** before content query predicates (**CONTAINS** and **FREETEXT**). The following statement is not valid.

 


```
SELECT FileName FROM SCOPE()
  WHERE NOT CONTAINS ('search')
```



The following statement is valid.


```
SELECT FileName FROM SCOPE()
  WHERE CONTAINS ('search') AND NOT CONTAINS ('light')
```



A predicate is an expression that makes a factual assertion about values.

-   If the expression evaluates to TRUE, the associated condition is satisfied.
-   If the expression evaluates to FALSE, the condition is not satisfied.

The following table lists the predicate types you can use with the **WHERE** clause and summarizes each.



| Predicate Type                         | Description                                                                     |
|----------------------------------------|---------------------------------------------------------------------------------|
| [ARRAY](array-predicate.md)           | Performs comparisons of two arrays using logical operators.                     |
| [Comparison](comparison-predicate.md) | Uses arithmetic operators to compare column data to a literal value.            |
| [CONTAINS](contains-predicate.md)     | Specifies certain Boolean, proximity and stemming conditions for matching text. |
| [FREETEXT](freetext-predicate.md)     | Specifies searching for the best match for the words and phrases.               |
| [LIKE](like-predicate.md)             | Performs queries using pattern matching with wildcard characters.               |
| [MATCHES](matches-predicate.md)       | Performs queries using pattern matching with regular expressions.               |
| [NULL](null-predicate.md)             | Determines whether a column in a selected row is defined.                       |



 

## Related topics

<dl> <dt>

[FROM Clause](from-clause.md)
</dt> <dt>

[ORDER BY Clause](order-by-clause.md)
</dt> <dt>

[SELECT Statement](select-statement.md)
</dt> </dl>

 

 




