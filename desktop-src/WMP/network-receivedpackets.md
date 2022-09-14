---
title: Network.receivedPackets
description: The receivedPackets property retrieves the number of packets received.
ms.assetid: db4f6f08-c248-4db8-ab19-fdd5d2794085
keywords:
- Network.receivedPackets Windows Media Player
topic_type:
- apiref
api_name:
- Network.receivedPackets
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Network.receivedPackets

The **receivedPackets** property retrieves the number of packets received.

## Syntax

*player*.*network*.**receivedPackets**

## Possible Values

This property is a read-only **Number** (**long**).

## Remarks

Each time clip playback is stopped and restarted, this property is set to zero. It is not reset if file playback is paused.

## Examples

The following JScript example uses *Network*.**receivedPackets** to display the number of packets received. The information is displayed in an HTML DIV created with ID = "RP". The example uses a timer with a 1-second interval to update the display. The **Player** object was created with ID = "Player".


```JScript
<!-- Create an event handler for play state change. -->
<SCRIPT FOR = Player EVENT = PlayStateChange(NewState)>

   var idI; // Variable for the interval id.

   // Test whether packets may be arriving.
   switch (NewState){
      case 1, 2, 4, 5, 7, 8, 9:
          window.clearInterval(idI);
          break;

      default:
         idI = window.setInterval("UpdateRP()", 1000);

   }</SCRIPT>

<!-- Put the function to update the display in a separate code block. -->
<SCRIPT>
function UpdateRP(){
   RP.innerHTML = "";
   RP.innerHTML = "Packets received: " + Player.network.receivedPackets;         
}

```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Network Object**](network-object.md)
</dt> </dl>

 

 





