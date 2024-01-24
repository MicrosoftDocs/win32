---
title: Framebuffer Control State Variables
description: Framebuffer Control State Variables
ms.assetid: ab57e07d-a694-45e7-a3b3-2e856111b87d
keywords:
- Framebuffer Control State Variables OpenGL
topic_type:
- apiref
api_name:
- Framebuffer Control State Variables
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# Framebuffer Control State Variables

<dl> <dt><span id="GL_DRAW_BUFFER"></span><span id="gl_draw_buffer"></span>GL\_DRAW\_BUFFER</dt> <dd> 

| Property | Value |
|------------------|----------------------------------------|
| Description:     | Buffers selected for drawing           |
| Attribute group: | color-buffer                           |
| Initial value:   |                                        |
| Get command:     | [**glGetIntegerv**](glgetintegerv.md) |



 

</dd> <dt><span id="GL_INDEX_WRITEMASK"></span><span id="gl_index_writemask"></span>GL\_INDEX\_WRITEMASK</dt> <dd> 

| Property | Value |
|------------------|----------------------------------------------------------------------------------|
| Description:     | Color-index writemask                                                            |
| Attribute group: | color-buffer                                                                     |
| Initial value:   | 1's                                                                              |
| Get command:     | [**glGetIntegerv**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) |



 

</dd> <dt><span id="GL_COLOR_WRITEMASK"></span><span id="gl_color_writemask"></span>GL\_COLOR\_WRITEMASK</dt> <dd> 

| Property | Value |
|------------------|----------------------------------------------------------------------------------|
| Description:     | Color write enables; R, G, B, or A                                               |
| Attribute group: | color-buffer                                                                     |
| Initial value:   | GL\_TRUE                                                                         |
| Get command:     | [**glGetBooleanv**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) |



 

</dd> <dt><span id="GL_DEPTH_WRITEMASK"></span><span id="gl_depth_writemask"></span>GL\_DEPTH\_WRITEMASK</dt> <dd> 

| Property | Value |
|------------------|----------------------------------------------------------------------------------|
| Description:     | Depth buffer enabled for writing                                                 |
| Attribute group: | depth-buffer                                                                     |
| Initial value:   | GL\_TRUE                                                                         |
| Get command:     | [**glGetBooleanv**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) |



 

</dd> <dt><span id="GL_STENCIL_WRITEMASK"></span><span id="gl_stencil_writemask"></span>GL\_STENCIL\_WRITEMASK</dt> <dd> 

| Property | Value |
|------------------|----------------------------------------------------------------------------------|
| Description:     | Stencil-buffer writemask                                                         |
| Attribute group: | stencil-buffer                                                                   |
| Initial value:   | 1's                                                                              |
| Get command:     | [**glGetIntegerv**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) |



 

</dd> <dt><span id="GL_COLOR_CLEAR_VALUE"></span><span id="gl_color_clear_value"></span>GL\_COLOR\_CLEAR\_VALUE</dt> <dd> 

| Property | Value |
|------------------|--------------------------------------------------------------------------------|
| Description:     | Color-buffer clear value (RGBA mode)                                           |
| Attribute group: | color-buffer                                                                   |
| Initial value:   | 0, 0, 0, 0                                                                     |
| Get command:     | [**glGetFloatv**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) |



 

</dd> <dt><span id="GL_INDEX_CLEAR_VALUE"></span><span id="gl_index_clear_value"></span>GL\_INDEX\_CLEAR\_VALUE</dt> <dd> 

| Property | Value |
|------------------|--------------------------------------------------------------------------------|
| Description:     | Color-buffer clear value (color-index mode)                                    |
| Attribute group: | color-buffer                                                                   |
| Initial value:   | 0                                                                              |
| Get command:     | [**glGetFloatv**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) |



 

</dd> <dt><span id="GL_DEPTH_CLEAR_VALUE"></span><span id="gl_depth_clear_value"></span>GL\_DEPTH\_CLEAR\_VALUE</dt> <dd> 

| Property | Value |
|------------------|----------------------------------------------------------------------------------|
| Description:     | Depth-buffer clear value                                                         |
| Attribute group: | depth-buffer                                                                     |
| Initial value:   | 1                                                                                |
| Get command:     | [**glGetIntegerv**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) |



 

</dd> <dt><span id="GL_STENCIL_CLEAR_VALUE"></span><span id="gl_stencil_clear_value"></span>GL\_STENCIL\_CLEAR\_VALUE</dt> <dd> 

| Property | Value |
|------------------|----------------------------------------------------------------------------------|
| Description:     | Stencil-buffer clear value                                                       |
| Attribute group: | stencil-buffer                                                                   |
| Initial value:   | 0                                                                                |
| Get command:     | [**glGetIntegerv**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) |



 

</dd> <dt><span id="GL_ACCUM_CLEAR_VALUE"></span><span id="gl_accum_clear_value"></span>GL\_ACCUM\_CLEAR\_VALUE</dt> <dd> 

| Property | Value |
|------------------|--------------------------------------------------------------------------------|
| Description:     | Accumulation-buffer clear value                                                |
| Attribute group: | accum-buffer                                                                   |
| Initial value:   | 0                                                                              |
| Get command:     | [**glGetFloatv**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) |



 

</dd> </dl>

 

 




