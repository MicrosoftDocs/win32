---
title: SLIDER.foregroundProgress
description: The foregroundProgress attribute specifies or retrieves the current position of the foreground progress bar as a percentage of the slider area.
ms.assetid: 1218ca5a-445c-441b-aa62-74a184a25c2d
keywords:
- SLIDER.foregroundProgress Windows Media Player
topic_type:
- apiref
api_name:
- SLIDER.foregroundProgress
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# SLIDER.foregroundProgress

The **foregroundProgress** attribute specifies or retrieves the current position of the foreground progress bar as a percentage of the slider area.

``` syntax
        elementID.foregroundProgress
```

## Possible Values

This attribute is a read/write **Number** (**float**) ranging from 0 to 100.

## Remarks

This attribute is used primarily to track the download progress of a media file while simultaneously tracking the current play position of the file using the **value** attribute. The position of the slider thumb is constrained to the area of the foreground progress. This allows interactive seeking to take place only within the available portion of a downloading file.

To use this functionality, the **useForegroundProgress** attribute must be set to true.

## Examples


```C++
<SLIDER
  id="seek"
  backgroundColor="blue"
  foregroundColor="red"
  thumbImage="seekthumb.bmp"
  min="0"
  max="wmpprop:player.currentMedia.duration"
  value="wmpprop:player.controls.currentPosition"
  useForegroundProgress="true"
  foregroundProgress="wmpprop:player.network.downloadProgress"
  ondragend="player.controls.currentposition=value"
/>

```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**SLIDER Element**](slider-element.md)
</dt> <dt>

[**SLIDER.min**](slider-min.md)
</dt> <dt>

[**SLIDER.max**](slider-max.md)
</dt> <dt>

[**SLIDER.useForegroundProgress**](slider-useforegroundprogress.md)
</dt> <dt>

[**SLIDER.value**](slider-value.md)
</dt> </dl>

 

 





