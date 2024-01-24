---
title: Player.close method
description: The close method releases Windows Media Player resources.
ms.assetid: '15bd5a05-dbfa-4bea-90c2-afd9f69631e0'
keywords:
- close method Windows Media Player
- close method Windows Media Player , Player class
- Player class Windows Media Player , close method
topic_type:
- apiref
api_name:
- Player.close
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Player.close method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **close** method releases Windows Media Player resources.

## Syntax


```JScript
Player.close()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

This method closes the current digital media file, not Windows Media Player itself.

## Examples

The following example creates an HTML BUTTON element that, when clicked, stops playback in Windows Media Player and releases the resources in use. The **Player** object was created with ID = "Player".


```JScript
<INPUT  TYPE = "BUTTON"  ID = "CLOSEIT"  VALUE = "Close it"  onClick = "

        /* Close the Player object. */
        Player.close();
">

```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Player Object**](player-object.md)
</dt> </dl>

 

 





