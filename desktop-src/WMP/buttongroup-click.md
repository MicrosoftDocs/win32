---
title: BUTTONGROUP.click
description: The click method calls the onclick event handler defined for the BUTTONELEMENT with the specified index.
ms.assetid: a853e0a4-af4c-46c4-a3f7-d2a403eeb390
keywords:
- BUTTONGROUP.click Windows Media Player
topic_type:
- apiref
api_name:
- BUTTONGROUP.click
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# BUTTONGROUP.click

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **click** method calls the **onclick** event handler defined for the **BUTTONELEMENT** with the specified index.

``` syntax
        elementID.click(button)
```

## Parameters

<dl> <dt>

<span id="button"></span><span id="BUTTON"></span>*button*
</dt> <dd>

**Number** (**long**) containing the index of the **BUTTONELEMENT** with the **onclick** event handler to be called.

</dd> </dl>

## Return Value

This method does not return a value.

## Remarks

Use this method to provide an alternate means of running the code associated with a button contained within the **BUTTONGROUP**.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**BUTTONGROUP Element**](buttongroup-element.md)
</dt> <dt>

[**BUTTONELEMENT.index**](buttonelement-index.md)
</dt> </dl>

 

 





