---
Description: 'Turns on or off all D3DX debug output.'
ms.assetid: 'e35cbfd2-401e-47ec-9f5b-e2ed63ea1fcd'
title: D3DXDebugMute function
---

# D3DXDebugMute function

Turns on or off all D3DX debug output.

## Syntax


```C++
BOOL D3DXDebugMute(
  _In_ BOOL Mute
);
```



## Parameters

<dl> <dt>

*Mute* \[in\]
</dt> <dd>

Type: **[**BOOL**](winprog.windows_data_types)**

If **TRUE**, debugger output is halted; if **FALSE**, debug output is enabled.

</dd> </dl>

## Return value

Type: **[**BOOL**](winprog.windows_data_types)**

Returns the previous value of Mute.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9core.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[General Purpose Functions](dx9-graphics-reference-d3dx-functions-general-purpose.md)
</dt> </dl>

 

 




