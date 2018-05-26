---
Description: VMR Support for DirectX Video Acceleration
ms.assetid: 4bb5612d-3841-4920-a5ef-39ce357a6d1c
title: VMR Support for DirectX Video Acceleration
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# VMR Support for DirectX Video Acceleration

DirectX Video Acceleration is an Application Programming Interface (API) and a corresponding Device Driver Interface (DDI) for hardware acceleration of digital video decoding processing, with support of alpha blending for such purposes as DVD subpicture support. DirectX VA is documented in the Windows DDK. The [**IAMVideoAccelerator**](/windows/win32/videoacc/nn-videoacc-iamvideoaccelerator?branch=master) interface, which provides user mode access to DirectX VA functionality on a hardware device, is documented in this SDK.

The VMR supports [**IAMVideoAccelerator**](/windows/win32/videoacc/nn-videoacc-iamvideoaccelerator?branch=master), and its implementation is identical to the old Overlay Mixer except for one important difference. The Overlay Mixer guaranteed that the output is rendered into an overlay surface, while the VMR can send the output for further processing, for example a 3D operation, or it might send the output to an offscreen surface which is then blitted to the primary surface.

## Related topics

<dl> <dt>

[About DirectX Video Acceleration](about-directx-video-acceleration.md)
</dt> </dl>

 

 



