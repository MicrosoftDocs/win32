---
title: BUTTONGROUP.radio
description: The radio attribute specifies or retrieves a value indicating whether the BUTTONGROUP is composed of radio buttons.
ms.assetid: f84479f8-af4f-4ca8-991e-1c2ab39d7110
keywords:
- BUTTONGROUP.radio Windows Media Player
topic_type:
- apiref
api_name:
- BUTTONGROUP.radio
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# BUTTONGROUP.radio

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **radio** attribute specifies or retrieves a value indicating whether the **BUTTONGROUP** is composed of radio buttons.

``` syntax
        elementID.radio
```

## Possible Values

This attribute is a read/write **Boolean**.



| Value | Description                                      |
|-------|--------------------------------------------------|
| true  | The **BUTTONGROUP** is radio style.              |
| false | Default. The **BUTTONGROUP** is not radio style. |



 

## Remarks

If **radio** is set to true, all the **BUTTONELEMENT** elements in the **BUTTONGROUP** will be sticky, but only one button at a time will be in the down state.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**BUTTONELEMENT.sticky**](buttonelement-sticky.md)
</dt> <dt>

[**BUTTONGROUP Element**](buttongroup-element.md)
</dt> </dl>

 

 





