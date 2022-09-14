---
title: THEME.playSound
description: The playSound method plays the specified sound file.
ms.assetid: 42675a66-0139-4e74-9abe-1b42017fc6fe
keywords:
- THEME.playSound Windows Media Player
topic_type:
- apiref
api_name:
- THEME.playSound
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# THEME.playSound

The **playSound** method plays the specified sound file.

``` syntax
        theme.playSound(soundFile)
```

## Parameters

<dl> <dt>

<span id="soundFile"></span><span id="soundfile"></span><span id="SOUNDFILE"></span>*soundFile*
</dt> <dd>

A **String** specifying the name of the sound file to play.

</dd> </dl>

## Return Value

This method does not return a value.

## Remarks

This method allows you to add sound effects to a skin for example, when buttons are clicked. The sound is played by the operating system directly and not by Windows Media Player. This means that the sound cannot be controlled with Windows Media Player settings and methods, but it can be played while Windows Media Player is playing another digital media file.

This method supports WAV files only.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**THEME Element**](theme-element.md)
</dt> </dl>

 

 





