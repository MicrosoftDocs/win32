---
description: Supplying a Custom Allocator-Presenter for VMR-9
ms.assetid: 61bb6b0d-25b5-481b-a241-74c6e421f109
title: Supplying a Custom Allocator-Presenter for VMR-9
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Supplying a Custom Allocator-Presenter for VMR-9

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

To use a custom allocator-presenter with the Video Mixing Renderer 9 (VMR-9) filter, perform the following steps:

1.  Implement a class that supports the [**IVMRSurfaceAllocator9**](/previous-versions/windows/desktop/api/Vmr9/nn-vmr9-ivmrsurfaceallocator9) and [**IVMRImagePresenter9**](/previous-versions/windows/desktop/api/Vmr9/nn-vmr9-ivmrimagepresenter9) interfaces.
2.  Call **QueryInterface** on the VMR-9 filter for the [**IVMRFilterConfig9**](/previous-versions/windows/desktop/api/Vmr9/nn-vmr9-ivmrfilterconfig9) interface.
3.  Call the [**IVMRFilterConfig9::SetRenderingMode**](/previous-versions/windows/desktop/api/Vmr9/nf-vmr9-ivmrfilterconfig9-setrenderingmode) method and pass in the **VMR9Mode\_Renderless** flag.
4.  **QueryInterface** on the VMR-9 filter for the [**IVMRSurfaceAllocatorNotify9**](/previous-versions/windows/desktop/api/Vmr9/nn-vmr9-ivmrsurfaceallocatornotify9) interface.
5.  Call the [**IVMRSurfaceAllocatorNotify9::AdviseSurfaceAllocator**](/previous-versions/windows/desktop/api/Vmr9/nf-vmr9-ivmrsurfaceallocatornotify9-advisesurfaceallocator) method and pass in a pointer to your allocator-presenter's [**IVMRSurfaceAllocator9**](/previous-versions/windows/desktop/api/Vmr9/nn-vmr9-ivmrsurfaceallocator9) method.
6.  Call your allocator-presenter's [**IVMRSurfaceAllocator9::AdviseNotify**](/previous-versions/windows/desktop/api/Vmr9/nf-vmr9-ivmrsurfaceallocator9-advisenotify) method and pass in a pointer to the VMR-9 filter's [**IVMRSurfaceAllocatorNotify9**](/previous-versions/windows/desktop/api/Vmr9/nn-vmr9-ivmrsurfaceallocatornotify9) interface.
7.  In your implementation of [**IVMRSurfaceAllocator9::AdviseNotify**](/previous-versions/windows/desktop/api/Vmr9/nf-vmr9-ivmrsurfaceallocator9-advisenotify), call [**IVMRSurfaceAllocatorNotify9::SetD3DDevice**](/previous-versions/windows/desktop/api/Vmr9/nf-vmr9-ivmrsurfaceallocatornotify9-setd3ddevice) Pass in a pointer to the Direct3D device and a handle to the monitor where the video will appear.
8.  In your implementation of the [**IVMRSurfaceAllocator9::InitializeDevice**](/previous-versions/windows/desktop/api/Vmr9/nf-vmr9-ivmrsurfaceallocator9-initializedevice) method, Create Direct3D surfaces that match the parameters given in the **InitializeDevice** method. Optionally, you can use the VMR-9 filter's [**IVMRSurfaceAllocatorNotify9::AllocateSurfaceHelper**](/previous-versions/windows/desktop/api/Vmr9/nf-vmr9-ivmrsurfaceallocatornotify9-allocatesurfacehelper) method to allocate these surfaces. Store the surface pointers in an array.
    > [!Note]  
    > If you want the VMR-9 to draw the video frames onto a texture surface, add the **VMR9AllocFlag\_TextureSurface** flag to the [**VMR9AllocationInfo**](/previous-versions/windows/desktop/api/Vmr9/ns-vmr9-vmr9allocationinfo) structure. If the device does not support textures in the native video format, you might need to create a separate texture surface, and then copy the video frames from the video surface to the texture.

     

9.  During streaming, the VMR-9 gets surfaces from the allocator-presenter by calling the [**IVMRSurfaceAllocator9::GetSurface**](/previous-versions/windows/desktop/api/Vmr9/nf-vmr9-ivmrsurfaceallocator9-getsurface) method. The VMR-9 specifies the surface by its index within the surface array (step 8).
10. Present the image when the VMR-9 calls the [**IVMRImagePresenter9::PresentImage**](/previous-versions/windows/desktop/api/Vmr9/nf-vmr9-ivmrimagepresenter9-presentimage) method. The parameters include a pointer to the Direct3D surface that contains the video image.
11. If the Direct3D device is lost at any time, the allocator-presenter must restore the device and recreate the surfaces. For example, the device can be lost if the display mode changes or the user moves the window to another monitor. If the Direct3D device changes, call the VMR-9 filter's [**IVMRSurfaceAllocatorNotify9::ChangeD3DDevice**](/previous-versions/windows/desktop/api/Vmr9/nf-vmr9-ivmrsurfaceallocatornotify9-changed3ddevice) method.
12. When streaming stops, the VMR-9 calls the [**IVMRSurfaceAllocator9::TerminateDevice**](/previous-versions/windows/desktop/api/Vmr9/nf-vmr9-ivmrsurfaceallocator9-terminatedevice) method. The allocator-presenter should release all of its Direct3D resources.

There are some differences between the VMR-7 and the VMR-9 in the way custom allocator-presenters are managed:

-   The VMR-9 filter's [**AllocateSurfaceHelper**](/previous-versions/windows/desktop/api/Vmr9/nf-vmr9-ivmrsurfaceallocatornotify9-allocatesurfacehelper) method is available for the allocator-presenter to use when allocating surfaces. This method makes it unnecessary for a custom allocator-presenter to forward any calls to the default allocator-presenter. For this reason, the CLSID of the VMR-9 filter's default allocator-presenter is not published.
-   Unlike the VMR-7, the VMR-9 does not provide a special DirectDraw Exclusive Mode allocator-presenter. The [**IVMRSurfaceAllocatorNotify9::AllocateSurfaceHelper**](/previous-versions/windows/desktop/api/Vmr9/nf-vmr9-ivmrsurfaceallocatornotify9-allocatesurfacehelper) method makes this object unnecessary.
-   For interlaced video, the VMR-9 always de-interlaces the video before it presents the image. The allocator-presenter is no longer responsible for de-interlacing the image before displaying it.

## Related topics

<dl> <dt>

[VMR Renderless Playback Mode (Custom Allocator-Presenters)](vmr-renderless-playback-mode--custom-allocator-presenters.md)
</dt> </dl>

 

 



