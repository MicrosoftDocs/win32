---
description: Working with Effects and Transitions
ms.assetid: 00e97d02-ff43-4e1f-9806-abaeb9288058
title: Working with Effects and Transitions
ms.topic: article
ms.date: 05/31/2018
---

# Working with Effects and Transitions

\[This API is not supported and may be altered or unavailable in the future.\]

Effects modify a single clip, track, or composition. Transitions create seques from one track or compositionsto another.

[DirectShow Editing Services](directshow-editing-services.md) uses DirectX Transform objects for its video transitions and video effects. For video transitions, use any 2-D two-input DirectX Transform object. For video effects, use any 2-D one-input DirectX Transform object. Microsoft no longer supports the development of third-party DirectX Transform objects. However, several are provided with DirectShow and others are provided with Microsoft Internet Explorer. For more information about the transitions provided with Internet Explorer, see [Visual Filters and Transitions Reference](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms532853(v=vs.85)).

For audio effects, you can use any DirectShow audio effect filter. DES also provides a [Volume Envelope Effect](volume-envelope-effect.md) for setting the volume on a track or clip. DES does not support audio transitions.

This section contains the following topics:

-   [Adding Effect and Transition Objects](adding-effect-and-transition-objects.md)
-   [Previewing Effects and Transitions](previewing-effects-and-transitions.md)
-   [Enumerating Effects and Transitions](enumerating-effects-and-transitions.md)
-   [Setting Properties on Effects and Transitions](setting-properties-on-effects-and-transitions.md)
-   [Transition Direction](transition-direction.md)

## Related topics

<dl> <dt>

[Using DirectShow Editing Services](using-directshow-editing-services.md)
</dt> </dl>

 

 
