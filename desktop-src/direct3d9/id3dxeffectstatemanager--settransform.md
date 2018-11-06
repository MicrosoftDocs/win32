---
Description: A callback function that must be implemented by a user to set a transform.
ms.assetid: 5d886554-ddb6-4b8a-a7fd-453e94b9516f
title: ID3DXEffectStateManager::SetTransform method
ms.topic: article
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- ID3DXEffectStateManager.SetTransform
api_type:
- COM
api_location:
- D3dx9.lib
- D3dx9.dll
---

# ID3DXEffectStateManager::SetTransform method

A callback function that must be implemented by a user to set a transform.

## Syntax


```C++
HRESULT SetTransform(
  [in]       D3DTRANSFORMSTATETYPE State,
  [in] const D3DMATRIX             *pMatrix
);
```



## Parameters

<dl> <dt>

*State* \[in\]
</dt> <dd>

Type: **[**D3DTRANSFORMSTATETYPE**](https://msdn.microsoft.com/en-us/library/Bb172619(v=VS.85).aspx)**

The type of transform to apply the matrix to. See [**D3DTRANSFORMSTATETYPE**](https://msdn.microsoft.com/en-us/library/Bb172619(v=VS.85).aspx).

</dd> <dt>

*pMatrix* \[in\]
</dt> <dd>

Type: **const [**D3DMATRIX**](d3dmatrix.md)\***

A transformation matrix. See [**D3DMATRIX**](d3dmatrix.md).

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/en-us/library/Bb401631(v=MSDN.10).aspx)**

The user-implemented method should return S\_OK. If the callback fails when setting the device state, either of the following will occur:

-   The effect will fail during [**ID3DXEffect::BeginPass**](id3dxeffect--beginpass.md).
-   The dynamic effect state call (such as [**IDirect3DDevice9::SetTransform**](https://msdn.microsoft.com/library/Bb174463(v=VS.85).aspx)) will fail.

## Requirements



|                    |                                                                                          |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Effect.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXEffectStateManager](id3dxeffectstatemanager.md)
</dt> </dl>

 

 




