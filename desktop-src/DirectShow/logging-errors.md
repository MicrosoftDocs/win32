---
description: Logging Errors
ms.assetid: 690ea91b-5bc0-45f0-8354-ec625709f7bd
title: Logging Errors
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Logging Errors

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

\[This API is not supported and may be altered or unavailable in the future.\]

[DirectShow Editing Services](directshow-editing-services.md) (DES) provides a built-in mechanism for logging errors that occur when loading, constructing, or rendering a DES project. This article presents a sample console application that loads an XML project file and attempts to render it. If an error occurs, the application prints an error message in the console window. The sample code presented in this article builds on the example given in [Loading and Previewing a Project](loading-and-previewing-a-project.md).

> [!Note]  
> Your application is not required to implement error logging. DES does not log errors unless you explicitly request it.

 

This article assumes that you understand COM client programming and the DES timeline model. In addition, you need to understand the basics of COM object programming. For information about timelines in DES, see [The Timeline Model](the-timeline-model.md).

This article contains the following sections.

-   [Overview of Error Logging](overview-of-error-logging.md)
-   [Creating an Error Logging Class](creating-an-error-logging-class.md)
-   [Implementing IAMErrorLog](implementing-iamerrorlog.md)
-   [Setting the Error Log](setting-the-error-log.md)
-   [DES Error Logging: Example Code](des-error-logging--example-code.md)

## Related topics

<dl> <dt>

[Using DirectShow Editing Services](using-directshow-editing-services.md)
</dt> </dl>

 

 



