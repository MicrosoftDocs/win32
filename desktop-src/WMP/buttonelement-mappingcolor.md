---
title: BUTTONELEMENT.mappingColor
description: The mappingColor attribute specifies or retrieves the color key that identifies this BUTTONELEMENT in the BUTTONGROUP.
ms.assetid: e7b1663c-3263-41d5-9a69-4cf1dcf0fc1f
keywords:
- BUTTONELEMENT.mappingColor Windows Media Player
topic_type:
- apiref
api_name:
- BUTTONELEMENT.mappingColor
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# BUTTONELEMENT.mappingColor

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **mappingColor** attribute specifies or retrieves the color key that identifies this **BUTTONELEMENT** in the **BUTTONGROUP**.

``` syntax
        elementID.mappingColor
```

## Possible Values

This attribute is a read/write **String** containing any Microsoft Internet Explorer color value. It has no default value.

## Remarks

This attribute specifies the color of the region in the button group **mappingImage** that corresponds to this button element. All clicks on this region are handled by this button element.

If an invalid color is specified, the **BUTTONELEMENT** is not activated.

## Examples

The following sample is a complete skin definition file that illustrates how some of the **BUTTONELEMENT** attributes are used. It can be found in the Samples directory that was installed with the SDK.


```
<THEME>
  <VIEW
    backgroundImage = "background.bmp"
    titleBar = "False"
  >
    <PLAYER
      URL = "https://proseware.com/mellow.wma"
    />
    <EFFECTS
      id = "myeffects"
      top = "25"
      left = "88"
      width = "180"
      height = "150"
    />
    <BUTTONGROUP
      mappingImage = "map.bmp"
      hoverImage = "hover.bmp"
    >
      <BUTTONELEMENT
        mappingColor = "#00FF00"
        upToolTip = "Next"
        onClick = "JScript:myeffects.next();"
      />
      <BUTTONELEMENT
        mappingColor = "#FF0000"
        upToolTip = "Previous"
        onClick = "JScript:myeffects.previous();"
      />
    </BUTTONGROUP>
  </VIEW>
</THEME>

```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**Color Reference**](color-reference.md)
</dt> <dt>

[**BUTTONELEMENT Element**](buttonelement-element.md)
</dt> <dt>

[**BUTTONGROUP.mappingImage**](buttongroup-mappingimage.md)
</dt> </dl>

 

 





