---
title: BUTTONGROUP.getButton
description: The getButton method retrieves the BUTTONELEMENT with the specified index.
ms.assetid: 49e1cf61-f5de-430d-8492-bd49b186f5ea
keywords:
- BUTTONGROUP.getButton Windows Media Player
topic_type:
- apiref
api_name:
- BUTTONGROUP.getButton
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# BUTTONGROUP.getButton

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **getButton** method retrieves the **BUTTONELEMENT** with the specified index.

``` syntax
        elementID.getButton(button)
```

## Parameters

<dl> <dt>

<span id="button"></span><span id="BUTTON"></span>*button*
</dt> <dd>

**Number** (**long**) containing the index of the **BUTTONELEMENT** to retrieve.

</dd> </dl>

## Return Value

This method returns an Object corresponding to a **BUTTONELEMENT** element.

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

 

 





