---
description: A subquery is a saved search file (\*.search-ms) that you can use as a filter for a new query.
title: SUBQUERY Argument (The Windows Shell)
ms.topic: article
ms.date: 05/31/2018
ms.assetid: 2d97b891-ba62-4009-bc6a-9f42e6dbbb34
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# SUBQUERY Argument (The Windows Shell)

A subquery is a saved search file (\*.search-ms) that you can use as a filter for a new query. The results of the subquery are used as the source for the new query. For example, say you have several saved search files that restrict a query by email distribution list: mydepartment.search-ms, teamproject.search-ms, and corporatewide.search-ms. Using the `subquery` argument enables you to limit email searches to any or all of these saved searches.

## Example


```
search:query=vacation&subquery=mydepartment.search-ms
```



### Argument Information



|                          |                                         |
|--------------------------|-----------------------------------------|
| Minimum Operating System | Windows Vista with Service Pack 1 (SP1) |



 

 

 



