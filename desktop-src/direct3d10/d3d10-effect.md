---
description: These constants used when creating an effect to define either compilation behavior or runtime effect behavior.
ms.assetid: cff99200-8bdc-416c-b1a5-3ae515a17a17
title: D3D10_EFFECT Constants
ms.topic: reference
ms.date: 05/31/2018
---

# D3D10\_EFFECT Constants

These constants used when creating an effect to define either compilation behavior or runtime effect behavior.



| \#define                                 | Value        | Description                                                                                                                                                                                                                                                 |
|------------------------------------------|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| D3D10\_EFFECT\_COMPILE\_CHILD\_EFFECT    | 1 << 0 | Compile the .fx file to a child effect. Child effects have no initializes for any shared values because these are initialized in the effect pool.                                                                                                           |
| D3D10\_EFFECT\_COMPILE\_ALLOW\_SLOW\_OPS | 1 << 1 | By default, performance mode is enabled. Performance mode disallows mutable state objects by preventing non-literal expressions from appearing in state object definitions. Specifying this flag will disable the mode and allow for mutable state objects. |
| D3D10\_EFFECT\_SINGLE\_THREADED          | 1 << 3 | Do not attempt to synchronize with other threads loading effects into the same pool.                                                                                                                                                                        |



 

These constants are defined as macros in d3d10effect.h.

## Related topics

<dl> <dt>

[Effect Constants (Direct3D 10)](d3d10-graphics-reference-effect-constants.md)
</dt> </dl>

 

 



