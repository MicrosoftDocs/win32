---
description: Enable or disable debug messages.
ms.assetid: 5c2aa3cf-ee6a-40fd-b300-67cb6ce691b6
title: D3DX10DebugMute function (D3DX10Core.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DX10DebugMute
api_type: 
- LibDef
api_location: 
- D3DX10.lib
- D3DX10.dll
---

# D3DX10DebugMute function

Enable or disable debug messages.

## Syntax


```C++
HRESULT D3DX10DebugMute(
  _In_ BOOL Mute
);
```



## Parameters

<dl> <dt>

*Mute* \[in\]
</dt> <dd>

Type: **[**BOOL**](../winprog/windows-data-types.md)**

Set to **TRUE** to enable debug messages; set to **FALSE** to disable debug messages.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

The return value is one of the values listed in [Direct3D 10 Return Codes](d3d10-graphics-reference-returnvalues.md).

## Remarks

Use this function to disable error messages for D3DX10 APIs during debug; the use of this function should be guarded by the D3D10\_DEBUG compiler switch.


```
#ifdef D3D10_DEBUG
  BOOL WINAPI D3DX10DebugMute(BOOL Mute);  
#endif
```



The default state is **TRUE** for a debug build.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10Core.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl>   |



## See also

<dl> <dt>

[General Purpose Functions](d3d10-graphics-reference-d3dx10-functions-general-purpose.md)
</dt> </dl>

 

 
