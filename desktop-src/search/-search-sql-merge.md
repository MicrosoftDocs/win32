---
description: Used with the RANK BY clause to aggregate the ranks from all of the results to generate a final ranked list of merge results.
title: MERGE(<merge_operation>)
ms.topic: article
ms.date: 02/26/2025
---

# MERGE(<merge_operation>)

Used with the [RANK BY](-search-sql-rankby.md) clause to aggregate the ranks from all of the results to generate a final ranked list of merge results.


The syntax for the MERGE clause is as follows:


```
RANK BY MERGE ( <merge_operation>) 
```

## Merge operations

The following table describes the supported operations for the *merge_operation* parameter.

| Merge operation | Description |
|-----------------|-------------|
| CONVEXCOMBINATION | This merging algorithm employs a convex combination approach that combines scores from all the results using a weighted sum approach, where lexical scores are prioritized with higher weights over semantic ones. The aggregated score is then scaled by multiplying it by 1000 to determine the final rank.  |
| MIN | This merging algorithm is the default behavior in the case of an AND cursor. It selects the minimum rank from all results.|
| MAX | This merging algorithm is the default behavior in the case of an OR cursor. It selects the maximum rank from all results. |

The following example demonstrates the use of the MERGE function to search for items lexically and semantically matching with the word "computer" in either the "Image" or "Text" fields. The search results are then ranked using RANK BY MERGE operator which aggregates scores from all the results to generate a final ranked list. 

## Example

```sql
WHERE (CONTAINS(*,'computer', 1033)  
OR CONTAINSSEMANTIC('Image', *, 'computer', 1033)  
OR CONTAINSSEMANTIC('Text', System.ItemNameDisplay, 'computer', 1033)  
OR CONTAINSSEMANTIC('Text', *, 'computer', 1033))  
RANK BY MERGE(CONVEXCOMBINATION) 
```

For more information on the CONTAINSSEMANTIC predicate, see [CONTAINSSEMANTIC predicate](-search-sql-containssemantic.md).

## Related topics

[RANK BY](-search-sql-rankby.md)
[CONTAINSSEMANTIC predicate](-search-sql-containssemantic.md).

### Reference

[WHERE Clause](-search-sql-where.md)

 

 



