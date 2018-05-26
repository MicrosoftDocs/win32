---
Description: Sets the track to the specified local animation time.
ms.assetid: 2ce87b06-1196-415f-958c-7bd407d6c69c
title: ID3DXAnimationControllerSetTrackPosition method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXAnimationController::SetTrackPosition method

Sets the track to the specified local animation time.

## Syntax


```C++
HRESULT SetTrackPosition(
  [in] UINT   Track,
  [in] DOUBLE Position
);
```



## Parameters

<dl> <dt>

*Track* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Track identifier.

</dd> <dt>

*Position* \[in\]
</dt> <dd>

Type: **[**DOUBLE**](winprog.windows_data_types)**

Local animation time value to assign to the track.

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

 

 




