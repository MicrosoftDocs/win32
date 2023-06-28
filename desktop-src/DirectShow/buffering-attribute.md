---
description: The buffering attribute specifies the number of frames to render in advance during preview.
ms.assetid: c00fd24d-5c3c-44cf-93dd-9750f614d2af
title: buffering Attribute (Wmp.h)
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# buffering Attribute

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `buffering` attribute specifies the number of frames to render in advance during preview.

## Possible Values

The value must be a number greater than 1. The default value is 30.

## Applies To

[**group**](group-element.md)

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmp.h</dt> </dl> |



## See also

<dl> <dt>

[XTL Attributes](xtl-attributes.md)
</dt> <dt>

[**IAMTimelineGroup::SetOutputBuffering**](iamtimelinegroup-setoutputbuffering.md)
</dt> </dl>

 

 




