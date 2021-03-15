---
description: This macro creates a value used by Issue to issue a query end.
ms.assetid: 9ced932a-5d98-4bf8-aa11-06560f53546d
title: D3DISSUE_END (D3d9types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DISSUE_END
api_type:
- HeaderDef
api_location:
- D3d9types.h
---

# D3DISSUE\_END

This macro creates a value used by [**Issue**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3dquery9-issue) to issue a query end.

``` syntax
#define D3DISSUE_END (1 << 0)
```

## Parameters





 

## Remarks

This macro changes the query state to nonsignaled.

D3DISSUE\_END is valid for the following query types.

-   D3DQUERYTYPE\_VCACHE
-   D3DQUERYTYPE\_ResourceManager
-   D3DQUERYTYPE\_VERTEXSTATS
-   D3DQUERYTYPE\_EVENT
-   D3DQUERYTYPE\_OCCLUSION

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3d9types.h</dt> </dl> |



## See also

<dl> <dt>

[Macros](dx9-graphics-reference-d3d-macros.md)
</dt> <dt>

[**D3DISSUE\_BEGIN**](d3dissue-begin.md)
</dt> <dt>

[**D3DQUERYTYPE**](./d3dquerytype.md)
</dt> </dl>

 

 
