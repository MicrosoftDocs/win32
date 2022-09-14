---
description: Column group aliases provide a way to use shorter names in place of the name of a column or a group of columns. The optional group alias predicate is part of the WHERE clause.
ms.assetid: 7782ac24-ea6c-4a97-b1b6-982f276fcefc
title: WITH -- AS Group Alias Predicate
ms.topic: article
ms.date: 05/31/2018
---

# WITH -- AS Group Alias Predicate

Column group aliases provide a way to use shorter names in place of the name of a column or a group of columns. The optional group alias predicate is part of the WHERE clause. Its syntax follows:


```
...WHERE[ WITH(<columns>) AS #<alias_name>]
[,WITH(<columns>) AS #<alias_name>]
```



You can specify more than one group alias, separating the WITH...AS predicates by commas.

When a group alias is referred to in a WHERE clause predicate, the condition is applied to each column in the group. The logical values resulting from matching each column are combined by using the logical **OR** operator.

An alias must be defined before it can be used, and it can be used only within the WHERE clause. The alias name must be a regular identifier preceded by a required pound sign (\#).

The column specifier can contain one or more column specifiers, separated by commas. The list of columns must be enclosed in parentheses and weighting can be assigned to each. Each column has the following syntax:


```
<column_identifier> [<weight_assignment>]
```



For information on specifying column weights, see [FREETEXT Predicate](-search-sql-freetext.md) and [CONTAINS Predicate](-search-sql-contains.md).

The column identifier can be regular or delimited.

## Examples

The following WHERE clause examples demonstrate when and how you can use the group alias predicate. The first example shows a more repetitive WHERE clause that does not use group aliasing.


```
...WHERE
    FREETEXT("System.ItemNameDisplay",'"computer software"')
    OR
    FREETEXT("System.Title",'"computer software"')
    OR 
    FREETEXT("System.Keywords",'"computer software"')
```



The preceding example can be simplified by using a group alias, as shown in the following example.


```
...WHERE
    WITH("System.ItemNameDisplay","System.Title","System.Keywords")
    AS #Doc-Descriptions
    FREETEXT(#Doc-Descriptions,'"computer software"')
```



The following is an example of positive weighting where the **Title** property is given more weight in determining the relative rank.


```
...WHERE
    WITH("System.Title":0.8,*:0.5,
         "System.Keywords")
    AS #Doc-Descriptions
    FREETEXT(#Doc-Descriptions,'"computer software"')
```



The following is an example of negative weighting where the **Title** property with weight of 0 is not considered.


```
...WHERE
    WITH("System.Title":0,*:1.0,
         "System.Keywords")
    AS #Doc-Descriptions
    FREETEXT(#Doc-Descriptions,'"computer software"')
```



## Related topics

<dl> <dt>

**Reference**
</dt> <dt>

[FREETEXT Predicate](-search-sql-freetext.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Full-Text Predicates](-search-sql-fulltextpredicates.md)
</dt> <dt>

[Non-Full-Text Predicates](-search-sql-nonfulltextpredicates.md)
</dt> </dl>

 

 



