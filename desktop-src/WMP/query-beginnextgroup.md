---
title: Query.beginNextGroup method
description: The beginNextGroup method begins a new condition group. | Query.beginNextGroup method
ms.assetid: 'e0c59bd0-0789-413e-ade8-8d53c6f3e19b'
keywords:
- beginNextGroup method Windows Media Player
- beginNextGroup method Windows Media Player , Query class
- Query class Windows Media Player , beginNextGroup method
topic_type:
- apiref
api_name:
- Query.beginNextGroup
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Query.beginNextGroup method

The **beginNextGroup** method begins a new condition group.

## Syntax


```JScript
Query.beginNextGroup()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

Beginning a new condition group implies that you have completed the current condition group. The new condition group is always concatenated to the previous condition group using OR logic.

## Requirements



|                    |                                                                                    |
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

[**Query.addCondition**](query-addcondition.md)
</dt> </dl>

 

 





