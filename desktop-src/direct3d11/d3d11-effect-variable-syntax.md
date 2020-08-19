---
title: Effect Variable Syntax (Direct3D 11)
description: An effect variable is declared with the syntax described in this section.
ms.assetid: c0cfc9dd-2df3-4f38-a0e4-2e494456b3c9
ms.topic: reference
ms.date: 05/31/2018
---

# Effect Variable Syntax (Direct3D 11)

An effect variable is declared with the syntax described in this section.

## Syntax

Basic syntax:

*DataType* *VariableName* \[ *: SemanticName* \] < *Annotations* > \[ = InitialValue \];

See [Variable Syntax (DirectX HLSL)](/windows/desktop/direct3dhlsl/dx-graphics-hlsl-variable-syntax) for full syntax.



| Name         | Description                                                                                                                                                                                 |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DataType     | Any [basic](/windows/desktop/direct3dhlsl/dx-graphics-hlsl-variable-syntax), [texture](/windows/desktop/direct3dhlsl/dx-graphics-hlsl-to-type), unordered access view, shader or state block type.                            |
| VariableName | An ASCII string that uniquely identifies the name of the effect variable.                                                                                                                   |
| SemanticName | A ASCII string that denotes additional information about how a variable should be used. A semantic is an ASCII string that can be either a predefined system-value or a custom-user string. |
| Annotations  | One or more pieces of user-supplied information (metadata) that is ignored by the effect system. For syntax, see [Annotation Syntax (Direct3D 11)](d3d11-effect-annotation-syntax.md).     |
| InitialValue | The default value of the variable.                                                                                                                                                          |



 

An effect variable that is declared outside of all functions, is considered global in scope; variables declared within a function are local to that function.

## Example

This example illustrates global effect numeric variables.


```
float4 g_MaterialAmbientColor;      // Material's ambient color
float4 g_MaterialDiffuseColor;      // Material's diffuse color
float3 g_LightDir[3];               // Light's direction in world space
float4x4 g_mWorld;                  // World matrix for object
```



This example illustrates effect variables that are local to a shader function.


```
VS_OUTPUT RenderSceneVS( ... )
{
    float3 vNormalWorldSpace;
    float4 vAnimatedPos;

    // shader body
}
```



This example illustrates function parameters that have semantics.


```
VS_OUTPUT RenderSceneVS( float4 vPos : SV_POSITION,
                         float3 vNormal : NORMAL,
                         float2 vTexCoord0 : TEXCOORD0,
                         uniform int nNumLights,
                         uniform bool bTexture,
                         uniform bool bAnimate )
{
  ...
}
```



This example illustrates declaring a global texture variable.


```
Texture2D g_MeshTexture;            // Color texture for mesh
```



Sampling a texture is done with a texture sampler. To set up a sampler in an effect, see the [sampler type](/windows/desktop/direct3dhlsl/dx-graphics-hlsl-sampler).

This example illustrates declaring global unordered access view variables.


```
RWStructuredBuffer<uint> bc : register(u2) < string name="bc"; >;
RWBuffer<uint> bRW;
struct S
{
   uint key;
   uint value;
};
AppendStructuredBuffer<S> asb : register(u5);
RWByteAddressBuffer rwbab : register(u1);
RWStructuredBuffer<uint> rwsb : register(u3);
RWTexture1D<float> rwt1d : register(u1);
RWTexture1DArray<uint> rwt1da : register(u4);
RWTexture2D<uint> rwt2d : register(u2);
RWTexture2DArray<uint> rwt2da : register(u6);
RWTexture3D<uint> rwt3d : register(u7); 
 This example illustrates declaring global shader variables.
VertexShader pVS = CompileShader( vs_5_0, VS() );
HullShader pHS = NULL;
DomainShader pDS = NULL;
GeometryShader pGS = ConstructGSWithSO( CompileShader( gs_5_0, VS() ), 
                                        "0:Position.xy; 1:Position.zw; 2:Color.xy", 
                                        "3:Texcoord.xyzw; 3:$SKIP.x;", 
                                        NULL, 
                                        NULL, 
                                        1 );
PixelShader pPS = NULL;
ComputeShader pCS = NULL;
This example illustrates declaring global state block variables.
BlendState myBS[2] < bool IsValid = true; >
{
  {
    BlendEnable[0] = false;
  },
  {
    BlendEnable[0] = true;
    SrcBlendAlpha[0] = Inv_Src_Alpha;
  }
};

RasterizerState myRS
{
      FillMode = Solid;
      CullMode = NONE;
      MultisampleEnable = true;
      DepthClipEnable = false;
};

DepthStencilState myDS
{
    DepthEnable = false;
    DepthWriteMask = Zero;
    DepthFunc = Less;
};
sampler mySS[2] : register(s3) 
{
    {
        Filter = ANISOTROPIC;
        MaxAnisotropy = 3;
    },
    {
        Filter = ANISOTROPIC;
        MaxAnisotropy = 4;
    }
};
  
  
```



## Related topics

<dl> <dt>

[Effect Format](d3d11-effect-format.md)
</dt> </dl>

 

 