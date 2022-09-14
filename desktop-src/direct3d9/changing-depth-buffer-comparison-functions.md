---
description: By default, when depth-testing is performed on a rendering surface, the Direct3D system updates the render-target surface if the corresponding depth value (z or w) for each point is less than the value in the depth buffer.
ms.assetid: e9243c05-e943-4a42-ab73-e684900fc81d
title: Changing Depth Buffer Comparison Functions (D3D9)
ms.topic: article
ms.date: 05/31/2018
---

# Changing Depth Buffer Comparison Functions (D3D9)

By default, when depth-testing is performed on a rendering surface, the Direct3D system updates the render-target surface if the corresponding depth value (z or w) for each point is less than the value in the depth buffer. In a C++ application, you change how the system performs comparisons on depth values by calling the [**IDirect3DDevice9::SetRenderState**](/windows/desktop/api) method with the *State* parameter set to D3DRS\_ZFUNC. The *Value* parameter should be set to a value in the [**D3DCMPFUNC**](./d3dcmpfunc.md) enumerated type.

## Related topics

<dl> <dt>

[Depth Buffers](depth-buffers.md)
</dt> </dl>

 

 
