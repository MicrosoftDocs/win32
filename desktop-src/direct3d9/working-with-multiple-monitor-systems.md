---
description: The concept of exclusive full-screen mode is retained in Direct3D 9, but it is kept entirely implicit in the IDirect3D9::CreateDevice and IDirect3DDevice9::Reset method calls.
ms.assetid: c3503d62-d9f9-4eec-8af3-ebcbfe7064d4
title: Working with Multiple Monitor Systems (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Working with Multiple Monitor Systems (Direct3D 9)

The concept of exclusive full-screen mode is retained in Direct3D 9, but it is kept entirely implicit in the [**IDirect3D9::CreateDevice**](/windows/desktop/api) and [**IDirect3DDevice9::Reset**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-reset) method calls. Whenever a device is successfully reset or created in full-screen operation, the Direct3D object that created the device is marked as owning all adapters on that system. This state is known as exclusive mode, and at this point the Direct3D object owns exclusive mode. Exclusive mode means that devices created by any other Direct3D9 object can neither assume full-screen operation nor allocate video memory. In addition, when a Direct3D9 object assumes exclusive mode, all devices other than the device that went full-screen are placed into the lost state. For information about how to handle lost devices, see [Lost Devices (Direct3D 9)](lost-devices.md).

Along with exclusive mode, the Direct3D9 object is informed of the focus window to be used by the device. Exclusive mode is released when the last full-screen device owned by that Direct3D9 object is either reset to windowed mode or destroyed.

Devices can be divided into two categories when a Direct3D9 object owns exclusive mode. The first category of devices are those that were created by the same Direct3D9 object that created the device that is already full-screen, have the same focus window as the device that is already full-screen, and represent a different adapter from any full-screen device. Devices in this category have no restrictions concerning their ability to be reset or created and are not placed into the lost state. Devices in this category can even be placed into full-screen mode.

Devices not in this category, which would be those created by a different Direct3D9 object, or with a different focus window, or for some adapter with a device already full-screen cannot be reset and remain in the lost state until exclusive mode is lost.

The practical implication is that a multiple monitor application can place several devices in full-screen mode, but only if all these devices are for different adapters, were created by the same Direct3D9 object, and all share the same focus window.

When you create a new device using the same [**IDirect3D9**](/windows/desktop/api) object and focus window, your original device will lose its surfaces. You will need to call [**IDirect3DDevice9::Reset**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-reset) on the first device in order for your application to use it. For example, to create two devices, do the following:

1.  Create Device 1
2.  Create Device 2
3.  Reset Device 1

## Related topics

<dl> <dt>

[Programming Tips](programming-tips.md)
</dt> </dl>

 

 
