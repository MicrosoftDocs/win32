---
Description: Toggles the mode to draw OpenGL-style lines.
ms.assetid: 298bf391-9f2b-4352-b9f8-3bc2ab661eee
title: ID3DXLine::SetGLLines method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ID3DXLine::SetGLLines method

Toggles the mode to draw OpenGL-style lines.

## Syntax


```C++
HRESULT SetGLLines(
  [in] BOOL bGLLines
);
```



## Parameters

<dl> <dt>

*bGLLines* \[in\]
</dt> <dd>

Type: **[**BOOL**](https://msdn.microsoft.com/windows/desktop/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Toggles OpenGL-style line drawing. **TRUE** enables OpenGL-style lines, and **FALSE** enables Direct3D-style lines.

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

 

 




