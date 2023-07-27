---
description: Declaring the Factory Template
ms.assetid: 3060c167-ea23-4061-b32a-16e750f55e6f
title: Declaring the Factory Template
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Declaring the Factory Template

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The next step is to declare the factory template for your filter. A factory template is a C++ class that contains information for the class factory. In your DLL, declare a global array of [**CFactoryTemplate**](cfactorytemplate.md) objects, one for each filter or COM component in your DLL. The array must be named *g\_Templates*. For more information about factory templates, see [How to Create a DirectShow Filter DLL](how-to-create-a-dll.md).

The **m\_pAMovieSetup\_Filter** member of the factory template is a pointer to the [**AMOVIESETUP\_FILTER**](amoviesetup-filter.md) structure described previously. The following example shows a factory template, using the structure given in the previous example:


```C++
CFactoryTemplate g_Templates[] = {
    {
        g_wszName,                      // Name.
        &CLSID_SomeFilter,              // CLSID.
        CSomeFilter::CreateInstance,    // Creation function.
        NULL,
        &sudFilterReg                   // Pointer to filter information.
    }
};
int g_cTemplates = sizeof(g_Templates) / sizeof(g_Templates[0]);
```



If you did not declare any filter information, **m\_pAMoveSetup\_Filter** can be **NULL**.

## Related topics

<dl> <dt>

[How to Register DirectShow Filters](how-to-register-directshow-filters.md)
</dt> </dl>

 

 



