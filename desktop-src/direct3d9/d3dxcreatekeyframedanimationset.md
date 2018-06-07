---
Description: Creates a ID3DXKeyframedAnimationSet key framed animation set interface.
ms.assetid: 7b4fffdc-696c-400c-a0cc-fc755fd25b75
title: D3DXCreateKeyframedAnimationSet function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# D3DXCreateKeyframedAnimationSet function

Creates a [**ID3DXKeyframedAnimationSet**](id3dxkeyframedanimationset.md) key framed animation set interface.

## Syntax


```C++
HRESULT D3DXCreateKeyframedAnimationSet(
  _In_        LPCSTR                      pName,
  _In_        DOUBLE                      TicksPerSecond,
  _In_        D3DXPLAYBACK_TYPE           Playback,
  _In_        UINT                        NumAnimations,
  _In_        UINT                        NumCallbackKeys,
  _In_  const LPD3DXKEY_CALLBACK          *pCallKeys,
  _Out_       LPD3DXKEYFRAMEDANIMATIONSET *ppAnimationSet
);
```



## Parameters

<dl> <dt>

*pName* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Pointer to the name of the animation set.

</dd> <dt>

*TicksPerSecond* \[in\]
</dt> <dd>

Type: **[**DOUBLE**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Number of key frame ticks that elapse per second.

</dd> <dt>

*Playback* \[in\]
</dt> <dd>

Type: **[**D3DXPLAYBACK\_TYPE**](https://msdn.microsoft.com/VS|directx_sdk|~\d3dxplayback_type.htm)**

Type of the animation set playback loop. See [**D3DXPLAYBACK\_TYPE**](https://msdn.microsoft.com/VS|directx_sdk|~\d3dxplayback_type.htm).

</dd> <dt>

*NumAnimations* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Number of scale, rotate, and translate (SRT) animation sets.

</dd> <dt>

*NumCallbackKeys* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Number of callback keys.

</dd> <dt>

*pCallKeys* \[in\]
</dt> <dd>

Type: **const [**LPD3DXKEY\_CALLBACK**](d3dxkey-callback.md)\***

Pointer to a [**D3DXKEY\_CALLBACK**](d3dxkey-callback.md) structure that stores user callback data.

</dd> <dt>

*ppAnimationSet* \[out\]
</dt> <dd>

Type: **[**LPD3DXKEYFRAMEDANIMATIONSET**](id3dxkeyframedanimationset.md)\***

Address of a pointer to the [**ID3DXKeyframedAnimationSet**](id3dxkeyframedanimationset.md) key framed animation set interface.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/windows/desktop/455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the function succeeds, the return value is S\_OK. If the function fails, the return value can be one of the following values: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Animation Functions](dx9-graphics-reference-d3dx-functions-animation.md)
</dt> </dl>

 

 




