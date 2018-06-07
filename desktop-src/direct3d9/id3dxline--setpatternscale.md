---
Description: Stretches the stipple pattern along the line direction.
ms.assetid: 411464db-d721-4252-bff3-bec57252273e
title: ID3DXLine::SetPatternScale method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ID3DXLine::SetPatternScale method

Stretches the stipple pattern along the line direction.

## Syntax


```C++
HRESULT SetPatternScale(
  [in] FLOAT fPatternScale
);
```



## Parameters

<dl> <dt>

*fPatternScale* \[in\]
</dt> <dd>

Type: **[**FLOAT**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Stipple pattern scaling value. 1.0f is the default value and represents no scaling. A value less than 1.0f shrinks the pattern, and a value greater than 1.0 stretches the pattern.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/windows/desktop/455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, D3DXERR\_INVALIDDATA.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9core.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXLine](id3dxline.md)
</dt> </dl>

 

 




