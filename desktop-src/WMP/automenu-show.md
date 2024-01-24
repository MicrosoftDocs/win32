---
title: AUTOMENU.show
description: The show method displays the Quick Access Panel.
ms.assetid: c4f2b106-180a-4526-af9b-6ce54c083578
keywords:
- AUTOMENU.show Windows Media Player
topic_type:
- apiref
api_name:
- AUTOMENU.show
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AUTOMENU.show

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **show** method displays the **Quick Access Panel**.

``` syntax
        elementID.show("Play")
        
```

## Parameters

<dl> <dt>

<span id="_Play_"></span><span id="_play_"></span><span id="_PLAY_"></span>*"Play"*
</dt> <dd>

Always specify this value.

</dd> </dl>

## Return Value

This method does not return a value.

## Remarks

The **Quick Access Panel** appears at the location specified by the **left** and **top** attributes of the **AUTOMENU** element.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**AUTOMENU Element**](automenu-element.md)
</dt> </dl>

 

 





