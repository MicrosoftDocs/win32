---
Description: Turns on or off all D3DX debug output.
ms.assetid: e35cbfd2-401e-47ec-9f5b-e2ed63ea1fcd
title: D3DXDebugMute function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

Type: **[**BOOL**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

If **TRUE**, debugger output is halted; if **FALSE**, debug output is enabled.

</dd> </dl>

## Return value

Type: **[**BOOL**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

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

 

 




