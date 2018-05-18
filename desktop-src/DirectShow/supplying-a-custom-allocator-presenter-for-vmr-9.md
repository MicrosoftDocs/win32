---
Description: 'Supplying a Custom Allocator-Presenter for VMR-9'
ms.assetid: '61bb6b0d-25b5-481b-a241-74c6e421f109'
title: 'Supplying a Custom Allocator-Presenter for VMR-9'
---

# Supplying a Custom Allocator-Presenter for VMR-9

To use a custom allocator-presenter with the Video Mixing Renderer 9 (VMR-9) filter, perform the following steps:

1.  Implement a class that supports the [**IVMRSurfaceAllocator9**](ivmrsurfaceallocator9.md) and [**IVMRImagePresenter9**](ivmrimagepresenter9.md) interfaces.
2.  Call **QueryInterface** on the VMR-9 filter for the [**IVMRFilterConfig9**](ivmrfilterconfig9.md) interface.
3.  Call the [**IVMRFilterConfig9::SetRenderingMode**](ivmrfilterconfig9-setrenderingmode.md) method and pass in the **VMR9Mode\_Renderless** flag.
4.  **QueryInterface** on the VMR-9 filter for the [**IVMRSurfaceAllocatorNotify9**](ivmrsurfaceallocatornotify9.md) interface.
5.  Call the [**IVMRSurfaceAllocatorNotify9::AdviseSurfaceAllocator**](ivmrsurfaceallocatornotify9-advisesurfaceallocator.md) method and pass in a pointer to your allocator-presenter's [**IVMRSurfaceAllocator9**](ivmrsurfaceallocator9.md) method.
6.  Call your allocator-presenter's [**IVMRSurfaceAllocator9::AdviseNotify**](ivmrsurfaceallocator9-advisenotify.md) method and pass in a pointer to the VMR-9 filter's [**IVMRSurfaceAllocatorNotify9**](ivmrsurfaceallocatornotify9.md) interface.
7.  In your implementation of [**IVMRSurfaceAllocator9::AdviseNotify**](ivmrsurfaceallocator9-advisenotify.md), call [**IVMRSurfaceAllocatorNotify9::SetD3DDevice**](ivmrsurfaceallocatornotify9-setd3ddevice.md) Pass in a pointer to the Direct3D device and a handle to the monitor where the video will appear.
8.  In your implementation of the [**IVMRSurfaceAllocator9::InitializeDevice**](ivmrsurfaceallocator9-initializedevice.md) method, Create Direct3D surfaces that match the parameters given in the **InitializeDevice** method. Optionally, you can use the VMR-9 filter's [**IVMRSurfaceAllocatorNotify9::AllocateSurfaceHelper**](ivmrsurfaceallocatornotify9-allocatesurfacehelper.md) method to allocate these surfaces. Store the surface pointers in an array.
    > [!Note]  
    > If you want the VMR-9 to draw the video frames onto a texture surface, add the **VMR9AllocFlag\_TextureSurface** flag to the [**VMR9AllocationInfo**](vmr9allocationinfo.md) structure. If the device does not support textures in the native video format, you might need to create a separate texture surface, and then copy the video frames from the video surface to the texture.

     

9.  During streaming, the VMR-9 gets surfaces from the allocator-presenter by calling the [**IVMRSurfaceAllocator9::GetSurface**](ivmrsurfaceallocator9-getsurface.md) method. The VMR-9 specifies the surface by its index within the surface array (step 8).
10. Present the image when the VMR-9 calls the [**IVMRImagePresenter9::PresentImage**](ivmrimagepresenter9-presentimage.md) method. The parameters include a pointer to the Direct3D surface that contains the video image.
11. If the Direct3D device is lost at any time, the allocator-presenter must restore the device and recreate the surfaces. For example, the device can be lost if the display mode changes or the user moves the window to another monitor. If the Direct3D device changes, call the VMR-9 filter's [**IVMRSurfaceAllocatorNotify9::ChangeD3DDevice**](ivmrsurfaceallocatornotify9-changed3ddevice.md) method.
12. When streaming stops, the VMR-9 calls the [**IVMRSurfaceAllocator9::TerminateDevice**](ivmrsurfaceallocator9-terminatedevice.md) method. The allocator-presenter should release all of its Direct3D resources.

There are some differences between the VMR-7 and the VMR-9 in the way custom allocator-presenters are managed:

-   The VMR-9 filter's [**AllocateSurfaceHelper**](ivmrsurfaceallocatornotify9-allocatesurfacehelper.md) method is available for the allocator-presenter to use when allocating surfaces. This method makes it unnecessary for a custom allocator-presenter to forward any calls to the default allocator-presenter. For this reason, the CLSID of the VMR-9 filter's default allocator-presenter is not published.
-   Unlike the VMR-7, the VMR-9 does not provide a special DirectDraw Exclusive Mode allocator-presenter. The [**IVMRSurfaceAllocatorNotify9::AllocateSurfaceHelper**](ivmrsurfaceallocatornotify9-allocatesurfacehelper.md) method makes this object unnecessary.
-   For interlaced video, the VMR-9 always de-interlaces the video before it presents the image. The allocator-presenter is no longer responsible for de-interlacing the image before displaying it.

## Related topics

<dl> <dt>

[VMR Renderless Playback Mode (Custom Allocator-Presenters)](vmr-renderless-playback-mode--custom-allocator-presenters.md)
</dt> </dl>

 

 



