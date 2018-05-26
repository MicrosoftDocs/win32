---
Description: Specifies the thickness of the line.
ms.assetid: cedf9217-2b47-40c3-a64c-9872c1083d71
title: ID3DXLineSetWidth method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXLine::SetWidth method

Specifies the thickness of the line.

## Syntax


```C++
HRESULT SetWidth(
  [in] FLOAT fWidth
);
```



## Parameters

<dl> <dt>

*fWidth* \[in\]
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)**

Describes the line width.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

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

 

 




