---
description: Supplying a Custom Allocator-Presenter for VMR-7
ms.assetid: 19b43c9b-2578-418f-b03b-af7c7a3a46e4
title: Supplying a Custom Allocator-Presenter for VMR-7
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Supplying a Custom Allocator-Presenter for VMR-7

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The allocator-presenter is responsible for allocating DirectDraw surfaces and presenting the video frames for rendering. In the vast majority of scenarios, the functionality of the default allocator-presenter will be more than sufficient for an application's needs. But by plugging in a custom allocator-presenter, an application can obtain direct access to the video bits and completely control the rendering process. The trade-off for this increased power is that the application must handle the added complexity of DirectDraw surface management.

![using a custom allocator-presenter](images/custom-ap.png)

The preceding figure shows the communication interfaces used by the VMR and the allocator-presenter. A custom allocator-presenter that overrides all of the default allocation and presentation functionality must implement the [**IVMRImagePresenter**](/windows/desktop/api/Strmif/nn-strmif-ivmrimagepresenter) and [**IVMRSurfaceAllocator**](/windows/desktop/api/Strmif/nn-strmif-ivmrsurfaceallocator) interfaces, and optionally, [**IVMRWindowlessControl**](/windows/desktop/api/Strmif/nn-strmif-ivmrwindowlesscontrol).

To replace the default allocator-presenter, an application calls the [**IVMRSurfaceAllocatorNotify::AdviseSurfaceAllocator**](/windows/desktop/api/Strmif/nf-strmif-ivmrsurfaceallocatornotify-advisesurfaceallocator) method and passes in a pointer to the new allocator-presenter. In response to this call, the VMR will call the allocator-presenter's [**IVMRSurfaceAllocator::AdviseNotify**](/windows/desktop/api/Strmif/nf-strmif-ivmrsurfaceallocator-advisenotify) method to provide the pointer to the VMR's [**IVMRSurfaceAllocatorNotify**](/windows/desktop/api/Strmif/nn-strmif-ivmrsurfaceallocatornotify) interface. The allocator-presenter will use this interface pointer when passing events to the VMR with the [**IVMRSurfaceAllocatorNotify::NotifyEvent**](/windows/desktop/api/Strmif/nf-strmif-ivmrsurfaceallocatornotify-notifyevent) method.

As an alternate solution, an application can use both its own allocator-presenter and the default allocator-presenter. In this scenario, the custom allocator-presenter handles only those calls where custom functionality is needed, and passes the rest of the calls from the VMR through to the default allocator-presenter. In many cases, it is only necessary to override the [**IVMRImagePresenter**](/windows/desktop/api/Strmif/nn-strmif-ivmrimagepresenter) interface.

![using two allocator-presenters](images/custom-ap2.png)

To use both a custom allocator-presenter and the default allocator-presenter, an application would first call [**IVMRSurfaceAllocatorNotify::AdviseSurfaceAllocator**](/windows/desktop/api/Strmif/nf-strmif-ivmrsurfaceallocatornotify-advisesurfaceallocator) to provide a pointer to the new allocator-presenter. This causes the default allocator-presenter to be destroyed, so the application must create another instance of it by calling **QueryInterface** on the VMR and requesting the [**IVMRSurfaceAllocator**](/windows/desktop/api/Strmif/nn-strmif-ivmrsurfaceallocator) interface. As shown in the preceding figure, the custom allocator-presenter overrides the [**IVMRImagePresenter**](/windows/desktop/api/Strmif/nn-strmif-ivmrimagepresenter) interface methods, and simply passes all calls to the **IVMRSurfaceAllocator** interface through to the default implementation. The figure also shows the [**IVMRWindowlessControl**](/windows/desktop/api/Strmif/nn-strmif-ivmrwindowlesscontrol) interface as being implemented on the allocator-presenter.

## Related topics

<dl> <dt>

[Supplying a Custom Allocator-Presenter for VMR-9](supplying-a-custom-allocator-presenter-for-vmr-9.md)
</dt> <dt>

[VMR Renderless Playback Mode (Custom Allocator-Presenters)](vmr-renderless-playback-mode--custom-allocator-presenters.md)
</dt> </dl>

 

 



