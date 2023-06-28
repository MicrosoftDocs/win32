---
title: Network.downloadProgress
description: The downloadProgress property retrieves the percentage of download completed.
ms.assetid: bb57ce84-babb-4dc2-bc2b-c40cbb587e91
keywords:
- Network.downloadProgress Windows Media Player
topic_type:
- apiref
api_name:
- Network.downloadProgress
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Network.downloadProgress

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **downloadProgress** property retrieves the percentage of download completed.

## Syntax

*player*.*network*.**downloadProgress**

## Possible Values

This property is a read-only **Number** (**long**).

## Remarks

When the Windows Media Player control is connected to a media file that can be played and downloaded at the same time, the **downloadProgress** property returns the percentage of the total file that has been downloaded. This feature is currently supported only on web servers. The following file formats can be downloaded and played simultaneously:

-   Advanced Systems Format (ASF)
-   Windows Media Audio (WMA)
-   Windows Media Video (WMV)
-   MP3
-   MPEG
-   WAV
-   Some AVI files

Use the *Player*.**Buffering** event to determine when the downloading begins and ends.

## Examples

The following JScript example uses *Network*.**downloadProgress** to display the percentage of downloading completed. The information is displayed in an HTML DIV created with ID = "DP". The example uses a timer with a 1 second interval to update the display. The **Player** object was created with ID = "Player".


```JScript
<!-- Create an event handler for buffering. -->
<SCRIPT FOR = Player EVENT = buffering(Start)>
   var idI; // Variable for the interval id.
   
   // Test whether downloading has started or stopped.
   if (true == Start){ 
      // Start the timer. Call the function to update the display.
      idI = window.setInterval("UpdateDP()", 1000);
   }
   else{
      // Downloading is complete. Stop the timer.
      window.clearInterval(idI);
   }
</SCRIPT>

<!-- Put the function to update the display in a separate code block. -->
<SCRIPT>
function UpdateDP(){
   DP.innerHTML = "";
   DP.innerHTML = "Download progress: " + Player.network.downloadProgress;
   DP.innerHTML += " percent complete";
}
</SCRIPT>

```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Network Object**](network-object.md)
</dt> <dt>

[**Player.Buffering Event**](player-player-buffering.md)
</dt> </dl>

 

 





