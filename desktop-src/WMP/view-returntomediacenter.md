---
title: VIEW.returnToMediaCenter
description: The returnToMediaCenter method returns the user to the full mode of Windows Media Player.
ms.assetid: eebf0679-5704-498c-8eb3-f7710e0cb1fe
keywords:
- VIEW.returnToMediaCenter Windows Media Player
topic_type:
- apiref
api_name:
- VIEW.returnToMediaCenter
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# VIEW.returnToMediaCenter

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **returnToMediaCenter** method returns the user to the full mode of Windows Media Player.

``` syntax
        elementID.returnToMediaCenter()
```

## Parameters

This method has no parameters.

## Return Value

This method does not return a value.

## Examples


```JScript
<THEME>
  <VIEW id="View1" backgroundImage="greenstone.bmp">
    <BUTTON id="Open" image="Open.png" 
        onclick="jscript:View1.returnToMediaCenter()">
    </BUTTON>
  </VIEW>
</THEME>
```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**VIEW Element**](view-element.md)
</dt> </dl>

 

 





