---
title: Differences Between Effects 10 and Effects 11
description: This topic shows the differences between Effects 10 and Effects 11.
ms.assetid: c3e5e6bc-c544-49ee-b6d9-021ce87f9b12
ms.topic: article
ms.date: 05/31/2018
---

# Differences Between Effects 10 and Effects 11

This topic shows the differences between Effects 10 and Effects 11.

## Device Contexts, Threading, and Cloning

The ID3D10Device interface has been split into two interfaces in Direct3D 11: ID3D11Device and ID3D11DeviceContext. You can create multiple ID3D11DeviceContexts to facilitate concurrent execution on multiple threads. Effects 11 extends this concept to the Effects framework.

The Effects 11 runtime is single-threaded. For this reason, you should not use a single ID3DX11Effect instance with multiple threads concurrently.

To use the Effects 11 runtime on multiple instances, you must create separate ID3DX11Effect instances. Because the ID3D11DeviceContext is also single-threaded, you should pass different ID3D11DeviceContext instances to each effect instance on Apply. You can use these separate device contexts to create command lists so that the rendering thread can apply them on the immediate device context.

The easiest way to create multiple effects that encapsulate the same functionality, for use on multiple threads, is to create one effect and then make cloned copies. Cloning has the following advantages over creating multiple copies from scratch:

1.  The cloning routine is faster than the creation routine.
2.  Cloned effects share created shaders, state blocks, and class instances (so they don't have to be recreated).
3.  Cloned effects can share constant buffers.
4.  Cloned effects begin with state that matches the current effect (variable values, whether or not it has been optimized).

See [Cloning an Effect](d3d11-graphics-programming-guide-effects-cloning.md) for more information.

## Effect Pools and Groups

By far the most prevalent use of effect pools in Direct3D 10 was for grouping materials. Effect Pools have been removed from Effects 11 and groups have been added, which is a more efficient method of grouping materials.

An effect group is simply a set of techniques. See [Effect Group Syntax (Direct3D 11)](d3d11-effect-group-syntax.md) for more information.

Consider the following effect hierarchy with four child effects and one effect pool:


```
// Effect Pool
cbufer A { ... }
PixelShader pPSGrass;
PixelShader pPSWater;

// Effect Child 1
#include "EffectPool.fx"
technique10 GrassMaterialLowSpec { ... }

// Effect Child 2
#include "EffectPool.fx"
technique10 GrassMaterialHighSpec { ... }

// Effect Child 3
#include "EffectPool.fx"
technique10 WaterMaterialLowSpec { ... }

// Effect Child 4
#include "EffectPool.fx"
technique10 WaterMaterialHighSpec { ... }
```



You can achieve the same functionality in Effects 11 by using groups:


```
cbufer A { ... }
PixelShader pPSGrass;
PixelShader pPSWater;

fxgroup GrassMaterial
{
    technique10 LowSpec { ... }
    technique10 HighSpec { ... }
}

fxgroup WaterMaterial
{
    technique10 LowSpec { ... }
    technique10 HighSpec { ... }
}
```



## New Shader Stages

There are three new shader stages in Direct3D 11: the hull shader, domain shader, and compute shader. Effects 11 handles these in a similar manner to vertex shaders, geometry shaders, and pixel shaders.

Three new variable types have been added to Effects 11:

-   HullShader
-   DomainShader
-   ComputeShader

If you use these shaders in a technique, you must label that technique "technique11", and not "technique10". The compute shader cannot be set in the same pass as any other graphics state (other shaders, state blocks, or render targets).

## New Texture Types

Direct3D 11 supports the following texture types:

-   [AppendStructuredBuffer](/windows/desktop/direct3dhlsl/sm5-object-appendstructuredbuffer)
-   [ByteAddressBuffer](/windows/desktop/direct3dhlsl/sm5-object-byteaddressbuffer)
-   [ConsumeStructuredBuffer](/windows/desktop/direct3dhlsl/sm5-object-consumestructuredbuffer)
-   [StructuredBuffer](/windows/desktop/direct3dhlsl/sm5-object-structuredbuffer)

## Unordered Access Views

Effects 11 supports getting and setting the new unordered access view types. This works in a similar manner as textures.

Consider this Effects HLSL example:


```
  
RWTexture1D<float> myUAV;
```



You can set this variable in C++ as follows:


```
  
ID3D11UnorderedAccessView* pUAVTexture1D = NULL;
ID3DX11EffectUnorderedAccessViewVariable* pUAVVar;
pUAVVar = pEffect->GetVariableByName("myUAV")->AsUnorderedAccessView();
pUAVVar->SetUnorderedAccessView( pUAVTexture1D );
```



Direct3D 11 supports the following unordered access view types:

-   RWBuffer
-   RWByteAddressBuffer
-   RWStructuredBuffer
-   RWTexture1D
-   RWTexture1DArray
-   RWTexture2D
-   RWTexture2DArray
-   RWTexture3D

## Interfaces and Class Instances

For interface and class syntax, see [Interfaces and Classes](/windows/desktop/direct3dhlsl/overviews-direct3d-11-hlsl-dynamic-linking-class).

For using interfaces and classes in effects, see [Interfaces and Classes in Effects](d3d11-graphics-programming-guide-effects-interfaces-and-classes.md).

## Addressable Stream Out

In Direct3D 10, geometry shaders could output one stream of data to the stream output unit and the rasterizer unit. In Direct3D11, geometry shaders can output up to four streams of data to the stream output unit, and at most one of those streams to the rasterizer unit. The **ConstructGSWithSO** intrinsic has been updated to reflect this new functionality.

See [Stream Out Syntax](d3d11-graphics-reference-effect-streamout.md) for more information.

## Setting and Unsetting Device State

In Effects 10, you could make constant buffers and texture buffers user-managed by using the [**ID3D10EffectConstantBuffer::SetConstantBuffer**](/windows/desktop/api/d3d10effect/nf-d3d10effect-id3d10effectconstantbuffer-setconstantbuffer) and [**SetTextureBuffer**](id3dx11effectconstantbuffer-settexturebuffer.md) functions. After you call these functions, the Effects 10 runtime no longer manages the constant buffer or texture buffer and the user must fill the data by using the ID3D10Device interface.

In Effects 11, you can also make the state blocks (blend state, rasterizer state, depth-stencil state, and sampler state) user-managed by using the following calls:

-   [**ID3DX11EffectBlendVariable::SetBlendState**](id3dx11effectblendvariable-setblendstate.md)
-   [**ID3DX11EffectRasterizerVariable::SetRasterizerState**](id3dx11effectrasterizervariable-setrasterizerstate.md)
-   [**ID3DX11EffectDepthStencilVariable::SetDepthStencilState**](id3dx11effectdepthstencilvariable-setdepthstencilstate.md)
-   [**ID3DX11EffectSamplerVariable::SetSampler**](id3dx11effectsamplervariable-setsampler.md)

After you call these functions, the Effects 11 runtime no longer manages the state block variables, and there values will remain unchanged. Note that because state blocks are immutable, the user must set a new state block to change the values.

You can also revert constant buffers, texture buffers, and state blocks to the non-user managed state. If you unset these variables, the Effects 11 runtime will continue to update them when necessary. You can use the following calls to unset user managed variables:

-   [**ID3DX11EffectConstantBuffer::UndoSetConstantBuffer**](id3dx11effectconstantbuffer-undosetconstantbuffer.md)
-   [**ID3DX11EffectConstantBuffer::UndoSetTextureBuffer**](id3dx11effectconstantbuffer-undosettexturebuffer.md)
-   [**ID3DX11EffectBlendVariable::UndoSetBlendState**](id3dx11effectblendvariable-undosetblendstate.md)
-   [**ID3DX11EffectRasterizerVariable::UndoSetRasterizerState**](id3dx11effectrasterizervariable-undosetrasterizerstate.md)
-   [**ID3DX11EffectDepthStencilVariable::UndoSetDepthStencilState**](id3dx11effectdepthstencilvariable-undosetdepthstencilstate.md)
-   [**ID3DX11EffectSamplerVariable::UndoSetSampler**](id3dx11effectsamplervariable-undosetsampler.md)

## Effects Virtual Machine

The effects virtual machine, which evaluated complex expressions outside of functions, has been removed.

The following examples of complex expressions are not supported:

1.  SetPixelShader( myPSArray( i \* 3 + j ) );
2.  SetPixelShader( myPSArray( (float)i );
3.  FILTER = i + 2;

The following examples of non-complex expressions are supported:

1.  SetPixelShader( myPS );
2.  SetPixelShader( myPS\[i\] );
3.  SetPixelShader( myPS\[ uIndex \] ); // uIndex is a uint variable
4.  FILTER = i;
5.  FILTER = ANISOTROPIC;

These expressions could appear in state block expressions (such as FILTER) and pass expressions (such as SetPixelShader).

## Source Availability and Location

Effects 10 was distributed in D3D10.dll. Effects 11 is distributed as source, with corresponding Visual Studio solutions to compile it. When you create effects-type applications, we recommend that you include the Effects 11 source directly in those applications.

You can get Effects 11 from [Effects for Direct3D 11 Update](https://github.com/Microsoft/FX11).

## Related topics

<dl> <dt>

[Effects (Direct3D 11)](d3d11-graphics-programming-guide-effects.md)
</dt> </dl>

 

 