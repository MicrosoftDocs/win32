---
description: Fog effects can give a 3D scene greater realism.
ms.assetid: 26fe4f7c-7bb3-4a52-b539-5de2b11256e9
title: Fog State (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Fog State (Direct3D 9)

Fog effects can give a 3D scene greater realism. You can use fog effects for more than simulating fog. They can also decrease the clarity of a scene with distance. This mirrors what happens in the real world; as objects become more distant from the user, their detail is less distinct.

For more information about using fog in your application, see [Fog (Direct3D 9)](fog.md).

A C++ application controls fog through device rendering states. The [**D3DRENDERSTATETYPE**](./d3drenderstatetype.md) enumerated type includes states to control whether pixel (table) or vertex fog is used, what color it is, the fog formula the system applies, and the parameters of the formula.

You enable fog by setting the D3DRS\_FOGENABLE render state to **TRUE**. The fog color can be set to any color value by using the D3DRS\_FOGCOLOR render state; the alpha component of the fog color is ignored.

The D3DRS\_FOGTABLEMODE and D3DRS\_FOGVERTEXMODE render states control the fog formula applied for fog calculations, and they indirectly control which type of fog is applied. Both render states can be set to a member of the [**D3DFOGMODE**](./d3dfogmode.md) enumerated type. Setting either render state to D3DFOG\_NONE disables pixel or vertex fog, respectively. If both render states are set to valid modes, the system applies only pixel fog effects.

The D3DRS\_FOGSTART and D3DRS\_FOGEND render states control fog formula parameters for the D3DFOG\_LINEAR mode. The D3DRS\_FOGDENSITY render state controls fog density in the exponential fog modes.

For more information, see [Fog Parameters (Direct3D 9)](fog-parameters.md).

## Related topics

<dl> <dt>

[Render States](render-states.md)
</dt> </dl>

 

 
