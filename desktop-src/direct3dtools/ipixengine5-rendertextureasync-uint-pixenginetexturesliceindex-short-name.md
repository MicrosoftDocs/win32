---
description: Renders a texture to a file and returns the result to the host asynchrnously.
MS-HAID: vspixengine.IPixEngine5\_RenderTextureAsync\_UINT\_PixEngineTextureSliceIndex\_int\_float\_arr4\_float\_arr4\_BSTR\_UINT\_BSTR\_arr\_float\_arr\_UINT\_BSTR\_arr\_BOOL\_arr\_BSTR\_IPixEngine5Callbacks\_ptr\_DWORD\_DWORD
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IPixEngine5::RenderTextureAsync method
ms.topic: reference
ms.date: 05/31/2018
---

# <span id="vspixengine.ipixengine5_rendertextureasync_uint_pixenginetexturesliceindex_int_float_arr4_float_arr4_bstr_uint_bstr_arr_float_arr_uint_bstr_arr_bool_arr_bstr_ipixengine5callbacks_ptr_dword_dword"></span>IPixEngine5::RenderTextureAsync method

Renders a texture to a file and returns the result to the host asynchrnously.

## Syntax


```C++
HRESULT RenderTextureAsync(
   UINT                       textureId,
   PixEngineTextureSliceIndex sliceIndex,
   int                        formatOverride,
   float [4]                  lower,
   float [4]                  upper,
   BSTR                       shaderFileName,
   UINT                       numFloatShaderVars,
   BSTR []                    count6_shaderFloatVarName,
   float []                   count6_shaderFloatVarValue,
   UINT                       numBoolShaderVars,
   BSTR []                    count9_shaderBoolVarName,
   BOOL []                    count9_shaderBoolVarValue,
   BSTR                       renderContentFileName,
   IPixEngine5Callbacks*      callbacks,
   DWORD                      requestCookie,
   DWORD                      progressIntervalMsecs
);
```

## Parameters

*textureId*   
The ID of the texture to render.

*sliceIndex*   
The index of the slice within the texture to render.

*formatOverride*   
The color format override.

*lower*   

*upper*   

*shaderFileName*   
A COM string containing the pathname of the shader file.

*numFloatShaderVars*   
The number of floating-point shader variables

*count6\_shaderFloatVarName*   
COM strings contianing the names of the floating-point shader variables.

*count6\_shaderFloatVarValue*   
The floating-point shader variables.

*numBoolShaderVars*   
The number of boolean shader variables.

*count9\_shaderBoolVarName*   
COM strings contianing the names of the boolean shader variables.

*count9\_shaderBoolVarValue*   
The boolean shader variables.

*renderContentFileName*   
A COM string containing the pathname of the file where the rendered texture was written.

*callbacks*   
The address of an object that provides the IPixEngine5 callbacks interface.

*requestCookie*   
A cookie that uniquely identifies the request, and can be used to signal for it to be cancelled.

*progressIntervalMsecs*   
Not used.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

## <span id="see_also"></span>See also

[**IPixEngine5**](/windows/desktop/direct3dtools/ipixengine5)

 

 
