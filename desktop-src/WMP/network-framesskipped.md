---
title: Network.framesSkipped
description: The framesSkipped property retrieves the total number of frames skipped during playback.
ms.assetid: fc7561a4-1e52-4192-b8df-ed2fb407fb78
keywords:
- Network.framesSkipped Windows Media Player
topic_type:
- apiref
api_name:
- Network.framesSkipped
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Network.framesSkipped

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **framesSkipped** property retrieves the total number of frames skipped during playback.

## Syntax

*player*.*network*.**framesSkipped**

## Possible Values

This property is a read-only **Number** (**long**).

## Examples

The following JScript example uses *Network*.**framesSkipped** to display the total number of frames skipped during playback when the user clicks a button. The information is displayed in an HTML DIV created with ID = "FS". The **Player** object was created with ID = "Player".


```JScript
<!-- Create an HTML BUTTON element. -->
<INPUT TYPE = "BUTTON" ID = "skipped" NAME = "skipped"
       VALUE = "Count frames skipped" 
       onClick = "FS.innerHTML = 'Frames skipped: ' + Player.network.framesSkipped;">

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

 

 





