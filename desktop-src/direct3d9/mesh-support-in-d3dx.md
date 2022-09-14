---
description: Learn about mesh support in D3DX. D3DX is a utility library that provides helper services. It is a layer above the Direct3D component.
ms.assetid: 7892370f-0807-4ab7-b7cd-a7e1182e3f9c
title: Mesh Support in D3DX (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Mesh Support in D3DX (Direct3D 9)

D3DX is a utility library that provides helper services. It is a layer above the Direct3D component.

## Meshes

D3DX implements the mesh construct to load, manipulate, and render .x file contents. A mesh is basically a collection of vertices defining some geometry, and a set of indices defining the faces. There are several mesh types.

[**ID3DXBaseMesh**](id3dxbasemesh.md) provides the fundamentals. [**ID3DXMesh**](id3dxmesh.md) inherits from ID3DXBaseMesh, and adds mesh optimization using per-chip vertex cache. [**ID3DXSkinInfo**](id3dxskininfo.md) provides skinned mesh support.

[**ID3DXBaseMesh**](id3dxbasemesh.md) provides methods to manipulate and query [**ID3DXMesh**](id3dxmesh.md) mesh objects, which inherit from the base mesh. This includes adjacency operations, geometry buffer retrieval, lock/unlock operations (vertex and index), and copying, rendering, face, and vertex information.

> [!Note]  
> The ID3DXPMesh and ID3DXSPMesh interfaces (to support progressive and simplified meshes, respectively) available in earlier releases of Direct3D 9 have been dropped.

 

## Mesh Architecture

A mesh contains the data for a complex model. It is an abstract data container that contains resources such as textures and materials, and attributes such as position data and adjacency data. There are several mesh operations that improve drawing performance and the appearance of a surface. In addition, there are a number of other mesh concepts that will effect the functionality of mesh operations. Understanding these mesh concepts so you can apply them will improve mesh performance.

## Mesh Object Data

A mesh contains a vertex buffer, an index buffer, and an attribute buffer.

-   The vertex buffer contains the vertex data, which are the mesh vertices.
-   The index buffer contains vertex indices for accessing the vertex buffer. This can reduce the vertex buffer size by reducing duplicate vertices. Only an indexed mesh uses the index buffer. If a mesh is made up of a triangle list, for example, it does not use the index buffer.
-   The attribute buffer contains attribute data. Attributes are properties of the mesh vertices, in no particular order. A D3DX mesh stores attributes in a group of DWORDS, for each face.

### Attribute Tables

An attribute table is a concise representation of the contents of an attribute buffer. Attribute tables can be created by calling one of the Optimize methods with D3DXMESHOPT\_ATTRSORT, by locking the attribute buffer and filling it with data, or by calling SetAttributeTable. A mesh contains an attribute table when the mesh is reordered into groups. This happens when Optimize is called, assuming an attribute sorting option (D3DXMESHOPT\_ATTRSORT or higher) is supplied. D3DX Meshes use indexed triangle lists, and are therefore drawn with [**IDirect3DDevice9::DrawIndexedPrimitive**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-drawindexedprimitive).

Attribute tables are created as a result of calling Optimize. The faces don't have to be adjacent, because Optimize will reorder them to be adjacent. For example, the hands of a human mesh could use the same attribute. The id helps sort the faces into groups. Meshes from .x files have automatically generated attributes for material and texture properties. You do need to call Optimize(ATTRSORT) or the more effective Optimize(VERTEXCACHE) to get good performance. The load functions try to present the data in the exact form it was saved out in. If you are using a vertex buffer/index buffer based mesh, the mesh API provides optimization functions and skinning transformations with little overhead.

The optimization types are cumulative, starting from the least optimal (D3DXMESHOPT\_COMPACT) to the most optimal (D3DXMESHOPT\_IGNOREVERTS). D3DXMESHOPT\_STRIPREORDER does a compaction and attribute sort. D3DXMESHOPT\_VERTEXCACHE is always recommended, even on devices without a true vertex cache.

## Application Data

Application data is mesh data that is managed by an application. There is a tight coupling between the mesh vertex data and the data managed by these buffers.

The materials buffer contains n materials. The materials are returned by the Load function when the .x file is loaded. Each subset can have its own materials and textures. The materials buffer is static.

The adjacency buffer contains information about edges, faces, and adjacent faces. Some mesh operations depend on knowing which faces are adjacent to each other. This information, called adjacency data, is kept in an adjacency buffer. It is not part of the mesh but is maintained by the application and must be supplied to the mesh methods when necessary.

The effects instance buffer contains a list of effect instances. An effect instance stores state. This state information is used to initialize the pipeline. An effect instance contains name-value pairs in an effect.

## Advanced Mesh Topics

Optimized meshes build on the base mesh functionality and add vertex-cache optimization capability with two methods: Optimize, which creates a new mesh, and OptimizeInPlace, which modifies the original mesh.

D3DXGeneratePMesh uses the D3DX simplification algorithm to generate a progressive mesh from the input mesh. D3DXSimplifyMesh generates a standard mesh of the given level-of-detail from an input mesh using the same simplification algorithm. The user has control over the error metric used through the weights specified per-vertex component and weights specified per vertex. Per-component weights are multiplied against that components portion of error calculated per edge collapse. Per-vertex weights are multiplied against the error metric value determined for removal of that vertex. For example, if you never want a vertex to be removed, set that specific vertex's weight to a large value. Conversely, if you want it removed earlier, set it to a small value (less than 1).

[**ID3DXSkinInfo**](id3dxskininfo.md) supports skinned characters. A skinned character is defined by a set of meshes and a set of bones that affect the vertices of the meshes. The bones are represented as a transform hierarchy. For each mesh, there is a matrix for every bone that affects it, which transforms the mesh into the local coordinate space of the bone. This matrix is the bone-space transform of the bone for the mesh. This is defined at the time the skeleton is associated with the mesh in the authoring process.

### Skinning

Skinning is a technique for transforming mesh vertices using bones. Bones are typically arranged in a hierarchical skeleton, much like the bones in a human body. Object vertices are then associated with the bones, like attaching skin to the bones. When the bones get transformed, the skin is also transformed.

Skinned meshes use bones to influence a number of vertices. Bone transformation data is supplied by the user, to influence how to SRT the bones. The mesh uses the transformed bones to influence the vertices associated with the bones. Palettes are arrays of SRT transformations. Palettes are often implemented as matrices, but they can contain SRT values.

### Progressive Mesh Trimming

Low detail areas can afford to lose vertices which don't change the rendered appearance of the surface. This is especially true of objects as they move farther from the camera. This is referred to as level-of-detail. Users have API-level render controls for setting the level-of-detail to maximize rendering efficiency.

Progressive mesh objects start with a high number of faces and use simplification to reduce the number of faces. A progressive mesh that is view independent is referred to as a view-independent progressive mesh (VIPM).

Another way to reduce the number of faces is by trimming. This actually removes vertices and faces from the mesh. Trimming can be done at the high end (to limit the max number of faces) or at the low end (to limit the minimum number of faces.) Trimming improves draw performance, however, care should be used to preserve the visual quality. Trimming is demonstrated in the Progressive Mesh SDK Sample.

For high visibility areas, the resolution can be increased using progressive level of detail (PLOD). This is a technique for breaking a single face into two faces.

### Patch Meshes

Two specialized types of patch meshes are also supported: rectangle and triangle patches. The rectangle patch mesh is a patch mesh whose control points are laid out in a winding, rectangular sequence. Rectangle and triangle patches are used to create high-order surfaces. They are not as commonly used as triangle meshes.

## Related topics

<dl> <dt>

[D3DX](d3dx.md)
</dt> </dl>

 

 
