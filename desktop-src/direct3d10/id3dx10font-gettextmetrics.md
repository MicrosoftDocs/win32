---
Description: Retrieve font characteristics.
ms.assetid: ef7e0d18-492b-476b-945a-bfc0232a939a
title: ID3DX10FontGetTextMetrics method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

Pointer to a [TEXTMETRIC](http://msdn2.microsoft.com/en-us/library/ms534202.aspx) structure, which contains font properties. If Unicode is defined, the function returns a TEXTMETRICW structure. Otherwise, the function returns a TEXTMETRICA structure.

</dd> </dl>

## Return value

Type: **[**BOOL**](winprog.windows_data_types)**

Nonzero if the function is successful; otherwise 0.

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl> |



## See also

<dl> <dt>

[ID3DX10Font](id3dx10font.md)
</dt> <dt>

[D3DX Interfaces](d3d10-graphics-reference-d3dx10-interfaces.md)
</dt> </dl>

 

 




