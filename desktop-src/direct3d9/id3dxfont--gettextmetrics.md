---
description: Retrieves font characteristics that are identified in a TEXTMETRIC structure. This method supports ANSI and Unicode compiler settings.
ms.assetid: 37788281-5bb0-45bb-b6d4-bdc4d811e3af
title: ID3DXFont::GetTextMetrics method (D3dx9core.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXFont.GetTextMetrics
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXFont::GetTextMetrics method

Retrieves font characteristics that are identified in a [**TEXTMETRIC**](/windows/win32/api/wingdi/ns-wingdi-textmetrica) structure. This method supports ANSI and Unicode compiler settings.

## Syntax


```C++
BOOL GetTextMetrics(
  [out] TEXTMETRIC *pTextMetrics
);
```



## Parameters

<dl> <dt>

*pTextMetrics* \[out\]
</dt> <dd>

Type: **[**TEXTMETRIC**](/windows/win32/api/wingdi/ns-wingdi-textmetrica)\***

Pointer to a [**TEXTMETRIC**](/windows/win32/api/wingdi/ns-wingdi-textmetrica) structure, which contains font properties.

</dd> </dl>

## Return value

Type: **[**BOOL**](../winprog/windows-data-types.md)**

Nonzero if the function is successful; otherwise 0.

## Remarks

The compiler setting also determines the structure type. If Unicode is defined, the function returns a TEXTMETRICW structure. Otherwise, the function call returns a TEXTMETRICA structure.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9core.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXFont](id3dxfont.md)
</dt> </dl>

 

 
