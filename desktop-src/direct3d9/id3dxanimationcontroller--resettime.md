---
Description: Resets the global animation time to zero. Any pending events will retain their original schedules, but in the new timeframe.
ms.assetid: 70b073ec-ef97-4af4-9f42-b6a6cc13605f
title: ID3DXAnimationControllerResetTime method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXAnimationController::ResetTime method

Resets the global animation time to zero. Any pending events will retain their original schedules, but in the new timeframe.

## Syntax


```C++
HRESULT ResetTime();
```



## Parameters

This method has no parameters.

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is S\_OK. If the method fails, the following value will be returned: D3DERR\_INVALIDCALL.

## Remarks

This method is typically used when the global animation time value is nearing the maximum precision of DOUBLE storage, or 2⁶⁴ - 1.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXAnimationController](id3dxanimationcontroller.md)
</dt> </dl>

 

 




