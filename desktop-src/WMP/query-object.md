---
title: Query Object
description: The Query object represents a compound query.
ms.assetid: 'a0094897-a7f5-40ba-af49-e5a5a8fcb762'
keywords:
- Query Object Windows Media Player
topic_type:
- apiref
api_name:
- Query Object
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# Query Object

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **Query** object represents a compound query.

The **Query** object supports the following methods.



| Method                                     | Description                                               |
|--------------------------------------------|-----------------------------------------------------------|
| [addCondition](query-addcondition.md)     | Adds a condition to the **Query** object using AND logic. |
| [beginNextGroup](query-beginnextgroup.md) | Begins a new condition group.                             |



 

For purposes of illustration, player.mediaCollection.createQuery() is used to represent the **Query** object in the reference syntax sections.

-   [About the Query Object](about-the-query-object.md)
-   [MediaCollection.createQuery](mediacollection-createquery.md)
-   [MediaCollection.getPlaylistByQuery](mediacollection-getplaylistbyquery.md)
-   [MediaCollection.getStringCollectionByQuery](mediacollection-getstringcollectionbyquery.md)
-   [Object Model Reference for Scripting](object-model-reference-for-scripting.md)

 

 




