---
description: DMO Functions
ms.assetid: 0a380dc0-23f0-4ef0-898a-3b5afddf5eaa
title: DMO Functions
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DMO Functions

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This section describes the Microsoft DirectX Media Object (DMO) functions.



| Function                                             | Description                                                   |
|------------------------------------------------------|---------------------------------------------------------------|
| [**DMOEnum**](/previous-versions/windows/desktop/api/Dmoreg/nf-dmoreg-dmoenum)                           | Enumerates DMOs listed in the registry.                       |
| [**DMOGetName**](/previous-versions/windows/desktop/api/Dmoreg/nf-dmoreg-dmogetname)                     | Retrieves the name of a DMO from the registry.                |
| [**DMOGetTypes**](/previous-versions/windows/desktop/api/Dmoreg/nf-dmoreg-dmogettypes)                   | Retrieves the media types registered for a DMO.               |
| [**DMORegister**](/previous-versions/windows/desktop/api/Dmoreg/nf-dmoreg-dmoregister)                   | Registers a DMO.                                              |
| [**DMOUnregister**](/previous-versions/windows/desktop/api/Dmoreg/nf-dmoreg-dmounregister)               | Unregisters a DMO.                                            |
| [**MoCopyMediaType**](/previous-versions/windows/desktop/api/Dmort/nf-dmort-mocopymediatype)           | Copies one media type structure to another.                   |
| [**MoCreateMediaType**](/previous-versions/windows/desktop/api/Dmort/nf-dmort-mocreatemediatype)       | Allocates a new media type structure.                         |
| [**MoDeleteMediaType**](/previous-versions/windows/desktop/api/Dmort/nf-dmort-modeletemediatype)       | Deletes a media type structure that was previously allocated. |
| [**MoDuplicateMediaType**](/previous-versions/windows/desktop/api/Dmort/nf-dmort-moduplicatemediatype) | Duplicates a media type structure.                            |
| [**MoFreeMediaType**](/previous-versions/windows/desktop/api/Dmort/nf-dmort-mofreemediatype)           | Frees the allocated members of a media type structure.        |
| [**MoInitMediaType**](/previous-versions/windows/desktop/api/Dmort/nf-dmort-moinitmediatype)           | Initializes a media type structure.                           |



 

## Related topics

<dl> <dt>

[DMO Reference](dmo-reference.md)
</dt> </dl>

 

 



