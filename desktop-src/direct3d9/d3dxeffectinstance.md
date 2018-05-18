---
Description: 'Data type for managing a set of default effect parameters.'
ms.assetid: 'a3408c0b-b4a6-47b1-b12e-594c13bd3a7d'
title: D3DXEFFECTINSTANCE structure
---

# D3DXEFFECTINSTANCE structure

Data type for managing a set of default effect parameters.

## Syntax


```C++
typedef struct D3DXEFFECTINSTANCE {
  LPSTR               pEffectFilename;
  DWORD               NumDefaults;
  LPD3DXEFFECTDEFAULT pDefaults;
} D3DXEFFECTINSTANCE, *LPD3DXEFFECTINSTANCE;
```



## Members

<dl> <dt>

**pEffectFilename**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Name of the effect file.

</dd> <dt>

**NumDefaults**
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

</dd> <dd>

Number of default parameters.

</dd> <dt>

**pDefaults**
</dt> <dd>

Type: **[**LPD3DXEFFECTDEFAULT**](d3dxeffectdefault.md)**

</dd> <dd>

Pointer to an array of [**D3DXEFFECTDEFAULT**](d3dxeffectdefault.md) elements, each of which contains an effect parameter.

</dd> </dl>

## Requirements



|                   |                                                                                        |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9mesh.h</dt> </dl> |



## See also

<dl> <dt>

[Effect Structures](dx9-graphics-reference-effects-structures.md)
</dt> </dl>

 

 




