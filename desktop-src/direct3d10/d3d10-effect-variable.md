---
description: These constants apply to effect variables.
ms.assetid: ef996443-b558-4aa6-acc1-38f8a89c9855
title: D3D10_EFFECT_VARIABLE Constants
ms.topic: reference
ms.date: 05/31/2018
---

# D3D10\_EFFECT\_VARIABLE Constants

These constants apply to effect variables.



| \#define                                       | Description  | Value                                                                                                                                                                                                                                                             |
|------------------------------------------------|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| D3D10\_EFFECT\_VARIABLE\_ANNOTATION            | 1 << 0 | Indicates that this is an annotation or a global variable.                                                                                                                                                                                                        |
| D3D10\_EFFECT\_VARIABLE\_POOLED                | 1 << 1 | Indicates that this variable or constant buffer resides in an effect pool. If this flag is not set, then the variable resides in a standalone effect or a child effect (standalone effects return false from [**ID3D10Effect::IsPool**](/windows/desktop/api/D3D10Effect/nf-d3d10effect-id3d10effect-ispool). |
| D3D10\_EFFECT\_VARIABLE\_EXPLICIT\_BIND\_POINT | 1 << 2 | Indicates that the variable has been explicitly bound using the register keyword.                                                                                                                                                                                 |



 

These flags are defined as macros in d3d10effect.h.

## Related topics

<dl> <dt>

[Effect Constants (Direct3D 10)](d3d10-graphics-reference-effect-constants.md)
</dt> </dl>

 

 



