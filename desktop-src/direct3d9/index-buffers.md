---
description: Index buffers, represented by the IDirect3DIndexBuffer9 interface, are memory buffers that contain index data.
ms.assetid: baa60cd1-a1f0-4dbe-b934-aeb1a5c6b784
title: Index Buffers (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Index Buffers (Direct3D 9)

Index buffers, represented by the [**IDirect3DIndexBuffer9**](/windows/win32/api/d3d9helper/nn-d3d9helper-idirect3dindexbuffer9) interface, are memory buffers that contain index data. Index data, or indices, are integer offsets into vertex buffers and are used to render primitives using the [**IDirect3DDevice9::DrawIndexedPrimitive**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-drawindexedprimitive) method.

A vertex buffer contains vertices; therefore, you can draw a vertex buffer either with or without indexed primitives. However, because an index buffer contains indices, you cannot use an index buffer without a corresponding vertex buffer. (As a side note, [**IDirect3DDevice9::DrawIndexedPrimitiveUP**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-drawindexedprimitiveup) and [**IDirect3DDevice9::DrawPrimitiveUP**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-drawprimitiveup) are the only draw methods that draw without an index or a vertex buffer.)

## Index Buffer Description

An index buffer is described in terms of its capabilities, such as where it exists in memory, whether it supports reading and writing, and the type and number of indices it can contain. These traits are held in a [**D3DINDEXBUFFER\_DESC**](d3dindexbuffer-desc.md) structure.

Index buffer descriptions tell your application how an existing buffer was created. You provide an empty description structure for the system to fill with the capabilities of a previously created index buffer.

-   The Format member describes the surface format of the index buffer data.
-   The Type identifies the resource type of the index buffer.
-   The Usage structure member contains general capability flags. The D3DUSAGE\_SOFTWAREPROCESSING flag indicates that the index buffer is to be used with software vertex processing. The presence of the D3DUSAGE\_WRITEONLY flag in Usage indicates that the index buffer memory is used only for write operations. This frees the driver to place the index data in the best memory location to enable fast processing and rendering. If the D3DUSAGE\_WRITEONLY flag is not used, the driver is less likely to put the data in a location that is inefficient for read operations. This sacrifices some processing and rendering speed. If this flag is not specified, it is assumed that applications perform read and write operations on the data in the index buffer.
-   Pool specifies the memory class allocated for the index buffer. The D3DPOOL\_SYSTEMMEM flag indicates that the system created the index buffer in system memory.
-   The Size member stores the size, in bytes, of the vertex buffer data.
-   The last parameter pSharedHandle is not used. Set it to **NULL**.

## Index Processing Requirements

The performance of index processing operations depends heavily on where the index buffer exists in memory and what type of rendering device is being used. Applications control the memory allocation for index buffers when they are created. When the D3DPOOL\_SYSTEMMEM memory flag is set, the index buffer is created in system memory. When the D3DPOOL\_DEFAULT memory flag is used, the device driver determines where the memory for the index buffer is best allocated, often referred to as driver-optimal memory. Driver-optimal memory can be local video memory, non-local video memory, or system memory.

Setting the D3DUSAGE\_SOFTWAREPROCESSING behavior flag when calling the [**IDirect3DDevice9::CreateIndexBuffer**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-createindexbuffer) method specifies that the index buffer is to be used with software vertex processing. This flag is required in mixed mode vertex processing (D3DCREATE\_MIXED\_VERTEXPROCESSING) when software vertex processing is used.

The application can directly write indices to a index buffer allocated in driver-optimal memory. This technique prevents a redundant copy operation later. This technique does not work well if your application reads data back from an index buffer, because read operations done by the host from driver-optimal memory can be very slow. Therefore, if your application needs to read during processing or writes data to the buffer erratically, a system-memory index buffer is a better choice.

> [!Note]  
> Always use D3DPOOL\_DEFAULT, except when you don't want to use video memory or use large amounts of page-locked RAM when the driver is putting vertex or index buffers into AGP memory.

 

## Create an Index Buffer

Create an index buffer object by calling the [**IDirect3DDevice9::CreateIndexBuffer**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-createindexbuffer) method, which accepts six parameters.

-   The first parameter specifies the index buffer length, in bytes.
-   The second parameter is a set of usage controls. Among other things, its value determines whether the vertices being referred to by the indices are capable of containing clipping information. To improve performance, specify D3DUSAGE\_DONOTCLIP when clipping is not required.

    The D3DUSAGE\_SOFTWAREPROCESSING flag can be set when mixed-mode or software vertex processing (D3DCREATE\_MIXED\_VERTEXPROCESSING / D3DCREATE\_SOFTWARE\_VERTEXPROCESSING) is enabled for that device. D3DUSAGE\_SOFTWAREPROCESSING must be set for buffers to be used with software vertex processing in mixed mode, but it should not be set for the best possible performance when using hardware index processing in mixed mode (D3DCREATE\_HARDWARE\_VERTEXPROCESSING). However, setting D3DUSAGE\_SOFTWAREPROCESSING is the only option when a single buffer is used with both hardware and software vertex processing. D3DUSAGE\_SOFTWAREPROCESSING is allowed for mixed and software devices.

    It is possible to force vertex and index buffers into system memory by specifying D3DPOOL\_SYSTEMMEM, even when the index processing is being done in hardware. This is a way to avoid overly large amounts of page-locked memory when a driver is putting these buffers into AGP memory.

-   The third parameter is either the D3DFMT\_INDEX16 or D3DFMT\_INDEX32 member of the [D3DFORMAT](d3dformat.md) enumerated type that specifies the size of each index.

-   The fourth parameter is a member of the [**D3DPOOL**](./d3dpool.md) enumerated type that tells the system where in memory to place the new index buffer.

-   The final parameter that [**IDirect3DDevice9::CreateIndexBuffer**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-createindexbuffer) accepts is the address of a variable that is filled with a pointer to the new [**IDirect3DIndexBuffer9**](/windows/win32/api/d3d9helper/nn-d3d9helper-idirect3dindexbuffer9) interface of the vertex buffer object, if the call succeeds.

The following C++ code example shows what creating an index buffer might look like in code.


```
/*
 * For the purposes of this example, the d3dDevice variable is the 
 * address of an IDirect3DDevice9 interface exposed by a 
 * Direct3DDevice object, g_IB is a variable of type 
 * LPDIRECT3DINDEXBUFFER9.
 */

if( FAILED( d3dDevice->CreateIndexBuffer( 16384 *sizeof(WORD),
           D3DUSAGE_WRITEONLY, D3DFMT_INDEX16, D3DPOOL_DEFAULT, 
           &g_IB, NULL ) ) )
    return E_FAIL;
```



## Access an Index Buffer

Index buffer objects enable applications to directly access the memory allocated for index data. You can retrieve a pointer to index buffer memory by calling the [**IDirect3DIndexBuffer9::Lock**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3dindexbuffer9-lock) method, and then accessing the memory as needed to fill the buffer with new index data or to read any data it contains. The Lock method accepts four parameters. The first, *OffsetToLock*, is the offset into the index data. The second parameter is the size, measured in bytes, of the index data. The third parameter accepted by the **IDirect3DIndexBuffer9::Lock** method, *ppbData*, is the address of a BYTE pointer filled with a pointer to the index data, if the call succeeds.

The last parameter, *Flags*, tells the system how the memory should be locked. You can use it to indicate how the application accesses the data in the buffer. Specify constants for the *Flags* parameter according to the way the index data will be accessed by your application. This allows the driver to lock the memory and provide the best performance given the requested access type. Use D3DLOCK\_READONLY flag if your application will read only from the index buffer memory. Including this flag enables Direct3D to optimize its internal procedures to improve efficiency, given that access to the memory will be read-only.

After you fill or read the index data, call the [**IDirect3DIndexBuffer9::Unlock**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3dindexbuffer9-unlock) method, as shown in the following code example.


```
// This code example assumes the m_pIndexBuffer is a variable of type 
// LPDIRECT3DINDEXBUFFER9 and that g_Indices has been properly 
// initialized with indices.

// To fill the index buffer, you must lock the buffer to gain 
// access to the indices. This mechanism is required because index
// buffers may be in device memory.

VOID* pIndices;

if( FAILED( m_pIndexBuffer->Lock( 
      0,                 // Fill from start of the buffer
      sizeof(g_Indices), // Size of the data to load
      BYTE**)&pIndices,  // Returned index data
      0 ) ) )            // Send default flags to the lock
{
    SAFE_RELEASE(m_pIndexBuffer);
    return E_FAIL;
}

memcpy( pIndices, g_Indices, sizeof(g_Indices) );
m_pIndexBuffer->Unlock();
```



> [!Note]
>
> If you create an index buffer with the D3DUSAGE\_WRITEONLY flag, do not use the D3DLOCK\_READONLY locking flag. Use the D3DLOCK\_READONLY flag if your application will read only from the index buffer memory. Including this flag enables Direct3D to optimize its internal procedures to improve efficiency, given that access to the memory will be read-only.
>
> For information about using D3DLOCK\_DISCARD or D3DLOCK\_NOOVERWRITE for the *Flags* parameter of the [**IDirect3DIndexBuffer9::Lock**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3dindexbuffer9-lock) method, see [Performance Optimizations (Direct3D 9)](performance-optimizations.md).

 

In C++, because you directly access the memory allocated for the index buffer, make sure your application properly accesses the allocated memory. Otherwise, you risk rendering that memory invalid. Use the stride of the index format your application uses to move from one index in the allocated buffer to another.

Retrieve information about an index buffer by calling the [**IDirect3DIndexBuffer9::GetDesc**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3dindexbuffer9-getdesc) method. This method fills the members of the [**D3DINDEXBUFFER\_DESC**](d3dindexbuffer-desc.md) structure with information about the index buffer.

## Related topics

<dl> <dt>

[Direct3D Resources](direct3d-resources.md)
</dt> <dt>

[Rendering from Vertex and Index Buffers (Direct3D 9)](rendering-from-vertex-and-index-buffers.md)
</dt> <dt>

[Vertex Buffers (Direct3D 9)](vertex-buffers.md)
</dt> </dl>

 

 
