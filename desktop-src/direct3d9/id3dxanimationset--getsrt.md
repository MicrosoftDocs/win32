---
Description: Gets the scale, rotation, and translation values of the animation set.
ms.assetid: 84fc56f3-15bf-4e27-ad06-57fab94f3a33
title: ID3DXAnimationSet::GetSRT method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

Type: **[**DOUBLE**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Position of the animation set. The position can be obtained by calling [**ID3DXAnimationSet::GetPeriodicPosition**](id3dxanimationset--getperiodicposition.md).

</dd> <dt>

*Animation* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

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

Type: **[**HRESULT**](https://msdn.microsoft.com/windows/desktop/455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

The return values of this method are implemented by an application programmer. In general, if no error occurs, program the method to return D3D\_OK. Otherwise, program the method to return an appropriate error message from [D3DERR](d3derr.md) or [**D3DXERR**](https://msdn.microsoft.com/VS|directx_sdk|~\d3dxerr.htm).

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXAnimationSet](id3dxanimationset.md)
</dt> </dl>

 

 




