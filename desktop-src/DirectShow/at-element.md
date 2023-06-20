---
description: The at element defines the value of a param element at a particular time, relative to the start of the transition or effect that contains the parameter.
ms.assetid: 523aa25c-790b-4532-9c69-76544235bdfe
title: at Element
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# at Element

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `at` element defines the value of a [**param**](param-element.md) element at a particular time, relative to the start of the transition or effect that contains the parameter. The `at` element causes the parameter to jump abruptly to the new value at the given time. For a smooth progression to a new value, use the [**linear**](linear-element.md) element.

## Attributes

[**time**](time-attribute.md), [**value**](value-attribute.md)

## Parent/Child Information



| Label | Value |
|----------|--------------------------------|
| Parent   | [**param**](param-element.md) |
| Children | None                           |



 

## Examples


```XML
<at time="1" value="0.5" />
```



## See also

<dl> <dt>

[XTL Elements](xtl-elements.md)
</dt> </dl>

 

 



