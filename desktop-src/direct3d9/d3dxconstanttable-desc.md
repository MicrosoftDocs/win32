---
Description: A description of the constant table.
ms.assetid: 848b328a-95a4-4fd0-a7d4-4fb0e5d14f64
title: D3DXCONSTANTTABLE\_DESC structure
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DXCONSTANTTABLE\_DESC structure

A description of the constant table.

## Syntax


```C++
typedef struct D3DXCONSTANTTABLE_DESC {
  LPCSTR Creator;
  DWORD  Version;
  UINT   Constants;
} D3DXCONSTANTTABLE_DESC, *LPD3DXCONSTANTTABLE_DESC;
```



## Members

<dl> <dt>

**Creator**
</dt> <dd>

Type: **[**LPCSTR**](winprog.windows_data_types)**

</dd> <dd>

Name of the constant table creator.

</dd> <dt>

**Version**
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

</dd> <dd>

Shader version.

</dd> <dt>

**Constants**
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

</dd> <dd>

Number of constants in the constant table.

</dd> </dl>

## Requirements



|                   |                                                                                          |
|-------------------|------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9shader.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Structures](dx9-graphics-reference-d3dx-structures.md)
</dt> <dt>

[**D3DXCONSTANT\_DESC**](d3dxconstant-desc.md)
</dt> </dl>

 

 




