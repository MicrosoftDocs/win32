---
title: FREETEXT Predicate
description: FREETEXT Predicate
ms.assetid: '14039562-4dea-44d1-9610-b23efbe7a255'
---

# FREETEXT Predicate

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **FREETEXT** predicate performs a best match of the specified words and phrases by finding rows in which the terms and phrases match the meaning, rather than the exact wording of the query. This predicate is an optional part of the optional **WHERE** clause of the **SELECT** statement.

``` syntax
SELECT Select_List | *
       FROM_Clause
       [WHERE FREETEXT([ Column_Reference,] 'Free_Text_String') 
       [ Boolean_Operator FREETEXT(</b>[<i>Column_Reference,] 'Free_Text_String') ]
        ... ]
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

Specifies the column name (alias). Its data type must be compatible with the format of the *Free\_Text\_String* parameter specified.

</dd> <dt>

<span id="Free_Text_String"></span><span id="free_text_string"></span><span id="FREE_TEXT_STRING"></span>*Free\_Text\_String*
</dt> <dd>

Specifies the literal of type Basic String from which to match the meaning.

</dd> <dt>

<span id="Boolean_Operator"></span><span id="boolean_operator"></span><span id="BOOLEAN_OPERATOR"></span>*Boolean\_Operator*
</dt> <dd>

Specifies the Boolean operator to use, following the precedence rules previously stated, that combines the **FREETEXT** predicates.

</dd> <dt>

<span id="ORDER_BY_Clause"></span><span id="order_by_clause"></span><span id="ORDER_BY_CLAUSE"></span>*ORDER\_BY\_Clause*
</dt> <dd>

Specifies the ordering of the resulting rowset. This clause is optional. For details about this parameter, see [ORDER BY Clause](order-by-clause.md).

</dd> </dl>

### Remarks

Index Server 1.*x* and 2.0 required a &gt; 0 comparison operation at the end of the **FREETEXT** predicate; for example, **FREETEXT( … ) &gt;0**. Beginning with Indexing Service 3.0, the comparison operation is neither required nor recommended, but is supported for backward compatibility.

A **FREETEXT** query ignores Boolean, proximity, and wildcard operators.

> [!Note]  
> It is not valid to place **NOT** before a **FREETEXT** predicate that begins with a **WHERE** clause.

 

### Examples

The following example returns files in which the Contents property mentions Microsoft Excel, printing worksheets, and pasting worksheets.


```
... WHERE FREETEXT('how do I print in Microsoft Excel')
      OR FREETEXT('how can I paste a worksheet into another file')
```



## Related topics

<dl> <dt>

[ARRAY Predicate](array-predicate.md)
</dt> <dt>

[Comparison Predicate](comparison-predicate.md)
</dt> <dt>

[CONTAINS Predicate](contains-predicate.md)
</dt> <dt>

[LIKE Predicate](like-predicate.md)
</dt> <dt>

[MATCHES Predicate](matches-predicate.md)
</dt> <dt>

[NULL Predicate](null-predicate.md)
</dt> <dt>

[WHERE Clause](where-clause.md)
</dt> </dl>

 

 




