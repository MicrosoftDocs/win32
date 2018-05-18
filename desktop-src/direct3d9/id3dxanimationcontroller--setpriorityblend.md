---
Description: 'Sets the priority blending weight used by the animation controller.'
ms.assetid: 'b053024b-f219-48b3-906e-161d9cf47556'
title: 'ID3DXAnimationController::SetPriorityBlend method'
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

Type: **[**FLOAT**](winprog.windows_data_types)**

Priority blending weight used by the animation controller.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be one of the following values: D3DERR\_INVALIDCALL.

## Remarks

The blend weight is used to blend high and low priority tracks together.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXAnimationController](id3dxanimationcontroller.md)
</dt> <dt>

[**GetPriorityBlend**](id3dxanimationcontroller--getpriorityblend.md)
</dt> </dl>

 

 




