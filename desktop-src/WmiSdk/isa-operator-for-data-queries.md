---
description: Use the ISA operator in the WHERE clause of a data query to request embedded objects in a class hierarchy.
ms.assetid: a4eb4c34-2ed0-4e85-84c6-6b8f17c8b07d
ms.tgt_platform: multiple
title: ISA Operator for Data Queries
ms.topic: article
ms.date: 05/31/2018
---

# ISA Operator for Data Queries

Use the ISA operator in the WHERE clause of a data query to request embedded objects in a class hierarchy.

The following example shows the syntax to request embedded objects in a class hierarchy.


```sql
SELECT * FROM Class WHERE EmbeddedProp ISA "ParentClass"
```



The result includes instances of **Class** having embedded objects that are derived from **ParentClass** in the **EmbeddedProp** property. Not every instance of the **Class** object is derived from **ParentClass**, but the result returns the embedded objects that are derived from **ParentClass**.

For example, in the following query, **ClassA** includes the weakly typed **EmbeddedObj** property. The **ClassA** class has ten instances. Five of those instances have embedded objects with a type derived from **ClassZ**. The other five have embedded objects of other types.

The following example shows the query that returns the five instances, which include the objects that are derived from **ClassZ**.


```sql
SELECT * FROM ClassA WHERE EmbeddedObj ISA "ClassZ"
```



 

 



