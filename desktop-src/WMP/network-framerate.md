---
title: Network.frameRate
description: The frameRate property retrieves the current video frame rate in frames per hundred seconds. For example, a value of 2998 indicates 29.98 frames per second.
ms.assetid: ee30dce5-a42e-4be5-ab4b-0d5f8869d23a
keywords:
- Network.frameRate Windows Media Player
topic_type:
- apiref
api_name:
- Network.frameRate
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Network.frameRate

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **frameRate** property retrieves the current video frame rate in frames per hundred seconds. For example, a value of 2998 indicates 29.98 frames per second.

## Syntax

*player*.*network*.**frameRate**

## Possible Values

This property is a read-only **Number** (**long**).

## Examples

The following JScript example uses *Network*.**frameRate** to display the current frame rate. The information is displayed in an HTML DIV created with ID = "FR". The **Player** object was created with ID = "Player".


```JScript
<!-- Create an event handler for play state. -->
<SCRIPT FOR = Player EVENT = PlayStateChange(NewState)>
   switch (NewState){
      case 3:
          // Display the current frame rate.
          FR.innerHTML = "Frame Rate: ";
          FR.innerHTML += Player.network.frameRate;
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

[**Network.encodedFrameRate**](network-encodedframerate.md)
</dt> </dl>

 

 





