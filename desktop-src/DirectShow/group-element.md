---
description: The group element defines a group, the top-level object in a timeline.
ms.assetid: db2f1fdd-bcb1-4401-91f4-5e167e4da215
title: group Element (DirectShow)
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# group Element

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The **group** element defines a group, the top-level object in a timeline.

## Attributes

[**bitdepth**](bitdepth-attribute.md), [**buffering**](buffering-attribute.md), [**framerate**](framerate-attribute.md), [**height**](height-attribute.md), [**lock**](lock-attribute.md), [**mute**](mute-attribute.md), [**name**](name-attribute.md), [**previewmode**](previewmode-attribute.md), [**samplingrate**](samplingrate-attribute.md), [**type**](type-attribute.md), [**userdata**](userdata-attribute.md), [**userid**](userid-attribute.md), [**username**](username-attribute.md), [**width**](width-attribute.md)

## Parent/Child Information



| Label | Value |
|----------|----------------------------------------------------------------------------------------------------------|
| Parent   | [**timeline**](timeline-element.md)                                                                     |
| Children | [**composite**](composite-element.md), [**effect**](effect-element.md), [**track**](track-element.md) |



 

## Remarks

Within a `group` element, the priority of nested layers is determined implicitly by the order they appear within the element. The first layer has priority 0, and subsequent layers have increasing priority values.

## Examples


```XML
<group type="video" width="640" height="480" framerate="30"> </group>
```



## See also

<dl> <dt>

[XTL Elements](xtl-elements.md)
</dt> </dl>

 

 



