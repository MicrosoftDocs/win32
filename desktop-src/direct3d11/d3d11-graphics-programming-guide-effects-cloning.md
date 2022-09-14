---
title: Cloning an Effect
description: Cloning an effect creates a second, almost identical copy of the effect.
ms.assetid: e3870363-5ee8-4fdc-a489-cdaeef8c9c39
ms.topic: article
ms.date: 05/31/2018
---

# Cloning an Effect

Cloning an effect creates a second, almost identical copy of the effect. See the following single qualifier for an explanation of why it is not exact. A second copy of an effect is useful when one wants to use the effects framework on multiple threads, since the effect runtime is not thread safe to maintain high performance.

Since device contexts are also non-thread-safe, different threads should pass different device contexts to the ID3DX11EffectPass::Apply method.

An effect can be cloned with the following syntax:


```
ID3DX11Effect* pClonedEffect = NULL;
UINT Flags = D3DX11_EFFECT_CLONE_FORCE_NONSINGLE;
HRESULT hr = pEffect->CloneEffect( Flags, &pClonedEffect );
```



In the above example, the cloned copy will encapsulate the same state as the original effect, regardless of what state the original effect is in. In particular:

1.  If pEffect is optimized, pCloned Effect is optimized
2.  If pEffect has some user-managed variables, pCloned Effect will have the same user-managed variables (see the single description below)
3.  Any pending variable updates (until an Apply call updates device state) in pEffect will be pending in pClonedEffect

The following Direct3D 11 device objects are immutable or never updated by the effects framework, so the cloned effect will point to the same objects as the original effect:

1.  State block objects (ID3D11BlendState, ID3D11RasterizerState, ID3D11DepthStencilState, ID3D11SamplerState)
2.  Shaders
3.  Class instances
4.  Textures (not including texture buffers)
5.  Unordered access views

The following Direct3D 11 device objects are both immutable and modified by the effect runtime (unless user-managed or single in a cloned effect); new copies of these objects are created when non-single:

1.  Constant buffers
2.  Texture Buffers

## Single Constant Buffers and Texture Buffers

Note that this discussion applies to both constant buffers and textures, but constant buffers are assumed for ease of reading.

There may be cases where a constant buffer is only updated by one thread, but device state set by cloned effects will use this data. For example, the main effect may update the world and view matrices which are referenced from shaders in cloned effects which do not change the world and view matrices. In these cases, the cloned effects need to reference the current constant buffer instead of recreating one.

There are two ways to achieve this desired result:

1.  Use ID3DX11EffectConstantBuffer::SetConstantBuffer on the cloned effect to make it user-managed
2.  Mark the constant buffer as "single" in the HLSL code, forcing the effect runtime to treat is as user-managed after cloning

There are two differences between the two methods above. First, in method 1, a new ID3D11Buffer will be created and user before SetConstantBuffer is called. Also, after calling UndoSetConstantBuffer in the cloned effect, the variable in method 1will point to the newly-created buffer (which effects will update on Apply) while the variable in method 2 will continue to point to the original buffer (not updating it on Apply).

See the following example in HLSL:


```
cbuffer ObjectData
{
    float4 Position;
};
single cbuffer ViewData
{
    float4x4 ViewMatrix;
};
```



While cloning, the cloned effect will create a new ID3D11Buffer for ObjectData, and fill its contents on Apply, but reference the original ID3D11Buffer for ViewData. The single qualifier can be ignored in the cloning process by setting the D3DX11\_EFFECT\_CLONE\_FORCE\_NONSINGLE flag.

## Related topics

<dl> <dt>

[Effects (Direct3D 11)](d3d11-graphics-programming-guide-effects.md)
</dt> </dl>

 

 




