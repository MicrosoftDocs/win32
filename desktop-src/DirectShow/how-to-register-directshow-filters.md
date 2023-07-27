---
description: How to Register DirectShow Filters
ms.assetid: 2b6304c0-4b67-4723-94a0-7b1fff534f91
title: How to Register DirectShow Filters
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# How to Register DirectShow Filters

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This article describes how to make a Microsoft DirectShow filter self-registering. It contains the following sections:

-   [Layout of the Registry Keys](layout-of-the-registry-keys.md)
-   [Declaring Filter Information](declaring-filter-information.md)
-   [Declaring the Factory Template](declaring-the-factory-template.md)
-   [Implementing DllRegisterServer](implementing-dllregisterserver.md)
-   [Guidelines for Registering Filters](guidelines-for-registering-filters.md)
-   [Unregistering a Filter](unregistering-a-filter.md)

This article does not describe how to create a DLL for a DirectShow filter. For information on creating DLLs, see [How to Create a DirectShow Filter DLL](how-to-create-a-dll.md).

## Related topics

<dl> <dt>

[DirectShow and COM](directshow-and-com.md)
</dt> </dl>

 

 



