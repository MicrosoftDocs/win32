---
description: All resources share the following properties.
ms.assetid: 6ef6ce68-44fa-4964-8b61-2a37382eda1c
title: Resource Properties (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Resource Properties (Direct3D 9)

All resources share the following properties.

-   Usage. The way a resource is used, for example, as a texture or a render target.
-   Format. The format of the data, for example, the pixel format of a 2D surface.
-   Pool. The type of memory where the resource is allocated.
-   Type. The type of resource, for example, a vertex buffer or render target.

Resource uses are enforced. An application that will use a resource in a certain operation must specify that operation at resource-creation time. For a list of the usage constants defined for resources, see [**D3DUSAGE**](d3dusage.md).

The D3DUSAGE\_RTPATCHES, D3DUSAGE\_NPATCHES, and D3DUSAGE\_POINTS constants indicate to the driver that the data in these buffers is likely to be used for triangular or grid patches, N-patches, or point sprites, respectively. These flags are provided in case the hardware cannot perform these operations without host processing. Therefore, the driver will want to allocate these surfaces in system memory so that the CPU can access them. If the driver can perform these operations entirely in hardware, it can allocate these surfaces in video or AGP memory to avoid a host copy and improve performance at least twofold. Note that the information provided by these flags is not absolutely required. A driver can detect that such operations are being performed on the data, and it will move the buffer back to system memory for subsequent frames.

For details about the usage flags and how they relate to specific resources, see the reference pages on the individual resource creation methods.

For information about the surface format of resources, see the [D3DFORMAT](d3dformat.md) enumerated type.

The class of memory that holds a resource's buffers is called a pool. Pool values are defined by the [**D3DPOOL**](./d3dpool.md) enumerated type. A pool cannot be mixed for different objects contained in a single resource - that is, mip levels in a mipmap - and, when a pool is chosen for a resource, the pool cannot be changed.

The resources types are set implicitly at run time when the application calls a resource creation method such as [**IDirect3DDevice9::CreateCubeTexture**](/windows/desktop/api). Resource types are defined by the [**D3DRESOURCETYPE**](./d3dresourcetype.md) enumerated type. Applications can query these types at run time; however, it is expected that most scenarios will not require run-time type checking.

## Related topics

<dl> <dt>

[Direct3D Resources](direct3d-resources.md)
</dt> </dl>

 

 
