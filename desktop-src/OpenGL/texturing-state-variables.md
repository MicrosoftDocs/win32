---
title: Texturing State Variables
description: Texturing State Variables
ms.assetid: 2d9d3d8b-ecaa-412c-8105-ae2ca801784e
keywords:
- Texturing State Variables OpenGL
topic_type:
- apiref
api_name:
- Texturing State Variables
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# Texturing State Variables

<dl> <dt><span id="GL_TEXTURE_x"></span><span id="gl_texture_x"></span><span id="GL_TEXTURE_X"></span>GL\_TEXTURE\_*x*</dt> <dd> 

| Property | Value |
|------------------|-------------------------------------------------------|
| Description:     | True if *x* - D texturing enabled (*x* is 1-D or 2-D) |
| Attribute group: | texture/enable                                        |
| Initial value:   | GL\_FALSE                                             |
| Get command:     | [**glIsEnabled**](glisenabled.md)                    |



 

</dd> <dt><span id="GL_TEXTURE"></span><span id="gl_texture"></span>GL\_TEXTURE</dt> <dd> 

| Property | Value |
|------------------|----------------------------------------------|
| Description:     | *x* - D texture image at level of detail *i* |
| Attribute group: |                                              |
| Initial value:   |                                              |
| Get command:     | [**glGetTexImage**](glgetteximage.md)       |



 

</dd> <dt><span id="GL_TEXTURE_WIDTH"></span><span id="gl_texture_width"></span>GL\_TEXTURE\_WIDTH</dt> <dd> 

| Property | Value |
|------------------|----------------------------------------------------------|
| Description:     | *x* - D texture image *i* 's width                       |
| Attribute group: |                                                          |
| Initial value:   | 0                                                        |
| Get command:     | [**glGetTexLevelParameter**](glgettexlevelparameter.md) |



 

</dd> <dt><span id="GL_TEXTURE_HEIGHT"></span><span id="gl_texture_height"></span>GL\_TEXTURE\_HEIGHT</dt> <dd> 

| Property | Value |
|------------------|----------------------------------------------------------|
| Description:     | *x* - D texture image *i* 's height                      |
| Attribute group: |                                                          |
| Initial value:   | 0                                                        |
| Get command:     | [**glGetTexLevelParameter**](glgettexlevelparameter.md) |



 

</dd> <dt><span id="GL_TEXTURE_BORDER"></span><span id="gl_texture_border"></span>GL\_TEXTURE\_BORDER</dt> <dd> 

| Property | Value |
|------------------|----------------------------------------------------------|
| Description:     | *x* - D texture image *i* 's border                      |
| Attribute group: |                                                          |
| Initial value:   | 0                                                        |
| Get command:     | [**glGetTexLevelParameter**](glgettexlevelparameter.md) |



 

</dd> <dt><span id="GL_TEXTURE_COMPONENTS"></span><span id="gl_texture_components"></span>GL\_TEXTURE\_COMPONENTS</dt> <dd> 

| Property | Value |
|------------------|----------------------------------------------------------|
| Description:     | Texture image components                                 |
| Attribute group: |                                                          |
| Initial value:   | 1                                                        |
| Get command:     | [**glGetTexLevelParameter**](glgettexlevelparameter.md) |



 

</dd> <dt><span id="GL_TEXTURE_BORDER_COLOR"></span><span id="gl_texture_border_color"></span>GL\_TEXTURE\_BORDER\_COLOR</dt> <dd> 

| Property | Value |
|------------------|------------------------------------------------|
| Description:     | Texture border color                           |
| Attribute group: | texture                                        |
| Initial value:   | 0, 0, 0, 0                                     |
| Get command:     | [**glGetTexParameter**](glgettexparameter.md) |



 

</dd> <dt><span id="GL_TEXTURE_MIN_FILTER"></span><span id="gl_texture_min_filter"></span>GL\_TEXTURE\_MIN\_FILTER</dt> <dd> 

| Property | Value |
|------------------|------------------------------------------------|
| Description:     | Texture minification function                  |
| Attribute group: | texture                                        |
| Initial value:   | GL\_NEAREST\_MIPMAP\_LINEAR                    |
| Get command:     | [**glGetTexParameter**](glgettexparameter.md) |



 

</dd> <dt><span id="GL_TEXTURE_MAG_FILTER"></span><span id="gl_texture_mag_filter"></span>GL\_TEXTURE\_MAG\_FILTER</dt> <dd> 

| Property | Value |
|------------------|------------------------------------------------|
| Description:     | Texture magnification function                 |
| Attribute group: | texture                                        |
| Initial value:   | GL\_LINEAR                                     |
| Get command:     | [**glGetTexParameter**](glgettexparameter.md) |



 

</dd> <dt><span id="GL_TEXTURE_WRAP__x"></span><span id="gl_texture_wrap__x"></span><span id="GL_TEXTURE_WRAP__X"></span>GL\_TEXTURE\_WRAP\_ *x*</dt> <dd> 

| Property | Value |
|------------------|------------------------------------------------|
| Description:     | Texture wrap mode (*x* is S or T)              |
| Attribute group: | texture                                        |
| Initial value:   | GL\_REPEAT                                     |
| Get command:     | [**glGetTexParameter**](glgettexparameter.md) |



 

</dd> <dt><span id="GL_TEXTURE_ENV_MODE"></span><span id="gl_texture_env_mode"></span>GL\_TEXTURE\_ENV\_MODE</dt> <dd> 

| Property | Value |
|------------------|--------------------------------------|
| Description:     | Texture application function         |
| Attribute group: | texture                              |
| Initial value:   | GL\_MODULATE                         |
| Get command:     | [**glGetTexEnviv**](glgettexenv.md) |



 

</dd> <dt><span id="GL_TEXTURE_ENV_COLOR"></span><span id="gl_texture_env_color"></span>GL\_TEXTURE\_ENV\_COLOR</dt> <dd> 

| Property | Value |
|------------------|--------------------------------------|
| Description:     | Texture environment color            |
| Attribute group: | texture                              |
| Initial value:   | 0, 0, 0, 0                           |
| Get command:     | [**glGetTexEnvfv**](glgettexenv.md) |



 

</dd> <dt><span id="GL_TEXTURE_GEN__x"></span><span id="gl_texture_gen__x"></span><span id="GL_TEXTURE_GEN__X"></span>GL\_TEXTURE\_GEN\_ *x*</dt> <dd> 

| Property | Value |
|------------------|------------------------------------------|
| Description:     | Texgen is enabled (*x* is S, T, R, or Q) |
| Attribute group: | texture/enable                           |
| Initial value:   | GL\_FALSE                                |
| Get command:     | [**glIsEnabled**](glisenabled.md)       |



 

</dd> <dt><span id="GL_EYE_PLANE"></span><span id="gl_eye_plane"></span>GL\_EYE\_PLANE</dt> <dd> 

| Property | Value |
|------------------|--------------------------------------|
| Description:     | Texgen plane equation coefficients   |
| Attribute group: | texture                              |
| Initial value:   |                                      |
| Get command:     | [**glGetTexGenfv**](glgettexgen.md) |



 

</dd> <dt><span id="GL_OBJECT_PLANE"></span><span id="gl_object_plane"></span>GL\_OBJECT\_PLANE</dt> <dd> 

| Property | Value |
|------------------|--------------------------------------|
| Description:     | Texgen object linear coefficients    |
| Attribute group: | texture                              |
| Initial value:   |                                      |
| Get command:     | [**glGetTexGenfv**](glgettexgen.md) |



 

</dd> <dt><span id="GL_TEXTURE_GEN_MODE"></span><span id="gl_texture_gen_mode"></span>GL\_TEXTURE\_GEN\_MODE</dt> <dd> 

| Property | Value |
|------------------|--------------------------------------|
| Description:     | Function used for texgen             |
| Attribute group: | texture                              |
| Initial value:   | GL\_EYE\_LINEAR                      |
| Get command:     | [**glGetTexGeniv**](glgettexgen.md) |



 

</dd> </dl>

 

 




