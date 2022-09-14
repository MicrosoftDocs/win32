---
title: Network.encodedFrameRate
description: The encodedFrameRate property retrieves the video frame rate specified by the content author in frames per second.
ms.assetid: 7dad5c90-f750-48d7-9dda-3fc07394edcc
keywords:
- Network.encodedFrameRate Windows Media Player
topic_type:
- apiref
api_name:
- Network.encodedFrameRate
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Network.encodedFrameRate

The **encodedFrameRate** property retrieves the video frame rate specified by the content author in frames per second.

## Syntax

*player*.*network*.**encodedFrameRate**

## Possible Values

This property is a read-only **Number** (**long**).

## Examples

The following JScript example uses *Network*.**encodedFrameRate** to display the frame rate specified when the file was encoded. The information is displayed in an HTML DIV created with ID = "FR". The **Player** object was created with ID = "Player".


```JScript
<!-- Create an event handler for play state. -->
<SCRIPT FOR = Player EVENT = PlayStateChange(NewState)>
   switch (NewState){
      case 3:
          // Display the encoded frame rate.
          FR.innerHTML = "Encoded Frame Rate: ";
          FR.innerHTML += Player.network.encodedFrameRate;
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

[**Network.frameRate**](network-framerate.md)
</dt> </dl>

 

 





