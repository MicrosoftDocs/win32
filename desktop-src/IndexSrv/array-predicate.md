---
Description: ARRAY Predicate
ms.assetid: c1630f2e-8384-4e27-9bd9-233a6b6d83d9
title: ARRAY Predicate
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ARRAY Predicate

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **ARRAY** (or Vector) predicate performs comparisons of two arrays using logical operators. This predicate is an optional part of the optional **WHERE** clause of the **SELECT** statement.

``` syntax
SELECT Select_List | *
       FROM_Clause
       [WHERE Column_Reference Comparison_Operator [ALL | SOME] ARRAY [Array_Parameters]]
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

Specifies the column name (alias). Its data type must be compatible with the format of the specified *Array\_Parameters* parameter. A column reference can have multiple values, such as in a vector property or file attribute bitmask.

</dd> <dt>

<span id="Comparison_Operator"></span><span id="comparison_operator"></span><span id="COMPARISON_OPERATOR"></span>*Comparison\_Operator*
</dt> <dd>

Specifies the arithmetic operator to use to compare the *Array\_Parameters* parameter.

*Comparison\_Operator* can be any of the following:

-   Equals (=) and not equals (!=).
-   Greater than (&gt;) and greater than or equals (&gt;=).
-   Less than (&lt;) and less than or equals (&lt;=).

</dd> <dt>

<span id="ALL___SOME"></span><span id="all___some"></span>**ALL** \| **SOME**
</dt> <dd>

Specifies the ways to quantify the *Array\_Parameters* parameter. You can use either the **ALL** or **SOME** quantifier. If you specify **ALL**, each parameter on the left side of the expression is tested by using each parameter on the right side. If you specify **SOME**, at least one parameter on the left side is tested by using at least one parameter of the right side.

For example, the following test fails because parameter 1 on the left side is less than parameter 2 on the right side.


```
[1,2,3] > ALL ARRAY [1,2]
```



The following test passes because parameter 2 on the left side is greater than parameter 2 on the right side (and parameter 3 on the left side is greater than parameters 1 and 2 on the right side, but one passed test is sufficient).


```
[1,2,3] > SOME ARRAY [2,1]
```



If the **ALL** or **SOME** quantifier is absent, each parameter in the vector value on the left side of the operator is compared to its right-side counterpart at the same ordinal position. The test begins with the leftmost parameters and progresses left to right. A test passes if all the individual tests pass. For example, if vectors A\[a₁, a₂, a₃\] and B\[b₁, b₂, b₃\] are used, then


```
A > B
```



passes if and only if a1 &gt; b1, a2 &gt; b2, and a3 &gt; b3.

If the first *m* parameters of the vector value on the right match the first *m* parameters on the right side of the comparison operator, then comparisons actually begin with the (*m*+1)<sup>th</sup> parameters where the values on the two sides differ. If all parameters match, then comparison is determined by cardinality, and the one with the higher cardinality is considered greater. The following vector tests all pass.


```
ARRAY [2,3,4] > ARRAY [1,2]
ARRAY [2,3,4] > ARRAY [1,2,3]
ARRAY [2,3,4] > ARRAY [1,2,3,4]
ARRAY [2,3,4] > ARRAY [1,2,5]
ARRAY [2,3,4] > ARRAY [2,3,3]
ARRAY [2,3,4] > ARRAY [2,3]
ARRAY [2,3,4] < ARRAY [2,3,4,5]
ARRAY [2,3,4]!= ARRAY [2,3,4,5]
```



</dd> <dt>

<span id="Array_Parameters"></span><span id="array_parameters"></span><span id="ARRAY_PARAMETERS"></span>*Array\_Parameters*
</dt> <dd>

Specifies the parameters in the array. You must include the square brackets when you specify the array parameters.

It is legal to have an empty array. For example, you can use:


```
SELECT search FROM SCOPE()
  WHERE bar = ARRAY[]
```



</dd> <dt>

<span id="ORDER_BY_Clause"></span><span id="order_by_clause"></span><span id="ORDER_BY_CLAUSE"></span>*ORDER\_BY\_Clause*
</dt> <dd>

Specifies the ordering of the resulting rowset. This clause is optional. For details about this parameter, see [ORDER BY Clause](order-by-clause.md).

</dd> </dl>

### Examples

The following example finds all the compressed files with the archive bit set to ON.


```
... WHERE attrib = ARRAY [0X820]
```



The following example finds the files with the archive bit set to ON or the compressed bit set to ON.


```
... WHERE attrib = SOME ARRAY [0X820]
```



The following example finds ActiveX documents with a vectorprop property value of \[10,15,20\].


```
... WHERE vectorprop = ARRAY [10, 15, 20]
```



The following example finds ActiveX documents where at least one vectorprop property value is 15.


```
... WHERE vectorprop = SOME ARRAY [15]
```



The following example finds files that must be printed by printers named HP3 or HP4.


```
... WHERE printerprop = SOME ARRAY ['HP4' , 'HP3']
```



## Related topics

<dl> <dt>

[Comparison Predicate](comparison-predicate.md)
</dt> <dt>

[CONTAINS Predicate](contains-predicate.md)
</dt> <dt>

[FREETEXT Predicate](freetext-predicate.md)
</dt> <dt>

[LIKE Predicate](like-predicate.md)
</dt> <dt>

[MATCHES Predicate](matches-predicate.md)
</dt> <dt>

[NULL Predicate](null-predicate.md)
</dt> <dt>

[WHERE Clause](where-clause.md)
</dt> </dl>

 

 



