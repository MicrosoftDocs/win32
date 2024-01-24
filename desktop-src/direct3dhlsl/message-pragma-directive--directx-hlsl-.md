---
title: message pragma Directive
description: Pragma directive that produces compiler-time messages.
ms.assetid: dc3ece10-9730-4ab1-acc8-f95abc92de7d
keywords:
- message pragma Directive HLSL
topic_type:
- apiref
api_name:
- message pragma Directive
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# message pragma Directive

Pragma directive that produces compiler-time messages.



| \#pragma message("*token-string*") |
|-----------------------------------|



 

## Parameters



| Item                                                                                    | Description                  |
|-----------------------------------------------------------------------------------------|------------------------------|
| <span id="token-string"></span><span id="TOKEN-STRING"></span>*token-string*<br/> | Compiler message.<br/> |



 

## Examples

The following example demonstrates message processing during preprocessing.


```
#pragma message "Debugging flag set."
```



## See also

<dl> <dt>

[Preprocessor Directives (DirectX HLSL)](dx-graphics-hlsl-appendix-preprocessor.md)
</dt> <dt>

[\#pragma Directive (DirectX HLSL)](dx-graphics-hlsl-appendix-pre-pragma.md)
</dt> </dl>

 

 





