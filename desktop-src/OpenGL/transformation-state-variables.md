---
title: Transformation State Variables
description: Transformation State Variables
ms.assetid: 3a6be5ac-ac7a-4c3e-8b65-0404849ae67c
keywords:
- Transformation State Variables OpenGL
topic_type:
- apiref
api_name:
- Transformation State Variables
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# Transformation State Variables

<dl> <dt><span id="GL_MODELVIEW_MATRIX"></span><span id="gl_modelview_matrix"></span>GL\_MODELVIEW\_MATRIX</dt> <dd> 

| Property | Value |
|------------------|------------------------------------|
| Description:     | Modelview matrix stack             |
| Attribute group: |                                    |
| Initial value:   | Identity                           |
| Get command:     | [**glGetFloatv**](glgetfloatv.md) |



 

</dd> <dt><span id="GL_PROJECTION_MATRIX"></span><span id="gl_projection_matrix"></span>GL\_PROJECTION\_MATRIX</dt> <dd> 

| Property | Value |
|------------------|--------------------------------------------------------------------------------|
| Description:     | Projection matrix stack                                                        |
| Attribute group: |                                                                                |
| Initial value:   | Identity                                                                       |
| Get command:     | [**glGetFloatv**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) |



 

</dd> <dt><span id="GL_TEXTURE_MATRIX"></span><span id="gl_texture_matrix"></span>GL\_TEXTURE\_MATRIX</dt> <dd> 

| Property | Value |
|------------------|--------------------------------------------------------------------------------|
| Description:     | Texture matrix stack                                                           |
| Attribute group: |                                                                                |
| Initial value:   | Identity                                                                       |
| Get command:     | [**glGetFloatv**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) |



 

</dd> <dt><span id="GL_VIEWPORT"></span><span id="gl_viewport"></span>GL\_VIEWPORT</dt> <dd> 

| Property | Value |
|------------------|----------------------------------------------------------------------------------|
| Description:     | Viewport origin and extent                                                       |
| Attribute group: | viewport                                                                         |
| Initial value:   |                                                                                  |
| Get command:     | [**glGetIntegerv**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) |



 

</dd> <dt><span id="GL_DEPTH_RANGE"></span><span id="gl_depth_range"></span>GL\_DEPTH\_RANGE</dt> <dd> 

| Property | Value |
|------------------|--------------------------------------------------------------------------------|
| Description:     | Depth range near and far                                                       |
| Attribute group: | viewport                                                                       |
| Initial value:   | 0, 1                                                                           |
| Get command:     | [**glGetFloatv**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) |



 

</dd> <dt><span id="GL_MODELVIEW_STACK_DEPTH"></span><span id="gl_modelview_stack_depth"></span>GL\_MODELVIEW\_STACK\_DEPTH</dt> <dd> 

| Property | Value |
|------------------|----------------------------------------------------------------------------------|
| Description:     | Modelview matrix stack pointer                                                   |
| Attribute group: |                                                                                  |
| Initial value:   | 1                                                                                |
| Get command:     | [**glGetIntegerv**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) |



 

</dd> <dt><span id="GL_PROJECTION_STACK_DEPTH"></span><span id="gl_projection_stack_depth"></span>GL\_PROJECTION\_STACK\_DEPTH</dt> <dd> 

| Property | Value |
|------------------|----------------------------------------------------------------------------------|
| Description:     | Projection matrix stack pointer                                                  |
| Attribute group: |                                                                                  |
| Initial value:   | 1                                                                                |
| Get command:     | [**glGetIntegerv**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) |



 

</dd> <dt><span id="GL_TEXTURE_STACK_DEPTH"></span><span id="gl_texture_stack_depth"></span>GL\_TEXTURE\_STACK\_DEPTH</dt> <dd> 

| Property | Value |
|------------------|----------------------------------------------------------------------------------|
| Description:     | Texture matrix stack pointer                                                     |
| Attribute group: |                                                                                  |
| Initial value:   | 1                                                                                |
| Get command:     | [**glGetIntegerv**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) |



 

</dd> <dt><span id="GL_MATRIX_MODE"></span><span id="gl_matrix_mode"></span>GL\_MATRIX\_MODE</dt> <dd> 

| Property | Value |
|------------------|----------------------------------------------------------------------------------|
| Description:     | Current matrix mode                                                              |
| Attribute group: | transform                                                                        |
| Initial value:   | GL\_MODELVIEW                                                                    |
| Get command:     | [**glGetIntegerv**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) |



 

</dd> <dt><span id="GL_NORMALIZE"></span><span id="gl_normalize"></span>GL\_NORMALIZE</dt> <dd> 

| Property | Value |
|------------------|-------------------------------------|
| Description:     | Current normal normalization on/off |
| Attribute group: | transform/enable                    |
| Initial value:   | GL\_FALSE                           |
| Get command:     | [**glIsEnabled**](glisenabled.md)  |



 

</dd> <dt><span id="GL_CLIP_PLANE_i"></span><span id="gl_clip_plane_i"></span><span id="GL_CLIP_PLANE_I"></span>GL\_CLIP\_PLANE *i*</dt> <dd> 

| Property | Value |
|------------------|------------------------------------------|
| Description:     | User clipping plane coefficients         |
| Attribute group: | transform                                |
| Initial value:   | 0, 0, 0, 0                               |
| Get command:     | [**glGetClipPlane**](glgetclipplane.md) |



 

</dd> <dt><span id="GL_CLIP_PLANE_i"></span><span id="gl_clip_plane_i"></span><span id="GL_CLIP_PLANE_I"></span>GL\_CLIP\_PLANE *i*</dt> <dd> 

| Property | Value |
|------------------|------------------------------------|
| Description:     | *i* th user clipping plane enabled |
| Attribute group: | transform/enable                   |
| Initial value:   | GL\_FALSE                          |
| Get command:     | [**glIsEnabled**](glisenabled.md) |



 

</dd> </dl>

 

 




