---
description: You create a vertex buffer object by calling the IDirect3DDevice9::CreateVertexBuffer method, which accepts five parameters.
ms.assetid: 95116ef5-af88-47e7-abf7-1ade9735e2a7
title: Creating a Vertex Buffer (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Vertex Buffer (Direct3D 9)

You create a vertex buffer object by calling the [**IDirect3DDevice9::CreateVertexBuffer**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-createvertexbuffer) method, which accepts five parameters. The first parameter specifies the vertex buffer length, in bytes. Use the sizeof operator to determine the size of a vertex format, in bytes. Consider the following custom vertex format.


```
struct CUSTOMVERTEX {
        FLOAT x, y, z;
        FLOAT rhw;
        DWORD color;
        FLOAT tu, tv;   // Texture coordinates
};

// Custom flexible vertex format (FVF) describing the custom vertex structure
#define D3DFVF_CUSTOMVERTEX (D3DFVF_XYZRHW | D3DFVF_DIFFUSE | D3DFVF_TEX1)
```



To create a vertex buffer to hold four CUSTOMVERTEX structures, specify \[4\*sizeof(CUSTOMVERTEX)\] for the *Length* parameter.

The second parameter is a set of usage controls. Among other things, its value determines whether the vertex buffer is capable of containing clipping information - in the form of clip flags - for vertices that exist outside the viewing area. To create a vertex buffer that cannot contain clip flags, include the D3DUSAGE\_DONOTCLIP flag for the *Usage* parameter. The D3DUSAGE\_DONOTCLIP flag is applied only if you also indicate that the vertex buffer will contain transformed vertices - the D3DFVF\_XYZRHW flag is included in the *FVF* parameter. The [**IDirect3DDevice9::CreateVertexBuffer**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-createvertexbuffer) method ignores the D3DUSAGE\_DONOTCLIP flag if you indicate that the buffer will contain untransformed vertices (the D3DFVF\_XYZ flag). Clipping flags occupy additional memory, making a clipping-capable vertex buffer slightly larger than a vertex buffer incapable of containing clipping flags. Because these resources are allocated when the vertex buffer is created, you must request a clipping-capable vertex buffer ahead of time.

The third parameter, *FVF*, is a combination of [D3DFVF](d3dfvf.md) that describe the vertex format of the vertex buffer. If you specify 0 for this parameter, then the vertex buffer is a non-FVF vertex buffer. For more information, see [FVF Vertex Buffers (Direct3D 9)](fvf-vertex-buffers.md). The fourth parameter describes the memory class into which to place the vertex buffer.

The final parameter that [**IDirect3DDevice9::CreateVertexBuffer**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-createvertexbuffer) accepts is the address of a variable that will be filled with a pointer to the new [**IDirect3DVertexBuffer9**](/windows/win32/api/d3d9helper/nn-d3d9helper-idirect3dvertexbuffer9) interface of the vertex buffer object, if the call succeeds.

You cannot produce clip flags for a vertex buffer that was created without support for them.

The following C++ code example shows what creating a vertex buffer might look like in code.


```
   
// d3dDevice contains the address of an IDirect3DDevice9 interface
// g_pVB is a variable of type LPDIRECT3DVERTEXBUFFER9 

// The custom vertex type
struct CUSTOMVERTEX {
    FLOAT x, y, z;
    FLOAT rhw;
    DWORD color;
    FLOAT tu, tv;   // The texture coordinates
};

#define D3DFVF_CUSTOMVERTEX (D3DFVF_XYZRHW | D3DFVF_DIFFUSE | D3DFVF_TEX1)

// Create a clipping-capable vertex buffer. Allocate enough memory 
// in the default memory pool to hold three CUSTOMVERTEX 
// structures

    if( FAILED( d3dDevice->CreateVertexBuffer( 3*sizeof(CUSTOMVERTEX),
            0 /*Usage*/, D3DFVF_CUSTOMVERTEX, D3DPOOL_DEFAULT, &g_pVB, NULL ) ) )
        return E_FAIL;
```



## Related topics

<dl> <dt>

[Vertex Buffers](vertex-buffers.md)
</dt> </dl>

 

 
