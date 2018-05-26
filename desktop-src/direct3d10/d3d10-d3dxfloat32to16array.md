---
Description: Converts an array of 32-bit floats to 16-bit floats.
ms.assetid: 2114cf25-cc83-4c4a-9db5-ecc0f8ff1e85
title: D3DXFloat32To16Array function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DXFloat32To16Array function

Converts an array of 32-bit floats to 16-bit floats.

## Syntax


```C++
D3DXFLOAT16* D3DXFloat32To16Array(
  _In_       D3DXFLOAT16 *pOut,
  _In_ const FLOAT       *pIn,
  _In_       UINT        n
);
```



## Parameters

<dl> <dt>

*pOut* \[in\]
</dt> <dd>

Type: **[**D3DXFLOAT16**](direct3d9.d3dxfloat16)\***

Pointer to the array of 16-bit floats.

</dd> <dt>

*pIn* \[in\]
</dt> <dd>

Type: **const [**FLOAT**](winprog.windows_data_types)\***

Pointer to an array of 32-bit floats.

</dd> <dt>

*n* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

The number of elements in the array.

</dd> </dl>

## Return value

Type: **[**D3DXFLOAT16**](direct3d9.d3dxfloat16)\***

Pointer to an array of 16-bit floats.

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10Math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](d3d10-graphics-reference-d3dx10-functions-math.md)
</dt> </dl>

 

 




