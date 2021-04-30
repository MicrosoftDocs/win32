---
description: The results from a query include both the rows returned by the query and a rank value for each row if the rank column is included in the SELECT clause.
ms.assetid: 8655eec4-5151-4f82-b485-4dbef947df0d
title: RANK BY Clause
ms.topic: article
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


```
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


```
WEIGHT ( <weight_multipler> ) 
```



The multiplier must be a decimal from 0.001 to 1.000. The raw rank value returned by the search condition predicate is multiplied by the weight multiplier to set a new rank value.

In the following example, the WEIGHT function gives documents with the word "Theresa" in the System.Document.LastAuthor field half the rank value of documents with "Theresa" in the System.Author field:


```
WHERE CONTAINS ( System.Author,'"Theresa"' ) 
         RANK BY WEIGHT ( 1.000 )
      OR
      CONTAINS ( System.Document.LastAuthor,'"Theresa"' ) 
         RANK BY WEIGHT ( 0.500 ) 
```



 

> [!Note]  
> The CONTAINS and FREETEXT predicate column weighting features support a shorthand format using a colon between the search term and the multiplier ("software":0.25). The RANK BY clause does not support the shortened form.

 

There is a limitation when using RANK BY WEIGHT: it does not work with CONTAINS clauses that use Boolean conditions; for example, the following example is not permitted:


```
CONTAINS ( System.Author,'"Theresa" OR "Teresa"' ) RANK BY WEIGHT ( 0.400 )
```



## COERCION Function

The rank coercion function can be used to change the returned rank value by addition or multiplication or by assigning it a specific value.

The syntax of the COERCION function is:


```
COERCION ( <coercion_operation> , <coercion_value> )
```



The coercion value is an integer value.

The following table describes the available coercion operation settings.



| Coercion operation | Description                                                                                    | Value range  |
|--------------------|------------------------------------------------------------------------------------------------|--------------|
| ABSOLUTE           | The rank value returned is the value specified in the coercion value.                          | 0 to 1000    |
| ADD                | The rank value returned is the sum of the raw rank value and the specified coercion value.     | 0.001 to 1.0 |
| MULTIPLY           | The rank value returned is the product of the raw rank value and the specified coercion value. | 0.001 to 1.0 |



 

 

> [!IMPORTANT]
> Search can return rank values only in the range of 0 to 1000.

 

 

The following example uses the COERCION function to set all documents with "computer" in the title to have a rank of 1000, while reducing by one-quarter the rank of documents containing both "computer" and "software" in the title.


```
WHERE CONTAINS ( System.Title, 'computer' )
        RANK BY COERCION ( ABSOLUTE , 1000 )
        OR 
       CONTAINS ( System.Title, '"computer" AND "software"' )
        RANK BY COERCION ( MULTIPLY, 0.750 ) 
```



 

 



