---
title: Network.recoveredPackets
description: The recoveredPackets property retrieves the number of recovered packets.
ms.assetid: ce10b906-2e8b-4b9f-83d0-56ba67cacd3f
keywords:
- Network.recoveredPackets Windows Media Player
topic_type:
- apiref
api_name:
- Network.recoveredPackets
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Network.recoveredPackets

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **recoveredPackets** property retrieves the number of recovered packets.

## Syntax

*player*.*network*.**recoveredPackets**

## Possible Values

This property is a read-only **Number** (**long**).

## Remarks

Each time playback is stopped and restarted, this property is set to zero. It is not reset if playback is paused.

This property returns valid information only during run time and only if the *Player*.**URL** property is also set. It will equal zero when using the HTTP protocol, which is lossless.

## Examples

The following JScript example uses *Network*.**recoveredPackets** to display the number of recovered packets. The information is displayed in an HTML DIV created with ID = "PR". The example uses a timer with a 1-second interval to update the display. The **Player** object was created with ID = "Player".


```JScript
<!-- Create an event handler for play state change. -->
<SCRIPT FOR = Player EVENT = PlayStateChange(NewState)>
   var idI; // Variable for the interval id.

   // Test whether content is playing.
   if (3 == NewState){
      // Start the timer. Call the function to update the display every second.
      idI = window.setInterval("UpdatePR()", 1000);
   }
   else{
      // Not playing; stop the timer.
      window.clearInterval(idI);
   }   
</SCRIPT>

<!-- Put the function to update the display in a separate code block. -->
<SCRIPT>
function UpdatePR(){
   PR.innerHTML = "";
   PR.innerHTML = "Packets recovered: " + Player.network.recoveredPackets;
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

[**Player.URL**](player-url.md)
</dt> </dl>

 

 





