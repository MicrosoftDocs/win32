---
description: Describes preprocessor definitions used by an effect object.
ms.assetid: 43413b79-e331-4466-b288-bd4439c135a2
title: D3DXMACRO structure (D3dx9shader.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXMACRO
api_type: 
- HeaderDef
api_location: 
- d3dx9shader.h
---

# D3DXMACRO structure

Describes preprocessor definitions used by an effect object.

## Syntax


```C++
typedef struct D3DXMACRO {
  LPCSTR Name;
  LPCSTR Definition;
} D3DXMACRO, *LPD3DXMACRO;
```



## Members

<dl> <dt>

**Name**
</dt> <dd>

Type: **[**LPCSTR**](../winprog/windows-data-types.md)**

</dd> <dd>

Preprocessor name.

</dd> <dt>

**Definition**
</dt> <dd>

Type: **[**LPCSTR**](../winprog/windows-data-types.md)**

</dd> <dd>

Definition name.

</dd> </dl>

## Remarks

To use **D3DXMACRO**s in more than one line, prefix each new line character with a backslash (like a \#define in the C language). For example:


```
sample=
macro.Name = "DO_CODE_BLOCK";
macro.Definition =
    "/* here is a block of code */\\\n"
    "{ do something ... }\\\n";
```



Notice the 3 backslash characters at the end of the line. The first two are required to output a single '\\', followed by the newline character "\\n". Optionally, you may also want to terminate your lines using "\\\\\\r\\n".

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9shader.h</dt> </dl> |



## See also

<dl> <dt>

[Effect Structures](dx9-graphics-reference-effects-structures.md)
</dt> <dt>

[**D3DXCreateEffectFromFile**](d3dxcreateeffectfromfile.md)
</dt> </dl>

 

 
