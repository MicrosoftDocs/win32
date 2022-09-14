---
title: register
description: register
ms.assetid: 45149f8c-8b76-4247-98d7-d141d7268da3
keywords:
- register HLSL
topic_type:
- apiref
api_name:
- register
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# register

Optional keyword for assigning a shader variable to a particular register, which uses the following syntax:



| : register ( *\[shader\_profile\]*, *Type\#\[subcomponent\]* ) |
|----------------------------------------------------------------|



 

## Parameters

<dl> <dt>

<span id="register"></span><span id="REGISTER"></span>register
</dt> <dd>

Required keyword.

</dd> <dt>

<span id="_shader_profile_"></span><span id="_SHADER_PROFILE_"></span>*\[shader\_profile\]*
</dt> <dd>

Optional [shader profile](/windows/desktop/direct3dtools/dx-graphics-tools-fxc-syntax), which can be a shader target or simply **ps** or **vs**.

</dd> <dt>

<span id="Type__subcomponent_"></span><span id="type__subcomponent_"></span><span id="TYPE__SUBCOMPONENT_"></span>*Type\#\[subcomponent\]*
</dt> <dd>

Register type, number, and subcomponent declaration.

-   Type is one of the following:

    

    | Type | Register Description       |
    |------|----------------------------|
    | b    | Constant buffer            |
    | t    | Texture and texture buffer |
    | c    | Buffer offset              |
    | s    | Sampler                    |
    | u    | Unordered Access View      |

    

     

-   *\#* is the register number, which is an integer number.
-   The *subcomponent* is an optional integer number.

</dd> </dl>

## Remarks

You may add one or more register assignments to the same variable declaration, separated by spaces.

For Direct3D 10 variables in global scope, the **register** keyword acts the same as the [packoffset (DirectX HLSL)](dx-graphics-hlsl-variable-packoffset.md) keyword.

## Examples

Here are some examples:


```
sampler myVar : register( ps_5_0, s ); 
```




```
sampler myVar : register( vs, s[8] );
```




```
sampler myVar : register( ps, s[2] ) 
              : register( ps_5_0, s[0] ) 
              : register( vs, s[8] );
```



## See also

<dl> <dt>

[Variable Syntax](dx-graphics-hlsl-variable-syntax.md)
</dt> <dt>

[Variables (DirectX HLSL)](dx-graphics-hlsl-variables.md)
</dt> </dl>

 

 