---
Description: Note  Instead of using this legacy function, we recommend that you use the D3DDisassemble API. This function -- which disassembles a compiled effect into a text string that contains assembly instructions and register assignments -- has been deprecated.
ms.assetid: 218ac120-33ce-44db-84a7-99fef3281f07
title: D3DX10DisassembleEffect function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# D3DX10DisassembleEffect function

> [!Note]  
> Instead of using this legacy function, we recommend that you use the [**D3DDisassemble**](https://msdn.microsoft.com/VS|directx_sdk|~\d3ddisassemble.htm) API.

 

This function -- which disassembles a compiled effect into a text string that contains assembly instructions and register assignments -- has been deprecated. Instead, use [**D3DDisassemble10Effect**](https://msdn.microsoft.com/VS|directx_sdk|~\d3ddisassemble10effect.htm).

## Syntax


```C++
HRESULT D3DX10DisassembleEffect(
  _In_  ID3D10Effect *pEffect,
  _In_  BOOL         EnableColorCode,
  _Out_ ID3D10Blob   **ppDisassembly
);
```



## Parameters

<dl> <dt>

*pEffect* \[in\]
</dt> <dd>

Type: **[**ID3D10Effect**](/windows/desktop/api/D3D10Effect/nn-d3d10effect-id3d10effect)\***

A pointer to the effect interface (see [**ID3D10Effect Interface**](/windows/desktop/api/D3D10Effect/nn-d3d10effect-id3d10effect)).

</dd> <dt>

*EnableColorCode* \[in\]
</dt> <dd>

Type: **[**BOOL**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Include HTML tags in the output to color code the result.

</dd> <dt>

*ppDisassembly* \[out\]
</dt> <dd>

Type: **[**ID3D10Blob**](/windows/desktop/api/D3DCommon/nn-d3dcommon-id3d10blob)\*\***

Address of a buffer (see [**ID3D10Blob Interface**](/windows/desktop/api/D3DCommon/nn-d3dcommon-id3d10blob)) which contains the disassembled effect.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/windows/desktop/455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

Returns one of the following [Direct3D 10 Return Codes](d3d10-graphics-reference-returnvalues.md).

## Requirements



|                   |                                                                                         |
|-------------------|-----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3DX10Core.h</dt> </dl> |



## See also

<dl> <dt>

[General Purpose Functions](d3d10-graphics-reference-d3dx10-functions-general-purpose.md)
</dt> </dl>

 

 




