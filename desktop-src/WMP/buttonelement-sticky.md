---
title: BUTTONELEMENT.sticky
description: The sticky attribute specifies or retrieves a value indicating whether the BUTTONELEMENT is a toggle, that is, whether it is a two-state or single-state button.
ms.assetid: a7e74f70-9fa6-45a1-ab65-2db107e13551
keywords:
- BUTTONELEMENT.sticky Windows Media Player
topic_type:
- apiref
api_name:
- BUTTONELEMENT.sticky
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# BUTTONELEMENT.sticky

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **sticky** attribute specifies or retrieves a value indicating whether the **BUTTONELEMENT** is a toggle, that is, whether it is a two-state or single-state button.

``` syntax
        elementID.sticky
```

## Possible Values

This attribute is a read/write **Boolean**.



| Value | Description                               |
|-------|-------------------------------------------|
| true  | **BUTTONELEMENT** is sticky.              |
| false | Default. **BUTTONELEMENT** is not sticky. |



 

## Remarks

If the **sticky** attribute is set to true, the button element will change to the down state when clicked and will remain in that state until clicked again. When the button element is in the down state, the **down** attribute will be true and the appropriate portion of the button group **downImage** will be displayed.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**BUTTONELEMENT Element**](buttonelement-element.md)
</dt> <dt>

[**BUTTONELEMENT.down**](buttonelement-down.md)
</dt> <dt>

[**BUTTONGROUP.downImage**](buttongroup-downimage.md)
</dt> </dl>

 

 





