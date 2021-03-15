---
description: Get a description of the current font object.
ms.assetid: f08beb35-351f-4087-a2db-097843463291
title: ID3DX10Font::GetDesc method (D3DX10.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DX10Font.GetDesc
api_type: 
- COM
api_location: 
- D3DX10.lib
- D3DX10.dll
---

# ID3DX10Font::GetDesc method

Get a description of the current font object.

## Syntax


```C++
HRESULT GetDesc(
  [in] D3DX10_FONT_DESC *pDesc
);
```



## Parameters

<dl> <dt>

*pDesc* \[in\]
</dt> <dd>

Type: **[**D3DX10\_FONT\_DESC**](d3dx10-font-desc.md)\***

Pointer to a [**D3DX10\_FONT\_DESC**](d3dx10-font-desc.md) structure that describes the font object. If UNICODE is defined, a pointer to a D3DX10FONT\_DESCW is returned; otherwise a pointer to a D3DX10FONT\_DESCA is returned.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is S\_OK. If the method fails, the following value will be returned: D3DERR\_INVALIDCALL.

## Remarks

This method describes Unicode font objects if UNICODE is defined. Otherwise GetDescA is called, which returns a pointer to the D3DX10FONT\_DESCA structure.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl> |



## See also

<dl> <dt>

[ID3DX10Font](id3dx10font.md)
</dt> <dt>

[D3DX Interfaces](d3d10-graphics-reference-d3dx10-interfaces.md)
</dt> </dl>

 

 




