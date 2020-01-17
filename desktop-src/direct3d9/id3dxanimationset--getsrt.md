---
Description: Gets the scale, rotation, and translation values of the animation set.
ms.assetid: 84fc56f3-15bf-4e27-ad06-57fab94f3a33
title: ID3DXAnimationSet::GetSRT method (D3dx9anim.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXAnimationSet.GetSRT
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXAnimationSet::GetSRT method

Gets the scale, rotation, and translation values of the animation set.

## Syntax


```C++
HRESULT GetSRT(
  [in]  DOUBLE         PeriodicPosition,
  [in]  UINT           Animation,
  [out] D3DXVECTOR3    *pScale,
  [out] D3DXQUATERNION *pRotation,
  [out] D3DXVECTOR3    *pTranslation
);
```



## Parameters

<dl> <dt>

*PeriodicPosition* \[in\]
</dt> <dd>

Type: **[**DOUBLE**](https://msdn.microsoft.com/library/Aa383751(v=VS.85).aspx)**

Position of the animation set. The position can be obtained by calling [**ID3DXAnimationSet::GetPeriodicPosition**](id3dxanimationset--getperiodicposition.md).

</dd> <dt>

*Animation* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/Aa383751(v=VS.85).aspx)**

Animation index.

</dd> <dt>

*pScale* \[out\]
</dt> <dd>

Type: **[**D3DXVECTOR3**](d3dxvector3.md)\***

Pointer to the [**D3DXVECTOR3**](d3dxvector3.md) vector that describes the scale of the animation set.

</dd> <dt>

*pRotation* \[out\]
</dt> <dd>

Type: **[**D3DXQUATERNION**](d3dxquaternion.md)\***

Pointer to the [**D3DXQUATERNION**](d3dxquaternion.md) quaternion that describes the rotation of the animation set.

</dd> <dt>

*pTranslation* \[out\]
</dt> <dd>

Type: **[**D3DXVECTOR3**](d3dxvector3.md)\***

Pointer to the [**D3DXVECTOR3**](d3dxvector3.md) vector that describes the translation of the animation set.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

The return values of this method are implemented by an application programmer. In general, if no error occurs, program the method to return D3D\_OK. Otherwise, program the method to return an appropriate error message from [D3DERR](d3derr.md) or [**D3DXERR**](https://msdn.microsoft.com/library/Bb172825(v=VS.85).aspx).

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXAnimationSet](id3dxanimationset.md)
</dt> </dl>

 

 




