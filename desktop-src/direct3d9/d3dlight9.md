---
description: Defines a set of lighting properties.
ms.assetid: 25ce9d72-949c-41fc-8e3b-146d6a2de0dc
title: D3DLIGHT9 structure (D3D9Types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DLIGHT9
api_type:
- HeaderDef
api_location:
- D3D9Types.h
---

# D3DLIGHT9 structure

Defines a set of lighting properties.

## Syntax


```C++
typedef struct D3DLIGHT9 {
  D3DLIGHTTYPE  Type;
  D3DCOLORVALUE Diffuse;
  D3DCOLORVALUE Specular;
  D3DCOLORVALUE Ambient;
  D3DVECTOR     Position;
  D3DVECTOR     Direction;
  float         Range;
  float         Falloff;
  float         Attenuation0;
  float         Attenuation1;
  float         Attenuation2;
  float         Theta;
  float         Phi;
} D3DLIGHT9, *LPD3DLIGHT;
```



## Members

<dl> <dt>

**Type**
</dt> <dd>

Type: **[**D3DLIGHTTYPE**](./d3dlighttype.md)**

</dd> <dd>

Type of the light source. This value is one of the members of the [**D3DLIGHTTYPE**](./d3dlighttype.md) enumerated type.

</dd> <dt>

**Diffuse**
</dt> <dd>

Type: **[**D3DCOLORVALUE**](d3dcolorvalue.md)**

</dd> <dd>

Diffuse color emitted by the light. This member is a [**D3DCOLORVALUE**](d3dcolorvalue.md) structure.

</dd> <dt>

**Specular**
</dt> <dd>

Type: **[**D3DCOLORVALUE**](d3dcolorvalue.md)**

</dd> <dd>

Specular color emitted by the light. This member is a [**D3DCOLORVALUE**](d3dcolorvalue.md) structure.

</dd> <dt>

**Ambient**
</dt> <dd>

Type: **[**D3DCOLORVALUE**](d3dcolorvalue.md)**

</dd> <dd>

Ambient color emitted by the light. This member is a [**D3DCOLORVALUE**](d3dcolorvalue.md) structure.

</dd> <dt>

**Position**
</dt> <dd>

Type: **[**D3DVECTOR**](d3dvector.md)**

</dd> <dd>

Position of the light in world space, specified by a [**D3DVECTOR**](d3dvector.md) structure. This member has no meaning for directional lights and is ignored in that case.

</dd> <dt>

**Direction**
</dt> <dd>

Type: **[**D3DVECTOR**](d3dvector.md)**

</dd> <dd>

Direction that the light is pointing in world space, specified by a [**D3DVECTOR**](d3dvector.md) structure. This member has meaning only for directional and spotlights. This vector need not be normalized, but it should have a nonzero length.

</dd> <dt>

**Range**
</dt> <dd>

Type: **float**

</dd> <dd>

Distance beyond which the light has no effect. The maximum allowable value for this member is the square root of FLT\_MAX. This member does not affect directional lights.

</dd> <dt>

**Falloff**
</dt> <dd>

Type: **float**

</dd> <dd>

Decrease in illumination between a spotlight's inner cone (the angle specified by Theta) and the outer edge of the outer cone (the angle specified by Phi).

The effect of falloff on the lighting is subtle. Furthermore, a small performance penalty is incurred by shaping the falloff curve. For these reasons, most developers set this value to 1.0.

</dd> <dt>

**Attenuation0**
</dt> <dd>

Type: **float**

</dd> <dd>

Value specifying how the light intensity changes over distance. Attenuation values are ignored for directional lights. This member represents an attenuation constant. For information about attenuation, see [Light Properties (Direct3D 9)](light-properties.md). Valid values for this member range from 0.0 to infinity. For non-directional lights, all three attenuation values should not be set to 0.0 at the same time.

</dd> <dt>

**Attenuation1**
</dt> <dd>

Type: **float**

</dd> <dd>

Value specifying how the light intensity changes over distance. Attenuation values are ignored for directional lights. This member represents an attenuation constant. For information about attenuation, see [Light Properties (Direct3D 9)](light-properties.md). Valid values for this member range from 0.0 to infinity. For non-directional lights, all three attenuation values should not be set to 0.0 at the same time.

</dd> <dt>

**Attenuation2**
</dt> <dd>

Type: **float**

</dd> <dd>

Value specifying how the light intensity changes over distance. Attenuation values are ignored for directional lights. This member represents an attenuation constant. For information about attenuation, see [Light Properties (Direct3D 9)](light-properties.md). Valid values for this member range from 0.0 to infinity. For non-directional lights, all three attenuation values should not be set to 0.0 at the same time.

</dd> <dt>

**Theta**
</dt> <dd>

Type: **float**

</dd> <dd>

Angle, in radians, of a spotlight's inner cone - that is, the fully illuminated spotlight cone. This value must be in the range from 0 through the value specified by Phi.

</dd> <dt>

**Phi**
</dt> <dd>

Type: **float**

</dd> <dd>

Angle, in radians, defining the outer edge of the spotlight's outer cone. Points outside this cone are not lit by the spotlight. This value must be between 0 and pi.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3D9Types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Structures](dx9-graphics-reference-d3d-structures.md)
</dt> <dt>

[**GetLight**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-getlight)
</dt> <dt>

[**SetLight**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setlight)
</dt> </dl>

 

 
