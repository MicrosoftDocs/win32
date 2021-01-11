---
description: Techniques provide the rendering muscle. A technique encapsulates the effect state that determines a rendering style. A technique is made up of one or more passes.
ms.assetid: 0a4d8f44-c7c0-4355-ac7f-6bc3315eeff0
title: Techniques and Passes (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Techniques and Passes (Direct3D 9)

Techniques provide the rendering muscle. A technique encapsulates the effect state that determines a rendering style. A technique is made up of one or more passes.

## Techniques

The syntax for calling a technique is as follows:


```
technique [ id ]  [< annotation(s) >] 
    { pass(es) }
```



Where:

-   id is an optional unique name.
-   annotation is zero or more optional pieces of user-specific information. See [Add Information to Effect Parameters with\_Annotations](using-an-effect.md).
-   pass(es) is zero or more passes. Each pass contains state assignments. See below.

## Passes

A pass contains the state assignments required to render.


```
pass  [ id ]  [< annotation(s) >] 
    { state assignment(s) }
```



Where:

-   id is an optional unique name.
-   annotation is one or more optional piece of user-specific information. See [Add Information to Effect Parameters with\_Annotations](using-an-effect.md).
-   assignment(s) assigns zero or more state values, or evaluates one or more expressions. See [Effect States (Direct3D 9)](effect-states.md) and [Expressions (Direct3D 9)](expressions.md).

Passes ignore all but the last assignment in a set of repeated assignments to the same state.

## Related topics

<dl> <dt>

[Effect Format](dx9-graphics-reference-effects-file-format.md)
</dt> </dl>

 

 



