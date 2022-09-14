---
title: Player.MediaError event
description: The MediaError event occurs when the Media object has an error condition.
ms.assetid: b2e0176a-cc52-4f59-8894-440f426a1b6e
keywords:
- MediaError event Windows Media Player
- MediaError event Windows Media Player , Player class
- Player class Windows Media Player , MediaError event
topic_type:
- apiref
api_name:
- Player.MediaError
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Player.MediaError event

The **MediaError** event occurs when the **Media** object has an error condition.

## Syntax


```JScript
Player.MediaError(
  pMediaObject
)
```



## Parameters

<dl> <dt>

*pMediaObject* 
</dt> <dd>

**Media** object that has an error condition.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

The value of event parameters is specified by Windows Media Player, and can be accessed or passed to a method in an imported JScript file using the parameter name given. This parameter name must be typed exactly as shown, including capitalization.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player for Windows XP or later.<br/>                           |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Player Object**](player-object.md)
</dt> </dl>

 

 





