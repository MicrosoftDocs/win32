---
description: Defines effect floating-point numbers. This template replaces the EffectFloats template.
ms.assetid: 7b41d0dc-209f-4ade-a7ed-aa54f421e520
title: EffectParamFloats
ms.topic: reference
ms.date: 05/31/2018
---

# EffectParamFloats

Defines effect floating-point numbers. This template replaces the [**EffectFloats**](effectfloats.md) template.

``` syntax
template EffectParamFloats
{
    < 3014B9A0-62F5-478c-9B86-E4AC9F4E418B >
    STRING ParamName;
    DWORD nFloats;
    array float Floats[nFloats];
} 
```

Where:

-   ParamName - Name of the array of floats.
-   nFloats - Number of floating-point values in the array.
-   Floats\[nFloats\] - Array of floating-point values.

## See also

<dl> <dt>

[Templates](dx9-graphics-reference-x-file-format-templates.md)
</dt> </dl>

 

 



