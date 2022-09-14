---
title: Lighting State Variables
description: Lighting State Variables
ms.assetid: a9fb1e22-5e33-4b46-9c3b-2f64de5dd646
keywords:
- Lighting State Variables OpenGL
topic_type:
- apiref
api_name:
- Lighting State Variables
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# Lighting State Variables

<dl> <dt><span id="GL_LIGHTING"></span><span id="gl_lighting"></span>GL\_LIGHTING</dt> <dd> 

| Property | Value |
|------------------|------------------------------------|
| Description:     | True if lighting is enabled        |
| Attribute group: | lighting/enable                    |
| Initial value:   | GL\_FALSE                          |
| Get command:     | [**glIsEnabled**](glisenabled.md) |



 

</dd> <dt><span id="GL_COLOR_MATERIAL"></span><span id="gl_color_material"></span>GL\_COLOR\_MATERIAL</dt> <dd> 

| Property | Value |
|------------------|------------------------------------|
| Description:     | True if color tracking is enabled  |
| Attribute group: | lighting                           |
| Initial value:   | GL\_FALSE                          |
| Get command:     | [**glIsEnabled**](glisenabled.md) |



 

</dd> <dt><span id="GL_COLOR_MATERIAL_PARAMETER"></span><span id="gl_color_material_parameter"></span>GL\_COLOR\_MATERIAL\_PARAMETER</dt> <dd> 

| Property | Value |
|------------------|----------------------------------------------------------------------------------|
| Description:     | Material properties tracking current color                                       |
| Attribute group: | lighting                                                                         |
| Initial value:   | GL\_AMBIENT\_AND\_DIFFUSE                                                        |
| Get command:     | [**glGetIntegerv**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) |



 

</dd> <dt><span id="GL_COLOR_MATERIAL_FACE"></span><span id="gl_color_material_face"></span>GL\_COLOR\_MATERIAL\_FACE</dt> <dd> 

| Property | Value |
|------------------|----------------------------------------------------------------------------------|
| Description:     | Faces affected by color tracking                                                 |
| Attribute group: | lighting                                                                         |
| Initial value:   | GL\_FRONT\_AND\_BACK                                                             |
| Get command:     | [**glGetIntegerv**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) |



 

</dd> <dt><span id="GL_AMBIENT"></span><span id="gl_ambient"></span>GL\_AMBIENT</dt> <dd> 

| Property | Value |
|------------------|------------------------------------------|
| Description:     | Ambient material color                   |
| Attribute group: | lighting                                 |
| Initial value:   | (0.2,0.2,0.2,1.0)                        |
| Get command:     | [**glGetMaterialfv**](glgetmaterial.md) |



 

</dd> <dt><span id="GL_DIFFUSE"></span><span id="gl_diffuse"></span>GL\_DIFFUSE</dt> <dd> 

| Property | Value |
|------------------|------------------------------------------|
| Description:     | Diffuse material color                   |
| Attribute group: | lighting                                 |
| Initial value:   | (0.8,0.8,0.8,1.0)                        |
| Get command:     | [**glGetMaterialfv**](glgetmaterial.md) |



 

</dd> <dt><span id="GL_SPECULAR"></span><span id="gl_specular"></span>GL\_SPECULAR</dt> <dd> 

| Property | Value |
|------------------|------------------------------------------|
| Description:     | Specular material color                  |
| Attribute group: | lighting                                 |
| Initial value:   | (0.0,0.0,0.0,1.0)                        |
| Get command:     | [**glGetMaterialfv**](glgetmaterial.md) |



 

</dd> <dt><span id="GL_EMISSION"></span><span id="gl_emission"></span>GL\_EMISSION</dt> <dd> 

| Property | Value |
|------------------|------------------------------------------|
| Description:     | Emissive material color                  |
| Attribute group: | lighting                                 |
| Initial value:   | (0.0,0.0,0.0,1.0)                        |
| Get command:     | [**glGetMaterialfv**](glgetmaterial.md) |



 

</dd> <dt><span id="GL_SHININESS"></span><span id="gl_shininess"></span>GL\_SHININESS</dt> <dd> 

| Property | Value |
|------------------|------------------------------------------|
| Description:     | Specular exponent of material            |
| Attribute group: | lighting                                 |
| Initial value:   | 0.0                                      |
| Get command:     | [**glGetMaterialfv**](glgetmaterial.md) |



 

</dd> <dt><span id="GL_LIGHT_MODEL_AMBIENT"></span><span id="gl_light_model_ambient"></span>GL\_LIGHT\_MODEL\_AMBIENT</dt> <dd> 

| Property | Value |
|------------------|--------------------------------------------------------------------------------|
| Description:     | Ambient scene color                                                            |
| Attribute group: | lighting                                                                       |
| Initial value:   | (0.2,0.2,0.2,1.0)                                                              |
| Get command:     | [**glGetFloatv**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) |



 

</dd> <dt><span id="GL_LIGHT_MODEL_LOCAL_VIEWER"></span><span id="gl_light_model_local_viewer"></span>GL\_LIGHT\_MODEL\_LOCAL\_VIEWER</dt> <dd> 

| Property | Value |
|------------------|----------------------------------------------------------------------------------|
| Description:     | Viewer is local                                                                  |
| Attribute group: | lighting                                                                         |
| Initial value:   | GL\_FALSE                                                                        |
| Get command:     | [**glGetBooleanv**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) |



 

</dd> <dt><span id="GL_LIGHT_MODEL_TWO_SIDE"></span><span id="gl_light_model_two_side"></span>GL\_LIGHT\_MODEL\_TWO\_SIDE</dt> <dd> 

| Property | Value |
|------------------|----------------------------------------------------------------------------------|
| Description:     | Use two-sided lighting                                                           |
| Attribute group: | lighting                                                                         |
| Initial value:   | GL\_FALSE                                                                        |
| Get command:     | [**glGetBooleanv**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) |



 

</dd> <dt><span id="GL_AMBIENT"></span><span id="gl_ambient"></span>GL\_AMBIENT</dt> <dd> 

| Property | Value |
|------------------|------------------------------------|
| Description:     | Ambient intensity of light *i*     |
| Attribute group: | lighting                           |
| Initial value:   | (0.0,0.0,0.0,1.0)                  |
| Get command:     | [**glGetLightfv**](glgetlight.md) |



 

</dd> <dt><span id="GL_DIFFUSE"></span><span id="gl_diffuse"></span>GL\_DIFFUSE</dt> <dd> 

| Property | Value |
|------------------|------------------------------------|
| Description:     | Diffuse intensity of light *i*     |
| Attribute group: | lighting                           |
| Initial value:   |                                    |
| Get command:     | [**glGetLightfv**](glgetlight.md) |



 

</dd> <dt><span id="GL_SPECULAR"></span><span id="gl_specular"></span>GL\_SPECULAR</dt> <dd> 

| Property | Value |
|------------------|------------------------------------|
| Description:     | Specular intensity of light *i*    |
| Attribute group: | lighting                           |
| Initial value:   |                                    |
| Get command:     | [**glGetLightfv**](glgetlight.md) |



 

</dd> <dt><span id="GL_POSITION"></span><span id="gl_position"></span>GL\_POSITION</dt> <dd> 

| Property | Value |
|------------------|------------------------------------|
| Description:     | Position of light *i*              |
| Attribute group: | lighting                           |
| Initial value:   | (0.0,0.0,1.0,0.0)                  |
| Get command:     | [**glGetLightfv**](glgetlight.md) |



 

</dd> <dt><span id="GL_CONSTANT_ATTENUATION"></span><span id="gl_constant_attenuation"></span>GL\_CONSTANT\_ATTENUATION</dt> <dd> 

| Property | Value |
|------------------|------------------------------------|
| Description:     | Constant attenuation factor        |
| Attribute group: | lighting                           |
| Initial value:   | 1.0                                |
| Get command:     | [**glGetLightfv**](glgetlight.md) |



 

</dd> <dt><span id="GL_LINEAR_ATTENUATION"></span><span id="gl_linear_attenuation"></span>GL\_LINEAR\_ATTENUATION</dt> <dd> 

| Property | Value |
|------------------|------------------------------------|
| Description:     | Linear attenuation factor          |
| Attribute group: | lighting                           |
| Initial value:   | 0.0                                |
| Get command:     | [**glGetLightfv**](glgetlight.md) |



 

</dd> <dt><span id="GL_QUADRATIC_ATTENUATION"></span><span id="gl_quadratic_attenuation"></span>GL\_QUADRATIC\_ATTENUATION</dt> <dd> 

| Property | Value |
|------------------|------------------------------------|
| Description:     | Quadratic attenuation factor       |
| Attribute group: | lighting                           |
| Initial value:   | 0.0                                |
| Get command:     | [**glGetLightfv**](glgetlight.md) |



 

</dd> <dt><span id="GL_SPOT_DIRECTION"></span><span id="gl_spot_direction"></span>GL\_SPOT\_DIRECTION</dt> <dd> 

| Property | Value |
|------------------|------------------------------------|
| Description:     | Spotlight direction of light *i*   |
| Attribute group: | lighting                           |
| Initial value:   | (0.0,0.0,-1.0)                     |
| Get command:     | [**glGetLightfv**](glgetlight.md) |



 

</dd> <dt><span id="GL_SPOT_EXPONENT"></span><span id="gl_spot_exponent"></span>GL\_SPOT\_EXPONENT</dt> <dd> 

| Property | Value |
|------------------|------------------------------------|
| Description:     | Spotlight exponent of light *i*    |
| Attribute group: | lighting                           |
| Initial value:   | 0.0                                |
| Get command:     | [**glGetLightfv**](glgetlight.md) |



 

</dd> <dt><span id="GL_SPOT_CUTOFF"></span><span id="gl_spot_cutoff"></span>GL\_SPOT\_CUTOFF</dt> <dd> 

| Property | Value |
|------------------|------------------------------------|
| Description:     | Spotlight angle of light *i*       |
| Attribute group: | lighting                           |
| Initial value:   | 180.0                              |
| Get command:     | [**glGetLightfv**](glgetlight.md) |



 

</dd> <dt><span id="GL_LIGHT_i"></span><span id="gl_light_i"></span><span id="GL_LIGHT_I"></span>GL\_LIGHT *i*</dt> <dd> 

| Property | Value |
|------------------|------------------------------------|
| Description:     | True if light *i* enabled          |
| Attribute group: | lighting/enable                    |
| Initial value:   | GL\_FALSE                          |
| Get command:     | [**glIsEnabled**](glisenabled.md) |



 

</dd> <dt><span id="GL_COLOR_INDEXES"></span><span id="gl_color_indexes"></span>GL\_COLOR\_INDEXES</dt> <dd> 

| Property | Value |
|------------------|--------------------------------------------------------------------------------|
| Description:     | *C (a)*, *C (d)*, and *C (s)* for color-index lighting                         |
| Attribute group: | lighting/enable                                                                |
| Initial value:   | 0,1,1                                                                          |
| Get command:     | [**glGetFloatv**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) |



 

</dd> </dl>

 

 




