---
description: Returns the values of the attributes at the vertex.
nms.assetid:
title: GetAttributeAtVertex
ms.topic: reference
ms.date: 07/10/2024
topic_type:
- APIRef
- kbSyntax
api_name:
- GetAttributeAtVertex
api_type:
- NA
---


# GetAttributeAtVertex

Returns the values of the attributes at the vertex.

## Syntax


```syntax
numeric<> GetAttributeAtVertex(numeric<> value, uint VertexID);
```

## Parameters

| Item | Description |
|------|-------------|
| *value* | [in] A scalar, vector, or matrix input from which to retrieve the attribute.  || *VertexID* | [in] The ID of the vertex at which to retrieve the attribute. Must be an integer.  |
## Return value

 Returns the attribute of the specified vertex. The return type can be a scalar, vector, or matrix with a component type of float or int.
## Type Description

| Name  | [**Template Type**](../direct3dhlsl/dx-graphics-hlsl-data-types.md)| [**Component Type**](../direct3dhlsl/dx-graphics-hlsl-data-types.md) | Size |
|-------|--------------------------------------------------------------------|----------------------------------------------------------------------|------|
| *ret*   | [**scalar**](../direct3dhlsl/dx-graphics-hlsl-scalar.md), [**vector**](../direct3dhlsl/dx-graphics-hlsl-vector.md), or [**matrix**](../direct3dhlsl/dx-graphics-hlsl-matrix.md) | [**float**](../WinProg/windows-data-types) or [**int**](../WinProg/windows-data-types) | any |
| *value*   | [**scalar**](../direct3dhlsl/dx-graphics-hlsl-scalar.md), [**vector**](../direct3dhlsl/dx-graphics-hlsl-vector.md), or [**matrix**](../direct3dhlsl/dx-graphics-hlsl-matrix.md) | [**float**](../WinProg/windows-data-types) or [**int**](../WinProg/windows-data-types) | any |
| *VertexID*   | [**scalar**](../direct3dhlsl/dx-graphics-hlsl-scalar.md) | [**uint**](../WinProg/windows-data-types) | 1 |

## Minimum Shader Model

This function is supported in the following shader models.
|Shader Model |	Supported|
|-------------|----------|
|[Shader Model 6.1](https://github.com/microsoft/DirectXShaderCompiler/wiki/Shader-Model-6.1) and higher shader models | yes |

## Shader Stages

* [**Pixel Shader**](../direct3dhlsl/dx-graphics-hlsl-writing-shaders-9.md#pixel-shader-basics)

## Remarks

GetAttributeAtVertex retrieves vertex attributes at specific vertices, useful for per-vertex operations in vertex shaders.
## See also


- [**Intrinsic Functions (DirectX HLSL)**](../direct3dhlsl/dx-graphics-hlsl-intrinsic-functions.md)
-  **See [GetAttributeAtVertex MeshShader Usage](https://microsoft.github.io/DirectX-Specs/d3d/MeshShader#:~:text=Attributes%20used%20with,have%20any%20effect.).**