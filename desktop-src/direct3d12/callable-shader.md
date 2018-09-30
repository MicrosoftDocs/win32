---
Description: A shader that is invoked from another shader with the CallShader intrinsic.    
ms.assetid: 
title: Callable Shader
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Callable Shader
api_type: 
- NA
---

# Callable Shader

A shader that is invoked from another shader with the **CallShader** intrinsic.

There is a parameter structure supplied at the **CallShader** call site that must match the parameter structure used in the callable shader pointed to by the requested index into the callable shader table supplied through the **DispatchRays** method.  The callable shader must declare this parameter as *inout*.  Additionally, the callable shader may read launch index and dimension inputs. For more information, see **System Values**. 


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

 

 




