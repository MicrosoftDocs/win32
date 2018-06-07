---
Description: Saves a compressed precomputed radiance transfer (PRT) buffer to disk.
ms.assetid: cc94a83e-f755-411d-a993-4529c5d53cd5
title: D3DXSavePRTCompBufferToFile function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# D3DXSavePRTCompBufferToFile function

Saves a compressed precomputed radiance transfer (PRT) buffer to disk.

## Syntax


```C++
HRESULT D3DXSavePRTCompBufferToFile(
  _In_ LPCSTR              pFileName,
  _In_ LPD3DXPRTCOMPBUFFER pBuffer
);
```



## Parameters

<dl> <dt>

*pFileName* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Name of the file to which the compressed buffer is to be saved.

</dd> <dt>

*pBuffer* \[in\]
</dt> <dd>

Type: **[**LPD3DXPRTCOMPBUFFER**](id3dxprtcompbuffer.md)**

Address of a pointer to the input [**ID3DXPRTCompBuffer**](id3dxprtcompbuffer.md) object.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/windows/desktop/455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be D3DERR\_INVALIDCALL.

## Remarks

The compiler setting also determines the function version. If Unicode is defined, the function call resolves to D3DXSavePRTCompBufferToFileW. Otherwise, the function call resolves to D3DXSavePRTCompBufferToFileA.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Precomputed Radiance Transfer Functions](dx9-graphics-reference-d3dx-functions-prt.md)
</dt> </dl>

 

 




