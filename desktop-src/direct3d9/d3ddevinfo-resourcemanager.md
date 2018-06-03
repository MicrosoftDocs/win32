---
Description: Resource usage statistics.
ms.assetid: e43de550-2025-4210-a420-e41d14620704
title: D3DDEVINFO\_ResourceManager structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# D3DDEVINFO\_ResourceManager structure

Resource usage statistics.

## Syntax


```C++
typedef struct D3DDEVINFO_ResourceManager {
  D3DRESOURCESTATS stats[D3DRTYPECOUNT];
} D3DDEVINFO_ResourceManager, *LPD3DDEVINFO_ResourceManager;
```



## Members

<dl> <dt>

**stats**
</dt> <dd>

Type: **[**D3DRESOURCESTATS**](d3dresourcestats.md)**

</dd> <dd>

Array of resource statistics elements. See [**D3DRESOURCESTATS**](d3dresourcestats.md).

</dd> </dl>

## Remarks

D3DRTYPECOUNT refers to the number of enumerations in [**D3DRESOURCETYPE**](https://msdn.microsoft.com/windows/desktop/6b360fb1-4a5a-47a2-bef9-d8234770bf0c).

## Requirements



|                   |                                                                                        |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3D9Types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Structures](dx9-graphics-reference-d3d-structures.md)
</dt> </dl>

 

 




