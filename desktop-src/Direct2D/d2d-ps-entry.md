---
title: D2D_PS_ENTRY function (D2d1effecthelpers.h)
description: A macro that defines a pixel shader entry point with the given function name.
ms.assetid: 4C87369A-EF51-46BA-9CA4-386630A7F866
keywords:
- D2D_PS_ENTRY function Direct2D
topic_type:
- apiref
api_name:
- D2D_PS_ENTRY
api_location:
- d2d1.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# D2D\_PS\_ENTRY function

A macro that defines a pixel shader entry point with the given function name.

## Syntax

``` syntax
void WINAPI D2D_PS_ENTRY(
  in string Entryname
);
```

## Parameters

<dl> <dt>

*Entryname* \[in\]
</dt> <dd>

The pixel shader entry point name.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

Use this macro instead of specifying the entry point s input signature in the normal manner: all parameters are implicit and added by Direct2D during compilation depending on the compilation target type (full shader or export function).

``` syntax
#define D2D_INPUT_COUNT 1 
#define D2D_INPUT0_SIMPLE 
#include  d2d1effectauthor.hlsli  

D2D_PS_ENTRY(LinkingCompatiblePixelShader) 
{ 
    float4 input = D2DGetInput(0);  

    input.rgb *= input.a; 

    return input; 
} 
```

In this short example note that no function parameters are declared, that the number of inputs and type of each input is declared before the entry function, the input is retrieved by calling [D2DGetInput](d2dgetinput.md), and that preprocessor directives must be defined before the helper file is included.

A linking-compatible shader must provide both a regular single-pass pixel shader and an export shader function. The D2D\_PS\_ENTRY macro allows each of these to be generated from the same code, when used in conjunction with the shader compilation script.

When compiling a full shader, the macros are expanded into the following code, which has a D2D Effects-compatible input signature.

``` syntax
Texture2D<float4> InputTexture0; 
SamplerState InputSampler0; 

float4 LinkingCompatiblePixelShader(
    float4 pos   : SV_POSITION,   
    float4 posScene : SCENE_POSITION,    
    float4 uv0  : TEXCOORD0 
    ) : SV_Target 
{ 
    float4 input = InputTexture0.Sample(InputSampler0, uv0.xy);  

    input.rgb *= input.a; 

    return input; 
} 
```

When compiling an export function version of the same code, the following code is generated:

``` syntax
// Shader function version 
export float4 LinkingCompatiblePixelShader_Function( 
    float4 input0 : INPUT0 
    ) 
{ 
    input.rgb *= input.a; 

    return input; 
} 
```

Note that the texture input, normally retrieved by sampling a Texture2D, has been replaced with a function input input0.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D2d1effecthelpers.hlsli</dt> </dl> |
| DLL<br/>    | <dl> <dt>D2d1.dll</dt> </dl>                |



## See also

<dl> <dt>

[Effect Shader Linking](effect-shader-linking.md)
</dt> <dt>

[HLSL Helpers](hlsl-helpers.md)
</dt> </dl>

 

 





