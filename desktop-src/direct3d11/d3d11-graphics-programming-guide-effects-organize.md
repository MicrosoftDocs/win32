---
title: Organizing State in an Effect (Direct3D 11)
description: With Direct3D 11, effect state for certain pipeline stages is organized by structures.
ms.assetid: e5057f94-69dd-4219-a5f4-569e48502475
ms.topic: article
ms.date: 05/31/2018
---

# Organizing State in an Effect (Direct3D 11)

With Direct3D 11, effect state for certain pipeline stages is organized by structures. Here are the structures:



| Pipeline State | Structure                                                                                                          |
|----------------|--------------------------------------------------------------------------------------------------------------------|
| Rasterization  | [**D3D11\_RASTERIZER\_DESC**](/windows/desktop/api/D3D11/ns-d3d11-d3d11_rasterizer_desc)                                                           |
| Output Merger  | [**D3D11\_BLEND\_DESC**](/windows/desktop/api/D3D11/ns-d3d11-d3d11_blend_desc) and [**D3D11\_DEPTH\_STENCIL\_DESC**](/windows/desktop/api/D3D11/ns-d3d11-d3d11_depth_stencil_desc) |
| Shaders        | See below                                                                                                          |



 

For the shader stages, where the number of state changes need to be more controlled by an application, the state has been divided up into constant buffer state, sampler state, shader resource state, and unordered access view state (for pixel and compute shaders). This allows an application that is carefully designed to update only the state that is changing, which improves performance by reducing the amount of data that needs to be passed to the GPU.

So how do you organize the pipeline state in an effect?

The answer is, the order doesn't matter. Global variables do not have to be located at the top. However, all the samples in the SDK follow the same order, as it is good practice to organize the data the same way. So this is a brief description of the data ordering in the DirectX SDK samples.

-   [Global Variables](#global-variables)
-   [Shaders](#shaders)
-   [Groups, Techniques, and Passes](#groups-techniques-and-passes)

## Global Variables

Just like standard C practice, global variables are declared first, at the top of the file. Most often, these are variables that will be initialized by an application, and then used in an effect. Sometimes they are initialized and never changed, other times they are updated every frame. Just like C function scope rules, effect variables declared outside of the scope of effect functions are visible throughout the effect; any variable declared inside of an effect function is only visible within that function.

Here is an example of the variables declared in BasicHLSL10.fx.


```
// Global variables
float4 g_MaterialAmbientColor;      // Material's ambient color

Texture2D g_MeshTexture;            // Color texture for mesh

float    g_fTime;                   // App's time in seconds
float4x4 g_mWorld;                  // World matrix for object
float4x4 g_mWorldViewProjection;    // World * View * Projection matrix


// Texture samplers
SamplerState MeshTextureSampler
{
    Filter = MIN_MAG_MIP_LINEAR;
    AddressU = Wrap;
    AddressV = Wrap;
};
```



The syntax for effect variables is more fully detailed in [Effect Variable Syntax (Direct3D 11)](d3d11-effect-variable-syntax.md). The syntax for effect texture samplers is more fully detailed in [Sampler Type (DirectX HLSL)](/windows/desktop/direct3dhlsl/dx-graphics-hlsl-sampler).

## Shaders

Shaders are small executable programs. You can think of shaders as encapsulating shader state, since the HLSL code implements the shader functionality. The graphics pipeline up to five different kinds of shaders.

-   Vertex shaders - Operate on vertex data. One vertex in yields one vertex out.
-   Hull shaders - Operate on patch data. Control Point Phase: one invocation yields one control point; For each Fork and Join Phases: one patch yields some amount of patch constant data.
-   Domain shaders - Operate on primitive data. One primitive may yield 0, 1, or many primitives out.
-   Geometry shaders - Operate on primitive data. One primitive in may yield 0, 1, or many primitives out.
-   Pixel shaders - Operate on pixel data. One pixel in yields 1 pixel out (unless the pixel is culled out of a render).

The compute shader pipeline uses one shader:

-   Compute shaders - Operate on any kind of data. The output is independent of the number of threads.

Shaders are local functions and follow C style function rules. When an effect is compiled, each shader is compiled and a pointer to each shader function is stored internally. An ID3D11Effect interface is returned when compilation is successful. At this point the compiled effect is in an intermediate format.

To find out more information about the compiled shaders, you will need to use shader reflection. This is essentially like asking the runtime to decompile the shaders, and return information back to you about the shader code.


```
struct VS_OUTPUT
{
    float4 Position   : SV_POSITION; // vertex position 
    float4 Diffuse    : COLOR0;      // vertex diffuse color
    float2 TextureUV  : TEXCOORD0;   // vertex texture coords 
};

VS_OUTPUT RenderSceneVS( float4 vPos : POSITION,
                         float3 vNormal : NORMAL,
                         float2 vTexCoord0 : TEXCOORD,
                         uniform int nNumLights,
                         uniform bool bTexture,
                         uniform bool bAnimate )
{
    VS_OUTPUT Output;
    float3 vNormalWorldSpace;
 
    ....    
    
    return Output;    
}


struct PS_OUTPUT
{
    float4 RGBColor : SV_Target;  // Pixel color
};

PS_OUTPUT RenderScenePS( VS_OUTPUT In,
                         uniform bool bTexture ) 
{ 
    PS_OUTPUT Output;

    if( bTexture )
        Output.RGBColor = g_MeshTexture.Sample(MeshTextureSampler, In.TextureUV) * In.Diffuse;
    ....

    return Output;
}
```



The syntax for effect shaders is more fully detailed in [Effect Function Syntax (Direct3D 11)](d3d11-effect-function-syntax.md).

## Groups, Techniques, and Passes

A group is a collection of techniques. A technique is a collection of rendering passes (there must be at least one pass). Each effect pass (which is similar in scope to a single pass in a render loop) defines the shader state and any other pipeline state necessary to render geometry.

Groups are optional. There is a single, unnamed group which encompasses all global techniques. All other groups must be named.

Here is an example of one technique (which includes one pass) from BasicHLSL10.fx.


```
technique10 RenderSceneWithTexture1Light
{
    pass P0
    {
        SetVertexShader( CompileShader( vs_4_0, RenderSceneVS( 1, true, true ) ) );
        SetGeometryShader( NULL );
        SetPixelShader( CompileShader( ps_4_0, RenderScenePS( true ) ) );
    }
}

fxgroup g0
{
    technique11 RunComputeShader
    {
        pass P0
        {
            SetComputeShader( CompileShader( cs_5_0, CS() ) );
        }
    }
}

```



The syntax for effect shaders is more fully detailed in [Effect Technique Syntax (Direct3D 11)](d3d11-effect-technique-syntax.md).

## Related topics

<dl> <dt>

[Effects (Direct3D 11)](d3d11-graphics-programming-guide-effects.md)
</dt> </dl>

 

 