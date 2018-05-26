---
Description: Note  Instead of using this legacy function, we recommend that you use the D3DDisassemble API. This function -- which disassembles a compiled shader into a text string that contains assembly instructions and register assignments -- no longer exists.
ms.assetid: f94264f8-121a-4bb7-bf1f-cc5d2cac6cd2
title: D3DX10DisassembleShader function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DX10DisassembleShader function

> [!Note]  
> Instead of using this legacy function, we recommend that you use the [**D3DDisassemble**](direct3dhlsl.d3ddisassemble) API.

 

This function -- which disassembles a compiled shader into a text string that contains assembly instructions and register assignments -- no longer exists. Instead, use [**D3DDisassemble10Effect**](direct3dhlsl.d3ddisassemble10effect).

## Syntax


```C++
HRESULT D3DX10DisassembleShader(
  _In_  const void       *pShader,
  _In_        SIZE_T     BytecodeLength,
  _In_        BOOL       EnableColorCode,
  _In_        LPCSTR     pComments,
  _Out_       ID3D10Blob **ppDisassembly
);
```



## Parameters

<dl> <dt>

*pShader* \[in\]
</dt> <dd>

Type: **const void\***

A pointer to the [**compiled shader**](/windows/win32/D3D10/nf-d3d10-id3d10device-createinputlayout?branch=master).

</dd> <dt>

*BytecodeLength* \[in\]
</dt> <dd>

Type: **[**SIZE\_T**](winprog.windows_data_types)**

The size of pShader.

</dd> <dt>

*EnableColorCode* \[in\]
</dt> <dd>

Type: **[**BOOL**](winprog.windows_data_types)**

Include HTML tags in the output to color code the result.

</dd> <dt>

*pComments* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](winprog.windows_data_types)**

The comment string at the top of the shader that identifies the shader constants and variables.

</dd> <dt>

*ppDisassembly* \[out\]
</dt> <dd>

Type: **[**ID3D10Blob**](/windows/win32/D3DCommon/nn-d3dcommon-id3d10blob?branch=master)\*\***

Address of a buffer (see [**ID3D10Blob Interface**](/windows/win32/D3DCommon/nn-d3dcommon-id3d10blob?branch=master)) which contains the disassembled shader.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

Returns one of the following [Direct3D 10 Return Codes](d3d10-graphics-reference-returnvalues.md).

## Remarks

This returned text includes a header with the version of the HLSL compiler used to generate this object, comments describing the memory layout of the constant buffers used by the shader, input and output signatures, and resource binding points.

Here is an example of disassembling a compiled shader. The example assumes you start with a compiled shader (shown as *pVSBuf* which you can see in [HLSLWithoutFX10 Sample](61f892cf-4760-177b-5048-0ba3906d8bfc)).


```
LPCSTR commentString = NULL;
ID3D10Blob* pIDisassembly = NULL;
char* pDisassembly = NULL;
if( pVSBuf )
{
    D3D10DisassembleShader( (UINT*) pVSBuf->GetBufferPointer(), 
        pVSBuf->GetBufferSize(), TRUE, commentString, &amp;pIDisassembly );
    if( pIDisassembly )
    {
        FILE* pFile = fopen( "shader.htm", "w" );
        if( pFile)
        {
            fputs( (char*)pIDisassembly->GetBufferPointer(), pFile );
            fclose( pFile );
        }
    }
}
```



## Requirements



|                   |                                                                                         |
|-------------------|-----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3DX10Core.h</dt> </dl> |



## See also

<dl> <dt>

[General Purpose Functions](d3d10-graphics-reference-d3dx10-functions-general-purpose.md)
</dt> </dl>

 

 




