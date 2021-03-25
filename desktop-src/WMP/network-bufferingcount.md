---
title: Network.bufferingCount
description: The bufferingCount property retrieves the number of times buffering occurred during clip playback.
ms.assetid: 25a58795-161e-4290-8ea7-51acca968ef9
keywords:
- Network.bufferingCount Windows Media Player
topic_type:
- apiref
api_name:
- Network.bufferingCount
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Network.bufferingCount

The **bufferingCount** property retrieves the number of times buffering occurred during clip playback.

## Syntax

*player*.*network*.**bufferingCount**

## Possible Values

This property is a read-only **Number** (**long**).

## Remarks

Each time playback is stopped and restarted, this property is set to zero. It is not reset if playback is paused.

Buffering only applies to streaming content. This property returns valid information only during run time when the *Player*.**URL** property is set.

## Examples

The following JScript example uses *Network*.**bufferingCount** to display the number of times buffering occurs during playback. The information is displayed in an HTML DIV created with ID = "CB". The **Player** object was created with ID = "Player".


```JScript
<!-- Create an event handler. -->
<SCRIPT FOR = Player EVENT = buffering(Start)>
   if (true == Start) 
      CB.innerHTML = "Buffering count: " + Player.network.bufferingCount;
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

 

 





