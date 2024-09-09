---
description: The param element specifies the value of a property on a transition, effect, or other subobject.
ms.assetid: a727c47c-b925-436c-b1e8-d5f407120dc9
title: param Element (DirectShow)
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# param Element

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `param` element specifies the value of a property on a transition, effect, or other subobject.

## Attributes

[**name**](name-attribute.md), [**value**](value-attribute.md)

## Parent/Child Information



| Label | Value |
|----------|----------------------------------------------------------------------------------------------------------|
| Parent   | [**clip**](clip-element.md), [**effect**](effect-element.md), [**transition**](transition-element.md) |
| Children | [**at**](at-element.md), [**linear**](linear-element.md)                                               |



 

## Remarks

The **value** attribute specifies the value of the property at the start of the transition or effect. Use the **at** or **linear** element to specify changing values. If the **param** element contains no **at** or **linear** elements, the value remains constant over the duration of the effect or transition.

> [!Note]  
> A **param** element inside a **clip** element cannot contain **at** or **linear** elements.

 

Many transitions support a standard **Progress** property that ranges from 0 to 1.0, indicating what percentage of the transition is reflected in the output. At **Progress** = 0.0, the transition is at the beginning of its sequence (entirely the first video image). At **Progress** = 0.5, the transition is half complete. (For example, in a wipe, at **Progress** = 0.5 the transition boundary is in the center of the image) At **Progress** = 1.0, the transition is complete (entirely the second image). By default, transitions go from **Progress** = 0.0 at the start of the transition to **Progress** = 1.0 at the end.

Other properties are usually specific to one particular transition or effect. For example, the wipe transition supports a **GradientSize** property that controls the width of the transition area.

To run a transition backward, set the **Progress** property to 1.0 at the start of the transition, and use the **linear** element to change the value to 0.0, as shown in the following example:


```
<transition clsid="{af279b30-86eb-11d1-81bf-0000f87557db}" start="0" stop="6">
    <param name="progress" value="1.0">
        <linear time="6" value="0.0" />
    </param>
</transition>
```



## Examples


```XML
<param name="progress" value="1.0" />
```



## See also

<dl> <dt>

[XTL Elements](xtl-elements.md)
</dt> </dl>

 

 



