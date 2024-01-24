---
title: Network.sourceProtocol
description: The sourceProtocol property retrieves the source protocol used to receive data.
ms.assetid: f09bbcd0-9c34-49d1-8080-247aed2548d5
keywords:
- Network.sourceProtocol Windows Media Player
topic_type:
- apiref
api_name:
- Network.sourceProtocol
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Network.sourceProtocol

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **sourceProtocol** property retrieves the source protocol used to receive data.

## Syntax

*player*.*network*.**sourceProtocol**

## Possible Values

This property is a read-only **String**.

## Remarks

This property is set to "" (empty string) when playing media from a CD or DVD.

## Examples

The following JScript example uses *Network*.**sourceProtocol** to display the source protocol used to receive data. The information is displayed in an HTML DIV created with ID = "SP". The **Player** object was created with ID = "Player".


```JScript
<!-- Create an event handler for play state change. -->
<SCRIPT FOR = Player EVENT = PlayStateChange(NewState)>
   if (3 == NewState){
     SP.innerHTML = "Source protocol: " + Player.network.sourceProtocol;
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
</dt> </dl>

 

 





