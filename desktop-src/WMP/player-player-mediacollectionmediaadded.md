---
title: Player.MediaCollectionMediaAdded event
description: The MediaCollectionMediaAdded event occurs when a media item is added to the local library. | Player.MediaCollectionMediaAdded event
ms.assetid: 01696d28-e83b-4fd2-8e88-2871831b61e7
keywords:
- MediaCollectionMediaAdded event Windows Media Player
- MediaCollectionMediaAdded event Windows Media Player , Player class
- Player class Windows Media Player , MediaCollectionMediaAdded event
topic_type:
- apiref
api_name:
- Player.MediaCollectionMediaAdded
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Player.MediaCollectionMediaAdded event

The MediaCollectionMediaAdded event occurs when a media item is added to the local library.

## Syntax


```JScript
Player.MediaCollectionMediaAdded(
  pdispMedia
)
```



## Parameters

<dl> <dt>

*pdispMedia* 
</dt> <dd>

**Media** object that was added.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

This event only occurs for the local library.

**Windows Media Player 10 Mobile:** This event is not supported.

## Requirements



|                    |                                                                                    |
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

 

 





