---
title: Player.MediaCollectionMediaRemoved event
description: The MediaCollectionMediaRemoved event occurs when a media item is removed from the local library. | Player.MediaCollectionMediaRemoved event
ms.assetid: a1df6faf-38dc-4f5f-8f8a-953c91ea026c
keywords:
- MediaCollectionMediaRemoved event Windows Media Player
- MediaCollectionMediaRemoved event Windows Media Player , Player class
- Player class Windows Media Player , MediaCollectionMediaRemoved event
topic_type:
- apiref
api_name:
- Player.MediaCollectionMediaRemoved
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Player.MediaCollectionMediaRemoved event

The MediaCollectionMediaRemoved event occurs when a media item is removed from the local library.

## Syntax


```JScript
Player.MediaCollectionMediaRemoved(
  pdispMedia
)
```



## Parameters

<dl> <dt>

*pdispMedia* 
</dt> <dd>

**Media** object that was removed.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

This event only occurs for the local library.

**Windows Media Player 10 Mobile:** This event is not supported.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 11.<br/>                                                |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**MediaCollection Object**](mediacollection-object.md)
</dt> <dt>

[**Player Object**](player-object.md)
</dt> <dt>

[**Player.mediaCollection**](player-mediacollection.md)
</dt> </dl>

 

 





