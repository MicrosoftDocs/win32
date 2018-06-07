---
Description: Sets the priority blending weight for the specified animation track.
ms.assetid: 8d40b0f6-d79a-42c1-99fb-3f76bd46f30c
title: ID3DXAnimationController::SetTrackPriority method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ID3DXAnimationController::SetTrackPriority method

Sets the priority blending weight for the specified animation track.

## Syntax


```C++
HRESULT SetTrackPriority(
  [in] UINT              Track,
  [in] D3DXPRIORITY_TYPE Priority
);
```



## Parameters

<dl> <dt>

*Track* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Track identifier.

</dd> <dt>

*Priority* \[in\]
</dt> <dd>

Type: **[**D3DXPRIORITY\_TYPE**](https://msdn.microsoft.com/VS|directx_sdk|~\d3dxpriority_type.htm)**

Track priority. This parameter should be set to one of the constants from [**D3DXPRIORITY\_TYPE**](https://msdn.microsoft.com/VS|directx_sdk|~\d3dxpriority_type.htm).

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/windows/desktop/455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is S\_OK. If the method fails, the following value will be returned: D3DERR\_INVALIDCALL.

## Remarks

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXAnimationController](id3dxanimationcontroller.md)
</dt> </dl>

 

 




