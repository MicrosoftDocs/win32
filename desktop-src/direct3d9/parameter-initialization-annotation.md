---
description: Use this annotation to define the contents of an external file as the initialization value for an effect parameter.
ms.assetid: 3da1f951-cb8b-49ce-aba2-0badb3178093
title: Parameter Initialization Annotation
ms.topic: article
ms.date: 05/31/2018
---

# Parameter Initialization Annotation

Use this annotation to define the contents of an external file as the initialization value for an effect parameter. For example:


```
string SasResourceAddress = "Value";
```



where Value is an ASCII text string that may contain an absolute or relative path. A relative path is relative to the directory that contains the effect file.

Here is an example:


```
texture2D DetailTexture
<
    string SasResourceAddress = "noise.dds";
>;
```



The default value is an empty string.

## Related topics

<dl> <dt>

[DirectX Standard Annotations and Semantics Reference](dx9-graphics-reference-effects-dxsas.md)
</dt> </dl>

 

 



