---
description: This page will show you how to generate and use an effect.
ms.assetid: d9fdafed-5958-4995-a1b5-8881feca1291
title: Using an Effect (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Using an Effect (Direct3D 9)

This page will show you how to generate and use an effect. The topics covered include how to:

-   [Create an Effect](#create-an-effect)
-   [Render an Effect](#render-an-effect)
-   [Use Semantics to Find Effect Parameters](#use-semantics-to-find-effect-parameters)
-   [Use Handles to Get and Set Parameters Efficiently](#use-handles-to-get-and-set-parameters-efficiently)
-   [Add Parameter Information with Annotations](#add-parameter-information-with-annotations)
-   [Share Effect Parameters](#share-effect-parameters)
-   [Compile an Effect Offline](#compile-an-effect-offline)
-   [Improve Performance with Preshaders](#improve-performance-with-preshaders)
-   [Use Parameter Blocks to Manage Effect Parameters](#use-parameter-blocks-to-manage-effect-parameters)

## Create an Effect

Here is an example of creating an effect taken from the [BasicHLSL Sample](../directx-sdk--august-2009-.md). The effect creation code for creating a debug shader is from **OnCreateDevice**:


```
ID3DXEffect* g_pEffect = NULL;
DWORD dwShaderFlags = 0;

    dwShaderFlags |= D3DXSHADER_FORCE_VS_SOFTWARE_NOOPT;
    dwShaderFlags |= D3DXSHADER_FORCE_PS_SOFTWARE_NOOPT;
    dwShaderFlags |= D3DXSHADER_NO_PRESHADER;

    // Read the D3DX effect file
    WCHAR str[MAX_PATH];
    DXUTFindDXSDKMediaFileCch( str, MAX_PATH, L"BasicHLSL.fx" );

    D3DXCreateEffectFromFile( 
        pd3dDevice, 
        str, 
        NULL, // CONST D3DXMACRO* pDefines,
        NULL, // LPD3DXINCLUDE pInclude,
        dwShaderFlags, 
        NULL, // LPD3DXEFFECTPOOL pPool,
        &g_pEffect, 
        NULL );
```



This function takes these arguments:

-   The device.
-   The file name of the effect file.
-   A pointer to a NULL-terminated list of \#defines, to be used while parsing the shader.
-   An optional pointer to a user-written include handler. The handler is called by the processor whenever it needs to resolve a \#include.
-   A shader compile flag that gives the compiler hints about how the shader will be used. The options include:
    -   Skipping validation, if known good shaders are being compiled.
    -   Skipping optimization (sometimes used when optimizations make debugging harder).
    -   Requesting debug information to be included in the shader so it can be debugged.
-   The effect pool. If more than one effect uses the same memory pool pointer, the global variables in the effects are shared with each other. If there is no need to share effect variables, the memory pool can be set to **NULL**.
-   A pointer to the new effect.
-   A pointer to a buffer to which validation errors can be sent. In this example, the parameter was set to **NULL** and not used.

> [!Note]  
> Beginning with the December 2006 SDK, the DirectX 10 HLSL compiler is now the default compiler in both DirectX 9 and DirectX 10. See [Effect-Compiler Tool](../direct3dtools/fxc.md) for details.

 

## Render an Effect

The sequence of calls for applying effect state to a device is:

-   [**ID3DXEffect::Begin**](id3dxeffect--begin.md) sets the active technique.
-   [**ID3DXEffect::BeginPass**](id3dxeffect--beginpass.md) sets the active pass.
-   [**ID3DXEffect::CommitChanges**](id3dxeffect--commitchanges.md) updates changes to any set calls in the pass. This should be called before any draw call.
-   [**ID3DXEffect::EndPass**](id3dxeffect--endpass.md) ends a pass.
-   [**ID3DXEffect::End**](id3dxeffect--end.md) ends the active technique.

Effect render code is also simpler than the corresponding render code without an effect. Here's the render code with an effect:


```
// Apply the technique contained in the effect 
g_pEffect->Begin(&cPasses, 0);

for (iPass = 0; iPass < cPasses; iPass++)
{
    g_pEffect->BeginPass(iPass);

    // Only call CommitChanges if any state changes have happened
    // after BeginPass is called
    g_pEffect->CommitChanges();

    // Render the mesh with the applied technique
    g_pMesh->DrawSubset(0);

    g_pEffect->EndPass();
}
g_pEffect->End();
```



The render loop consists of querying the effect to see how many passes it contains, and then calling all the passes for a technique. The render loop could be expanded to call multiple techniques, each with multiple passes.

## Use Semantics to Find Effect Parameters

A semantic is an identifier that is attached to an effect parameter to allow an application to search for the parameter. A parameter can have at most one semantic. The semantic is located following a colon (:) after the parameter name. For instance:


```
float4x4 matWorldViewProj : WORLDVIEWPROJ;
```



If you declared the effect global variable without using a semantic, it would look like this instead:


```
float4x4 matWorldViewProj;
```



The effect interface can use a semantic to get a handle to a particular effect parameter. For instance, the following returns the handle of the matrix:


```
D3DHANDLE handle = 
    m_pEffect->GetParameterBySemantic(NULL, "WORLDVIEWPROJ");
```



In addition to searching by semantic name, the effect interface has many other methods to search for parameters.

## Use Handles to Get and Set Parameters Efficiently

Handles provide an efficient means for referencing effect parameters, techniques, passes, and annotations with an effect. Handles (which are of type D3DXHANDLE) are string pointers. The handles that are passed into functions such as GetParameterxxx or GetAnnotationxxx can be in one of three forms:

-   A handle returned by a function such as GetParameterxxx.
-   A string containing the name of the parameter, technique, pass, or annotation.
-   A handle set to **NULL**.

This example returns a handle to the parameter that has the WORLDVIEWPROJ semantic attached to it:


```
D3DHANDLE handle = 
    m_pEffect->GetParameterBySemantic(NULL, "WORLDVIEWPROJ");
```



## Add Parameter Information with Annotations

Annotations are user-specific data that can be attached to any technique, pass, or parameter. An annotation is a flexible way to add information to individual parameters. The information can be read back and used any way the application chooses. An annotation can be of any data type and can be added dynamically. Annotation declarations are delimited by angle brackets. An annotation contains:

-   A data type.
-   A variable name.
-   An equals sign (=).
-   The data value.
-   A ending semicolon (;).

For instance, both of the previous examples in this paper contain this annotation:


```
texture Tex0 < string name = "tiger.bmp"; >;
```



The annotation is attached to the texture object and specifies the texture file that should be used to initialize the texture object. The annotation does not initialize the texture object, it is simply a piece of user information that is attached to the variable. An application can read the annotation with either [**ID3DXBaseEffect::GetAnnotation**](id3dxbaseeffect--getannotation.md) or [**ID3DXBaseEffect::GetAnnotationByName**](id3dxbaseeffect--getannotationbyname.md) to return the string. Annotations can also be added by the application.

Each annotation:

-   Must be either numeric or strings.
-   Must always be initialized with a default value.
-   Can be associated with [Techniques and Passes (Direct3D 9)](techniques-and-passes.md) and top-level [Effect Parameters](/previous-versions/windows/desktop/ee417539(v=vs.85)).
-   Can be written to and read from with either [**ID3DXEffect**](id3dxeffect.md) or [**ID3DXEffectCompiler**](id3dxeffectcompiler.md).
-   Can be added with [**ID3DXEffect**](id3dxeffect.md).
-   Cannot be referenced inside the effect.
-   Cannot have sub-semantics or sub-annotations.

## Share Effect Parameters

Effect parameters are all the non-static variables declared in an effect. This can include global variables and annotations. Effect parameters can be shared between different effects by declaring parameters with the "shared" keyword and then creating the effect with an effect pool.

An effect pool contains shared effect parameters. The pool is created by calling [**D3DXCreateEffectPool**](d3dxcreateeffectpool.md), which returns an [**ID3DXEffectPool**](id3dxeffectpool.md) interface. The interface can be supplied as an input to any of the D3DXCreateEffectxxx functions when an effect is created. For a parameter to be shared across multiple effects, the parameter must have the same name, type, and semantic in each of the shared effects.


```
ID3DXEffectPool* g_pEffectPool = NULL;   // Effect pool for sharing parameters

    D3DXCreateEffectPool( &g_pEffectPool );
```



Effects that share parameters must use the same device. This is enforced to prevent the sharing of device-dependent parameters (such as shaders or textures) across different devices. Parameters are deleted from the pool whenever the effects that contain the shared parameters are released. If sharing parameters is not necessary, supply **NULL** for the effect pool when an effect is created.

Cloned effects use the same effect pool as the effect from which they are cloned. Cloning an effect makes an exact copy of an effect, including global variables, techniques, passes, and annotations.

## Compile an Effect Offline

You can compile an effect at run time with [**D3DXCreateEffect**](d3dxcreateeffect.md), or you can compile an effect offline using the command-line compiler tool fxc.exe. The effect in the [CompiledEffect Sample](https://msdn.microsoft.com/library/Ee416326(v=VS.85).aspx) contains a vertex shader, a pixel shader, and one technique:


```
// File: CompiledEffect.fx

// Global variables
float4 g_MaterialAmbientColor;    // Material's ambient color
...

// Texture samplers
sampler RenderTargetSampler = 
   ...

// Type: Vertex shader                                      
VS_OUTPUT RenderSceneVS( float4 vPos : POSITION, 
                         float3 vNormal : NORMAL,
                         float2 vTexCoord0 : TEXCOORD0 )
{
   ...
};
// Type: Pixel shader
PS_OUTPUT RenderScenePS( VS_OUTPUT In ) 
{ 
   ...
}

// Type: Technique                                     
technique RenderScene
{
    pass P0
    {          
        ZENABLE = true;
        VertexShader = compile vs_1_1 RenderSceneVS();
        PixelShader  = compile ps_1_1 RenderScenePS();
    }
}
```



Using [Effect-Compiler Tool](../direct3dtools/fxc.md) to compile the shader for vs\_1\_1 generated the following assembly shader instructions:


```
//
// Generated by Microsoft (R) D3DX9 Shader Compiler 4.09.02.1188
//
//   fxc /T vs_1_1 /E RenderSceneVS /Fc CompiledEffect.txt CompiledEffect.fx
//
//
// Parameters:
//
//   float4 g_LightAmbient;
//   float4 g_LightDiffuse;
//   float3 g_LightDir;
//   float4 g_MaterialAmbientColor;
//   float4 g_MaterialDiffuseColor;
//   float g_fTime;
//   float4x4 g_mWorld;
//   float4x4 g_mWorldViewProjection;
//
//
// Registers:
//
//   Name                   Reg   Size
//   ---------------------- ----- ----
//   g_mWorldViewProjection c0       4
//   g_mWorld               c4       3
//   g_MaterialAmbientColor c7       1
//   g_MaterialDiffuseColor c8       1
//   g_LightDir             c9       1
//   g_LightAmbient         c10      1
//   g_LightDiffuse         c11      1
//   g_fTime                c12      1
//
//
// Default values:
//
//   g_LightDir
//     c9   = { 0.57735, 0.57735, 0.57735, 0 };
//
//   g_LightAmbient
//     c10  = { 1, 1, 1, 1 };
//
//   g_LightDiffuse
//     c11  = { 1, 1, 1, 1 };
//

    vs_1_1
    def c13, 0.159154937, 0.25, 6.28318548, -3.14159274
    def c14, -2.52398507e-007, 2.47609005e-005, -0.00138883968, 0.0416666418
    def c15, -0.5, 1, 0.5, 0
    dcl_position v0
    dcl_normal v1
    dcl_texcoord v2
    mov r0.w, c12.x
    mad r0.w, r0.w, c13.x, c13.y
    expp r3.y, r0.w
    mov r0.w, r3.y
    mad r0.w, r0.w, c13.z, c13.w
    mul r0.w, r0.w, r0.w
    mad r1.w, r0.w, c14.x, c14.y
    mad r1.w, r0.w, r1.w, c14.z
    mad r1.w, r0.w, r1.w, c14.w
    mad r1.w, r0.w, r1.w, c15.x
    mad r0.w, r0.w, r1.w, c15.y
    mul r0.w, r0.w, v0.x
    mul r0.x, r0.w, c15.z
    dp3 r1.x, v1, c4
    dp3 r1.y, v1, c5
    dp3 r1.z, v1, c6
    mov r0.yzw, c15.w
    dp3 r2.x, r1, r1
    add r0, r0, v0
    rsq r1.w, r2.x
    dp4 oPos.x, r0, c0
    mul r1.xyz, r1, r1.w
    dp4 oPos.y, r0, c1
    dp3 r1.x, r1, c9
    dp4 oPos.z, r0, c2
    max r1.w, r1.x, c15.w
    mov r1.xyz, c8
    mul r1.xyz, r1, c11
    mov r2.xyz, c7
    mul r2.xyz, r2, c10
    dp4 oPos.w, r0, c3
    mad oD0.xyz, r1, r1.w, r2
    mov oD0.w, c15.y
    mov oT0.xy, v2

// approximately 34 instruction slots used
```



## Improve Performance with Preshaders

A preshader is a technique for increasing shader efficiency by pre-calculating constant shader expressions. The effect compiler automatically pulls out shader computations from the body of a shader and executes them on the CPU prior to the shader running. Consequently, preshaders only work with effects. For instance, these two expressions can be evaluated outside of the shader before it runs.


```
mul(World,mul(View, Projection));
sin(time)
```



Shader computations that can be moved are those associated with uniform parameters; that is, the computations do not change for each vertex or pixel. If you are using effects, the effect compiler automatically generates and runs a preshader for you; there are no flags to enable. Preshaders can reduce the number of instructions per shader and can also reduce the number of constant registers a shader consumes.

Think of the effect compiler as a sort of multi-processor compiler because it compiles shader code for two types of processors: a CPU and a GPU. In addition, the effect compiler is designed to move code from the GPU to the CPU and therefore improve shader performance. This is very similar to pulling a static expression out of a loop. A shader that transforms position from world space to projection space, and copies texture coordinates would look like this in HLSL:


```
float4x4 g_mWorldViewProjection;    // World * View * Projection matrix
float4x4 g_mWorldInverse;           // Inverse World matrix
float3 g_LightDir;                  // Light direction in world space
float4 g_LightDiffuse;              // Diffuse color of the light

struct VS_OUTPUT
{
    float4 Position   : POSITION;   // vertex position 
    float2 TextureUV  : TEXCOORD0;  // vertex texture coords 
    float4 Diffuse    : COLOR0;     // vertex diffuse color
};

VS_OUTPUT RenderSceneVS( float4 vPos : POSITION, 
                         float3 vNormal : NORMAL,
                         float2 vTexCoord0 : TEXCOORD0)
{
    VS_OUTPUT Output;
    
    // Transform the position from object space to projection space
    Output.Position = mul(vPos, g_mWorldViewProjection);

    // Transform the light from world space to object space    
    float3 vLightObjectSpace = normalize(mul(g_LightDir, (float3x3)g_mWorldInverse)); 

    // N dot L lighting
    Output.Diffuse = max(0,dot(vNormal, vLightObjectSpace));
    
    // Copy the texture coordinate
    Output.TextureUV = vTexCoord0; 
    
    return Output;    
}
technique RenderVS
{
    pass P0
    {          
        VertexShader = compile vs_1_1 RenderSceneVS();
    }
}
```



Using [Effect-Compiler Tool](../direct3dtools/fxc.md) to compile the shader for vs\_1\_1 generates the following assembly instructions:


```
technique RenderVS
{
    pass P0
    {
        vertexshader = 
            asm {
            //
            // Generated by Microsoft (R) D3DX9 Shader Compiler 9.15.779.0000
            //
            // Parameters:
            //
            //   float3 g_LightDir;
            //   float4x4 g_mWorldInverse;
            //   float4x4 g_mWorldViewProjection;
            //
            //
            // Registers:
            //
            //   Name                   Reg   Size
            //   ---------------------- ----- ----
            //   g_mWorldViewProjection c0       4
            //   g_mWorldInverse        c4       3
            //   g_LightDir             c7       1
            //
            
                vs_1_1
                def c8, 0, 0, 0, 0
                dcl_position v0
                dcl_normal v1
                dcl_texcoord v2
                mov r1.xyz, c7
                dp3 r0.x, r1, c4
                dp3 r0.y, r1, c5
                dp3 r0.z, r1, c6
                dp4 oPos.x, v0, c0
                dp3 r1.x, r0, r0
                dp4 oPos.y, v0, c1
                rsq r0.w, r1.x
                dp4 oPos.z, v0, c2
                mul r0.xyz, r0, r0.w
                dp4 oPos.w, v0, c3
                dp3 r0.x, v1, r0
                max oD0, r0.x, c8.x
                mov oT0.xy, v2
            
            // approximately 14 instruction slots used
            };

        //No embedded pixel shader
    }
}
```



This uses up approximately 14 slots and consumes 9 constant registers. With a preshader, the compiler moves the static expressions out of the shader and into the preshader. The same shader would look like this with a preshader:


```
technique RenderVS
{
    pass P0
    {
        vertexshader = 
            asm {
            //
            // Generated by Microsoft (R) D3DX9 Shader Compiler 9.15.779.0000
            //
            // Parameters:
            //
            //   float3 g_LightDir;
            //   float4x4 g_mWorldInverse;
            //
            //
            // Registers:
            //
            //   Name            Reg   Size
            //   --------------- ----- ----
            //   g_mWorldInverse c0       3
            //   g_LightDir      c3       1
            //
            
                preshader
                dot r0.x, c3.xyz, c0.xyz
                dot r0.y, c3.xyz, c1.xyz
                dot r0.z, c3.xyz, c2.xyz
                dot r1.w, r0.xyz, r0.xyz
                rsq r0.w, r1.w
                mul c4.xyz, r0.w, r0.xyz
            
            // approximately 6 instructions used
            //
            // Generated by Microsoft (R) D3DX9 Shader Compiler 9.15.779.0000
            //
            // Parameters:
            //
            //   float4x4 g_mWorldViewProjection;
            //
            //
            // Registers:
            //
            //   Name                   Reg   Size
            //   ---------------------- ----- ----
            //   g_mWorldViewProjection c0       4
            //
            
                vs_1_1
                def c5, 0, 0, 0, 0
                dcl_position v0
                dcl_normal v1
                dcl_texcoord v2
                dp4 oPos.x, v0, c0
                dp4 oPos.y, v0, c1
                dp4 oPos.z, v0, c2
                dp4 oPos.w, v0, c3
                dp3 r0.x, v1, c4
                max oD0, r0.x, c5.x
                mov oT0.xy, v2
            
            // approximately 7 instruction slots used
            };

        //No embedded pixel shader
    }
}
```



An effect executes a preshader just before executing a shader. The result is the same functionality with increased shader performance because the number of instructions that need to be executed (for each vertex or pixel depending on the type of shader) has been reduced. In addition, fewer constant registers are consumed by the shader as a result of the static expressions being moved to the preshader. This means that shaders previously limited by the number of constant registers they required may now compile because they require fewer constant registers. It is reasonable to expect a 5 percent and a 20 percent performance improvement from preshaders.

Keep in mind that the input constants are different from the output constants in a preshader. The output c1 is not the same as the input c1 register. Writing to a constant register in a preshader actually writes into the corresponding shader's input (constant) slot.


```
// BaseDelta c0 1
// Refinements c1 1
preshader
mul c1.x, c0.x, (-2)
add c0.x, c0.x, c0.x
cmp c5.x, c1.x, (1), (0)
```



The cmp instruction above will read the preshader c1 value, while the mul instruction will write to the hardware shader registers to be used by the vertex shader.

## Use Parameter Blocks to Manage Effect Parameters

Parameter blocks are blocks of effect state changes. A parameter block can record state changes, so that they can be applied later on with a single call. Create a parameter block by calling [**ID3DXEffect::BeginParameterBlock**](id3dxeffect--beginparameterblock.md):


```
    m_pEffect->SetTechnique( "RenderScene" );

    m_pEffect->BeginParameterBlock();
    D3DXVECTOR4 v4( Diffuse.r, Diffuse.g, Diffuse.b, Diffuse.a );
    m_pEffect->SetVector( "g_vDiffuse", &v4 );
    m_pEffect->SetFloat( "g_fReflectivity", fReflectivity );
    m_pEffect->SetFloat( "g_fAnimSpeed", fAnimSpeed );
    m_pEffect->SetFloat( "g_fSizeMul", fSize );
    m_hParameters = m_pEffect->EndParameterBlock();
```



The parameter block saves four changes applied by the API calls. Calling [**ID3DXEffect::BeginParameterBlock**](id3dxeffect--beginparameterblock.md) starts recording the state changes. [**ID3DXEffect::EndParameterBlock**](id3dxeffect--endparameterblock.md) stops adding the changes to the parameter block and returns a handle. The handle will be used when calling [**ID3DXEffect::ApplyParameterBlock**](id3dxeffect--applyparameterblock.md).

In the [EffectParam Sample](https://msdn.microsoft.com/library/Ee417535(v=VS.85).aspx), the parameter block is applied in the render sequence:


```
CObj g_aObj[NUM_OBJS];       // Object instances

    if( SUCCEEDED( pd3dDevice->BeginScene() ) )
    {
        // Set the shared parameters using the first mesh's effect.

        // Render the mesh objects
        for( int i = 0; i < NUM_OBJS; ++i )
        {
            ID3DXEffect *pEffect = g_aObj[i].m_pEffect;

            // Apply the parameters
            pEffect->ApplyParameterBlock( g_aObj[i].m_hParameters );

            ...

            pEffect->Begin( &cPasses, 0 );
            for( iPass = 0; iPass < cPasses; iPass++ )
            {
              ...
            }
            pEffect->End();
        }

        ...
        pd3dDevice->EndScene();
    }
```



The parameter block sets the value of all four of the state changes just before [**ID3DXEffect::Begin**](id3dxeffect--begin.md) is called. Parameter blocks are a handy way to set multiple state changes with a single API call.

## Related topics

<dl> <dt>

[Effects](effects.md)
</dt> </dl>

 

 
