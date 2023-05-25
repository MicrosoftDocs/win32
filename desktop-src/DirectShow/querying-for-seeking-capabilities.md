---
description: Querying for Seeking Capabilities
ms.assetid: d1d8c708-75f2-4dc7-a33a-8dd2cea0ee00
title: Querying for Seeking Capabilities
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Querying for Seeking Capabilities

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Microsoft® DirectShow® supports seeking through the [**IMediaSeeking**](/windows/desktop/api/Strmif/nn-strmif-imediaseeking) interface. The Filter Graph Manager exposes this interface, but the seeking functionality is always implemented by filters in the graph.

Some data cannot be seeked. For example, you cannot seek a live video stream from a camera. If a stream is seekable, however, there are various types of seeking it might support. These include:

-   Seeking to an arbitrary position in the stream.
-   Retrieving the duration of the stream.
-   Retrieving the current position within the stream.
-   Playing in reverse.

The **IMediaSeeking** interface defines a set of flags, [**AM\_SEEKING\_SEEKING\_CAPABILITIES**](/windows/win32/api/strmif/ne-strmif-am_seeking_seeking_capabilities), that describe the possible seeking capabilities. To retrieve the stream's capabilities, call the [**IMediaSeeking::GetCapabilities**](/windows/desktop/api/Strmif/nf-strmif-imediaseeking-getcapabilities) method. The method returns a bitwise combination of flags. The application can test them using the & (bitwise **AND**) operator. For example, the following code checks whether the graph can seek to an arbitrary position:


```C++
DWORD dwCap = 0;
HRESULT hr = pSeek->GetCapabilities(&dwCap);
if (AM_SEEKING_CanSeekAbsolute & dwCap)
{
    // Graph can seek to absolute positions.
}
```



 

 



