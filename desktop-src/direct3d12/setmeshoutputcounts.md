---
description: This function sets the actual number of outputs from the threadgroup.
ms.assetid: 
title: SetMeshOutputCounts
ms.topic: reference
ms.date: 4/28/2024
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SetMeshOutputCounts
api_type: 
- NA
---

# SetMeshOutputCounts function

This function sets the actual number of outputs from the threadgroup.

## Syntax


```c++
void SetMeshOutputCounts(
    uint numVertices,
    uint numPrimitives);
```

## Remarks

At the beginning of the shader the implementation internally sets a
count of vertices and primitives to be exported from a threadgroup to 0.
It means that if a mesh shader returns without calling this function,
it will not output any mesh. This function sets the actual number of
outputs from the threadgroup.

Some restrictions on the function use and interactions with output arrays follow.

1.  This function can only be called once per shader.

2.  This call must occur before any writes to any of the
    [shared output arrays](https://microsoft.github.io/DirectX-Specs/d3d/MeshShader.html#shared-output-arrays).
    The validator will verify this is the case.

3.  If the compiler can prove that this function is not called,
    then the threadgroup doesn't have any output.
    If the shader writes to any of the
    [shared output arrays](https://microsoft.github.io/DirectX-Specs/d3d/MeshShader.html#shared-output-arrays),
    compilation and shader validation will fail.
    If the shader does not call any of these functions,
    the compiler will issue a warning,
    and no rasterization work will be issued.

4.  Only the input values from the first active thread are used.

5.  This call must dominate all writes to
    [shared output arrays](https://microsoft.github.io/DirectX-Specs/d3d/MeshShader.html#shared-output-arrays).
    In other words, there must not be any execution path
    that even appears to reach any writes to any output array
    without first having executed this call.