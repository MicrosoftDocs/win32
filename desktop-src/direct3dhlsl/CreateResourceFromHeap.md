---
description: Creates a resource from a heap, typically used for dynamic resource allocation.
nms.assetid:
title: CreateResourceFromHeap
ms.topic: reference
ms.date: 07/10/2024
topic_type:
- APIRef
- kbSyntax
api_name:
- CreateResourceFromHeap
api_type:
- NA
---


# CreateResourceFromHeap

Creates a resource from a heap, typically used for dynamic resource allocation.

## Syntax


```syntax
resource CreateResourceFromHeap(uint index);
```

## Parameters

| Item | Description |
|------|-------------|
| *index* | [in] An integer value specifying the index of the resource in the heap to create the resource from.  |
## Return value

 Returns a resource with the template and component type of resource. The returned resource is created from the heap at the specified index.
## Type Description

| Name  | [**Template Type**](../direct3dhlsl/dx-graphics-hlsl-data-types.md)| [**Component Type**](../direct3dhlsl/dx-graphics-hlsl-data-types.md) | Size |
|-------|--------------------------------------------------------------------|----------------------------------------------------------------------|------|
| *ret*   | [**Resource Types**](../direct3d12/resource-binding-in-hlsl.md) | **resource** | 1 |
| *index*   | [**scalar**](../direct3dhlsl/dx-graphics-hlsl-scalar.md) | [**uint**](../WinProg/windows-data-types) | 1 |

## Minimum Shader Model

This function is supported in the following shader models.
|Shader Model |	Supported|
|-------------|----------|

## Shader Stages


## Remarks

CreateResourceFromHeap creates a resource from a specified heap, enabling efficient resource management in GPU programming.
## See also


- [**Intrinsic Functions (DirectX HLSL)**](../direct3dhlsl/dx-graphics-hlsl-intrinsic-functions.md)