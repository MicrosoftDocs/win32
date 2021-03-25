---
title: TEXT.value
description: The value attribute specifies or retrieves the text that is displayed in the Text control.
ms.assetid: dbc50be2-ee18-4661-a343-9e906879aba0
keywords:
- TEXT.value Windows Media Player
topic_type:
- apiref
api_name:
- TEXT.value
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# TEXT.value

The **value** attribute specifies or retrieves the text that is displayed in the Text control.

``` syntax
        elementID.value
```

## Possible Values

This attribute is a read/write **String**.

## Remarks

If the width of the Text control is insufficient to contain the text provided, the text is cropped, and an ellipsis is shown to illustrate the fact. If the **toolTip** attribute has not been set, the complete text will then appear as a ToolTip when the cursor hovers over the control.

If a width is not specified, the default width for the control is the width of the string.

If the height of the control is not specified, the default height is one line.

If the **wordWrap** attribute is set to true and the height of the control is enough to accommodate another line of text, the text wraps to a subsequent line. Wrapping only occurs between words. Line breaks may also be forced, as explained under **wordWrap**.

## Examples

The following sample is a complete skin definition file that illustrates how the attributes of the **TEXT** element are used. It can be found in the Samples directory that was installed with the SDK.


```C++
<THEME>
  <VIEW
    height = "175"
  >
    <TEXT 
      width = "150"
      fontSize = "30"
      hoverFontStyle = "Bold"
      hoverForegroundColor = "red"
      disabledForegroundColor = "#CCCCCC"
      justification = "Center"
      value = "Play"
      cursor = "hand"
      enabled = "wmpenabled:player.controls.play"
      onClick = "JScript: player.URL='https://proseware.com/laure.wma';"
    />
    <TEXT
      top = "50"
      width = "150"
      fontSize = "30"
      hoverFontStyle = "Bold"
      hoverForegroundColor = "red"
      disabledForegroundColor = "#CCCCCC"
      justification = "Center"
      value = "Stop"
      cursor = "hand"
      enabled = "wmpenabled:player.controls.stop"
      onClick = "JScript: player.controls.stop();"
    />
    <TEXT
      top = "100"
      width = "150"
      fontSize = "30"
      hoverFontStyle = "Bold"
      hoverForegroundColor = "red"
      justification = "Center"
      value = "Close"
      cursor = "hand"
      onClick = "JScript: view.close();"
    />
    <TEXT
      top = "30"
      left = "120"
      width = "200"
      fontSize = "20"
      fontStyle = "Underline"
      justification = "Center"
      value = "Volume"
    />
    <TEXT
      top = "60"
      left = "120"
      width = "200"
      fontSize = "40"
      justification = "Center"
      value = "wmpprop:player.settings.volume"
    />
    <TEXT
      top = "65"
      left = "142"
      width = "40"
      fontSize = "30"
      hoverFontStyle = "Bold"
      hoverForegroundColor = "red"
      justification = "Center"
      value = "-"
      cursor = "hand"
      toolTip = "decrease volume"
      onClick = "player.settings.volume = player.settings.volume - 5"
    />
    <TEXT
      top = "65"
      left = "260"
      width = "40"
      fontSize = "30"
      hoverFontStyle = "Bold"
      hoverForegroundColor = "red"
      justification = "Center"
      value = "+"
      cursor = "hand"
      toolTip = "increase volume"
      onClick = "player.settings.volume = player.settings.volume + 5"
    />
    <TEXT
      top = "155"
      width = "300"
      height = "30"
      fontFace = "System"
      backgroundColor = "blue"
      foregroundColor = "white"
      justification = "Center"
      scrolling = "true"
      scrollingAmount = "1"
      scrollingDelay = "50"
      value = "wmpprop:player.status"
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

[**TEXT Element**](text-element.md)
</dt> <dt>

[**TEXT.toolTip**](text-tooltip.md)
</dt> <dt>

[**TEXT.wordWrap**](text-wordwrap.md)
</dt> </dl>

 

 





