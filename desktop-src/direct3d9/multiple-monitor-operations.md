---
description: When a device is successfully reset (IDirect3DDevice9::Reset) or created (IDirect3D9::CreateDevice) in full-screen operations, the Direct3D object that created the device is marked as owning all adapters on that system.
ms.assetid: df3b6ed7-830b-4635-9295-fff05cc35891
title: Multiple-Monitor Operations (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Multiple-Monitor Operations (Direct3D 9)

When a device is successfully reset ([**IDirect3DDevice9::Reset**](/windows/desktop/api)) or created ([**IDirect3D9::CreateDevice**](/windows/desktop/api)) in full-screen operations, the Direct3D object that created the device is marked as owning all adapters on that system. This state is known as exclusive mode, and the Direct3D object owns exclusive mode. Exclusive mode means that devices created by any other Direct3D object can neither assume full-screen operations nor allocate video memory. In addition, when a Direct3D object assumes exclusive mode, all devices other than the one that went full-screen are placed in lost state. For details, see [Lost Devices (Direct3D 9)](lost-devices.md).

Along with exclusive mode, the Direct3D object is informed of the focus window that the device will use. Exclusive mode is released when the final full-screen device owned by that Direct3D object is either reset to windowed mode or destroyed.

Devices can be divided into two categories when a Direct3D object owns exclusive mode. The first category of devices have the following characteristics.

-   They are created by the same Direct3D object that created the device that is full-screen.
-   They have the same focus window as the device that is full-screen.
-   They represent a different adapter from any full-screen device.

Devices in this category have no restrictions concerning their ability to be reset or created, and they are not placed in lost state. Devices in this category can even be put into full-screen mode.

Devices that do not fall in the first category - devices created by another Direct3D object, created with a different focus window, and created for an adapter with a device that is already full-screen - cannot be reset and remain in lost state until the exclusive mode is lost. As a result, a multiple-monitor application can place several devices in full-screen mode, but only if all these devices are for different adapters, were created by the same Direct3D object, and share the same focus window.

## Related topics

<dl> <dt>

[Presenting a Scene](presenting-a-scene.md)
</dt> </dl>

 

 



