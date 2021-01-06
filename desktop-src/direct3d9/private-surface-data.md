---
description: You can store any kind of application-specific data with a surface. For example, a surface representing a map in a game might contain information about terrain.
ms.assetid: a66fe0b9-1ccd-4cbd-a3e7-78081047e378
title: Private Surface Data (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Private Surface Data (Direct3D 9)

You can store any kind of application-specific data with a surface. For example, a surface representing a map in a game might contain information about terrain.

A surface can have more than one private data buffer. Each buffer is identified by a GUID that you supply when attaching the data to the surface.

To store private surface data, use SetPrivateData, passing a pointer to the source buffer, the size of the data, and an application-defined GUID for the data. Optionally, the source data can exist in the form of a COM object; in this case, you pass a pointer to the object's [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface pointer and you set the D3DSPD\_IUNKNOWNPOINTER flag.

SetPrivateData allocates an internal buffer for the data and copies it. You can then safely free the source buffer or object. The internal buffer or interface reference is released when FreePrivateData is called. This happens automatically when the surface is freed.

To retrieve private data for a surface, you must allocate a buffer of the correct size and then call the GetPrivateData method, passing the GUID that was assigned to the data. You are responsible for freeing any dynamic memory you use for this buffer. If the data is a COM object, this method retrieves the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) pointer.

If you don't know how big a buffer to allocate, first call GetPrivateData with zero in pSizeOfData. If the method fails with D3DERR\_MOREDATA, it returns the necessary number of bytes for the buffer.

## Related topics

<dl> <dt>

[Direct3D Surfaces](direct3d-surfaces.md)
</dt> </dl>

 

 
