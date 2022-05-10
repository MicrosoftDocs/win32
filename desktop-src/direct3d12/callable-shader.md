---
description: A shader that is invoked from another shader with the CallShader intrinsic.
ms.assetid: 
title: Callable Shader
ms.date: 05/31/2018
ms.topic: reference
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Callable Shader
api_type: 
- NA
---

# Callable Shader

A shader that is invoked from another shader with the [**CallShader**](callshader-function.md) intrinsic.

There is a parameter structure supplied at the **CallShader** call site that must match the parameter structure used in the callable shader pointed to by the requested index into the callable shader table supplied through the [**DispatchRays**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist4-dispatchrays) method.  The callable shader must declare this parameter as *inout*.  Additionally, the callable shader may read launch index and dimension inputs. For more information, see [**System Value Intrinsics**](direct3d-12-raytracing-hlsl-system-value-intrinsics.md). 


## Shader Type attribute


```
[shader("callable")]
```



## Example

```
[shader("callable")]
void callable_main(inout MyParams params)
{
    // Perform some common operations and update params
    CallShader( ... );	// maybe
}

```

 

 




