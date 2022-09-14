---
description: Columns stored in the content index can have multiple values, and those multivalued columns can be compared by using the ARRAY comparison predicate.
ms.assetid: bc3de1bd-b833-459d-81a3-c6b08314e26f
title: Multi-Valued (ARRAY) Comparisons
ms.topic: article
ms.date: 05/31/2018
---

# Multi-Valued (ARRAY) Comparisons

Columns stored in the content index can have multiple values, and those multivalued columns can be compared by using the ARRAY comparison predicate.

The ARRAY comparison predicate has the following syntax:


```
...WHERE <column> <comp_op> [<quantifier>] <comparison_list>
                
...WHERE <column> <comp_op> <value>
```



An error is returned if the column reference is not a multivalued column. The column data type must be compatible with the elements of the comparison list. If necessary, the column reference can be [cast](-search-sql-castingdatacolumntype.md) as another data type.

The comparison operator (comp\_op) can be any of the normal comparison operators. In a multivalued comparison, the comparison operators have slightly different meanings depending on whether a quantifier is used. Quantifiers identify whether a comparison should be made against all or some of the values in the comparison list. The functions of the comparison operators are given in the tables describing each quantifier (ALL and SOME) later in this document.

The value after the operator specifies a single literal value that is compared against all elements of the multivalued column. If any element matches the value, the predicate is true.

The comparison list specifies an array of literal values that are compared against the multivalued column. The syntax for the comparison list follows:


```
ARRAY '['<literal> [,<literal>]']'
```



> [!IMPORTANT]
> Be aware of the comparison list syntax. The group of literals that make up the comparison list must be surrounded by square brackets. Do not surround individual elements of the comparison list by square brackets. Therefore, ARRAY \[1\] and ARRAY \[1,2,3\] are valid, but ARRAY \[1\[,2\]\[,3\]\] is not.

 

The method used to determine whether the multivalued comparison returns true or false is specified by the optional quantifier. The following sections describe each quantifier, and how each comparison operator works when the quantifier is used.

## Absent Quantifier

If no quantifier is specified, each element on the left side of the comparison is compared to the element in the same position on the right side. The comparison begins with the first element in the arrays, and progresses through the last element. If all the elements on the left side are equivalent to the corresponding elements on the right side, the number of array elements is used to determine which array is greater.

The following table shows the operation of the comparison operators when no quantifier is specified and provides a brief description of each.



| Operator       | Description                                                                                                                                                                                                                                                                                                                                                                           |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| =              | 'Equal to' returns true when each left-side element has the same value as the corresponding right-side element, and both arrays have the same number of elements.                                                                                                                                                                                                                     |
| != or <> | 'Not equal to' returns true when one or more left-side elements have values that differ from the corresponding right-side elements, or when the left-side and right-side arrays do not have the same number of elements.                                                                                                                                                              |
| >           | 'Greater than' returns true when the value of each left-side element is greater than the value of the corresponding right-side element. If all the left-side element values exactly match the corresponding right-side elements and the left-side array has more elements than the right-side array, 'greater than' returns true.                                                     |
| >=          | 'Greater than or equal to' returns true when the value of every left-side element is greater than or equal to the value of the corresponding right-side element. If all the left-side element values are equal to or greater than the corresponding right-side elements and the left-side array has the same or more elements than the right-side array, 'greater than' returns true. |
| <           | 'Less than' returns true when the value of each left-side element is less than the value of the corresponding right-side element. 'Less than' also returns true when the left-side side has fewer elements than the right-side side.                                                                                                                                                  |
| <=          | 'Less than or equal to' returns true when the value of every left-side element is less than or equal to the value of the corresponding right-side element. If all the left-side element values are equal to or less than the corresponding right-side elements and the left-side array has the same or fewer elements than the right-side array, 'greater than' returns true.         |



 

## ALL Quantifier

The ALL quantifier specifies that each element in the left side is compared against every element on the right side. To return true, the comparison must be true for each element on the left side when compared to every element on the right side. The number of elements in the left and right array sides has no effect on the result.

The following table shows how each comparison operator functions with the ALL quantifier.



| Operator       | Description                                                                                                                           |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------|
| =              | 'Equal to' returns true when each left-side element value is the same as every right-side element value.                              |
| != or <> | 'Not equal to' returns true when at least one of the left-side element values is different from any of the right-side element values. |
| >           | 'Greater than' returns true when each left-side element value is greater than every right-side element value.                         |
| >=          | 'Greater than or equal to' returns true when each left-side element value is greater than or equal to every right-side element value. |
| <           | 'Less than' returns true when each left-side element value is less than every right-side element value.                               |
| <=          | 'Less than or equal to' returns true when each left-side element value is less than or equal to every right-side element value.       |



 

## SOME (or ANY) Quantifier

The SOME quantifier and the ANY quantifier can be used interchangeably. Like the ALL quantifier, the SOME quantifier specifies that each element in the left side is compared against every element on the right side. To return true, the comparison must be true for at least one of the elements on the left side when compared to any element on the right side. The number of elements on the left and right side arrays has no effect on the result.

The following table shows how each comparison operator functions with the SOME quantifier.



| Operator       | Description                                                                                                                                                     |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| =              | 'Equal to' returns true when at least one of the left-side element values is the same as any of the right-side element values.                                  |
| != or <> | 'Not equal to' returns true when none of the left-side element values is the same as any of the right-side element values.                                      |
| >           | 'Greater than' returns true when at least one of the left-side element values is greater than any one of the right-side element values.                         |
| >=          | 'Greater than or equal to' returns true when at least one of the left-side element values is greater than or equal to any one of the right-side element values. |
| <           | 'Less than' returns true when at least one of the left-side element values is less than any one of the right-side element values.                               |
| <=          | 'Less than or equal to' returns true when at least one of the left-side element values is less than or equal to any one of the right-side element values.       |



 

## Examples

The following example checks whether documents are in the "Finance" or "Planning" categories:


```
SELECT System.ItemUrl FROM SystemIndex WHERE System.Category =
SOME ARRAY['Finance','Planning']
```



The following comparisons all evaluate true. Remember that in actual use, the search query syntax requires the left side to be a property, not a literal value.


```
ARRAY [1,2] > ARRAY [1,1]
ARRAY [1,2] > ARRAY [1,1,2]
ARRAY [1,2] < ARRAY [1,2,3]
ARRAY [1,2] = SOME ARRAY [1,12,27,35,2]
ARRAY [1,1] != ALL ARRAY [1,2]
ARRAY [1,20,21,22] < SOME ARRAY [0,40]
ARRAY [1,20,21,22] < ANY ARRAY [0,40]
```



## Related topics

<dl> <dt>

**Reference**
</dt> <dt>

[LIKE Predicate](-search-sql-like.md)
</dt> <dt>

[Literal Value Comparison](-search-sql-literalvaluecomparison.md)
</dt> <dt>

[NULL Predicate](-search-sql-null.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Full-Text Predicates](-search-sql-fulltextpredicates.md)
</dt> <dt>

[Non-Full-Text Predicates](-search-sql-nonfulltextpredicates.md)
</dt> </dl>

 

 



