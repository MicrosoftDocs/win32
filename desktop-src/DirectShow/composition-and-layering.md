---
description: Composition and Layering
ms.assetid: c1aefd92-b47f-4af1-8299-9ba401ad5fe8
title: Composition and Layering
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Composition and Layering

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

\[This API is not supported and may be altered or unavailable in the future.\]

In a collection of tracks, the first track has the lowest priority (priority 0) and each subsequent track has a priority one level higher. At each priority level, the source clips in that track hide the source clips in the tracks below it, unless that layer also contains a transition. Thus you can imagine DES making several passes when it renders.

First, it renders track 0. There is nothing "under" Track 0, so empty regions are rendered as a solid black image. Transitions in this layer occur between the black image and track 0 or vice versa. DES lays track 1 on top of track 0, generating any transitions between the two tracks. The result is the composite of the two tracks. Next, it places track 2 onto this composite. Transitions at this layer occur between the composite and track 2. The process continues until the last (highest-priority) track is put down.

When several tracks are composited together, they behave like a single track (called a virtual track). The composition object encapsulates this behavior, making complex transitions possible. For example, one video clip can wipe to a second clip, while the composite (both clips plus the wipe) fades to a third clip.

## Related topics

<dl> <dt>

[Getting Started with DirectShow Editing Services](getting-started-with-directshow-editing-services.md)
</dt> </dl>

 

 



