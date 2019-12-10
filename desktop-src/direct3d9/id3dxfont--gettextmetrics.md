---
Description: Retrieves font characteristics that are identified in a TEXTMETRIC structure. This method supports ANSI and Unicode compiler settings.
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

Retrieves font characteristics that are identified in a [**TEXTMETRIC**](https://msdn.microsoft.com/library/Dd145132(v=VS.85).aspx) structure. This method supports ANSI and Unicode compiler settings.

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

Type: **[**TEXTMETRIC**](https://msdn.microsoft.com/library/Dd145132(v=VS.85).aspx)\***

Pointer to a [**TEXTMETRIC**](https://msdn.microsoft.com/library/Dd145132(v=VS.85).aspx) structure, which contains font properties.

</dd> </dl>

## Return value

Type: **[**BOOL**](https://msdn.microsoft.com/library/Aa383751(v=VS.85).aspx)**

Nonzero if the function is successful; otherwise 0.

## Remarks

The compiler setting also determines the structure type. If Unicode is defined, the function returns a TEXTMETRICW structure. Otherwise, the function call returns a TEXTMETRICA structure.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9core.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXFont](id3dxfont.md)
</dt> </dl>

 

 




