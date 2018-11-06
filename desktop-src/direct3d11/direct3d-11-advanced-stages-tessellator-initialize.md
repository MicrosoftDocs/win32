---
title: How To Initialize the Tessellator Stage
description: This topic shows how to initialize the tessellator stage.
ms.assetid: 81f5461a-0938-4c46-b3e8-bef2bea125a5
ms.topic: article
ms.date: 05/31/2018
---

# How To: Initialize the Tessellator Stage

In general, tessellation expands the compact, user-defined, model of a patch into geometry that contains a programmable amount of detail. The geometry is typically a set of triangles that represents detailed surface geometry. This topic shows how to initialize the tessellator stage.

The tessellator stage is the second of three stages that work together to tessellate or tile a surface. The first stage is the hull-shader stage; it operates once per patch and configures how the next stage (the fixed function tessellator) behaves. A hull shader also generates user-defined outputs such as output-control points and patch constants that are sent past the tessellator directly to the third stage, the domain-shader stage. A domain shader is invoked once per tessellator-stage point and evaluates surface positions.

The tessellator stage is a fixed function stage, there is no shader to generate, and no state to set. It receives all of its setup state from the hull-shader stage; once the hull-shader stage has been initialized, the tessellator stage is automatically initialized.

**To initialize the tessellator stage**

-   Initialize the hull-shader stage using [**ID3D11DeviceContext::HSSetShader**](/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-hssetshader).

    ```
    void HSSetShader(
      ID3D11HullShader *pHullShader,  
      ID3D11ClassInstance *const *ppClassInstances,
      UINT NumClassInstances
    );
    ```

    

    *ppClassInstances* is a pointer to an array of shader interfaces, represented by [**ID3D11ClassInstance**](/windows/desktop/api/D3D11/nn-d3d11-id3d11classinstance) pointers and the number of interfaces, represented by *NumClassInstances*. If not used, these parameters can be set to **NULL** and 0 respectively.

After the hull-shader stage is initialized, you should also initialize the domain-shader stage.

## Related topics

<dl> <dt>

[How to Use Direct3D 11](how-to-use-direct3d-11.md)
</dt> <dt>

[Tessellation Overview](direct3d-11-advanced-stages-tessellation.md)
</dt> </dl>

 

 




