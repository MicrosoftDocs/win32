---
title: Player.newMedia method
description: The newMedia method creates a new Media object.
ms.assetid: 'fccf1559-bac3-4edf-bd88-da2c72cdec21'
keywords:
- newMedia method Windows Media Player
- newMedia method Windows Media Player , Player class
- Player class Windows Media Player , newMedia method
topic_type:
- apiref
api_name:
- Player.newMedia
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Player.newMedia method

The **newMedia** method creates a new **Media** object.

## Syntax


```JScript
retVal = Player.newMedia(
  URL
)
```



## Parameters

<dl> <dt>

*URL* \[in\]
</dt> <dd>

**String** containing the URL of the digital media file to create the **Media** object with.

</dd> </dl>

## Return value

This method returns a **Media** object.

## Remarks

The *URL* parameter must not be an empty string or null.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later.<br/>                                 |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Player Object**](player-object.md)
</dt> </dl>

 

 





