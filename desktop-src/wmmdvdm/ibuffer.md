---
title: IBuffer interface
description: The IBuffer interface wraps the source textures and the destination surface.
ms.assetid: 72a68658-19cf-4cf9-bdf7-141e14701ad9
keywords:
- IBuffer interface Windows Movie Maker and DVD Maker
- IBuffer interface Windows Movie Maker and DVD Maker , described
topic_type:
- apiref
api_name:
- IBuffer
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IBuffer interface

The **IBuffer** interface wraps the source textures and the destination surface. Your transform typically will not call methods on this interface directly, but instead will pass it to the [**GetSurface**](getsurface.md) or [**GetTexture**](gettexture.md) function to get a source or destination surface or texture. However, the interface is documented for completeness.

The object that underlies this interface also exposes the [**ISurface**](isurface.md) interface.

## Members

The **IBuffer** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **IBuffer** also has these types of members:

-   [Methods](#methods)

### Methods

The **IBuffer** interface has these methods.



| Method                                  | Description                                        |
|:----------------------------------------|:---------------------------------------------------|
| [**CopyTo**](ibuffer-copyto.md)        | Copies a buffer to another buffer.<br/>      |
| [**get\_Flags**](ibuffer-get-flags.md) | Retrieves information about the buffer.<br/> |



 

## See also

<dl> <dt>

[**Transform Interfaces**](transform-interfaces.md)
</dt> </dl>

 

 





