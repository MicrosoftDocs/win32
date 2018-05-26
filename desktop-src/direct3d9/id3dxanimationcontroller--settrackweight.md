---
Description: Sets the track weight. The weight is used to determine how to blend multiple tracks together.
ms.assetid: a00ceae4-47b4-4fb9-a028-97493e3dc071
title: ID3DXAnimationControllerSetTrackWeight method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXAnimationController::SetTrackWeight method

Sets the track weight. The weight is used to determine how to blend multiple tracks together.

## Syntax


```C++
HRESULT SetTrackWeight(
  [in] UINT  Track,
  [in] FLOAT Weight
);
```



## Parameters

<dl> <dt>

*Track* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Identifier of the track to set the weight on.

</dd> <dt>

*Weight* \[in\]
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)**

Weight value.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be one of the following values: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXAnimationController](id3dxanimationcontroller.md)
</dt> </dl>

 

 




