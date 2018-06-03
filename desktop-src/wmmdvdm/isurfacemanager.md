---
title: ISurfaceManager interface
description: The surface manager controls Direct3D and Direct3D surfaces. This interface can be queried for IBufferManager.
ms.assetid: 47909aec-7726-4205-b813-2ceee4dd7e74
keywords:
- ISurfaceManager interface Windows Movie Maker and DVD Maker
- ISurfaceManager interface Windows Movie Maker and DVD Maker , described
topic_type:
- apiref
api_name:
- ISurfaceManager
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# ISurfaceManager interface

The surface manager controls Direct3D and Direct3D surfaces. This interface can be queried for [**IBufferManager**](ibuffermanager.md).

## Members

The **ISurfaceManager** interface inherits from **IBufferManager**. **ISurfaceManager** also has these types of members:

-   [Methods](#methods)

### Methods

The **ISurfaceManager** interface has these methods.



| Method                                                            | Description                                                                                                                                                                                                                                            |
|:------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AllocSurface**](isurfacemanager-allocsurface.md)              | Allocates a new [**ISurface**](isurface.md) interface for the application to use. However, the recommended way to allocate a surface is described in the [**IMediaTransform::Process**](imediatransform-process.md) method documentation.<br/> |
| [**AllocSurfaceSize**](isurfacemanager-allocsurfacesize.md)      | Allocates a new **ISurface** of a specific size. However, the recommended way to allocate a surface is described in the **IMediaTransform::Process** documentation.<br/>                                                                         |
| [**get\_Device**](isurfacemanager-get-device.md)                 | Retrieves the device that owns the surface.<br/>                                                                                                                                                                                                 |
| [**get\_IdealVideoSize**](isurfacemanager-get-idealvideosize.md) | Retrieves the ideal video size for the surface.<br/>                                                                                                                                                                                             |
| [**get\_Monitor**](isurfacemanager-get-monitor.md)               | Retrieves a handle to the display monitor.<br/>                                                                                                                                                                                                  |



 

## See also

<dl> <dt>

[**Transform Interfaces**](transform-interfaces.md)
</dt> </dl>

 

 





