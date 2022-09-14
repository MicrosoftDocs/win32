---
description: Create a pixel shader version token.
ms.assetid: 70089a93-83df-4ac4-8d98-4e1bb6ad2581
title: D3DPS_VERSION macro (D3d9types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DPS_VERSION
api_type: 
- HeaderDef
api_location: 
- D3d9types.h
---

# D3DPS\_VERSION macro

Create a pixel shader version token.

## Syntax


```C++
DWORD D3DPS_VERSION(
   int _Major,
   int _Minor
);
```



## Parameters

<dl> <dt>

*\_Major* 
</dt> <dd>

The major pixel shader version.

</dd> <dt>

*\_Minor* 
</dt> <dd>

The minor pixel shader version.

</dd> </dl>

## Return value

Returns a DWORD value that is a pixel shader version.

## Remarks

Version Numbers

The version number is a combination of the major version and the minor vertex shader version numbers. Valid numbers are shown in the table.



| Major | Minor | Example             |
|-------|-------|---------------------|
| 1     | 1     | D3DPS\_VERSION(1,1) |
| 1     | 2     | D3DPS\_VERSION(1,2) |
| 1     | 3     | D3DPS\_VERSION(1,3) |
| 1     | 4     | D3DPS\_VERSION(1,4) |
| 2     | 0     | D3DPS\_VERSION(2,0) |
| 3     | 0     | D3DPS\_VERSION(3,0) |



 

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3d9types.h</dt> </dl> |



## See also

<dl> <dt>

[Macros](dx9-graphics-reference-d3d-macros.md)
</dt> <dt>

[D3DCAPS9](/windows/desktop/api/D3D9Caps/ns-d3d9caps-d3dcaps9)
</dt> </dl>

 

 




