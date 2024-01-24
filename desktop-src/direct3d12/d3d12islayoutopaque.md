---
title: D3D12IsLayoutOpaque function (D3dx12.h)
description: Indicates whether the layout is opaque.
ms.assetid: 43B46A18-A725-4999-BD97-108032793A95
keywords:
- D3D12IsLayoutOpaque function
topic_type:
- apiref
api_name:
- D3D12IsLayoutOpaque
api_location:
- D3D12.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# D3D12IsLayoutOpaque function

Indicates whether the layout is opaque.

## Syntax


```C++
bool inline D3D12IsLayoutOpaque(
   D3D12_TEXTURE_LAYOUT Layout
);
```



## Parameters

<dl> <dt>

*Layout* 
</dt> <dd>

Type: **[**D3D12\_TEXTURE\_LAYOUT**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_texture_layout)**

The layout to check, as a [**D3D12\_TEXTURE\_LAYOUT**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_texture_layout).

</dd> </dl>

## Return value

Type: **bool**

A **bool** that indicates whether the layout is opaque. A layout is opaque if it is D3D12\_TEXTURE\_LAYOUT\_UNKNOWN or D3D12\_TEXTURE\_LAYOUT\_64KB\_UNDEFINED\_SWIZZLE.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx12.h</dt> </dl>  |
| Library<br/> | <dl> <dt>D3D12.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>D3D12.dll</dt> </dl> |



## See also

<dl> <dt>

[Helper Functions for D3D12](helper-functions-for-d3d12.md)
</dt> </dl>

 

 





