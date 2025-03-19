---
description: The results from a query include both the rows returned by the query and a rank value for each row if the rank column is included in the SELECT clause.
ms.assetid: 8655eec4-5151-4f82-b485-4dbef947df0d
title: RANK BY Clause
ms.topic: reference
ms.date: 05/31/2018
---

# RANK BY Clause

The results from a query include both the rows returned by the query and a rank value for each row if the rank column is included in the SELECT clause. The rank values are calculated by the Search engine and are returned as integers in the range zero to 1000. To make the rank results more meaningful, the query can control how raw rank values are calculated in the RANK BY clause.

This topic is organized as follows:

-   [RANK BY Clause](#rank-by-clause)
-   [WEIGHT Function](#weight-function)
-   [COERCION Function](#coercion-function)

## RANK BY Clause

The syntax for the RANK BY clause is as follows:


```sql
WHERE ( <search_condition> ) 
RANK BY [ ( ] <rank_specification> [ ) ]
```



The RANK BY clause is applied to the search\_condition immediately preceding it, effectively specifying a lower or higher rank for rows returned by that search condition than rows returned by another search condition. The parentheses surrounding the search\_condition are required. The parentheses surrounding the rank specification are optional.

More than one RANK BY clause can be applied to a single condition. You can include additional RANK BY clauses one after the other using parentheses.

> [!Note]  
> Full-text predicates return rank values in the range 0 to 1000. Rank values for all documents matched by a non-full-text predicate are 1000. Modifications to the rank values should take this information into account.

 

The rank\_specification portion of the RANKBY clause identifies one or more functions to apply to the rank values. The WEIGHT function applies a multiplier to the raw rank value for a returned row. The smaller the multiplier, the lower the resulting rank value. The COERCION function can be used to multiply, add to, or set a specific rank value for a returned row. Each rank specification can include either zero or one WEIGHT function and zero or more COERCION functions. If both WEIGHT and COERCION functions are included in a RANK BY clause, the WEIGHT function must be first.

## WEIGHT Function

The syntax of the WEIGHT function is:


```sql
WEIGHT ( <weight_multipler> ) 
```



The multiplier must be a decimal from 0.001 to 1.000. The raw rank value returned by the search condition predicate is multiplied by the weight multiplier to set a new rank value.

In the following example, the WEIGHT function gives documents with the word "Theresa" in the System.Document.LastAuthor field half the rank value of documents with "Theresa" in the System.Author field:


```sql
WHERE CONTAINS ( System.Author,'"Theresa"' ) 
         RANK BY WEIGHT ( 1.000 )
      OR
      CONTAINS ( System.Document.LastAuthor,'"Theresa"' ) 
         RANK BY WEIGHT ( 0.500 ) 
```



 

> [!Note]  
> The CONTAINS and FREETEXT predicate column weighting features support a shorthand format using a colon between the search term and the multiplier ("software":0.25). The RANK BY clause does not support the shortened form.

 

There is a limitation when using RANK BY WEIGHT: it does not work with CONTAINS clauses that use Boolean conditions; for example, the following example is not permitted:


```sql
CONTAINS ( System.Author,'"Theresa" OR "Teresa"' ) RANK BY WEIGHT ( 0.400 )
```



## COERCION Function

The rank coercion function can be used to change the returned rank value by addition or multiplication or by assigning it a specific value.

The syntax of the COERCION function is:

```sql
COERCION ( <coercion_operation> , <coercion_value> )
```

The coercion value is an integer value.

The following table describes the available coercion operation settings.

| Coercion operation | Description                                                                                    | Value range  |
|--------------------|------------------------------------------------------------------------------------------------|--------------|
| ABSOLUTE           | The rank value returned is the value specified in the coercion value.                          | 0 to 1000    |
| ADD                | The rank value returned is the sum of the raw rank value and the specified coercion value.     | 0 to 1000 |
| MULTIPLY           | The rank value returned is the product of the raw rank value and the specified coercion value. | 0 to 1000 |
| MINMAX | The rank value returned is the linear mapping of the the 0-1000 rank score of the matching item from CONTAINS or CONTAINSSEMANTIC between the specified minimum and maximum coercion values. | 0 to 1000 |

> [!IMPORTANT]
> Search can return rank values only in the range of 0 to 1000.

The following example uses the COERCION function to set all documents with "computer" in the title to have a rank of 1000, while reducing by one-quarter the rank of documents containing both "computer" and "software" in the title.

```sql
WHERE CONTAINS ( System.Title, 'computer' )
        RANK BY COERCION ( ABSOLUTE , 1000 )
        OR 
       CONTAINS ( System.Title, '"computer" AND "software"' )
        RANK BY COERCION ( MULTIPLY, 0.750 ) 
```

The following example uses the COERCION function to map the raw rank of documents with the term "computer" to a range between 500 to 800 based on their semantic matches.

```sql
WHERE CONTAINSSEMANTIC('text', *, 'computer', 1033)
OR CONTAINSSEMANTIC('image', *, 'computer', 1033)
RANK BY COERCION(MINMAX, 500, 800)
ORDER BY System.Search.Rank DESC
```


 
## MERGE(<merge_operation>)

Used with the [RANK BY](-search-sql-rankby.md) clause to aggregate the ranks from all of the results to generate a final ranked list of merge results.


The syntax for the MERGE function is as follows:


```sql
RANK BY MERGE ( <merge_operation>) 
```

### Merge operations

The following table describes the supported operations for the *merge_operation* parameter.

| Merge operation | Description |
|-----------------|-------------|
| CONVEXCOMBINATION | This merging algorithm should be used exclusively when the query includes the following clauses: CONTAINS (lexical search), CONTAINSSEMANTIC('Text',...), and CONTAINSSEMANTIC('Image'...) (semantic search across text and images). It combines scores from these three clauses using a weighted sum approach, giving higher priority to lexical scores by assigning them greater weights when compared to semantic scores.  The final rank will be between 0 and 1000. |
| MIN | This merging algorithm is the default behavior in the case of an AND cursor. It selects the minimum rank from all results.|
| MAX | This merging algorithm is the default behavior in the case of an OR cursor. It selects the maximum rank from all results. |

> [!NOTE]
> Using RANK BY MERGE\(MIN\) with an OR cursor or RANK BY MERGE\(MAX\) with an AND cursor will not yield the expected results. It is recommended to explicitly use the MERGE function with the RANK BY clause only in conjunction with the CONVEXCOMBINATION operator when merging lexical and semantic search results into a single result set.


### Example

The following example demonstrates the use of the MERGE function to search for items lexically and semantically matching with the word "computer" in either the "Image" or "Text" fields. The search results are then ranked using RANK BY MERGE operator which aggregates scores from all the results to generate a final ranked list. 


```sql
WHERE (CONTAINS(*,'computer', 1033)  
OR CONTAINSSEMANTIC('Image', *, 'computer', 1033)  
OR CONTAINSSEMANTIC('Text', System.ItemNameDisplay, 'computer', 1033)  
OR CONTAINSSEMANTIC('Text', *, 'computer', 1033))  
RANK BY MERGE(CONVEXCOMBINATION) 
```

For more information on the CONTAINSSEMANTIC predicate, see [CONTAINSSEMANTIC predicate](-search-sql-containssemantic.md).
 



