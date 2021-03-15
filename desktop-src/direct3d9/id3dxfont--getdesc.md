---
description: Gets a description of the current font object. GetDescW and GetDescA are identical to this method, except that a pointer is returned to a D3DXFONT\_DESCW or D3DXFONT\_DESCA structure, respectively.
ms.assetid: 21bcd3e0-3659-4d64-959a-0f2d65850cb1
title: ID3DXFont::GetDesc method (D3dx9core.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXFont.GetDesc
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXFont::GetDesc method

Gets a description of the current font object. GetDescW and GetDescA are identical to this method, except that a pointer is returned to a [**D3DXFONT\_DESCW**](d3dxfont-desc.md) or **D3DXFONT\_DESCA** structure, respectively.

## Syntax


```C++
HRESULT GetDesc(
  [out] D3DXFONT_DESC *pDesc
);
```



## Parameters

<dl> <dt>

*pDesc* \[out\]
</dt> <dd>

Type: **[**D3DXFONT\_DESC**](d3dxfont-desc.md)\***

Pointer to a [**D3DXFONT\_DESC**](d3dxfont-desc.md) structure that describes the font object.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is S\_OK. If the method fails, the following value will be returned: D3DERR\_INVALIDCALL.

## Remarks

This method describes Unicode font objects if UNICODE is defined. Otherwise GetDescA is called, which returns a pointer to the [**D3DXFONT\_DESCA**](d3dxfont-desc.md) structure.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9core.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXFont](id3dxfont.md)
</dt> </dl>

 

 




