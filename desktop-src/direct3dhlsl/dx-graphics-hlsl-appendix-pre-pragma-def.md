---
title: def pragma Directive
description: Pragma directive that manually allocates a floating-point shader register.
ms.assetid: 45db94c4-f6f6-4c88-9bf2-4eaa9abf7844
keywords:
- def pragma Directive HLSL
topic_type:
- apiref
api_name:
- def pragma Directive
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# def pragma Directive

Pragma directive that manually allocates a floating-point shader register.



| \#pragma def( *target*, *register*, *val1*, *val2*,*val3*, *val4* ) |
|---------------------------------------------------------------------|



 

## Parameters



| Item                                                                        | Description                                                                 |
|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| <span id="target"></span><span id="TARGET"></span>*target*<br/>       | Target that contains the register to allocate. <br/>                  |
| <span id="register"></span><span id="REGISTER"></span>*register*<br/> | Floating-point shader register to allocate. <br/>                     |
| <span id="val0"></span><span id="VAL0"></span>*val0*<br/>             | First byte of the value to allocate to the specified register. <br/>  |
| <span id="val1"></span><span id="VAL1"></span>*val1*<br/>             | Second byte of the value to allocate to the specified register. <br/> |
| <span id="val2"></span><span id="VAL2"></span>*val2*<br/>             | Third byte of the value to allocate to the specified register. <br/>  |
| <span id="val3"></span><span id="VAL3"></span>*val3*<br/>             | Fourth byte of the value to allocate to the specified register. <br/> |



 

## Remarks

The def pragma allows a developer to prefill a floating-point shader register with the specified value. This pragma is infrequently used.

## See also

<dl> <dt>

[Preprocessor Directives (DirectX HLSL)](dx-graphics-hlsl-appendix-preprocessor.md)
</dt> <dt>

[\#pragma Directive (DirectX HLSL)](dx-graphics-hlsl-appendix-pre-pragma.md)
</dt> </dl>

 

 





