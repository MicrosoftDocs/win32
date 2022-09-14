---
title: EQUALIZERSETTINGS.crossFade
description: The crossFade attribute specifies or retrieves a value indicating whether cross-fade is enabled.
ms.assetid: 6c5a31f3-982e-4660-80ff-30b7a4290a15
keywords:
- EQUALIZERSETTINGS.crossFade Windows Media Player
topic_type:
- apiref
api_name:
- EQUALIZERSETTINGS.crossFade
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# EQUALIZERSETTINGS.crossFade

The **crossFade** attribute specifies or retrieves a value indicating whether cross-fade is enabled.

``` syntax
        elementID.crossFade
```

## Possible Values

This attribute is a read/write **Boolean**.



| Value | Description                      |
|-------|----------------------------------|
| true  | Cross-fade is enabled.           |
| false | Default. Cross-fade is disabled. |



 

## Remarks

Cross-fade is an audio processing feature that gradually decreases the volume of one media item near the end of its playback while simultaneously starting playback of the next media item at minimum volume and gradually increasing it to normal volume. The overlap between the start of the second media item and the end of the first media item is specified by the **crossFadeWindow** attribute.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**EQUALIZERSETTINGS Element**](equalizersettings-element.md)
</dt> <dt>

[**EQUALIZERSETTINGS.crossFadeWindow**](equalizersettings-crossfadewindow.md)
</dt> </dl>

 

 





