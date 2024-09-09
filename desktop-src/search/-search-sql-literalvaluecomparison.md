---
description: The literal value comparison uses standard comparison operators for matching a single-valued column to a literal value.
ms.assetid: 941298b4-d703-4b3f-8bde-0e6e158560df
title: Literal Value Comparison
ms.topic: article
ms.date: 05/31/2018
---

# Literal Value Comparison

The literal value comparison uses standard comparison operators for matching a single-valued column to a [literal](-search-sql-literals.md) value. For information about comparing multivalued columns, see [Multi-Valued (ARRAY) Comparisons](-search-sql-multivaluedcomparisons.md).

The literal value comparison predicate has the following syntax:


```
...WHERE <column> <comparison operator> <literal>
```



> [!Note]  
> The right side of the comparison must be a literal. You cannot compare a column against a computed value, and you cannot compare a column against another column.

 

The column part is any valid property column and can be cast to another type if necessary. Optionally, you can enclose the column name in double quotes for readability without affecting functionality. For more information, see [Casting the Data Type of a Column](-search-sql-castingdatacolumntype.md).

The literal can be any string, numeric, hexadecimal, Boolean, or date literal, enclosed in single quotation marks. Only exact matches are recognized, and wildcard characters are ignored. The literal can also be cast to another type.

## Comparison Operators

The following table describes the supported comparison operators.



| Comparison operator | Description              |
|---------------------|--------------------------|
| =                   | Equal to                 |
| != or <>      | Not equal to             |
| >                | Greater than             |
| >=               | Greater than or equal to |
| <                | Less than                |
| <=               | Less than or equal to    |



 

 

In conjunction with the "=" operator, Windows Search Structured Query Language (SQL) supports the use of BEFORE and AFTER keywords, which specify whether the query should compare column values before or after a specified value, in dictionary sort ordering.


```
...WHERE <column> <comparison operator> [BEFORE | AFTER](<https://msdn.microsoft.com/library/Ff637626(v=MSDN.10).aspx>)
```

Note: to compare dates, you must use [DATEADD](/windows/win32/search/-search-sql-dateadd).



## Examples

The following are examples of the literal value comparison predicate.


```
SELECT System.ItemUrl,System.ItemNameDisplay FROM SystemIndex 
    WHERE System.Title = 'Accounting'

SELECT System.ItemUrl,System.ItemNameDisplay FROM SystemIndex 
    WHERE System.IsFlagged != TRUE

SELECT System.ItemUrl,System.ItemNameDisplay FROM SystemIndex 
    WHERE System.Size >= 10000

SELECT System.ItemUrl,System.ItemNameDisplay FROM SystemIndex 
    WHERE System.Author = BEFORE('m')
```



## Related topics

<dl> <dt>

**Reference**
</dt> <dt>

[LIKE Predicate](-search-sql-like.md)
</dt> <dt>

[DATEADD Function](-search-sql-dateadd.md)
</dt> <dt>

[Multi-Valued (ARRAY) Comparisons](-search-sql-multivaluedcomparisons.md)
</dt> <dt>

[NULL Predicate](-search-sql-null.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Full-Text Predicates](-search-sql-fulltextpredicates.md)
</dt> <dt>

[Non-Full-Text Predicates](-search-sql-nonfulltextpredicates.md)
</dt> </dl>

 

 



