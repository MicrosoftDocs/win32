---
title: AmbientAttributes.zIndex
description: The zIndex attribute specifies or retrieves the order in which the control is rendered.
ms.assetid: b05c9efc-5d1d-4cba-89f4-b4200ce99e09
keywords:
- AmbientAttributes.zIndex Windows Media Player
topic_type:
- apiref
api_name:
- AmbientAttributes.zIndex
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AmbientAttributes.zIndex

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **zIndex** attribute specifies or retrieves the order in which the control is rendered.

``` syntax
        elementID.zIndex
```

## Possible Values

This attribute is a read/write **Number** (**long**) with a default value of zero. The range is that of a signed long integer.

## Remarks

The background bitmap of a **VIEW** or **SUBVIEW** has a fixed z index of zero. If you want a control to be behind the background, the **zIndex** must be set to a negative number.

The z index of a **VIEW** or **SUBVIEW** is an absolute index, while the z index of a control is relative to the z index of the **VIEW** or **SUBVIEW** that contains it.

The **zIndex** attribute is not supported by the **BROWSER** and **PLAYLIST** elements. It will not work with the **VIDEO** element if *VIDEO*.**windowless** is set to false, nor with the **EFFECTS** element if **EFFECTS**.**windowed** is set to true.

**BUTTONELEMENT** elements use the **zIndex** of their **BUTTONGROUP**.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**Ambient Attributes**](ambient-attributes.md)
</dt> </dl>

 

 





