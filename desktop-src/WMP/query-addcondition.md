---
title: Query.addCondition method
description: The addCondition method adds a condition to the Query object using AND logic.
ms.assetid: '29b5d372-eddf-4b70-882b-d2dde79d9287'
keywords:
- addCondition method Windows Media Player
- addCondition method Windows Media Player , Query class
- Query class Windows Media Player , addCondition method
topic_type:
- apiref
api_name:
- Query.addCondition
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Query.addCondition method

The **addCondition** method adds a condition to the **Query** object using AND logic.

## Syntax


```JScript
Query.addCondition(
  attribute,
  operator,
  value
)
```



## Parameters

<dl> <dt>

*attribute* \[in\]
</dt> <dd>

**String** containing the attribute name.

</dd> <dt>

*operator* \[in\]
</dt> <dd>

**String** containing the operator. See Remarks for supported values.

</dd> <dt>

*value* \[in\]
</dt> <dd>

**String** containing the attribute value.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

Compound queries using **Query** are not case sensitive.

A list of values for the *attribute* parameter can be found in the [Alphabetical Attribute Reference](alphabetical-attribute-reference.md) section.

Conditions contained in a **Query** object are organized into condition groups. Multiple conditions within a condition group are always concatenated using AND logic. Condition groups are always concatenated to each other using OR logic. To start a new condition group, call **Query.beginNextGroup**.

The following table lists the supported values for *operator*.



| Operator            | Applies to     |
|---------------------|----------------|
| BeginsWith          | Strings        |
| Contains            | Strings        |
| Equals              | All types      |
| GreaterThan         | Numbers, Dates |
| GreaterThanOrEquals | Numbers, Dates |
| LessThan            | Numbers, Dates |
| LessThanOrEquals    | Numbers, Dates |
| NotBeginsWith       | Strings        |
| NotContains         | Strings        |
| NotEquals           | All types      |



 

## Examples

The following JScript example uses **Query.addCondition** and **Query.beginNextGroup** to perform an example query.


```JScript
// Perform an example query for media for which:
// The genre contains "jazz"
// and the title begins with "a"
// OR the genre contains "jazz"
// and the author begins with "b".

// Create the query object.
var Query = Player.mediaCollection.createQuery();

// Add the first condition group.
Query.addCondition("WM/Genre", "Contains", "jazz");
Query.addCondition("Title", "BeginsWith", "a");

// Begin the new condition group ("or").
Query.beginNextGroup();

// Add the second condition group.
Query.addCondition("WM/Genre", "Contains", "jazz");
Query.addCondition("Author", "BeginsWith", "b");

// Perform the query on "audio" media.
var Playlist = Player.mediaCollection.getPlaylistByQuery(
    Query,      // query
    "audio",    // mediaType
    "",         // sortAttribute
    false);     // sortAscending
```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 11.<br/>                                                |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**MediaCollection.createQuery**](mediacollection-createquery.md)
</dt> <dt>

[**MediaCollection.getPlaylistByQuery**](mediacollection-getplaylistbyquery.md)
</dt> <dt>

[**MediaCollection.getStringCollectionByQuery**](mediacollection-getstringcollectionbyquery.md)
</dt> <dt>

[**Query Object**](query-object.md)
</dt> <dt>

[**Query.beginNextGroup**](query-beginnextgroup.md)
</dt> </dl>

 

 





