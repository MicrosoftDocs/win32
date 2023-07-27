---
description: Controlling Filter Graphs Using C
ms.assetid: 56e41f0a-2ea6-422c-8d3f-7849e91e3731
title: Controlling Filter Graphs Using C
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Controlling Filter Graphs Using C

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

If you are writing a DirectShow application in C (rather than C++), you must use a vtable pointer to call methods. The following example illustrates how to call the **IUnknown::QueryInterface** method from an application written in C:


```C++
pGraph->lpVtbl->QueryInterface(pGraph, &IID_IMediaEvent, (void **)&pEvent);
```



The following shows the equivalent call in C++:


```C++
pGraph->QueryInterface(IID_IMediaEvent, (void **)&pEvent);
```



In C, COM interfaces are defined as structures. The **lpVtbl** member is a pointer to a table of interface methods (the vtable). All methods take an additional parameter, which is a pointer to the interface.

## Related topics

<dl> <dt>

[Appendixes](appendixes.md)
</dt> </dl>

 

 



