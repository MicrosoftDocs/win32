---
title: D2DGetInput function (D2d1effecthelpers.h)
description: Returns the color of input N at the input coordinate. Only available for simple inputs.
ms.assetid: 74B6F814-53C7-4C8C-B45C-3CB23B9D8BED
keywords:
- D2DGetInput function Direct2D
topic_type:
- apiref
api_name:
- D2DGetInput
api_location:
- d2d1.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# D2DGetInput function

Returns the color of input N at the input coordinate. Only available for simple inputs.

## Syntax

``` syntax
float4 WINAPI D2DGetInput(
  in uint N
);
```

## Parameters

<dl> <dt>

*N* \[in\]
</dt> <dd>

The input number.

</dd> </dl>

## Return value

The function returns a **float4**, containing the RGBA color in the format INPUTN.

## Remarks

The following example shows the function being used as part of an arithmetic composite effect.

``` syntax
  
D2D_PS_ENTRY(PS_NAME)  
{  
    MIN_TYPE(float4) sourceColor = D2DGetInput(0);  
    MIN_TYPE(float4) destColor   = D2DGetInput(1);  
      
    MIN_TYPE(float4) output = // TODO: add math to composite source and dest

    return output;  
}  
```

Also, refer to the remarks for [D2D\_PS\_ENTRY](d2d-ps-entry.md) for another example of the use of this function.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D2d1effecthelpers.hlsli</dt> </dl> |
| DLL<br/>    | <dl> <dt>D2d1.dll</dt> </dl>                |



## See also

<dl> <dt>

[Effect Shader Linking](effect-shader-linking.md)
</dt> <dt>

[HLSL Helpers](hlsl-helpers.md)
</dt> </dl>

 

 





