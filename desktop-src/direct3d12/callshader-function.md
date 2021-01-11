---
description: Invokes another shader from within a shader.
ms.assetid: 
title: CallShader function
ms.date: 05/31/2018
ms.localizationpriority: low
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

An unsigned integer representing the index into the [callable shader](callable-shader.md) table specified in the call to [**DispatchRays**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist4-dispatchrays.

`Parameter`

The user-defined parameters to pass to the callable shader.  This parameter structure must match the parameter structure used in the callable shader pointed to in the shader table.


## Return Value

**void**

## Remarks

This function can be called from the following raytracing shader types:

* [**Callable Shader**](callable-shader.md)
* [**Closest Hit Shader**](closest-hit-shader.md)
* [**Miss Shader**](miss-shader.md)
* [**Ray Generation Shader**](ray-generation-shader.md)



## See also

<dl> <dt>

[Direct3D 12 Raytracing HLSL Reference](direct3d-12-raytracing-hlsl-reference.md)
</dt> </dl>

 

 




