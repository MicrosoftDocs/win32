---
title: Settings.defaultFrame
description: The defaultFrame property specifies or retrieves the name of the frame used to display a URL that is received in a ScriptCommand event.
ms.assetid: c2edb253-a545-4820-85aa-8fb7badf4d81
keywords:
- Settings.defaultFrame Windows Media Player
topic_type:
- apiref
api_name:
- Settings.defaultFrame
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Settings.defaultFrame

The **defaultFrame** property specifies or retrieves the name of the frame used to display a URL that is received in a **ScriptCommand** event.

## Syntax

player.settings.defaultFrame

## Possible Values

This property is a read/write **String** corresponding to the value of the **name** attribute of the target FRAME element.

## Remarks

If a target frame is specified in the **ScriptCommand** event itself, this property is ignored.

This property is ignored when using the Netscape Navigator Java applet. In Navigator, each URL script command received displays the URL in a new browser window, regardless of the value of *Settings*.**defaultFrame**.

**Windows Media Player 10 Mobile**: This property is read only, and always returns an empty string.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Player.ScriptCommand Event**](player-player-scriptcommand.md)
</dt> <dt>

[**Settings Object**](settings-object.md)
</dt> <dt>

[**Using Windows Media Player with Netscape 7.1**](using-windows-media-player-with-netscape-7-1.md)
</dt> </dl>

 

 





