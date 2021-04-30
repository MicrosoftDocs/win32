---
description: The Direct3D API defines several API elements to help you create and manage the effect system.
ms.assetid: d3b0b7a2-0820-4bb1-8b9e-c6b55a039963
title: Effect Reference (Direct3D 10 Graphics)
ms.topic: article
ms.date: 05/31/2018
---

# Effect Reference (Direct3D 10 Graphics)

The Direct3D API defines several API elements to help you create and manage the effect system.

-   [Interfaces](d3d10-graphics-reference-effect-interfaces.md)
-   [Functions](d3d10-graphics-reference-effect-functions.md)
-   [Structures](d3d10-graphics-reference-effect-structures.md)
-   [Constants](d3d10-graphics-reference-effect-constants.md)

The effect system encapsulates state assignments in an effect. Each effect is a collection of pipeline state which can be broken down into state assignments using state blocks, resources, and shaders. Depending on the size of an effect, you can choose to implement one in an ASCII text string or an effect file (.fx). To organize information in an effect, see the [effect format](d3d10-effect-format.md).

Having designed an effect, use the effect API to set state in the device during rendering. As well, the effect system supports a series of reflection API's for getting and setting effect data. For more information, see [Effect System Interfaces (Direct3D 10)](d3d10-graphics-programming-guide-effects-interfaces.md).

## Related topics

<dl> <dt>

[Direct3D Reference](d3d10-graphics-reference-d3d10.md)
</dt> </dl>

 

 



