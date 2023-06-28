---
description: The composite element defines a composition, a container object for tracks and other nested compositions.
ms.assetid: 7551da3a-1da6-426a-ba9d-f715df53718f
title: composite Element
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# composite Element

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `composite` element defines a composition, a container object for tracks and other nested compositions.

## Attributes

[**lock**](lock-attribute.md), [**mute**](mute-attribute.md), [**userdata**](userdata-attribute.md), [**userid**](userid-attribute.md), [**username**](username-attribute.md)

## Parent/Child Information



| Label | Value |
|----------|-------------------------------------------------------------------------------------------------------------------------|
| Parent   | `composite`, [**group**](group-element.md)                                                                             |
| Children | `composite`, [**effect**](effect-element.md), [**track**](track-element.md), [**transition**](transition-element.md) |



 

## Remarks

Within a `composite` element, the priority of nested layers is determined implicitly by the order in which they appear within the element. The first layer has priority 0, and subsequent layers have increasing priority values.

## Examples


```XML
<composite> </composite>
```



## See also

<dl> <dt>

[XTL Elements](xtl-elements.md)
</dt> </dl>

 

 



