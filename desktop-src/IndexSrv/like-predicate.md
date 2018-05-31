---
title: LIKE Predicate
description: LIKE Predicate
ms.assetid: 38e0dfda-92aa-4797-bfbe-0aebd6e109cc
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# LIKE Predicate

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **LIKE** predicate performs queries using wildcard-character pattern matching. This predicate is an optional part of the optional **WHERE** clause of the **SELECT** statement.

``` syntax
SELECT Select_List | *
       FROM_Clause
       [WHERE Column_Reference [NOT] LIKE 'String_Pattern']
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

Specifies the column name (alias). Its data type must be compatible with the format of the *String\_Pattern* parameter specified.

</dd> <dt>

<span id="String_Pattern"></span><span id="string_pattern"></span><span id="STRING_PATTERN"></span>*String\_Pattern*
</dt> <dd>

Specifies the literal of type Basic String to use as the pattern. You can use any combination of string literals along with the valid wildcard characters shown in the following table.



| Wildcard Character | Symbol | Description                                                                     |
|--------------------|--------|---------------------------------------------------------------------------------|
| Percent            | %      | Matches 0 or more characters.                                                   |
| Underscore         | \_     | Matches one character.                                                          |
| Square brackets    | \[ \]  | Matches any single character in the range or set specified within the brackets. |
| Caret              | ^      | Matches any single character not within the specified range or set.             |



 

</dd> <dt>

<span id="ORDER_BY_Clause"></span><span id="order_by_clause"></span><span id="ORDER_BY_CLAUSE"></span>*ORDER\_BY\_Clause*
</dt> <dd>

Specifies the ordering of the resulting rowset. This clause is optional. For details about this parameter, see [ORDER BY Clause](order-by-clause.md).

</dd> </dl>

### Remarks

In a **LIKE** search pattern, to use the percent sign ( % ), underscore ( \_ ),and left square bracket ( \[ ) as literal characters rather than as wildcard characters, surround the characters with square brackets. The right square bracket ( \] ) matches itself unless preceded by a left square bracket. The range character ( - ) matches itself unless it is inside square brackets and preceded and followed by a single character.

The following table shows patterns that illustrate using wildcard characters as literal characters.



| Pattern                | Meaning                                          |
|------------------------|--------------------------------------------------|
| **LIKE** 'd%'          | d followed by any string of 0 or more characters |
| **LIKE** 'd\[%\]'      | d%                                               |
| **LIKE** '\_n'         | an, in, on, etc.                                 |
| **LIKE** '\[\_\]n'     | \_n                                              |
| **LIKE** '\[a-cdf\]'   | a, b, c, d, or f                                 |
| **LIKE** '\[-acdf\]'   | -, a, c, d, or f                                 |
| **LIKE** '\[\[\]'      | \[                                               |
| **LIKE** '\]'          | \]                                               |
| **LIKE** '\[ab\]cd\]e' | acd\]e, or bcd\]e                                |



 

### Examples

The following example returns rows consisting of the DocAuthor, DocTitle, and size properties for all files under the virtual roots "/contracts" and "/legal", written by authors whose names are "Smith", "Smyth", "Smythe", and so on, where the comment field of those documents does not contain words starting with "real", such as "realty" or "realtor".


```
SELECT DocAuthor, DocTitle, size
  FROM SCOPE('"/contracts", "/legal"')
  WHERE DocAuthor LIKE 'SM_TH%'
    AND DocComments NOT LIKE 'REAL%'
```



The following example returns rows consisting of the DocTitle and size properties for all files under the virtual roots "/contracts" and "/legal", written by authors whose names begin with any characters except "A" through "F".


```
SELECT DocTitle, size
  FROM SCOPE('"/contracts", "/legal"')
  WHERE DocAuthor LIKE '[^a-f]%'
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

[MATCHES Predicate](matches-predicate.md)
</dt> <dt>

[NULL Predicate](null-predicate.md)
</dt> <dt>

[WHERE Clause](where-clause.md)
</dt> </dl>

 

 




