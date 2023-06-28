---
title: AmbientAttributes.tabStop
description: The tabStop attribute specifies or retrieves a value indicating whether the control is in the tabbing order. You set the tabbing order by placing the control in the overall script before or after other control tags.
ms.assetid: 3d4b7fe4-1032-44e1-bae5-f253d00881bf
keywords:
- AmbientAttributes.tabStop Windows Media Player
topic_type:
- apiref
api_name:
- AmbientAttributes.tabStop
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AmbientAttributes.tabStop

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **tabStop** attribute specifies or retrieves a value indicating whether the control is in the tabbing order. You set the tabbing order by placing the control in the overall script before or after other control tags.

``` syntax
        elementID.tabStop
```

## Possible Values

This attribute is a read/write **Boolean**.



| Value | Description                                                                                |
|-------|--------------------------------------------------------------------------------------------|
| true  | Control is in the tabbing order (control will have a tab stop: accessibility requirement). |
| false | Control is not in the tabbing order.                                                       |



 

## Remarks

The **tabStop** attribute is not applicable to the **EFFECTS** element.

The default value for this attribute is true for all elements except **AUTOMENU** and **TEXT**, which have a default value of false.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**Ambient Attributes**](ambient-attributes.md)
</dt> </dl>

 

 





