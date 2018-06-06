---
Description: Describes a function used by an effect.
ms.assetid: 5d9deb82-7fe5-4408-8a6a-b34ecd97e8ba
title: D3DXFUNCTION\_DESC structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
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

Type: **[**LPCSTR**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

</dd> <dd>

Function name.

</dd> <dt>

**Annotations**
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

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

 

 




