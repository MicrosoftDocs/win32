---
Description: Supplying a Custom Allocator-Presenter for VMR-9
ms.assetid: 61bb6b0d-25b5-481b-a241-74c6e421f109
title: Supplying a Custom Allocator-Presenter for VMR-9
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Supplying a Custom Allocator-Presenter for VMR-9

To use a custom allocator-presenter with the Video Mixing Renderer 9 (VMR-9) filter, perform the following steps:

1.  Implement a class that supports the [**IVMRSurfaceAllocator9**](/windows/win32/Vmr9/nn-vmr9-ivmrsurfaceallocator9?branch=master) and [**IVMRImagePresenter9**](/windows/win32/Vmr9/nn-vmr9-ivmrimagepresenter9?branch=master) interfaces.
2.  Call **QueryInterface** on the VMR-9 filter for the [**IVMRFilterConfig9**](/windows/win32/Vmr9/nn-vmr9-ivmrfilterconfig9?branch=master) interface.
3.  Call the [**IVMRFilterConfig9::SetRenderingMode**](/windows/win32/Vmr9/nf-vmr9-ivmrfilterconfig9-setrenderingmode?branch=master) method and pass in the **VMR9Mode\_Renderless** flag.
4.  **QueryInterface** on the VMR-9 filter for the [**IVMRSurfaceAllocatorNotify9**](/windows/win32/Vmr9/nn-vmr9-ivmrsurfaceallocatornotify9?branch=master) interface.
5.  Call the [**IVMRSurfaceAllocatorNotify9::AdviseSurfaceAllocator**](/windows/win32/Vmr9/nf-vmr9-ivmrsurfaceallocatornotify9-advisesurfaceallocator?branch=master) method and pass in a pointer to your allocator-presenter's [**IVMRSurfaceAllocator9**](/windows/win32/Vmr9/nn-vmr9-ivmrsurfaceallocator9?branch=master) method.
6.  Call your allocator-presenter's [**IVMRSurfaceAllocator9::AdviseNotify**](/windows/win32/Vmr9/nf-vmr9-ivmrsurfaceallocator9-advisenotify?branch=master) method and pass in a pointer to the VMR-9 filter's [**IVMRSurfaceAllocatorNotify9**](/windows/win32/Vmr9/nn-vmr9-ivmrsurfaceallocatornotify9?branch=master) interface.
7.  In your implementation of [**IVMRSurfaceAllocator9::AdviseNotify**](/windows/win32/Vmr9/nf-vmr9-ivmrsurfaceallocator9-advisenotify?branch=master), call [**IVMRSurfaceAllocatorNotify9::SetD3DDevice**](/windows/win32/Vmr9/nf-vmr9-ivmrsurfaceallocatornotify9-setd3ddevice?branch=master) Pass in a pointer to the Direct3D device and a handle to the monitor where the video will appear.
8.  In your implementation of the [**IVMRSurfaceAllocator9::InitializeDevice**](/windows/win32/Vmr9/nf-vmr9-ivmrsurfaceallocator9-initializedevice?branch=master) method, Create Direct3D surfaces that match the parameters given in the **InitializeDevice** method. Optionally, you can use the VMR-9 filter's [**IVMRSurfaceAllocatorNotify9::AllocateSurfaceHelper**](/windows/win32/Vmr9/nf-vmr9-ivmrsurfaceallocatornotify9-allocatesurfacehelper?branch=master) method to allocate these surfaces. Store the surface pointers in an array.
    > [!Note]  
    > If you want the VMR-9 to draw the video frames onto a texture surface, add the **VMR9AllocFlag\_TextureSurface** flag to the [**VMR9AllocationInfo**](/windows/win32/Vmr9/ns-vmr9-_vmr9allocationinfo?branch=master) structure. If the device does not support textures in the native video format, you might need to create a separate texture surface, and then copy the video frames from the video surface to the texture.

     

9.  During streaming, the VMR-9 gets surfaces from the allocator-presenter by calling the [**IVMRSurfaceAllocator9::GetSurface**](/windows/win32/Vmr9/nf-vmr9-ivmrsurfaceallocator9-getsurface?branch=master) method. The VMR-9 specifies the surface by its index within the surface array (step 8).
10. Present the image when the VMR-9 calls the [**IVMRImagePresenter9::PresentImage**](/windows/win32/Vmr9/nf-vmr9-ivmrimagepresenter9-presentimage?branch=master) method. The parameters include a pointer to the Direct3D surface that contains the video image.
11. If the Direct3D device is lost at any time, the allocator-presenter must restore the device and recreate the surfaces. For example, the device can be lost if the display mode changes or the user moves the window to another monitor. If the Direct3D device changes, call the VMR-9 filter's [**IVMRSurfaceAllocatorNotify9::ChangeD3DDevice**](/windows/win32/Vmr9/nf-vmr9-ivmrsurfaceallocatornotify9-changed3ddevice?branch=master) method.
12. When streaming stops, the VMR-9 calls the [**IVMRSurfaceAllocator9::TerminateDevice**](/windows/win32/Vmr9/nf-vmr9-ivmrsurfaceallocator9-terminatedevice?branch=master) method. The allocator-presenter should release all of its Direct3D resources.

There are some differences between the VMR-7 and the VMR-9 in the way custom allocator-presenters are managed:

-   The VMR-9 filter's [**AllocateSurfaceHelper**](/windows/win32/Vmr9/nf-vmr9-ivmrsurfaceallocatornotify9-allocatesurfacehelper?branch=master) method is available for the allocator-presenter to use when allocating surfaces. This method makes it unnecessary for a custom allocator-presenter to forward any calls to the default allocator-presenter. For this reason, the CLSID of the VMR-9 filter's default allocator-presenter is not published.
-   Unlike the VMR-7, the VMR-9 does not provide a special DirectDraw Exclusive Mode allocator-presenter. The [**IVMRSurfaceAllocatorNotify9::AllocateSurfaceHelper**](/windows/win32/Vmr9/nf-vmr9-ivmrsurfaceallocatornotify9-allocatesurfacehelper?branch=master) method makes this object unnecessary.
-   For interlaced video, the VMR-9 always de-interlaces the video before it presents the image. The allocator-presenter is no longer responsible for de-interlacing the image before displaying it.

## Related topics

<dl> <dt>

[VMR Renderless Playback Mode (Custom Allocator-Presenters)](vmr-renderless-playback-mode--custom-allocator-presenters.md)
</dt> </dl>

 

 



