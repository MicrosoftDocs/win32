---
title: About the Query Object
description: About the Query Object
ms.assetid: 41488036-bdcf-4fe6-8f7e-f0897157d3d9
keywords:
- Windows Media Player,Query object
- Windows Media Player object model,Query object
- object model,Query object
- Windows Media Player ActiveX control,Query object
- ActiveX control,Query object
- Windows Media Player Mobile ActiveX control,Query object
- Windows Media Player Mobile,Query object
- Query object
ms.topic: article
ms.date: 05/31/2018
---

# About the Query Object

The **Query** object represents a compound query. You create a new, empty **Query** object by calling *mediaCollection*.**createQuery**. After you have created a **Query** object, you can call **addCondition** to add a condition to the compound query. Each subsequent call to **addCondition** appends a new condition to the existing query using AND logic.

For example, suppose you want to create a query that represents all digital media where **WM/Genre** equals "Jazz" and **Author** contains "Jim". You could create a compound query to represent these conditions by using the following JScript code:


```C++
// Create the query object.
var Query = player.mediaCollection.createQuery();

// Add the conditions.
Query.addCondition("WM/Genre", "Equals", "Jazz");
Query.addCondition("Author", "Contains", "Jim");
```



To add a condition to a compound query using OR logic, you must call **Query.beginNextGroup**. This method signals that the previous condition group is completed and that the next call to **addCondition** represents the start of a new condition group.

For example, to create a query that represents all digital media where **WM/Genre** equals "Jazz" and **Author** contains "Jim" or **Author** contains "Dave", you could use the following example code:


```C++
// Create the query object.
var Query = player.mediaCollection.createQuery();

// Add the conditions.
Query.addCondition("WM/Genre", "Equals", "Jazz");
Query.addCondition("Author", "Contains", "Jim");

// Start the next condition group. This group will be
// combined with the previous group using a logical OR operation.
Query.beginNextGroup();

// Add the conditions.
Query.addCondition("WM/Genre", "Equals", "Jazz");
Query.addCondition("Author", "Contains", "Dave");
```



To execute your compound query, call **MediaCollection.getPlaylistByQuery**.

## Related topics

<dl> <dt>

[**MediaCollection.getPlaylistByQuery**](mediacollection-getplaylistbyquery.md)
</dt> <dt>

[**Player Object Model for Scripting Languages**](player-object-model-for-scripting-languages.md)
</dt> <dt>

[**Query Object**](query-object.md)
</dt> </dl>

 

 




