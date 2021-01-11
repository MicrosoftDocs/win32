---
description: The SET statement specifies PROPERTYNAME and RANKMETHOD options for the query.
ms.assetid: 14b833a5-5e6a-4f1a-b15e-3b32d7e0df37
title: SET Statement
ms.topic: article
ms.date: 05/31/2018
---

# SET Statement

The SET statement specifies PROPERTYNAME and RANKMETHOD options for the query.

## PROPERTYNAME

You can associate a property with a friendly alias for the query by using the following syntax:


```
SET PROPERTYNAME <guid_format> 
PROPID <property_id> | <property_name> 
AS <column_alias> [<type_clause>] 
```



## RANKMETHOD

You can specify the rank method for queries with the ISABOUT term by using the following syntax:


```
SET RANKMETHOD <rankmethod>      
```



The RANKMETHOD methods that can be specified by using the SET statement are JACCARD COEFFICIENT, DICE COEFFICIENT, and INNER PRODUCT.

 

 



