---
Description: Gets the index of an animation, given its name.
ms.assetid: 6e91a4fe-3202-447b-b486-d29e8da64af2
title: ID3DXAnimationSet::GetAnimationIndexByName method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXAnimationSet.GetAnimationIndexByName
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXAnimationSet::GetAnimationIndexByName method

Gets the index of an animation, given its name.

## Syntax


```C++
HRESULT GetAnimationIndexByName(
  [in]  LPCSTR pName,
  [out] UINT   *pIndex
);
```



## Parameters

<dl> <dt>

*pName* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

Name of the animation.

</dd> <dt>

*pIndex* \[out\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)\***

Pointer to the animation index.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/en-us/library/Bb401631(v=MSDN.10).aspx)**

The return values of this method are implemented by an application programmer. In general, if no error occurs, program the method to return D3D\_OK. Otherwise, program the method to return an appropriate error message from [D3DERR](d3derr.md) or [**D3DXERR**](https://msdn.microsoft.com/en-us/library/Bb172825(v=VS.85).aspx).

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXAnimationSet](id3dxanimationset.md)
</dt> </dl>

 

 




