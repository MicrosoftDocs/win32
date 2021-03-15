---
title: Player.AudioLanguageChange event
description: The AudioLanguageChange event occurs when the current audio language changes. | Player.AudioLanguageChange event
ms.assetid: 29006a51-1b72-4fab-9906-8a0af3d92560
keywords:
- AudioLanguageChange event Windows Media Player
- AudioLanguageChange event Windows Media Player , Player class
- Player class Windows Media Player , AudioLanguageChange event
topic_type:
- apiref
api_name:
- Player.AudioLanguageChange
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Player.AudioLanguageChange event

The **AudioLanguageChange** event occurs when the current audio language changes.

## Syntax


```JScript
Player.AudioLanguageChange(
  LangID
)
```



## Parameters

<dl> <dt>

*LangID* 
</dt> <dd>

**Number** (**long**) specifying the new locale identifier (LCID).

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

An LCID uniquely identifies a particular language dialect, called a locale.

The value of event parameters is specified by Windows Media Player, and can be accessed or passed to a method in an imported Microsoft JScript file by using the parameter name given. This parameter name must be typed exactly as shown, including capitalization.

**Windows Media Player 10 Mobile:** This event is not supported.

## Requirements



|                    |                                                                                    |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later.<br/>                                 |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Controls.currentAudioLanguage**](controls-currentaudiolanguage.md)
</dt> <dt>

[**Player Object**](player-object.md)
</dt> </dl>

 

 





