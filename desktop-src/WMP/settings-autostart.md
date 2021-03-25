---
title: Settings.autoStart
description: The autoStart property specifies or retrieves a value indicating whether the current media item begins playing automatically.
ms.assetid: 553f8534-9e3e-4fdc-bfc1-551939969289
keywords:
- Settings.autoStart Windows Media Player
topic_type:
- apiref
api_name:
- Settings.autoStart
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Settings.autoStart

The **autoStart** property specifies or retrieves a value indicating whether the current media item begins playing automatically.

## Syntax

player.settings.autoStart

## Possible Values

This property is a read/write **Boolean**.



| Value | Description                                                         |
|-------|---------------------------------------------------------------------|
| true  | Default. The media item begins playing automatically (see Remarks). |
| false | The media item does not begin playing automatically.                |



 

## Remarks

If **autoStart** is set to true, the media item will begin playing when *Player*.**URL**, *Player*.**currentPlaylist**, or *Player*.**currentMedia** is set. Otherwise, it will not start playing until the *Controls*.**play** method is called.

Because the **autoStart** property for the full mode of Windows Media Player can be set globally by external events (such as loading a CD), there is no reliable default value for skins and remoted Player controls. This is because the playback engine of the full mode Player is used in both cases.

You should set **autoStart** to false immediately before you set *Player*.**URL**, *Player*.**currentPlaylist**, or *Player*.**currentMedia** in skins and remoted Windows Media Player controls if you want to ensure that the media item does not start playing immediately. Also, unless you set **autostart** to true immediately before specifying a media item, you should not rely on this setting as a substitute for using the *Controls*.**play** method.

## Examples

The following example creates an HTML CHECKBOX element that allows the user to specify whether the Player control plays the current media item automatically. The **Player** object was created with ID = "Player".


```
<!-- Create an HTML CHECKBOX control. -->
<INPUT  TYPE = "CHECKBOX" ID = AS
              onClick = "
    /* Use the CHECKBOX state to specify the value 
       of the autoStart property. */
    Player.settings.autoStart = AS.checked;
"> 

```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Player.currentMedia**](player-currentmedia.md)
</dt> <dt>

[**Player.URL**](player-url.md)
</dt> <dt>

[**Settings Object**](settings-object.md)
</dt> </dl>

 

 





