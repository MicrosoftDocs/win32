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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Query.beginNextGroup method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

[**Query.addCondition**](query-addcondition.md)
</dt> </dl>

 

 





