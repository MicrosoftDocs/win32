---
description: How to Create a DirectShow Filter DLL
ms.assetid: 142bc8a2-240d-418f-9374-62d34a76ec38
title: How to Create a DirectShow Filter DLL
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# How to Create a DirectShow Filter DLL

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This article describes how to implement a component as a dynamic-link library (DLL) in Microsoft DirectShow. This article is a continuation from [How to Implement IUnknown](how-to-implement-iunknown.md), which describes how to implement the **IUnknown** interface by deriving your component from the [**CUnknown**](cunknown.md) base class.

This article contains the following sections.

-   [Class Factories and Factory Templates](class-factories-and-factory-templates.md)
-   [Factory Template Array](factory-template-array.md)
-   [DLL Functions](dll-functions.md)

Registering a DirectShow filter (as opposed to a generic COM object) requires some additional steps that are not covered in this article. For information on registering filters, see [How to Register DirectShow Filters](how-to-register-directshow-filters.md).

## Related topics

<dl> <dt>

[DirectShow and COM](directshow-and-com.md)
</dt> </dl>

 

 



