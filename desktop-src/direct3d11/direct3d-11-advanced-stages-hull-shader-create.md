---
title: How To Create a Hull Shader
description: This topic shows how to create a hull shader.
ms.assetid: 221cb578-fcfc-411a-8515-7880a96e32ce
ms.topic: article
ms.date: 05/31/2018
---

# How To: Create a Hull Shader

A hull shader is the first of three stages that work together to implement [tessellation](direct3d-11-advanced-stages-tessellation.md). The hull-shader outputs drive the tessellator stage, as well as the domain-shader stage. This topic shows how to create a hull shader.

A hull shader transforms a set of input control points (from a vertex shader) into a set of output control points. The number of input and output points can vary in contents and number depending on the transform (a typical transformation would be a basis transformation).

A hull shader also outputs patch constant information, such as tessellation factors, for a domain shader and the tessellator. The fixed-function tessellator stage uses the tessellation factors as well as other state declared in a hull shader to determine how much to tessellate.

**To create a hull shader**

1.  Design a hull shader. See [How To: Design a Hull Shader](direct3d-11-advanced-stages-hull-shader-design.md).
2.  Compile the shader code
3.  Create a hull-shader object using [**ID3D11Device::CreateHullShader**](/windows/desktop/api/D3D11/nf-d3d11-id3d11device-createhullshader).
    ```
    HRESULT CreateHullShader(
      const void *pShaderBytecode,  
      SIZE_T BytecodeLength,  
      ID3D11ClassLinkage *pClassLinkage,  
      ID3D11HullShader **ppHullShader
    );
    ```

    

4.  Initialize the pipeline stage using [**ID3D11DeviceContext::HSSetShader**](/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-hssetshader).
    ```
    void HSSetShader(
      ID3D11HullShader *pHullShader,  
      ID3D11ClassInstance *const *ppClassInstances,
      UINT NumClassInstances
    );
    ```

    

A domain shader must be bound to the pipeline if a hull shader is bound. In particular, it is not valid to directly stream out hull shader control points with the geometry shader.

## Related topics

<dl> <dt>

[How to Use Direct3D 11](how-to-use-direct3d-11.md)
</dt> <dt>

[Tessellation Overview](direct3d-11-advanced-stages-tessellation.md)
</dt> </dl>

 

 




