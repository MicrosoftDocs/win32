---
Description: A user-implemented method for opening and reading the contents of a shader \#include file.
ms.assetid: ad0105f7-042d-4e96-ad4a-1ece08e519af
title: ID3DXInclude::Open method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ID3DXInclude::Open method

A user-implemented method for opening and reading the contents of a shader \#include file.

## Syntax


```C++
HRESULT Open(
  [in]  D3DXINCLUDE_TYPE IncludeType,
  [in]  LPCSTR           pFileName,
  [in]  LPCVOID          pParentData,
  [out] LPCVOID          *ppData,
  [out] UINT             *pBytes
);
```



## Parameters

<dl> <dt>

*IncludeType* \[in\]
</dt> <dd>

Type: **[**D3DXINCLUDE\_TYPE**](https://msdn.microsoft.com/VS|directx_sdk|~\d3dxinclude_type.htm)**

The location of the \#include file. See [**D3DXINCLUDE\_TYPE**](https://msdn.microsoft.com/VS|directx_sdk|~\d3dxinclude_type.htm).

</dd> <dt>

*pFileName* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Name of the \#include file.

</dd> <dt>

*pParentData* \[in\]
</dt> <dd>

Type: **[**LPCVOID**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Pointer to the container that includes the \#include file. The compiler might pass NULL in *pParentData*. For more information, see the "Searching for Include Files" section in [Compile an Effect (Direct3D 11)](https://msdn.microsoft.com/7624d55e-6466-4156-8f31-30f0d25a2883).

</dd> <dt>

*ppData* \[out\]
</dt> <dd>

Type: **[**LPCVOID**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)\***

Pointer to the returned buffer that contains the include directives. This pointer remains valid until [**ID3DXInclude::Close**](id3dxinclude--close.md) is called.

</dd> <dt>

*pBytes* \[out\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)\***

Number of bytes returned in ppData.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/windows/desktop/455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

The user-implemented method should return S\_OK. If the callback fails when reading the \#include file, the API that caused the callback to be called will fail. This is one of the following:

-   The HLSL shader will fail one of the D3DXCompileShader\*\*\* functions.
-   The assembly shader will fail one of the D3DXAssembleShader\*\*\* functions.
-   The effect will fail one of the D3DXCreateEffect\*\*\* or D3DXCreateEffectCompiler\*\*\* functions.

## Requirements



|                    |                                                                                          |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Shader.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXInclude](id3dxinclude.md)
</dt> <dt>

[**ID3DXInclude::Close**](id3dxinclude--close.md)
</dt> </dl>

 

 




