---
description: Validation is performed during the effect compile. To validate the current technique, specify NULL as the technique handle to be validated.
ms.assetid: d1268f68-2893-4d7f-acd2-484346a20193
title: Validation (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Validation (Direct3D 9)

Validation is performed during the effect compile. To validate the current technique, specify **NULL** as the technique handle to be validated.

Validation will fail for any of the following:

-   If the specified technique handle does not exist.
-   If the application of any state in any pass of the technique fails.
-   If device validation fails after the application of all the states in any pass of the technique.
-   If the PIXELSHADER or VERTEXSHADER effect states are assigned invalid shaders in any pass of the technique.
-   If the device caps do not support cube mapping, and a TEXTURE effect state is assigned a value of type textureCUBE in any pass of the technique.
-   If the device caps do not support volume mapping and a TEXTURE effect state is assigned a value of type texture3D in any pass of the technique.

For more information, see [Effect States (Direct3D 9)](effect-states.md).

## Related topics

<dl> <dt>

[Effect Format](dx9-graphics-reference-effects-file-format.md)
</dt> </dl>

 

 



