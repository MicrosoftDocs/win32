---
title: MATCHES Predicate
description: MATCHES Predicate
ms.assetid: b2e8291d-01ec-4eec-bee6-fc4d6dd48ef1
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MATCHES Predicate

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **MATCHES** predicate performs queries using regular-expression pattern matching, which is more powerful than the wildcard pattern matching available with the **LIKE** predicate. This predicate is an optional part of the optional **WHERE** clause of the **SELECT** statement.

``` syntax
SELECT Select_List | *
       FROM_Clause
       [WHERE MATCHES(Column_Reference, ' {Grouped_Search_Pattern | Counted_Search_Pattern} ') ]
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

<span id="Column_Reference"></span><span id="column_reference"></span><span id="COLUMN_REFERENCE"></span>*Column\_Reference*
</dt> <dd>

Specifies the column name (alias). Its data type must be compatible with the format of the *Search\_Pattern* parameter specified.

</dd> <dt>

<span id="Grouped_Search_Pattern"></span><span id="grouped_search_pattern"></span><span id="GROUPED_SEARCH_PATTERN"></span>*Grouped\_Search\_Pattern*
</dt> <dd>

Specifies matches against multiple patterns.

</dd> <dt>

<span id="Counted_Search_Pattern"></span><span id="counted_search_pattern"></span><span id="COUNTED_SEARCH_PATTERN"></span>*Counted\_Search\_Pattern*
</dt> <dd>

Specifies searches for repetitions of the same pattern. You can request:

-   Exactly m matches: "m"
-   At least m matches: "m,"
-   Between m and n occurrences of the search pattern: "m,n"

</dd> <dt>

<span id="ORDER_BY_Clause"></span><span id="order_by_clause"></span><span id="ORDER_BY_CLAUSE"></span>*ORDER\_BY\_Clause*
</dt> <dd>

Specifies the ordering of the resulting rowset. This clause is optional. For details about this parameter, see [ORDER BY Clause](order-by-clause.md).

</dd> </dl>

### Remarks

Index Server 1.*x* and 2.0 required a &gt; 0 comparison operation at the end of the **MATCHES** predicate, for example, **MATCHES( … ) &gt;0**. Beginning with Indexing Service 3.0, the comparison operation is neither required nor recommended, but it is supported for backward compatibility.

A grouped or counted search pattern is formed like a literal of type Basic String but consists of a combination of characters and regular expressions (match symbols). Indexing Service is not case sensitive to characters in a search pattern other than the match symbols. The following table lists and describes the regular expressions that you can use with the **MATCH** predicate:



| Name            | Symbol | Description                                                                                                                                                                   |
|-----------------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Asterisk        | \*     | Matches 0 or more occurrences of the search pattern.                                                                                                                          |
| Question mark   | ?      | Matches 0 or 1 occurrence of the preceding pattern.                                                                                                                           |
| Plus sign       | \+     | Matches 1 or more occurrences of the preceding pattern.                                                                                                                       |
| Parentheses     | ( )    | Used to delimit search patterns &gt; 1 character.                                                                                                                             |
| Curly braces    | { }    | Used to delimit a counted match.                                                                                                                                              |
| Square Brackets | \[ \]  | Used to specify a range of characters in a pattern.                                                                                                                           |
| Vertical bar    | \|     | Used as an escape character that must precede any of the above symbols. Commas separating **OR** clauses in the matching terms must also be preceded by the escape character. |



 

### Examples

The following example uses a grouped match. The pattern matches text with the strings "McAlister", and "McAllister" (strings such as "McAlllister", if they existed, would also be matched). Note how the vertical-bar escape character precedes the embedded regular-expression symbols.


```
... WHERE MATCHES (Contents, 'McAl|+ister' )
```



The following example matches any string in which exactly three instances of the pattern "Bora" occur.


```
... WHERE MATCHES (Contents, '|(Bora|)|{3|}' )
```



The following example matches any string in which at least two instances of the pattern "Bora" occurs.


```
... WHERE MATCHES (Contents, '|(Bora|)|{2,|}' )
```



The following example matches any string in which between two and three instances of the pattern "Bora" occurs.


```
... WHERE MATCHES (Contents, '|(Bora|)|{2,3|}' )
```



## Related topics

<dl> <dt>

[ARRAY Predicate](array-predicate.md)
</dt> <dt>

[Comparison Predicate](comparison-predicate.md)
</dt> <dt>

[CONTAINS Predicate](contains-predicate.md)
</dt> <dt>

[FREETEXT Predicate](freetext-predicate.md)
</dt> <dt>

[LIKE Predicate](like-predicate.md)
</dt> <dt>

[NULL Predicate](null-predicate.md)
</dt> <dt>

[WHERE Clause](where-clause.md)
</dt> </dl>

 

 




