---
title: Media.duration
description: The duration property retrieves the duration of the current media item in seconds.
ms.assetid: d7d36858-812d-471b-84ce-fe2ab96b86b3
keywords:
- Media.duration Windows Media Player
topic_type:
- apiref
api_name:
- Media.duration
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Media.duration

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **duration** property retrieves the duration of the current media item in seconds.

## Syntax

*player*.*currentMedia*.**duration**

## Possible Values

This property is a read-only **Number** ( **double**).

## Remarks

If this property is used with a media item other than the one specified in *Player*.**currentMedia**, it may not contain a valid value.

To retrieve the duration for files that are not in the user's library, you must wait for Windows Media Player to open the file; that is, the current OpenState must equal MediaOpen. You can verify this by handling the *Player*.**OpenStateChange** event or by periodically checking the value of *Player*.**openState**.

For playlists, the duration of each media item can be retrieved when the individual media item is opened, rather than the when the playlist is opened.

To retrieve the value of this property, read access to the library is required. For more information, see [Library Access](library-access.md).

The following JScript example uses *Media*.**duration** to display the time remaining in the current media item. An HTML DIV element named RemTime displays the information. An HTML timer updates the text in the DIV element every second.

The following JScript code starts the timer:


```JScript
// Execute the update() function at one-second intervals.
idTmr = window.setInterval("update()",1000);
```



The following JScript code stops the timer:


```JScript
window.clearInterval(idTmr);
```



Use the *Player*.**PlayStateChange** event with a **switch** statement to determine when to start and stop the timer.

The following JScript code executes each time the timer calls the update function:


```JScript
// Store the current position of the current media item.
var TimeNow = Player.controls.currentPosition;

// Display the time remaining information.
RemTime.innerHTML = "Seconds remaining: ";

// Subtract the current position from the duration of the current media.
// Use the Math.floor method to round the result down to the nearest integer.
RemTime.innerHTML += Math.floor(Player.currentMedia.duration - TimeNow);
```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Media Object**](media-object.md)
</dt> <dt>

[**Player.currentMedia**](player-currentmedia.md)
</dt> <dt>

[**Player.PlayStateChange Event**](player-player-playstatechange.md)
</dt> <dt>

[**Settings.mediaAccessRights**](settings-mediaaccessrights.md)
</dt> <dt>

[**Settings.requestMediaAccessRights**](settings-requestmediaaccessrights.md)
</dt> </dl>

 

 





