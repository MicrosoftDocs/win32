---
description: Invokes another shader from within a shader.
ms.assetid: 
title: CallShader function
ms.date: 10/18/2022
ms.topic: reference
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CallShader
api_type: 
- NA
---

# CallShader function

Invokes another shader from within a shader.

## Syntax
This intrinsic function definition is equivalent to the following function template:

```
template<param_t>
void CallShader(uint ShaderIndex, inout param_t Parameter);
```

## Parameters

`ShaderIndex`

An unsigned integer representing the index into the [callable shader](callable-shader.md) table specified in the call to [**DispatchRays**](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist4-dispatchrays).

`Parameter`

The user-defined parameters to pass to the callable shader. This parameter structure must match the parameter structure used in the callable shader pointed to in the shader table.

## Return Value

**void**

## Remarks

This function can be called from the following raytracing shader types:

* [**Callable shader**](callable-shader.md)
* [**Closest hit shader**](closest-hit-shader.md)
* [**Miss shader**](miss-shader.md)
* [**Ray generation shader**](ray-generation-shader.md)

## See also

* [Direct3D 12 raytracing HLSL reference](direct3d-12-raytracing-hlsl-reference.md)
