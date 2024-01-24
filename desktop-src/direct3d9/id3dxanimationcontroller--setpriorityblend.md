---
description: Sets the priority blending weight used by the animation controller.
ms.assetid: b053024b-f219-48b3-906e-161d9cf47556
title: ID3DXAnimationController::SetPriorityBlend method (D3dx9anim.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXAnimationController.SetPriorityBlend
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXAnimationController::SetPriorityBlend method

Sets the priority blending weight used by the animation controller.

## Syntax


```C++
HRESULT SetPriorityBlend(
  [in] FLOAT BlendWeight
);
```



## Parameters

<dl> <dt>

*BlendWeight* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

Priority blending weight used by the animation controller.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be one of the following values: D3DERR\_INVALIDCALL.

## Remarks

The blend weight is used to blend high and low priority tracks together.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXAnimationController](id3dxanimationcontroller.md)
</dt> <dt>

[**GetPriorityBlend**](id3dxanimationcontroller--getpriorityblend.md)
</dt> </dl>

 

 
