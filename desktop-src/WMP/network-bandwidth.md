---
title: Network.bandWidth
description: The bandWidth property retrieves the current bandwidth of the clip.
ms.assetid: 2ef86f2a-98e9-4544-a740-c2237f06c135
keywords:
- Network.bandWidth Windows Media Player
topic_type:
- apiref
api_name:
- Network.bandWidth
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Network.bandWidth

The **bandWidth** property retrieves the current bandwidth of the clip.

## Syntax

*player*.*network*.**bandWidth**

## Possible Values

This property is a read-only **Number** (**long**).

## Remarks

This property returns zero if the *Player*.**URL** property is not set. This property is only valid for streaming media.

## Examples

The following Microsoft JScript example uses *Network*.**bandWidth** to display the current media bandwidth. The information is displayed in an HTML DIV created with ID = "BW". The **Player** object was created with ID = "Player".


```JScript
<!-- Create an event handler for play state.-->
<SCRIPT FOR = Player EVENT = PlayStateChange()>

   switch (Player.playState){

      case 3:

         if (Player.network.bandwidth != 0){
  
            BW.innerHTML = "Current Bandwidth: " + Player.network.bandWidth;
            BW.innerHTML += " K bits/second";
         }

         else
            BW.innerHTML = "Bandwidth is only available for streaming media.";

            break;

      default:
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

 

 





