---
title: ' error Directive'
description: Preprocessor directive that produces compiler-time error messages.
ms.assetid: e32bcd6f-f2c1-43f7-a0bb-2c384b056492
keywords:
- error Directive HLSL
topic_type:
- apiref
api_name:
- error Directive
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# \#error Directive

Preprocessor directive that produces compiler-time error messages.



| \#error *token-string* |
|------------------------|



 

## Parameters



| Item                                                                                    | Description                                                                                                                                                                    |
|-----------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="token-string"></span><span id="TOKEN-STRING"></span>*token-string*<br/> | Error message. This parameter consists of a series of tokens, such as keywords, constants, or complete statements. The token string is subject to macro expansion. <br/> |



 

## Remarks

\#error directives are most useful for detecting programmer inconsistencies and violation of constraints during preprocessing. When an \#error directive is encountered, compilation terminates.

## Examples

The following example demonstrates error processing during preprocessing.


```
#if !defined(__cplusplus)
  #error C++ compiler required.
#endif
```



## See also

<dl> <dt>

[Preprocessor Directives (DirectX HLSL)](dx-graphics-hlsl-appendix-preprocessor.md)
</dt> </dl>

 

 





