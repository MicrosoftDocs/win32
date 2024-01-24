---
description: Saving and Restoring DvdState Objects
ms.assetid: 65180fe2-0faf-47c0-bccd-728e01056c46
title: Saving and Restoring DvdState Objects
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Saving and Restoring DvdState Objects

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

[**IDvdState**](/windows/desktop/api/Strmif/nn-strmif-idvdstate) objects enable applications to save a snapshot of the user session, including information such as the current location on the disc, the parental level of the person who is viewing, the selected audio and subpicture streams, and so on. This means that users can save their place on a DVD-Video disc and watch it at a later time.

Applications cannot create DvdState objects. These objects are created internally by the DVD Navigator when an application calls [**IDvdInfo2::GetState**](/windows/desktop/api/Strmif/nf-strmif-idvdinfo2-getstate). DvdState objects expose the [**IDvdState**](/windows/desktop/api/Strmif/nn-strmif-idvdstate) interface to allow applications to query for certain information.

In the DVD sample application, the **CDvdCore::RestoreBookmark** and **CDvdCore::SaveBookmark** functions show how to save and retrieve DvdState objects.

## Related topics

<dl> <dt>

[DVD Applications](dvd-applications.md)
</dt> </dl>

 

 



