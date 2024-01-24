---
description: Every developer who creates real-time applications that use 3D graphics is concerned about performance optimization. This section provides guidelines for getting the best performance from your code.
ms.assetid: 074f848e-4a42-48a2-adf7-4026b8967413
title: Performance Optimizations (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Performance Optimizations (Direct3D 9)

Every developer who creates real-time applications that use 3D graphics is concerned about performance optimization. This section provides guidelines for getting the best performance from your code.

-   [General Performance Tips](#general-performance-tips)
-   [Databases and Culling](#databases-and-culling)
-   [Batching Primitives](#batching-primitives)
-   [Lighting Tips](#lighting-tips)
-   [Texture Size](#texture-size)
-   [Matrix Transforms](#matrix-transforms)
-   [Using Dynamic Textures](#using-dynamic-textures)
-   [Using Dynamic Vertex and Index Buffers](#using-dynamic-vertex-and-index-buffers)
-   [Using Meshes](#using-meshes)
-   [Z-Buffer Performance](#z-buffer-performance)

## General Performance Tips

-   Clear only when you must.
-   Minimize state changes and group the remaining state changes.
-   Use smaller textures, if you can do so.
-   Draw objects in your scene from front to back.
-   Use triangle strips instead of lists and fans. For optimal vertex cache performance, arrange strips to reuse triangle vertices sooner, rather than later.
-   Gracefully degrade special effects that require a disproportionate share of system resources.
-   Constantly test your application's performance.
-   Minimize vertex buffer switches.
-   Use static vertex buffers where possible.
-   Use one large static vertex buffer per FVF for static objects, rather than one per object.
-   If your application needs random access into the vertex buffer in AGP memory, choose a vertex format size that is a multiple of 32 bytes. Otherwise, select the smallest appropriate format.
-   Draw using indexed primitives. This can allow for more efficient vertex caching within hardware.
-   If the depth buffer format contains a stencil channel, always clear the depth and stencil channels at the same time.
-   Combine the shader instruction and the data output where possible. For example:
    ```
    // Rather than doing a multiply and add, and then output the data with 
    //   two instructions:
    mad r2, r1, v0, c0
    mov oD0, r2

    // Combine both in a single instruction, because this eliminates an  
    //   additional register copy.
    mad oD0, r1, v0, c0 
    ```

    

## Databases and Culling

Building a reliable database of the objects in your world is key to excellent performance in Direct3D. It is more important than improvements to rasterization or hardware.

You should maintain the lowest polygon count you can possibly manage. Design for a low polygon count by building low-polygon models from the start. Add polygons if you can do so without sacrificing performance later in the development process. Remember, the fastest polygons are the ones you don't draw.

## Batching Primitives

To get the best rendering performance during execution, try to work with primitives in batches and keep the number of render-state changes as low as possible. For example, if you have an object with two textures, group the triangles that use the first texture and follow them with the necessary render state to change the texture. Then group all the triangles that use the second texture. The simplest hardware support for Direct3D is called with batches of render states and batches of primitives through the hardware abstraction layer (HAL). The more effectively the instructions are batched, the fewer HAL calls are performed during execution.

## Lighting Tips

Because lights add a per-vertex cost to each rendered frame, you can improve performance significantly by being careful about how you use them in your application. Most of the following tips derive from the maxim, "the fastest code is code that is never called."

-   Use as few light sources as possible. To increase the overall lighting level, for example, use the ambient light instead of adding a new light source.
-   Directional lights are more efficient than point lights or spotlights. For directional lights, the direction to the light is fixed and doesn't need to be calculated on a per-vertex basis.
-   Spotlights can be more efficient than point lights, because the area outside the cone of light is calculated quickly. Whether spotlights are more efficient or not depends on how much of your scene is lit by the spotlight.
-   Use the range parameter to limit your lights to only the parts of the scene you need to illuminate. All the light types exit fairly early when they are out of range.
-   Specular highlights almost double the cost of a light. Use them only when you must. Set the D3DRS\_SPECULARENABLE render state to 0, the default value, whenever possible. When defining materials, you must set the specular power value to zero to turn off specular highlights for that material; just setting the specular color to 0,0,0 is not enough.

## Texture Size

Texture-mapping performance is heavily dependent on the speed of memory. There are a number of ways to maximize the cache performance of your application's textures.

-   Keep the textures small. The smaller the textures are, the better chance they have of being maintained in the main CPU's secondary cache.
-   Do not change the textures on a per-primitive basis. Try to keep polygons grouped in order of the textures they use.
-   Use square textures whenever possible. Textures whose dimensions are 256x256 are the fastest. If your application uses four 128x128 textures, for example, try to ensure that they use the same palette and place them all into one 256x256 texture. This technique also reduces the amount of texture swapping. Of course, you should not use 256x256 textures unless your application requires that much texturing because, as mentioned, textures should be kept as small as possible.

## Matrix Transforms

Direct3D uses the world and view matrices that you set to configure several internal data structures. Each time you set a new world or view matrix, the system recalculates the associated internal structures. Setting these matrices frequently - for example, thousands of times per frame - is computationally time-consuming. You can minimize the number of required calculations by concatenating your world and view matrices into a world-view matrix that you set as the world matrix, and then setting the view matrix to the identity. Keep cached copies of individual world and view matrices so that you can modify, concatenate, and reset the world matrix as needed. For clarity in this documentation, Direct3D samples rarely employ this optimization.

## Using Dynamic Textures

To find out if the driver supports dynamic textures, check the D3DCAPS2\_DYNAMICTEXTURES flag of the [**D3DCAPS9**](/windows/desktop/api/D3D9Caps/ns-d3d9caps-d3dcaps9) structure.

Keep the following things in mind when working with dynamic textures.

-   They cannot be managed. For example, their pool cannot be D3DPOOL\_MANAGED.
-   Dynamic textures can be locked, even if they are created in D3DPOOL\_DEFAULT.
-   D3DLOCK\_DISCARD is a valid lock flag for dynamic textures.

It is a good idea to create only one dynamic texture per format and possibly per size. Dynamic mipmaps, cubes, and volumes are not recommended because of the additional overhead in locking every level. For mipmaps, D3DLOCK\_DISCARD is allowed only on the top level. All levels are discarded by locking just the top level. This behavior is the same for volumes and cubes. For cubes, the top level and face 0 are locked.

The following pseudocode shows an example of using a dynamic texture.


```
DrawProceduralTexture(pTex)
{
    // pTex should not be very small because overhead of 
    //   calling driver every D3DLOCK_DISCARD will not 
    //   justify the performance gain. Experimentation is encouraged.
    pTex->Lock(D3DLOCK_DISCARD);
    <Overwrite *entire* texture>
    pTex->Unlock();
    pDev->SetTexture();
    pDev->DrawPrimitive();
}
```



## Using Dynamic Vertex and Index Buffers

Locking a static vertex buffer while the graphics processor is using the buffer can have a significant performance penalty. The lock call must wait until the graphics processor is finished reading vertex or index data from the buffer before it can return to the calling application, a significant delay. Locking and then rendering from a static buffer several times per frame also prevents the graphics processor from buffering rendering commands, since it must finish commands before returning the lock pointer. Without buffered commands, the graphics processor remains idle until after the application is finished filling the vertex buffer or index buffer and issues a rendering command.

Ideally the vertex or index data would never change, however this is not always possible. There are many situations where the application needs to change vertex or index data every frame, perhaps even multiple times per frame. For these situations, the vertex or index buffer should be created with D3DUSAGE\_DYNAMIC. This usage flag causes Direct3D to optimize for frequent lock operations. D3DUSAGE\_DYNAMIC is only useful when the buffer is locked frequently; data that remains constant should be placed in a static vertex or index buffer.

To receive a performance improvement when using dynamic vertex buffers, the application must call [**IDirect3DVertexBuffer9::Lock**](/windows/desktop/api) or [**IDirect3DIndexBuffer9::Lock**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3dindexbuffer9-lock) with the appropriate flags. D3DLOCK\_DISCARD indicates that the application does not need to keep the old vertex or index data in the buffer. If the graphics processor is still using the buffer when lock is called with D3DLOCK\_DISCARD, a pointer to a new region of memory is returned instead of the old buffer data. This allows the graphics processor to continue using the old data while the application places data in the new buffer. No additional memory management is required in the application; the old buffer is reused or destroyed automatically when the graphics processor is finished with it. Note that locking a buffer with D3DLOCK\_DISCARD always discards the entire buffer, specifying a nonzero offset or limited size field does not preserve information in unlocked areas of the buffer.

There are cases where the amount of data the application needs to store per lock is small, such as adding four vertices to render a sprite. D3DLOCK\_NOOVERWRITE indicates that the application will not overwrite data already in use in the dynamic buffer. The lock call will return a pointer to the old data, allowing the application to add new data in unused regions of the vertex or index buffer. The application should not modify vertices or indices used in a draw operation as they might still be in use by the graphics processor. The application should then use D3DLOCK\_DISCARD after the dynamic buffer is full to receive a new region of memory, discarding the old vertex or index data after the graphics processor is finished.

The asynchronous query mechanism is useful to determine if vertices are still in use by the graphics processor. Issue a query of type D3DQUERYTYPE\_EVENT after the last DrawPrimitive call that uses the vertices. The vertices are no longer in use when [**IDirect3DQuery9::GetData**](/windows/desktop/api) returns S\_OK. Locking a buffer with D3DLOCK\_DISCARD or no flags will always guarantee the vertices are synchronized properly with the graphics processor, however using lock without flags will incur the performance penalty described earlier. Other API calls such as [**IDirect3DDevice9::BeginScene**](/windows/desktop/api), [**IDirect3DDevice9::EndScene**](/windows/desktop/api), and [**IDirect3DDevice9::Present**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-present) do not guarantee the graphics processor is finished using vertices.

Below are ways to use dynamic buffers and the proper lock flags.


```
    // USAGE STYLE 1
    // Discard the entire vertex buffer and refill with thousands of vertices.
    // Might contain multiple objects and/or require multiple DrawPrimitive 
    //   calls separated by state changes, etc.
 
    // Determine the size of data to be moved into the vertex buffer.
    UINT nSizeOfData = nNumberOfVertices * m_nVertexStride;
 
    // Discard and refill the used portion of the vertex buffer.
    CONST DWORD dwLockFlags = D3DLOCK_DISCARD;
    
    // Lock the vertex buffer.
    BYTE* pBytes;
    if( FAILED( m_pVertexBuffer->Lock( 0, 0, &pBytes, dwLockFlags ) ) )
        return false;
    
    // Copy the vertices into the vertex buffer.
    memcpy( pBytes, pVertices, nSizeOfData );
    m_pVertexBuffer->Unlock();
 
    // Render the primitives.
    m_pDevice->DrawPrimitive( D3DPT_TRIANGLELIST, 0, nNumberOfVertices/3)
```




```
    // USAGE STYLE 2
    // Reusing one vertex buffer for multiple objects
 
    // Determine the size of data to be moved into the vertex buffer.
    UINT nSizeOfData = nNumberOfVertices * m_nVertexStride;
 
    // No overwrite will be used if the vertices can fit into 
    //   the space remaining in the vertex buffer.
    DWORD dwLockFlags = D3DLOCK_NOOVERWRITE;
    
    // Check to see if the entire vertex buffer has been used up yet.
    if( m_nNextVertexData > m_nSizeOfVB - nSizeOfData )
    {
        // No space remains. Start over from the beginning 
        //   of the vertex buffer.
        dwLockFlags = D3DLOCK_DISCARD;
        m_nNextVertexData = 0;
    }
    
    // Lock the vertex buffer.
    BYTE* pBytes;
    if( FAILED( m_pVertexBuffer->Lock( (UINT)m_nNextVertexData, nSizeOfData, 
               &pBytes, dwLockFlags ) ) )
        return false;
    
    // Copy the vertices into the vertex buffer.
    memcpy( pBytes, pVertices, nSizeOfData );
    m_pVertexBuffer->Unlock();
 
    // Render the primitives.
    m_pDevice->DrawPrimitive( D3DPT_TRIANGLELIST, 
               m_nNextVertexData/m_nVertexStride, nNumberOfVertices/3)
 
    // Advance to the next position in the vertex buffer.
    m_nNextVertexData += nSizeOfData;
```



## Using Meshes

You can optimize meshes by using Direct3D indexed triangles instead of indexed triangle strips. The hardware will discover that 95 percent of successive triangles actually form strips and adjust accordingly. Many drivers do this for older hardware also.

D3DX mesh objects can have each triangle, or face, tagged with a DWORD, called the attribute of that face. The semantics of the DWORD are user-defined. They are used by D3DX to classify the mesh into subsets. The application sets per-face attributes using the [**ID3DXMesh::LockAttributeBuffer**](id3dxmesh--lockattributebuffer.md) call. The [**ID3DXMesh::Optimize**](id3dxmesh--optimize.md) method has an option to group the mesh vertices and faces on attributes using the D3DXMESHOPT\_ATTRSORT option. When this is done, the mesh object calculates an attribute table that can be obtained by the application by calling [**ID3DXBaseMesh::GetAttributeTable**](id3dxbasemesh--getattributetable.md). This call returns 0 if the mesh is not sorted by attributes. There is no way for an application to set an attribute table because it is generated by the **ID3DXMesh::Optimize** method. The attribute sort is data sensitive, so if the application knows that a mesh is attribute sorted, it still needs to call **ID3DXMesh::Optimize** to generate the attribute table.

The following topics describe the different attributes of a mesh.

### Attribute ID

An attribute id is a value that associates a group of faces with an attribute group. This id describes which subset of faces [**ID3DXBaseMesh::DrawSubset**](id3dxbasemesh--drawsubset.md) should draw. Attribute ids are specified for the faces in the attribute buffer. The actual values of the attribute ids can be anything that fits in 32 bits, but it is common to use 0 to n where n is the number of attributes.

### Attribute Buffer

The attribute buffer is an array of DWORDs (one per face) that specifies which attribute group each face belongs in. This buffer is initialized to zero on creation of a mesh, but is either filled by the load routines or must be filled by the user if more than one attribute with id 0 is desired. This buffer contains the information that is used to sort the mesh based on attributes in [**ID3DXMesh::Optimize**](id3dxmesh--optimize.md). If no attribute table is present, [**ID3DXBaseMesh::DrawSubset**](id3dxbasemesh--drawsubset.md) scans this buffer to select the faces of the given attribute to draw.

### Attribute Table

The attribute table is a structure owned and maintained by the mesh. The only way for one to be generated is by calling [**ID3DXMesh::Optimize**](id3dxmesh--optimize.md) with attribute sorting or stronger optimization enabled. The attribute table is used to quickly initiate a single draw primitive call to [**ID3DXBaseMesh::DrawSubset**](id3dxbasemesh--drawsubset.md). The only other use is that progressing meshes also maintain this structure, so it is possible to see what faces and vertices are active at the current level of detail.

## Z-Buffer Performance

Applications can increase performance when using z-buffering and texturing by ensuring that scenes are rendered from front to back. Textured z-buffered primitives are pretested against the z-buffer on a scan line basis. If a scan line is hidden by a previously rendered polygon, the system rejects it quickly and efficiently. Z-buffering can improve performance, but the technique is most useful when a scene draws the same pixels more than once. This is difficult to calculate exactly, but you can often make a close approximation. If the same pixels are drawn less than twice, you can achieve the best performance by turning z-buffering off and rendering the scene from back to front.

## Related topics

<dl> <dt>

[Programming Tips](programming-tips.md)
</dt> </dl>

 

 
