---
title: ' undef Directive'
description: Preprocessor directive that removes the current definition of a constant or macro that was previously defined using the \ define directive.
ms.assetid: ba6bbe6b-ecfa-40cb-887f-e42b6e22c7bd
keywords:
- undef Directive HLSL
topic_type:
- apiref
api_name:
- undef Directive
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# \#undef Directive

Preprocessor directive that removes the current definition of a constant or macro that was previously defined using the [\#define](dx-graphics-hlsl-appendix-pre-define.md) directive.



| \#undef *identifier* |
|----------------------|



 

## Parameters



| Item                                                                              | Description                                                                                                                                                      |
|-----------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="identifier"></span><span id="IDENTIFIER"></span>*identifier*<br/> | Identifier of the constant or macro to remove the definition of. If you are undefining a macro, provide only the identifier, not the parameter list. <br/> |



 

## Remarks

You can apply the \#undef directive to an identifier that has no previous definition; this ensures that the identifier is undefined. Macro replacement is not performed within \#undef statements.

The \#undef directive is typically paired with a [\#define](dx-graphics-hlsl-appendix-pre-define.md) directive to create a region in a source program in which an identifier has a special meaning. For example, a specific function of the source program can use manifest constants to define environment-specific values that do not affect the rest of the program. The \#undef directive also works with the [) directive to control conditional compilation of the source program.

Constants and macros can be undefined from the command line using the /U option, followed by the identifiers to be undefined. This is equivalent to adding a sequence of \#undef directives at the beginning of the source file.

## Examples

The following example shows how to use the \#undef directive to remove definitions of a symbolic constant and a macro.


```
#define WIDTH           80
#define ADD( X, Y )     (X) + (Y)

#undef WIDTH
#undef ADD
```



## See also

<dl> <dt>

[Preprocessor Directives (DirectX HLSL)](dx-graphics-hlsl-appendix-preprocessor.md)
</dt> <dt>

[\#define Directive (DirectX HLSL)](dx-graphics-hlsl-appendix-pre-define.md)
</dt> <dt>

[\#if, )](dx-graphics-hlsl-appendix-pre-if.md)
</dt> </dl>

 

 





