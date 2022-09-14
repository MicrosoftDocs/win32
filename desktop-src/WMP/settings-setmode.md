---
title: Settings.setMode method
description: The setMode method sets various modes to active or inactive.
ms.assetid: '9ab88aeb-53f6-4798-9299-14961e373ca6'
keywords:
- setMode method Windows Media Player
- setMode method Windows Media Player , Settings class
- Settings class Windows Media Player , setMode method
topic_type:
- apiref
api_name:
- Settings.setMode
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Settings.setMode method

The **setMode** method sets various modes to active or inactive.

## Syntax


```JScript
Settings.setMode(
  modeName,
  state
)
```



## Parameters

<dl> <dt>

*modeName* \[in\]
</dt> <dd>

**String** specifying the name of the mode being changed, containing one of the following values.



| String     | Description                                                                                                                                                       |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| autoRewind | Mode indicating whether the tracks are rewound to the beginning after playing to the end. Default state is true.                                                  |
| loop       | Mode indicating whether the sequence of tracks repeats itself. Default state is false.                                                                            |
| showFrame  | Mode indicating whether the nearest video key frame is displayed at the current position when not playing. Default state is false. Has no effect on audio tracks. |
| shuffle    | Mode indicating whether the tracks are played in random order. Default state is false.                                                                            |



 

</dd> <dt>

*state* \[in\]
</dt> <dd>

**Boolean** specifying whether the new specified mode is active or not.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

When the showFrame mode is active, the Player must access the track content to retrieve the video frame. Due to bandwidth considerations, use this mode cautiously when playing non-local content.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | For loop and shuffle modes, Windows Media Player version 7.0 or later. For autoRewind and showFrame modes, Windows Media Player 9 Series or later.<br/> |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl>                                                                            |



## See also

<dl> <dt>

[**Settings Object**](settings-object.md)
</dt> <dt>

[**Settings.getMode**](settings-getmode.md)
</dt> </dl>

 

 





