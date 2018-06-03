---
Description: Retrieve font characteristics.
ms.assetid: ef7e0d18-492b-476b-945a-bfc0232a939a
title: ID3DX10Font::GetTextMetrics method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

Type: **[**BOOL**](https://msdn.microsoft.com/windows/desktop/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

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

 

 




