---
Description: Returns the square of the length of a quaternion.
ms.assetid: 358d2a2b-7baf-4ae9-9b92-7a7f01ca843b
title: D3DXQuaternionLengthSq function (D3dx9math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXQuaternionLengthSq
api_type: 
- LibDef
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# D3DXQuaternionLengthSq function

Returns the square of the length of a quaternion.

## Syntax


```C++
FLOAT D3DXQuaternionLengthSq(
  _In_ const D3DXQUATERNION *pQ
);
```



## Parameters

<dl> <dt>

*pQ* \[in\]
</dt> <dd>

Type: **const [**D3DXQUATERNION**](d3dxquaternion.md)\***

Pointer to the source [**D3DXQUATERNION**](d3dxquaternion.md) structure.

</dd> </dl>

## Return value

Type: **[**FLOAT**](https://msdn.microsoft.com/library/Aa383751(v=VS.85).aspx)**

The quaternion's squared length.

## Remarks

Use [**D3DXQuaternionNormalize**](d3dxquaternionnormalize.md) for any quaternion input that is not already normalized.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](dx9-graphics-reference-d3dx-functions-math.md)
</dt> <dt>

[**D3DXQuaternionLength**](d3dxquaternionlength.md)
</dt> </dl>

 

 




