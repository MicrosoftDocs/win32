---
Description: Gets the name of an animation, given its index.
ms.assetid: bcbdab21-ffaf-4c7e-96b9-f380dac284db
title: ID3DXAnimationSetGetAnimationNameByIndex method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXAnimationSet::GetAnimationNameByIndex method

Gets the name of an animation, given its index.

## Syntax


```C++
HRESULT GetAnimationNameByIndex(
  [in]  UINT   Index,
  [out] LPCSTR *ppName
);
```



## Parameters

<dl> <dt>

*Index* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Index of the animation.

</dd> <dt>

*ppName* \[out\]
</dt> <dd>

Type: **[**LPCSTR**](winprog.windows_data_types)\***

Address of a pointer to a string that receives the animation name.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

The return values of this method are implemented by an application programmer. In general, if no error occurs, program the method to return D3D\_OK. Otherwise, program the method to return an appropriate error message from [D3DERR](d3derr.md) or [**D3DXERR**](direct3d9.d3dxerr).

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXAnimationSet](id3dxanimationset.md)
</dt> </dl>

 

 




