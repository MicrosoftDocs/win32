---
title: Network.bitRate
description: The bitRate property retrieves the current bit rate being received.
ms.assetid: e970a43a-1773-4dc0-ac2f-115f698bc1f4
keywords:
- Network.bitRate Windows Media Player
topic_type:
- apiref
api_name:
- Network.bitRate
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Network.bitRate

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **bitRate** property retrieves the current bit rate being received.

## Syntax

*player*.*network*.**bitRate**

## Possible Values

This property is a read-only **Number** (**long**).

## Remarks

This value is a combination of the bit rates of both the current video and audio streams.

## Examples

The following JScript example uses *Network*.**bitRate** to display the current media bit rate. The information is displayed in an HTML DIV created with ID = "BR". The **Player** object was created with ID = "Player".


```JScript
<!<entity type="mdash"/>-Create an event handler. -->
<SCRIPT FOR = Player EVENT = PlayStateChange()>
   switch (Player.playState){

      case 3:

         if (Player.network.bitRate){

            BR.innerHTML = "Current Bit Rate: " + Player.network.bitRate;
            BR.innerHTML += " K bits/second";
          }

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
</dt> </dl>

 

 





