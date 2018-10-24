---
Description: Sets the priority blending weight for the specified animation track.
ms.assetid: 8d40b0f6-d79a-42c1-99fb-3f76bd46f30c
title: ID3DXAnimationController::SetTrackPriority method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXAnimationController.SetTrackPriority
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
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

Type: **[**UINT**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

Track identifier.

</dd> <dt>

*Priority* \[in\]
</dt> <dd>

Type: **[**D3DXPRIORITY\_TYPE**](https://msdn.microsoft.com/en-us/library/Bb205401(v=VS.85).aspx)**

Track priority. This parameter should be set to one of the constants from [**D3DXPRIORITY\_TYPE**](https://msdn.microsoft.com/en-us/library/Bb205401(v=VS.85).aspx).

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/en-us/library/Bb401631(v=MSDN.10).aspx)**

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

 

 




