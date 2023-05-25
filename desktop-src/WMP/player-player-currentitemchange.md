---
title: Player.CurrentItemChange event
description: The CurrentItemChange event occurs when Controls.currentItem changes.
ms.assetid: e6f68aeb-d7e7-460b-adc9-647f28c678a1
keywords:
- CurrentItemChange event Windows Media Player
- CurrentItemChange event Windows Media Player , Player class
- Player class Windows Media Player , CurrentItemChange event
topic_type:
- apiref
api_name:
- Player.CurrentItemChange
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Player.CurrentItemChange event

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **CurrentItemChange** event occurs when *Controls*.**currentItem** changes.

## Syntax


```JScript
Player.CurrentItemChange()
```



## Parameters

This event has no parameters.

## Return value

This event does not return a value.

## Examples

The following JScript example demonstrates an event handler for the *Player*.**currentItemChange** event. The **Player** object was created with ID = "Player".


```JScript
<!-- Create an HTML text box to display the media item name. -->
<INPUT TYPE="TEXT" NAME="MEDIA">

<!-- Create an event handler. -->
<SCRIPT LANGUAGE = "JScript"  FOR = Player EVENT = currentItemChange()>

   // Display the name of the new media item.
   MEDIA.value = Player.currentMedia.name;

</SCRIPT>
```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Controls.currentItem**](controls-currentitem.md)
</dt> <dt>

[**Player Object**](player-object.md)
</dt> </dl>

 

 





