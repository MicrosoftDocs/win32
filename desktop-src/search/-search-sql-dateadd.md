---
description: The DATEADD function performs time and date calculations for matching properties having date types. Use the DATEADD function to obtain dates and times in a specified amount of time before the present.
ms.assetid: 83ef098d-85ef-4883-a1e1-9229e050247f
title: DATEADD Function
ms.topic: article
ms.date: 05/31/2018
---

# DATEADD Function

The DATEADD function performs time and date calculations for matching properties having date types. Use the DATEADD function to obtain dates and times in a specified amount of time before the present.

## Syntax


```
DATEADD (DateTimeUnits, OffsetValue, DateTime)
```



## Arguments

*DateTimeUnits*

Specifies the units of the *DateTime* parameter: YEAR, QUARTER, MONTH, WEEK, DAY, HOUR, MINUTE, or SECOND. This value is case-sensitive, and quotation marks are not required around the parameter.

*OffsetValue*

Specifies the time offset, in the units specified by the *DateTimeUnits* parameter. **OffsetValue** must be a negative integer. Positive values are not supported.

*DateTime*

Specifies a time stamp from which to calculate the offset. This cannot be a date literal. It must be either GETGMTDATE or the result of another DATEADD function.

## Remarks

The DATEADD function can be used only in literal value comparisons and only on the right side of the comparison operator.

The GETGMTDATE function returns the current date and time in Greenwich Mean Time (GMT). Remember that this value may not be the same as the local time of your computer.

Do not use the equals (=) comparison operator because the internal time representation can produce rounding errors that result in unexpected matching results.

You can use multiple DATEADD functions to combine offset units.

### Examples

The following example WHERE clause matches documents that were modified within the last five days:


```
...WHERE System.DateModified <=DATEADD (DAY, -5, GETGMTDATE())
```



The following example WHERE clause matches documents that were modified within the last two days and four hours:


```
...WHERE System.DateModified <=DATEADD (DAY, -2, DATEADD (HOUR, -4, GETGMTDATE()))
```



## Related topics

<dl> <dt>

**Reference**
</dt> <dt>

[Literal Value Comparison](-search-sql-literalvaluecomparison.md)
</dt> <dt>

[Multi-Valued (ARRAY) Comparisons](-search-sql-multivaluedcomparisons.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Full-Text Predicates](-search-sql-fulltextpredicates.md)
</dt> <dt>

[Non-Full-Text Predicates](-search-sql-nonfulltextpredicates.md)
</dt> </dl>

 

 



