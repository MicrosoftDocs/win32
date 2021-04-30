---
title: Network.lostPackets
description: The lostPackets property retrieves the number of packets lost.
ms.assetid: b90faaaf-656a-4b9b-abfe-370e6f7c7c4b
keywords:
- Network.lostPackets Windows Media Player
topic_type:
- apiref
api_name:
- Network.lostPackets
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Network.lostPackets

The **lostPackets** property retrieves the number of packets lost.

## Syntax

*player*.*network*.**lostPackets**

## Possible Values

This property is a read-only **Number** (**long**).

## Remarks

This property is only valid for streaming media, and will equal zero when using the HTTP protocol, which is lossless.

Packets may be lost for a number of reasons, such as the type and quality of the network connection.

Each time playback is stopped and restarted, this property is set to zero. It is not reset if playback is paused and restarted. This property returns valid information only during run time, and only if the *Player*.**URL** property is set.

## Examples

The following JScript example uses *Network*.**lostPackets** to display the total number of packets lost during playback when the user clicks a button. The information is displayed in an HTML DIV created with ID = "LP". The **Player** object was created with ID = "Player".


```JScript
<!-- Create an HTML BUTTON element. -->
<INPUT TYPE = "BUTTON" ID = "lostpkts" NAME = "lostpkts"
       VALUE = "Count lost packets" 
       onClick = "LP.innerHTML = 'Packets lost: ' + Player.network.lostPackets;">

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

 

 





