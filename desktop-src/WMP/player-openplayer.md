---
title: Player.openPlayer method
description: The openPlayer method opens Windows Media Player using the specified URL. | Player.openPlayer method
ms.assetid: '9ddd63c9-f4a0-490a-8543-51ad0fa74a26'
keywords:
- openPlayer method Windows Media Player
- openPlayer method Windows Media Player , Player class
- Player class Windows Media Player , openPlayer method
topic_type:
- apiref
api_name:
- Player.openPlayer
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Player.openPlayer method

The **openPlayer** method opens Windows Media Player using the specified URL.

## Syntax


```JScript
Player.openPlayer(
  URL
)
```



## Parameters

<dl> <dt>

*URL* \[in\]
</dt> <dd>

**String** representing the URL of the media item to play.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

This method launches Windows Media Player with the specified URL set as the current media item. If the Player was previously closed in skin mode it will open using the skin last chosen by the user. Otherwise, the Player opens in full mode.

If this method is called from a Windows Media PlayerActiveX control embedded in remote mode, its behavior is identical to the *PlayerApplication*.**switchToPlayerApplication** method.

**Windows Media Player 10 Mobile:** This method is not supported.

## Requirements



|                    |                                                                                    |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later.<br/>                                 |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Player Object**](player-object.md)
</dt> <dt>

[**PlayerApplication.switchToPlayerApplication**](playerapplication-switchtoplayerapplication.md)
</dt> </dl>

 

 





