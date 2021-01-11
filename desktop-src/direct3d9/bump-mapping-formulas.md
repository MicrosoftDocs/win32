---
description: Direct3D applies the following formulas to the DU and DV components in each bump map pixel.
ms.assetid: ae1de432-d1cc-45a5-b25f-b669cd30af3b
title: Bump Mapping Formulas (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Bump Mapping Formulas (Direct3D 9)

Direct3D applies the following formulas to the D<sub>U</sub> and D<sub>V</sub> components in each bump map pixel.

![formulas of bump mapping matrix transformations](images/dudv-transform.png)

In these formulas, the D<sub>U</sub> and D<sub>V</sub> variables are taken directly from a bump map pixel and transformed by a 2x2 matrix to produce the output delta values D<sub>U</sub>' and D<sub>V</sub>'. The system uses the output values to modify the texture coordinates that address the environment map in the next texture stage. The coefficients of the transformation matrix are set though the D3DTSS\_BUMPENVMAT00, D3DTSS\_BUMPENVMAT10, D3DTSS\_BUMPENVMAT01, and D3DTSS\_BUMPENVMAT11 texture stage states.

In addition to the u and v delta values, the system can compute a luminance value that it uses to modulate the color of the environment map in the next blending stage, as shown in the following formula.

![formula for output luminance, computed from scale factor and offset](images/l-transform.png)

In this formula, L' is the output luminance being computed. The L variable is the luminance value taken from a bump map pixel, which is multiplied by the scaling factor, S, and offset by the value in the variable O. The D3DTSS\_BUMPENVLSCALE and D3DTSS\_BUMPENVLOFFSET texture stage states control the values for the S and O variables in the formula. This formula is only applied when the texture blending operation for the stage that contains the bump map is set to D3DTOP\_BUMPENVMAPLUMINANCE. When using D3DTOP\_BUMPENVMAP, the system uses a value of 1.0 for L'.

After computing the output delta values D<sub>U</sub>' and D<sub>V</sub>', the system adds them to the texture coordinates in the next texture stage, and modulates the chosen color by the luminance to produce the color applied to the polygon.

## Related topics

<dl> <dt>

[Bump Mapping](bump-mapping.md)
</dt> </dl>

 

 



