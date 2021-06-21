---
title: Fragment Declaration Syntax (Direct3D 9 HLSL)
description: Each Microsoft High Level Shader Language (HLSL) function can be converted into a shader fragment with the addition of a fragment declaration.
ms.assetid: 34ceef8c-8fb9-4c73-86cc-014b7a2ee4d7
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Fragment Declaration Syntax (Direct3D 9 HLSL)

Each Microsoft High Level Shader Language (HLSL) function can be converted into a shader fragment with the addition of a fragment declaration.

## Syntax


```
fragmentKeyword FragmentName = compile_fragment shaderProfile FunctionName();
```



where:



| Value                  | Description                                                                                                                                                                                                                                                      |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| fragmentKeyword   | Required keyword. Either pixelfragment or vertexfragment.                                                                                                                                                                                             |
| FragmentName      | An ASCII text string that specifies the compiled fragment name.                                                                                                                                                                                       |
| compile\_fragment | Required keyword.                                                                                                                                                                                                                                     |
| shaderProfile     | The shader model to compile against. Any valid vertex shader profile (see [**D3DXGetVertexShaderProfile**](/windows/desktop/direct3d9/d3dxgetvertexshaderprofile)) or pixel shader profile (see [**D3DXGetPixelShaderProfile**](/windows/desktop/direct3d9/d3dxgetpixelshaderprofile)). |
| FunctionName()    | The shader function name, followed by parentheses.                                                                                                                                                                                                    |



 

Shared fragment parameters are marked by adding an 'r\_' prefix to their semantic.


```
void AmbientDiffuse( float3 vPosWorld: r_PosWorld,
                     float3 vNormalWorld: r_NormalWorld,
                     out float4 vColor: COLOR0 )
{  
    // Compute the light vector
    float3 vLight = normalize( g_vLightPosition - vPosWorld );
    
    // Compute the ambient and diffuse components of illumination
    vColor = g_vLightColor * g_vMaterialAmbient;
    vColor += g_vLightColor * g_vMaterialDiffuse * saturate( dot( vLight, vNormalWorld ) );
}
vertexfragment AmbientDiffuseFragment = compile_fragment vs_1_1 AmbientDiffuse();
```



In this example, the r\_PosWorld and r\_NormalWorld semantics identify that these two parameters are shared parameters among other fragments.

> [!Note]  
> Fragment linker was a Microsoft Direct3D 9 technology in D3DX 9. Fragment linker was a tool (Flink.exe), a D3DX 9 API, and an HLSL enhancement. Fragment linker was dropped as of the August 2009 DirectX SDK release. Fragment linker never applied to Microsoft Direct3D 10, Microsoft Direct3D 10.1, or Microsoft Direct3D 11.

 

## Related topics

<dl> <dt>

[Shader Model 3 (DirectX HLSL)](dx-graphics-hlsl-sm3.md)
</dt> </dl>

 

 
