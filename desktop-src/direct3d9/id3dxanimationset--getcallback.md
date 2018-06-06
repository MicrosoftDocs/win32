---
Description: Gets information about a specific callback in the animation set.
ms.assetid: e8388bfc-5438-4216-a98f-dd0dbca12c87
title: ID3DXAnimationSet::GetCallback method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ID3DXAnimationSet::GetCallback method

Gets information about a specific callback in the animation set.

## Syntax


```C++
HRESULT GetCallback(
  [in]  DOUBLE Position,
  [in]  DWORD  Flags,
  [out] DOUBLE *pCallbackPosition,
  [out] LPVOID *ppCallbackData
);
```



## Parameters

<dl> <dt>

*Position* \[in\]
</dt> <dd>

Type: **[**DOUBLE**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Position from which to find callbacks.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Callback search flags. This parameter can be set to a combination of one or more flags from [**D3DXCALLBACK\_SEARCH\_FLAGS**](https://msdn.microsoft.com/VS|directx_sdk|~\d3dxcallback_search_flags.htm).

</dd> <dt>

*pCallbackPosition* \[out\]
</dt> <dd>

Type: **[**DOUBLE**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)\***

Pointer to the position of the callback.

</dd> <dt>

*ppCallbackData* \[out\]
</dt> <dd>

Type: **[**LPVOID**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)\***

Address of the callback data pointer.

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

 

 




