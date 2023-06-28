---
description: The cutpoint attribute specifies when a transition cuts from one source to the next, if the transition is rendered as a cut. The value is relative to the start of the transition.
ms.assetid: bdb0b8cd-025f-4b56-9cd4-f71c58ee809a
title: cutpoint Attribute
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# cutpoint Attribute

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `cutpoint` attribute specifies when a transition cuts from one source to the next, if the transition is rendered as a cut. The value is relative to the start of the transition.

## Possible Values

Must be a string with the format *hh:mm:ss.ff* format, where *hh* = hours, *mm* = minutes, *ss* = seconds, and *ff* = fractions of seconds. Example: 1:04:30.512. Leading units can be omitted. For example, 3:00 (three minutes) and 45 (45 seconds) are both valid.

## Applies To

[**transition**](transition-element.md)

## See also

<dl> <dt>

[XTL Attributes](xtl-attributes.md)
</dt> <dt>

[**IAMTimelineTrans::SetCutPoint**](iamtimelinetrans-setcutpoint.md)
</dt> </dl>

 

 



