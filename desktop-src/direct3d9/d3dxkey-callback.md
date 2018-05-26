---
Description: Describes a callback key for use in key frame animation.
ms.assetid: aca034f5-6961-49f1-ba7c-addcf016af2b
title: D3DXKEY\_CALLBACK structure
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DXKEY\_CALLBACK structure

Describes a callback key for use in key frame animation.

## Syntax


```C++
typedef struct D3DXKEY_CALLBACK {
  FLOAT  Time;
  LPVOID pCallbackData;
} D3DXKEY_CALLBACK, *LPD3DXKEY_CALLBACK;
```



## Members

<dl> <dt>

**Time**
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)**

</dd> <dd>

Key frame time stamp.

</dd> <dt>

**pCallbackData**
</dt> <dd>

Type: **[**LPVOID**](winprog.windows_data_types)**

</dd> <dd>

Pointer to user callback data.

</dd> </dl>

## Requirements



|                   |                                                                                        |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9anim.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Structures](dx9-graphics-reference-d3dx-structures.md)
</dt> </dl>

 

 




