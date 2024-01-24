---
description: Vertex buffer objects enable applications to directly access the memory allocated for vertex data.
ms.assetid: 63d255b7-fa7d-411b-9cdb-52113f30c933
title: Accessing the Contents of a Vertex Buffer (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Accessing the Contents of a Vertex Buffer (Direct3D 9)

Vertex buffer objects enable applications to directly access the memory allocated for vertex data. You can retrieve a pointer to vertex buffer memory by calling the [**IDirect3DVertexBuffer9::Lock**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3dvertexbuffer9-lock) method, and then accessing the memory as needed to fill the buffer with new vertex data or to read any data it already contains. The **IDirect3DVertexBuffer9::Lock** method accepts four parameters. The first, *OffsetToLock*, is the offset into the vertex data. The second parameter is the size, measured in bytes, of the vertex data. The third parameter accepted is the address of a pointer that points to the vertex data, if the call succeeds.

The last parameter, *Flags*, tells the system how the memory should be locked. Specify constants for the *Flags* parameter according to the way the vertex data will be accessed. Make sure the value chosen for [**D3DUSAGE**](d3dusage.md) matches the value chosen for [D3DLOCK](d3dlock.md). For example, if you are creating a vertex buffer with write access only, it doesn't make sense to try to read the data by specifying D3DLOCK\_READONLY. Wisely using these flags allows the driver to lock the memory and provide the best performance, given the requested access type.

After you finish filling or reading the vertex data, call the [**IDirect3DVertexBuffer9::Unlock**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3dvertexbuffer9-unlock) method, as shown in the following code example.


```
// This code example assumes the g_pVB is a variable of type 
//   LPDIRECT3DVERTEXBUFFER9 and that g_Vertices has been  
//   properly initialized with vertices

// Lock the buffer to gain access to the vertices 
VOID* pVertices;

if(FAILED(g_pVB->Lock(0, sizeof(g_Vertices), 
        (BYTE**)&pVertices, 0 ) ) ) 
    return E_FAIL;

memcpy(pVertices, g_Vertices, sizeof(g_Vertices));
g_pVB->Unlock();
```



If you create a vertex buffer with the D3DUSAGE\_WRITEONLY flag, do not use the D3DLOCK\_READONLY locking flag. Use the D3DLOCK\_READONLY flag if your application will read only from the vertex buffer memory. Including this flag enables Direct3D to optimize its internal procedures to improve efficiency, given that access to the memory will be read-only.

See [Using Dynamic Vertex and Index Buffers](performance-optimizations.md) for information about using D3DLOCK\_DISCARD or D3DLOCK\_NOOVERWRITE for the Flags parameter of [**IDirect3DVertexBuffer9::Lock**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3dvertexbuffer9-lock).

In C++, because you directly access the memory allocated for the vertex buffer, make sure your application properly accesses the allocated memory. Otherwise, you risk rendering that memory invalid. Use the stride of the vertex format that your application uses to move from one vertex in the allocated buffer to another. The vertex buffer memory is a simple array of vertices specified in FVF. Use the stride of whatever vertex format structure you define. You can calculate the stride of each vertex at run time by examining the [D3DFVF](d3dfvf.md) contained in the vertex buffer description. The following table shows the size for each vertex component.



| Vertex Format Flag | Size              |
|--------------------|-------------------|
| D3DFVF\_DIFFUSE    | sizeof(DWORD)     |
| D3DFVF\_NORMAL     | sizeof(float) x 3 |
| D3DFVF\_SPECULAR   | sizeof(DWORD)     |
| D3DFVF\_TEXn       | sizeof(float) x n |
| D3DFVF\_XYZ        | sizeof(float) x 3 |
| D3DFVF\_XYZRHW     | sizeof(float) x 4 |



 

The number of texture coordinates present in the vertex format is described by the D3DFVF\_TEX n flags (where n is a value from 0 to 8). Multiply the number of texture coordinate sets by the size of one set of texture coordinates, which can range from one to four floats, to calculate the memory required for that number of texture coordinates.

Use the total vertex stride to increment and decrement the memory pointer as needed to access particular vertices.

## Retrieving Vertex Buffer Descriptions

You can retrieve information about a vertex buffer by calling the [**IDirect3DVertexBuffer9::GetDesc**](/windows/desktop/api) method. This method fills the members of the [**D3DVERTEXBUFFER\_DESC**](d3dvertexbuffer-desc.md) structure with information about the vertex buffer.

## Related topics

<dl> <dt>

[Vertex Buffers](vertex-buffers.md)
</dt> </dl>

 

 
