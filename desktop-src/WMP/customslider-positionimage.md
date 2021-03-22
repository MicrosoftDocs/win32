---
title: CUSTOMSLIDER.positionImage
description: The positionImage attribute specifies or retrieves the image map used to determine which position image from the image file to display.
ms.assetid: 7e99dc21-ebba-438a-a983-190dbe429578
keywords:
- CUSTOMSLIDER.positionImage Windows Media Player
topic_type:
- apiref
api_name:
- CUSTOMSLIDER.positionImage
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# CUSTOMSLIDER.positionImage

The **positionImage** attribute specifies or retrieves the image map used to determine which position image from the image file to display.

``` syntax
        elementID.positionImage
```

## Possible Values

This attribute is a read/write **String** containing the name of an image file.

## Remarks

This attribute is required and must be specified.

The **positionImage** is not displayed. Instead, it serves as a map defining the clickable regions of the displayed image. The displayed image is one of the sub-images of the image file and represents the actual state of the slider. The **positionImage** includes a number of gray scale regions equal to the number of these sub-images. The sub-images must have the same dimensions as the **positionImage** or the custom slider will not work correctly.

Any region that is not in gray scale will not be clickable. The clickable regions should be set to color values that range evenly across the gray scale spectrum from black to white, with the first region being pure black and the last region being pure white. The color values of each successive region should be incremented by a value equal to 255 divided by the total number of regions minus one, rounding to the nearest whole number.

For example, if there are six regions, the increment would be 51 (255 divided by 5), and the six gray scale values would be 0, 51, 102, 153, 204, and 255. The hexadecimal color values for the six regions would then be \#000000, \#333333, \#666666, \#999999, \#CCCCCC, and \#FFFFFF.

In this way, the regions will have a sequence dictated by their gray scale color values, and this sequence will correspond to the sequence of sub-images in the image file. When one of the regions is clicked, the corresponding sub-image is shown and the **value** of the custom slider is updated accordingly.

The supported image file types are BMP, JPG, PNG, and GIF (not including animated GIFs).

## Examples

The following is an example of a custom slider **positionImage**. The corresponding image is shown in the example section of the **image** property.

![sample positionimage graphic](images/dialmap.png)

The following code illustrates the use of **CUSTOMSLIDER** attributes.


```XML
<THEME>
  <VIEW
    backgroundImage = "background.bmp"
    titleBar = "False"
  >

    <PLAYER
      URL = "https://proseware.com/mellow.wma"
    >
      <CONTROLS
        currentPosition_onchange = "myslider.value = player.controls.currentPosition;"
      />
    </PLAYER>

    <SLIDER
      id = "myslider"
      min = "0"
      max = "wmpprop:player.currentMedia.duration"
      onmouseup = "player.controls.currentPosition = myslider.value; "
      tooltip = "current position"
      height = "10"
      width = "180"
      top = "150"
      left = "88"
      backgroundColor = "red"
      foregroundColor = "blue"
      thumbImage = "thumb.bmp"
    />

    <CUSTOMSLIDER
      top = "120"
      left = "23"
      min = "0"
      max = "100"
      borderSize = "10"
      toolTip = "volume control"
      image = "dial.bmp"
      transparencyColor = "#00FFFF"
      positionImage = "dialmap.bmp"
      enabled = "true"
      value = "wmpprop:player.settings.volume"
      value_onchange = "player.settings.volume = value"
    />

    <EFFECTS
      id = "myeffects"
      top = "25"
      left = "88"
      width = "180"
      height = "100"
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

[**CUSTOMSLIDER Element**](customslider-element.md)
</dt> <dt>

[**CUSTOMSLIDER.image**](customslider-image.md)
</dt> </dl>

 

 





