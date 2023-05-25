---
description: Directly Hosting a DMO
ms.assetid: 10fb99cf-78d9-4519-9aec-23b0daeca9e2
title: Directly Hosting a DMO
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Directly Hosting a DMO

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This section describes how an application can act as the direct client of a DMO. The application delivers input to the DMO, the DMO creates output, and the application uses the output for rendering, further processing, or anything else. The application is responsible for issues such as memory allocation, timing and synchronization, and threading. These requirements will depend on the nature of the application.

The information in this section also applies if you are writing a component that acts as a layer between an application and a DMO (for example, an ActiveX Control that hosts a DMO). In addition, you should read this section if you are writing a DMO, because it describes the functionality that your DMO must implement.

This section contains the following topics:

-   [Setting Media Types on a DMO](setting-media-types-on-a-dmo.md)
-   [Processing Data in a DMO](processing-data-in-a-dmo.md)
-   [In-Place Processing](in-place-processing.md)
-   [Optional Streams](optional-streams.md)
-   [Implementing IMediaBuffer](implementing-imediabuffer.md)

## Related topics

<dl> <dt>

[Using DMOs](using-dmos.md)
</dt> </dl>

 

 



