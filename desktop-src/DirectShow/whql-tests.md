---
description: WHQL tests
ms.assetid: ca24fe89-d2fe-4aa9-8643-319ed16ba1a3
title: WHQL tests
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# WHQL tests

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Test various combinations of PanScan/Letterbox and 704/720 wide images:

-   16x9 video (704 or 720 wide), 16x9 subpicture (720 wide)
-   16x9 video (704 or 720 wide) Letterbox, 4x3 subpicture
-   16x9 video (704 or 720 wide) PanScan, 4x3 subpicture
-   4x3 video (704 or 720 wide), 4x3 subpicture

 

 



