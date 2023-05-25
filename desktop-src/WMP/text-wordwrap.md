---
title: TEXT.wordWrap
description: The wordWrap attribute specifies or retrieves a value indicating whether word wrap is enabled or disabled.
ms.assetid: 3bb127d8-42f1-4167-986a-d41690cb5647
keywords:
- TEXT.wordWrap Windows Media Player
topic_type:
- apiref
api_name:
- TEXT.wordWrap
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# TEXT.wordWrap

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **wordWrap** attribute specifies or retrieves a value indicating whether word wrap is enabled or disabled.

``` syntax
        elementID.wordWrap
```

## Possible Values

This attribute is a read/write **Boolean**.



| Value | Description                                                                                       |
|-------|---------------------------------------------------------------------------------------------------|
| true  | Word wrap is enabled.                                                                             |
| false | Default. Word wrap is disabled. If the text does not fit within the control, the text is cropped. |



 

## Remarks

The Text control does not split words apart. If a word extends beyond the width of the control, word wrap is employed to move the word to the next line. If a single word is longer than the control width, that word is clipped and occupies a single line.

If the **width** attribute is not specified, **wordWrap** is ignored and the Text control will resize rather than wrapping the text.

If line breaks are desired in particular locations, they must be explicitly specified in **value** using "&\#13;" or "\\r". If the latter form is used when specifying the value directly, the string must be prefixed with "JScript:" and the actual value must be surrounded by single quotes, as shown below. This is not necessary if the value is set dynamically from within an event handler.

If **wordWrap** is set to true and **toolTip** is not specified, the ToolTip will display the full text of the **value** attribute. If no ToolTip is desired, set **toolTip** to "" (empty string).

## Examples


```C++
<THEME>
  <VIEW>
    <TEXT
      width = "50"
      height = "200"
      wordWrap = "true"
      backgroundColor = "blue"
      foregroundColor = "white"
      value = "This is a test.&#13;&#13;It is only a test."
    />
    <TEXT
      width = "50"
      height = "200"
      left = "100"
      wordWrap = "true"
      backgroundColor = "green"
      foregroundColor = "white"
      value = "JScript:'This is a test.\r\rIt is only a test.'"
    />
  </VIEW>
</THEME>

```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**AmbientAttributes.width**](ambientattributes-width.md)
</dt> <dt>

[**TEXT Element**](text-element.md)
</dt> <dt>

[**TEXT.toolTip**](text-tooltip.md)
</dt> <dt>

[**TEXT.value**](text-value.md)
</dt> </dl>

 

 





