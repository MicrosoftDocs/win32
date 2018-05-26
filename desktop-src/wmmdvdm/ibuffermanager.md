---
title: IBufferManager interface
description: The IBufferManager interface is used to access all the surfaces and buffers that the transform uses.
ms.assetid: 6c0e7255-6fe4-4322-8330-a65fe120bb61
keywords:
- IBufferManager interface Windows Movie Maker and DVD Maker
- IBufferManager interface Windows Movie Maker and DVD Maker , described
topic_type:
- apiref
api_name:
- IBufferManager
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IBufferManager interface

The **IBufferManager** interface is used to access all the surfaces and buffers that the transform uses. The application is passed this interface in [**IMediaTransform::Process**](imediatransform-process.md) and [**IMediaTransform::InitBufferManager**](imediatransform-initbuffermanager.md). The object underlying this interface also exposes [**ISurfaceManager**](isurfacemanager.md).

## Members

The **IBufferManager** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **IBufferManager** also has these types of members:

-   [Methods](#methods)

### Methods

The **IBufferManager** interface has these methods.



| Method                                                   | Description                                                                       |
|:---------------------------------------------------------|:----------------------------------------------------------------------------------|
| [**AllocBuffer**](ibuffermanager-allocbuffer.md)        | Allocates a buffer for the transform to use.<br/>                           |
| [**get\_FormatType**](ibuffermanager-get-formattype.md) | Retrieves information about the type of buffer this object can create.<br/> |



 

## See also

<dl> <dt>

[**Transform Interfaces**](transform-interfaces.md)
</dt> </dl>

 

 





