---
description: The GROUP ON...
ms.assetid: 37f027c1-c2af-4d62-8b5f-918499fc2d7c
title: GROUP ON ... OVER ... Statement
ms.topic: article
ms.date: 05/31/2018
---

# GROUP ON ... OVER ... Statement

The GROUP ON... OVER... statement returns a hierarchical rowset in which search results are divided into groups based on a specified column and optional grouping ranges. If you group on the [System.Kind](../properties/props-system-kind.md) column, the result set is divided into multiple groups: one for documents, one for communications, and so on. If you group on [System.Size](../properties/props-system-size.md) and group range 100 KB, the result set is divided into three groups: items of size < 100 KB, items of size >= 100 KB, and items with no size value. You can also aggregate groupings with functions.

This topic covers the following subjects:

-   [Syntax](#syntax)
-   [Group Ranges](#group-ranges)
-   [Labeling Groups](#labeling-groups)
-   [Ordering Groups](#ordering-groups)
-   [Nesting Groups](#nesting-groups)
-   [Grouping on Vector Properties](#grouping-on-vector-properties)
-   [More Examples](#more-examples)
-   [Related topics](#related-topics)

## Syntax

The GROUP ON ... OVER ... statement has the following syntax:


```
GROUP ON <column> ['['<group ranges>']']] 
[AGGREGATE <aggregate_function>] 
[ORDER BY <column> [<direction>]] | [ORDER IN GROUP '<group name>' BY <column> [<direction>]]
    OVER (GROUP ON... | SELECT... ] )
```



where grouping ranges are defined as follows:


```
<group ranges> := <range limit> [/'<label>'] | <range limit> [/'<label>'], <group ranges>
<range limit> := (<number> | <date> | '<string>' | BEFORE('<string>') | AFTER('<string>')) 
```



The GROUP ON &lt;column&gt; can be a regular or delimited [identifier](-search-sql-identifiers.md) for a property in the property store.

The optional \<group range\> is a list of one or more values (number, date, or string) used for dividing the results into groups. The \<range limit\> identifies a division point in the returned result set, and the <label> identifies a user-friendly label for a group. You can divide the result set into as many groups as you need.

The first group of results includes items with the minimum possible value for the specified property up to but not including the first range limit. This group can be referred to with the MINVALUE keyword. The second group can be referred to with the range limit specifier itself and includes items whose value for the specified property is equal to or greater than the range limit. Any items that do not have a value for the specified property are returned last and can be referred to with the **NULL** keyword.

For example, a range limit of '2006-01-01' for the [System.DateCreated](../properties/props-system-datecreated.md) property divides the result set into items with dates before 2006-01-01 (MINVALUE group), items with dates on or after 2006-01-01 (2006-01-01 group), and items with no date (**NULL** group).

Within each group, the results are sorted by the values in the GROUP ON column by default. The optional [ORDER BY](-search-sql-orderby.md) clause can contain a direction specifier of either ASC for ascending (low to high) or DESC for descending (high to low), and the [ORDER IN GROUP BY](-search-sql-orderingroup.md) clause can order each group using different rules. See the [Ordering Groups](#ordering-groups) section below for more information.

## Group Ranges

The following table demonstrates how results are divided into groups based the range limits:



| Example (&lt;column&gt; \[group ranges\])        | Result                                                                                                                                                                                                                                                                         |
|--------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| System.Size \[1000, 5000\]                       | Results are grouped into four buckets: **MINVALUE**: Size < 1000<br/> **1000:** 1000 <= Size < 5000<br/> **5000:** Size >= 5000<br/> **NULL:** No value for Size<br/>                                                                      |
| System.Author \[BEFORE('m'),AFTER('r')\]         | Results are grouped into four buckets: **MINVALUE:** Author < character before "m"<br/> **m:** character before "m" <= Author < character after "r"<br/> **r:** character after "r" <= Author<br/> **NULL:** No value for Author<br/>      |
| System.Author \[MINVALUE/'a to l',"m"/'m to z'\] | Results are grouped into three buckets: **a to l:** Author < "m"<br/> **m to z:** "m" <= Author <br/> **NULL:** No value for Author<br/>                                                                                                               |
| System.DateCreated \['2005-1-01','2006-6-01'\]   | Results are grouped into four buckets:<br/> **MINVALUE:** DateCreated < 2005-1-01<br/> **2005-1-01:** 2005-1-01 <= DateCreated < 2006-6-01<br/> **2006-1-01:** DateCreated >= 2006-6-01<br/> **NULL:** No value for DateCreated<br/> |



 

 

> [!IMPORTANT]
>
> Incorrect: `GROUP ON System.Author['m','z','a']`
>
> Correct: `GROUP ON System.Author['a','m','z']`

 

 

## Labeling Groups

To improve readability, you can label groups using the following syntax:


```
GROUP ON <column> [<range limit>/'<label>',<range limit>/'<label>']
```



The label is separated from the range limit with a slash mark and is enclosed in single quotation marks. If you do not specify a label, the group name is the range limit string.

The following is an example of labeling groups:


```
GROUP ON System.Size [(MINVALUE/'Small','100')/'Medium','50000'/'Large']
    OVER (SELECT System.Size FROM SystemIndex)
```



In Windows 7 or later, you can also use a generic \[OTHER\] label to combine multiple grouping ranges. Results from all groups identified with this label will be combined into one group with this label. This group of results is returned after all other groups except for the **NULL** group. The **NULL** group contains results for items that do not have a value for the specified property. Prior to Windows 7 the \[OTHER\] label is treated like any other group label.

The following code is an example of using the \[OTHER\] label for groups that would be created in Windows 7 or later:


```
GROUP ON System.Author ['0', 'A'/'[OTHER]', 'I', 'Q', 'W'/'[OTHER]', 'Y']
    OVER (SELECT System.DateCreated FROM SystemIndex)
```



The following table shows the groups that would be created by the preceding grouping code in Windows 7 or later.



| Group     | System.Author | System.FileName |
|-----------|---------------|-----------------|
| 0         | 1Bill         | Lorem.docx      |
| Q         | Queen         | Ipsum.docx      |
|           | Robin         | dolor.docx      |
| Y         | Zara          | amet.docx       |
| \[OTHER\] | Abner         | nonummy.docx    |
|           | Bob           | laoreet.docx    |
|           | Xaria         | magna.docx      |
| **NULL**  |               | aliquam.docx    |



 

## Ordering Groups

There are three ways to order items in groups:

-   Default ordering: If you do not specify otherwise, the results are ordered by the values in the GROUP ON column, in ascending order.
-   ORDER BY: You can specify descending order in an ORDER BY clause. You must order the results by the GROUP ON column.
-   ORDER IN GROUP BY: You can specify a different order for each group. If you group on [System.Kind](../properties/props-system-kind.md), you can order documents by [System.Author](../properties/props-system-author.md) and music by [System.Music.Artist](../properties/props-system-music-artist.md).

For more information on ordering results, see the [ORDER BY Clause](-search-sql-orderby.md) and [ORDER IN GROUP Clause](-search-sql-orderingroup.md) reference pages.

## Nesting Groups

You can nest groups with multiple GROUP ON clauses. The order specified in the query is directly reflected in the output group hierarchy, as shown in the following example.


```
GROUP ON <System.Kind> 
      OVER (GROUP ON <System.Author> 
                  OVER (SELECT <System.DateCreated>))
```





| System.Kind    | System.Author | System.DateCreated |
|----------------|---------------|--------------------|
| documents      | Willa         | 2006-01-02         |
|                |               | 2006-01-05         |
|                | Zara          | 2007-06-02         |
|                |               | 2007-09-10         |
| communications | Abner         | 2006-04-16         |
|                | Jean          | 2007-02-20         |
|                | Willa         | 2006-10-15         |
|                | Zara          | 2008-01-02         |



 

 

## Grouping on Vector Properties

Grouping on vector properties, properties that can contain one or more values simultaneously, compares the vector values individually by default. For example, if there is one document, Lorem.docx, with the System.Author property as "Theresa;Zara" and another document, Ipsum.docx, with the System.Author property as "Zara", the query returns the result set in two groups as shown here:


```
GROUP ON <System.Author> 
      OVER (SELECT <System.FileName>)
```





| System.Author | System.FileName |
|---------------|-----------------|
| Theresa       | Lorem.docx      |
| Zara          | Lorem.docx      |
|               | Ipsum.docx      |



 

As you can see, grouping on vector properties returns duplicate rows. Lorem.docx appears twice because it has two authors.

 

## More Examples


```
GROUP ON System.Photo.ISOSpeed [0,10,100] 
      OVER (SELECT System.ItemName, System.Size, System.ItemUrl FROM SystemIndex)
            
GROUP ON System.DateCreated['2005/01/01 00:00:00', '2005/12/30 23:00:00'] 
      OVER (SELECT System.ItemName, System.Size, System.ItemUrl FROM SystemIndex)
            
GROUP ON System.Author ORDER BY System.Author DESC 
      OVER (GROUP ON System.DateCreated ORDER BY System.DateCreated ASC 
                  OVER (SELECT System.FileName, System.DateCreated, System.Size FROM SystemIndex 
                        WHERE CONTAINS(*, 'text')))

GROUP ON System.ItemName [before('a'), 'a', before ('c'), 'd', after('d')] 
      OVER (SELECT System.ItemName, System.ItemUrl FROM SystemIndex ORDER BY System.ItemName)                        
                        
GROUP ON System.ItemNameDisplay ['a' / 'col_a','c' / 'col_c'] 
      OVER (SELECT System.ItemNameDisplay FROM SystemIndex 
            ORDER BY System.ItemNameDisplay)

GROUP ON System.Size[1,2] 
      OVER (GROUP ON System.Author['a','f','mc','x'] 
                  OVER (GROUP ON System.DateCreated['2005/07/25 07:00:00', '2005/08/25 07:00:00']
                        ORDER BY System.DateCreated DESC 
                              OVER (SELECT System.FileName FROM SystemIndex 
                                    WHERE CONTAINS('text'))))   
```



## Related topics

<dl> <dt>

[Aggregate Functions](-search-sql-aggregates.md)
</dt> <dt>

[ORDER BY Clause](-search-sql-orderby.md)
</dt> <dt>

[ORDER IN GROUP Clause](-search-sql-orderingroup.md)
</dt> </dl>

 

 
