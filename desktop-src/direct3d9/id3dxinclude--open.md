---
Description: A user-implemented method for opening and reading the contents of a shader \#include file.
ms.assetid: ad0105f7-042d-4e96-ad4a-1ece08e519af
title: ID3DXInclude::Open method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXInclude.Open
api_type: 
- COM
api_location: 
- D3dx9.lib
- D3dx9.dll
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

Type: **[**D3DXINCLUDE\_TYPE**](https://msdn.microsoft.com/en-us/library/Bb172881(v=VS.85).aspx)**

The location of the \#include file. See [**D3DXINCLUDE\_TYPE**](https://msdn.microsoft.com/en-us/library/Bb172881(v=VS.85).aspx).

</dd> <dt>

*pFileName* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

Name of the \#include file.

</dd> <dt>

*pParentData* \[in\]
</dt> <dd>

Type: **[**LPCVOID**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

Pointer to the container that includes the \#include file. The compiler might pass NULL in *pParentData*. For more information, see the "Searching for Include Files" section in [Compile an Effect (Direct3D 11)](https://msdn.microsoft.com/en-us/library/Ff476139(v=VS.85).aspx).

</dd> <dt>

*ppData* \[out\]
</dt> <dd>

Type: **[**LPCVOID**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)\***

Pointer to the returned buffer that contains the include directives. This pointer remains valid until [**ID3DXInclude::Close**](id3dxinclude--close.md) is called.

</dd> <dt>

*pBytes* \[out\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)\***

Number of bytes returned in ppData.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/en-us/library/Bb401631(v=MSDN.10).aspx)**

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

 

 




