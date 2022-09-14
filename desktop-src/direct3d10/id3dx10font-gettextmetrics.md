---
description: Retrieve font characteristics.
ms.assetid: ef7e0d18-492b-476b-945a-bfc0232a939a
title: ID3DX10Font::GetTextMetrics method (D3DX10.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DX10Font.GetTextMetrics
api_type: 
- COM
api_location: 
- D3DX10.lib
- D3DX10.dll
---

# ID3DX10Font::GetTextMetrics method

Retrieve font characteristics.

## Syntax


```C++
BOOL GetTextMetrics(
  [in] TEXTMETRIC *pTextMetrics
);
```



## Parameters

<dl> <dt>

*pTextMetrics* \[in\]
</dt> <dd>

Type: **TEXTMETRIC\***

Pointer to a [TEXTMETRIC](/previous-versions//ms534202(v=vs.85)) structure, which contains font properties. If Unicode is defined, the function returns a TEXTMETRICW structure. Otherwise, the function returns a TEXTMETRICA structure.

</dd> </dl>

## Return value

Type: **[**BOOL**](../winprog/windows-data-types.md)**

Nonzero if the function is successful; otherwise 0.

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

 

 
