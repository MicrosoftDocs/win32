---
description: Processing Data
ms.assetid: 823615df-ce50-4e20-957a-f83d3be66658
title: Processing Data
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Processing Data

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

**Parsing Media Data**

If your filter parses media data, do not trust headers or other self-describing data in the content. For example, do not trust size values that appear in AVI RIFF chunks or MPEG packets. Common examples of this kind of error include:

-   Reading *N* bytes of data, where the value of *N* came from the content, without checking *N* against the actual size of your buffer.
-   Jumping to a byte offset within a buffer, without verifying that the offset falls within the buffer.

Another common class of errors involves not validating format descriptions that are found in the content. For example:

-   A [**BITMAPINFOHEADER**](/windows/win32/api/wingdi/ns-wingdi-bitmapinfoheader) structure can be followed by a color table. The **BITMAPINFO** structure is defined as a **BITMAPINFOHEADER** structure followed by an array of **RGBQUAD** values that make up the color table. The size of the array is determined by the value of **biClrUsed**. Never copy a color table into a **BITMAPINFO** without first checking the size of the buffer that was allocated for the **BITMAPINFO** structure.
-   A [**WAVEFORMATEX**](/previous-versions/dd757713(v=vs.85)) structure might have extra format information appended to the structure. The **cbSize** member specifies the size of the extra information.

During pin connection, a filter should verify that all format structures are well-formed and contain reasonable values. If not, reject the connection. In the code that validates the format structure, be especially careful about arithmetic overflow. For example, in a **BITMAPINFOHEADER**, the width and height are 32-bit **long** values but the image size (which is a function of the product of the two) is only a **DWORD** value.

If format data from the source is larger than your allocated buffer, do not truncate the source data in order to copy it into your buffer. Doing so can create a structure whose implicit size is larger than its actual size. For example, a bitmap header might specify a palette table which no longer exists. Instead, reallocate the buffer or simply fail the connection.

**Errors During Streaming**

When the graph is running, if your filter receives malformed content, it should terminate streaming. Do the following:

-   Return an error code from **Receive**.
-   Call [**IPin::EndOfStream**](/windows/desktop/api/Strmif/nf-strmif-ipin-endofstream) on the downstream filter.
-   Call [**CBaseFilter::NotifyEvent**](cbasefilter-notifyevent.md) to post an [**EC\_ERRORABORT**](ec-errorabort.md) event.

**Format Changes**

Several mechanisms exist for filters to change formats mid-stream. Each of them involves more than one step, which creates the potential for false acceptances. If your filter gets a request for a dynamic format change, then it must either reject the request, or else honor the new format when it arrives. Similarly, never switch formats unless the other filter agrees. For more information, see [Dynamic Format Changes](dynamic-format-changes.md).

 

 
