---
Description: 'Describes a function used by an effect.'
ms.assetid: '5d9deb82-7fe5-4408-8a6a-b34ecd97e8ba'
title: 'D3DXFUNCTION\_DESC structure'
---

# D3DXFUNCTION\_DESC structure

Describes a function used by an effect.

## Syntax


```C++
typedef struct D3DXFUNCTION_DESC {
  LPCSTR Name;
  UINT   Annotations;
} D3DXFUNCTION_DESC, *LPD3DXFUNCTION_DESC;
```



## Members

<dl> <dt>

**Name**
</dt> <dd>

Type: **[**LPCSTR**](winprog.windows_data_types)**

</dd> <dd>

Function name.

</dd> <dt>

**Annotations**
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

</dd> <dd>

Unused. This member will always be set to zero by [**GetFunctionDesc**](id3dxbaseeffect--getfunctiondesc.md).

</dd> </dl>

## Requirements



|                   |                                                                                          |
|-------------------|------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9effect.h</dt> </dl> |



## See also

<dl> <dt>

[Effect Structures](dx9-graphics-reference-effects-structures.md)
</dt> </dl>

 

 




