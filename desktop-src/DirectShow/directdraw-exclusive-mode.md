---
description: DirectDraw Exclusive Mode
ms.assetid: 3ef4f267-4dc2-421b-ade4-6b1efa364733
title: DirectDraw Exclusive Mode
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DirectDraw Exclusive Mode

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This topic applies to the VMR-7 only. In the VMR-9, you enable exclusive mode by supplying your own exclusive mode allocator-presenter. This is relatively straightforward if you use the [**IVMRSurfaceAllocatorNotify9::AllocateSurfaceHelper**](/previous-versions/windows/desktop/api/Vmr9/nf-vmr9-ivmrsurfaceallocatornotify9-allocatesurfacehelper) method. The VMR9Allocator sample shows how to implement a custom allocator-presenter.

 

In DirectDraw Exclusive Mode, an application takes exclusive control of the graphics hardware. This is useful for applications such as games, or perhaps full-screen video applications. Normally, the VMR creates the DirectDraw objects and sets the cooperative level to normal. However, to run the VMR in DirectDraw Exclusive Mode, the application itself must create the DirectDraw object and the primary surface, and call **SetCooperativeLevel** to specify exclusive mode.

The VMR has a special allocator-presenter that enables it to run in DirectDraw Exclusive Mode. To configure the VMR to use this allocator-presenter:

1.  Create the Filter Graph and add the VMR to it using the [**IFilterGraph::AddFilter**](/windows/desktop/api/Strmif/nf-strmif-ifiltergraph-addfilter) method. For a code example, see [VMR Windowless Mode](vmr-windowless-mode.md).
2.  Create the Exclusive Mode allocator-presenter:
    ```C++
    IVMRImagePresenterExclModeConfig* pExclModeConfig;
    CoCreateInstance(
            CLSID_AllocPresenterDDXclMode,
            NULL,
            CLSCTX_INPROC_SERVER,
            IID_IVMRImagePresenterExclModeConfig,
            (void**)&pExclModeConfig
            );
    ```

    

3.  Configure the new allocator-presenter:
    ```C++
    pExclModeConfig->SetXlcModeDDObjAndPrimarySurface(...);
    ```

    

4.  Plug the new allocator-presenter into the VMR.
5.  Build the rest of the filter graph in the usual ways.

## Related topics

<dl> <dt>

[VMR Modes of Operation](vmr-modes-of-operation.md)
</dt> </dl>

 

 



