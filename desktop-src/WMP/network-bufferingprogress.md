---
title: Network.bufferingProgress
description: The bufferingProgress property retrieves the percentage of buffering completed.
ms.assetid: d604159b-7c42-47f8-8085-53f859f24703
keywords:
- Network.bufferingProgress Windows Media Player
topic_type:
- apiref
api_name:
- Network.bufferingProgress
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Network.bufferingProgress

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **bufferingProgress** property retrieves the percentage of buffering completed.

## Syntax

*player*.*network*.**bufferingProgress**

## Possible Values

This property is a read-only **Number** (**long**).

## Remarks

Each time playback is stopped and restarted, this property is set to zero. It is not reset if playback is paused.

Buffering only applies to streaming content. This property returns valid information only during run time, when the *Player*.**URL** property is set.

Use the *Player*.****Buffering**** event to determine when buffering starts or stops.

## Examples

The following JScript example uses *Network*.**bufferingProgress** to display the percentage of buffering completed. The information is displayed in an HTML DIV created with ID = "BP". The example uses a timer with a 1-second interval to update the display. The **Player** object was created with ID = "Player".


```JScript
<!-- Create an event handler for buffering. -->
<SCRIPT FOR = Player EVENT = buffering(Start)>
   var idI; // Variable for the interval id.

   // Test whether buffering has started or stopped.
   if (true == Start){ 
      // Start the timer. Call the function to update the display every second.
      idI = window.setInterval("UpdateBP()", 1000);
   }

   else{
      // Buffering is complete. Stop the timer.
      window.clearInterval(idI);
   }
</SCRIPT>

<!-- Put the function to update the display in a separate code block. -->
<SCRIPT>
function UpdateBP(){
   BP.innerHTML = "";
   BP.innerHTML = "Buffering progress: " + Player.network.bufferingProgress;
   BP.innerHTML += " percent complete";
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
</dt> <dt>

[**Player.URL**](player-url.md)
</dt> </dl>

 

 





