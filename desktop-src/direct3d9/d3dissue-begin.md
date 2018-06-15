---
Description: This macro creates a value used by Issue to issue a query begin.
ms.assetid: 21b8a2b0-d18f-4412-b655-3a913b7312ee
title: D3DISSUE\_BEGIN
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# D3DISSUE\_BEGIN

This macro creates a value used by [**Issue**](/windows/desktop/api/d3d9helper/nf-d3d9-idirect3dquery9-issue) to issue a query begin.

``` syntax
#define D3DISSUE_BEGIN (1 << 1)
```

## Remarks

D3DISSUE\_BEGIN is valid for the following query type.

-   D3DQUERYTYPE\_OCCLUSION

## Requirements



|                   |                                                                                        |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3d9types.h</dt> </dl> |



## See also

<dl> <dt>

[Macros](dx9-graphics-reference-d3d-macros.md)
</dt> <dt>

[**D3DISSUE\_END**](d3dissue-end.md)
</dt> <dt>

[**D3DGETDATA\_FLUSH**](d3dgetdata-flush.md)
</dt> <dt>

[**D3DQUERYTYPE**](https://msdn.microsoft.com/en-us/library/Bb172594(v=VS.85).aspx)
</dt> </dl>

 

 




