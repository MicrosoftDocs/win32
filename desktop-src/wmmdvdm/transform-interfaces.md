---
title: Transform Interfaces
description: Transform Interfaces
ms.assetid: 5fb0dee4-593c-4807-9a82-3911e1497abe
keywords:
- Windows Movie Maker,interfaces
- Movie Maker,interfaces
- programming reference,Windows Movie Maker interfaces
- reference for Windows Movie Maker,interfaces
- Windows Movie Maker,transform interfaces
- Movie Maker,transform interfaces
- programming reference,Windows Movie Maker transform interfaces
- reference for Windows Movie Maker,transform interfaces
- transforms,interfaces
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Transform Interfaces

This section contains reference pages for the main Windows Movie Maker interfaces. All interfaces are required unless otherwise noted.



| Interface                                        | Description                                                                                                                                             |
|--------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IMediaTransform**](imediatransform.md)       | Implemented by a transform to enable it to communicate with Windows Movie Maker.                                                                        |
| [**IBufferManager**](ibuffermanager.md)         | Used to access all surfaces and buffers.                                                                                                                |
| [**IBuffer**](ibuffer.md)                       | Wraps the source textures and the destination surface.                                                                                                  |
| [**INotifySeek**](inotifyseek.md)               | Optional interface that a transform can implement to receive notifications of playback discontinuities that are caused when a user seeks within a file. |
| [**IControlOutputSize**](icontroloutputsize.md) | Optional interface that a transform can implement to enable it to change its output buffer requirements after each frame is processed.                  |
| [**ISurface**](isurface.md)                     | Wraps an **IDirect3DSurface9** interface that represents a video surface.                                                                               |
| [**ISurfaceManager**](isurfacemanager.md)       | Controls allocation and destruction of Direct3D surfaces.                                                                                               |



 

## Related topics

<dl> <dt>

[**Windows Movie Maker APIs**](windows-movie-maker-apis.md)
</dt> </dl>

 

 




