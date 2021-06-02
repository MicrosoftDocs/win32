---
description: An effect is created by loading it into the effects framework.
ms.assetid: b0a12620-4f8f-44d9-bc73-2c3ab30f80af
title: Create an Effect (Direct3D 10)
ms.topic: article
ms.date: 05/31/2018
---

# Create an Effect (Direct3D 10)

An effect is created by loading it into the effects framework. If the effect has never been compiled, it will be compiled when it is created. Effects that are already loaded into memory can be created by calling [**D3DX10CreateEffectFromMemory**](d3dx10createeffectfrommemory.md). The following code example uses [**D3DX10CreateEffectFromFile**](d3dx10createeffectfromfile.md) to create an effect from a file.


```
ID3D10Effect* g_pEffect10 = NULL; 

// Read the effect file 
D3DX10CreateEffectFromFile( "BasicHLSL10.fx", NULL, NULL,
  D3D10_SHADER_ENABLE_STRICTNESS, 0, pd3dDevice, NULL, NULL, 
  &g_pEffect10, NULL );
```



Reading an effect requires the same parameters as compiling an effect, plus a device and a pool.

## Related topics

<dl> <dt>

[Rendering an Effect (Direct3D 10)](d3d10-graphics-programming-guide-effects-render.md)
</dt> </dl>

 

 



