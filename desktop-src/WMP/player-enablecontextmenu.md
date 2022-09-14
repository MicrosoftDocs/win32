---
title: Player.enableContextMenu
description: The enableContextMenu property specifies or retrieves a value indicating whether to enable the context menu, which appears when the right mouse button is clicked.
ms.assetid: 736c8714-5650-4912-9e97-914a20137b91
keywords:
- Player.enableContextMenu Windows Media Player
topic_type:
- apiref
api_name:
- Player.enableContextMenu
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Player.enableContextMenu

The **enableContextMenu** property specifies or retrieves a value indicating whether to enable the context menu, which appears when the right mouse button is clicked.

## Syntax

*player*.**enableContextMenu**

## Possible Values

This property is a read/write Boolean.



| Value | Description                       |
|-------|-----------------------------------|
| true  | Default. Enable the context menu. |
| false | Do not enable the context menu.   |



 

## Remarks

During full-screen playback, Windows Media Player hides the mouse cursor when **enableContextMenu** equals false and **uiMode** equals "none".

**Windows Media Player 10 Mobile:** This property is not supported.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Player Object**](player-object.md)
</dt> </dl>

 

 





