---
Description: Converts an array of 16-bit floats to 32-bit floats.
ms.assetid: cf07a21d-9ea3-4fbe-ab8f-564e2bbb8d60
title: D3DXFloat16To32Array function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# D3DXFloat16To32Array function

Converts an array of 16-bit floats to 32-bit floats.

## Syntax


```C++
FLOAT* D3DXFloat16To32Array(
  _In_       FLOAT       *pOut,
  _In_ const D3DXFLOAT16 *pIn,
  _In_       UINT        n
);
```



## Parameters

<dl> <dt>

*pOut* \[in\]
</dt> <dd>

Type: **[**FLOAT**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)\***

Pointer to the array of 32-bit floats.

</dd> <dt>

*pIn* \[in\]
</dt> <dd>

Type: **const [**D3DXFLOAT16**](https://msdn.microsoft.com/VS|directx_sdk|~\d3dxfloat16.htm)\***

Pointer to an array of 16-bit floats.

</dd> <dt>

*n* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Number of elements in the array.

</dd> </dl>

## Return value

Type: **[**FLOAT**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)\***

Pointer to an array of 32-bit floats.

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10Math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](d3d10-graphics-reference-d3dx10-functions-math.md)
</dt> </dl>

 

 




