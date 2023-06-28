---
description: Media types (DirectShow)
ms.assetid: 'c8efe9e6-7d1d-4ec2-ab1b-70ee0798a6a3'
title: Media Types
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Media types (DirectShow)

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Microsoft® DirectShow® uses the [**AM\_MEDIA\_TYPE**](/windows/win32/api/strmif/ns-strmif-am_media_type) structure to describe media samples. This structure includes **GUID** members for major type, subtype, and format type. This section summarizes the major type and subtype GUIDs that are defined for DirectShow. Third-party filters may define their own media type GUIDs.

-   [**Major Types**](major-types.md)
-   [**Audio Subtypes**](audio-subtypes.md)
-   [**BDA Media Types**](bda-media-types.md)
-   [**DVD Media Types**](dvd-media-types.md)
-   [**Line 21 Media Types**](line-21-media-types.md)
-   [**MPEG-1 Media Types**](mpeg-1-media-types.md)
-   [MPEG-2 Media Types](mpeg-2-media-types.md)
-   [**Stream Subtypes**](stream-subtypes.md)
-   [VBI Media Types](vbi-media-types.md)
-   [Video Subtypes](video-subtypes.md)

 

 



