---
title: Rasterization State Variables
description: Rasterization State Variables
ms.assetid: 57ce3dc0-3983-449a-bbe1-153232727ff8
keywords:
- Rasterization State Variables OpenGL
topic_type:
- apiref
api_name:
- Rasterization State Variables
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# Rasterization State Variables

<dl> <dt><span id="GL_POINT_SIZE"></span><span id="gl_point_size"></span>GL\_POINT\_SIZE</dt> <dd> 

| Property | Value |
|------------------|------------------------------------|
| Description:     | Point size                         |
| Attribute group: | point                              |
| Initial value:   | 1.0                                |
| Get command:     | [**glGetFloatv**](glgetfloatv.md) |



 

</dd> <dt><span id="GL_POINT_SMOOTH"></span><span id="gl_point_smooth"></span>GL\_POINT\_SMOOTH</dt> <dd> 

| Property | Value |
|------------------|------------------------------------|
| Description:     | Point aliasing on                  |
| Attribute group: | point/enable                       |
| Initial value:   | GL\_FALSE                          |
| Get command:     | [**glIsEnabled**](glisenabled.md) |



 

</dd> <dt><span id="GL_LINE_WIDTH"></span><span id="gl_line_width"></span>GL\_LINE\_WIDTH</dt> <dd> 

| Property | Value |
|------------------|--------------------------------------------------------------------------------|
| Description:     | Line width                                                                     |
| Attribute group: | line                                                                           |
| Initial value:   | 1.0                                                                            |
| Get command:     | [**glGetFloatv**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) |



 

</dd> <dt><span id="GL_LINE_SMOOTH"></span><span id="gl_line_smooth"></span>GL\_LINE\_SMOOTH</dt> <dd> 

| Property | Value |
|------------------|------------------------------------|
| Description:     | Line antialiasing on               |
| Attribute group: | line/enable                        |
| Initial value:   | GL\_FALSE                          |
| Get command:     | [**glIsEnabled**](glisenabled.md) |



 

</dd> <dt><span id="GL_LINE_STIPPLE_PATTERN"></span><span id="gl_line_stipple_pattern"></span>GL\_LINE\_STIPPLE\_PATTERN</dt> <dd> 

| Property | Value |
|------------------|----------------------------------------------------------------------------------|
| Description:     | Line stipple                                                                     |
| Attribute group: | line                                                                             |
| Initial value:   | 1's                                                                              |
| Get command:     | [**glGetIntegerv**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) |



 

</dd> <dt><span id="GL_LINE_STIPPLE_REPEAT"></span><span id="gl_line_stipple_repeat"></span>GL\_LINE\_STIPPLE\_REPEAT</dt> <dd> 

| Property | Value |
|------------------|----------------------------------------------------------------------------------|
| Description:     | Line stipple repeat                                                              |
| Attribute group: | line                                                                             |
| Initial value:   | 1                                                                                |
| Get command:     | [**glGetIntegerv**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) |



 

</dd> <dt><span id="GL_LINE_STIPPLE"></span><span id="gl_line_stipple"></span>GL\_LINE\_STIPPLE</dt> <dd> 

| Property | Value |
|------------------|------------------------------------|
| Description:     | Line stipple enable                |
| Attribute group: | line/enable                        |
| Initial value:   | GL\_FALSE                          |
| Get command:     | [**glIsEnabled**](glisenabled.md) |



 

</dd> <dt><span id="GL_CULL_FACE"></span><span id="gl_cull_face"></span>GL\_CULL\_FACE</dt> <dd> 

| Property | Value |
|------------------|------------------------------------|
| Description:     | Polygon culling enabled            |
| Attribute group: | polygon/enable                     |
| Initial value:   | GL\_FALSE                          |
| Get command:     | [**glIsEnabled**](glisenabled.md) |



 

</dd> <dt><span id="GL_CULL_FACE_MODE"></span><span id="gl_cull_face_mode"></span>GL\_CULL\_FACE\_MODE</dt> <dd> 

| Property | Value |
|------------------|----------------------------------------------------------------------------------|
| Description:     | Cull front-facing/back-facing polygons                                           |
| Attribute group: | polygon                                                                          |
| Initial value:   | GL\_BACK                                                                         |
| Get command:     | [**glGetIntegerv**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) |



 

</dd> <dt><span id="GL_FRONT_FACE"></span><span id="gl_front_face"></span>GL\_FRONT\_FACE</dt> <dd> 

| Property | Value |
|------------------|----------------------------------------------------------------------------------|
| Description:     | Polygon front-face CW/CCW indicator                                              |
| Attribute group: | polygon                                                                          |
| Initial value:   | GL\_CCW                                                                          |
| Get command:     | [**glGetIntegerv**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) |



 

</dd> <dt><span id="GL_POLYGON_SMOOTH"></span><span id="gl_polygon_smooth"></span>GL\_POLYGON\_SMOOTH</dt> <dd> 

| Property | Value |
|------------------|------------------------------------|
| Description:     | Polygon antialiasing on            |
| Attribute group: | polygon/enable                     |
| Initial value:   | GL\_FALSE                          |
| Get command:     | [**glIsEnabled**](glisenabled.md) |



 

</dd> <dt><span id="GL_POLYGON_MODE"></span><span id="gl_polygon_mode"></span>GL\_POLYGON\_MODE</dt> <dd> 

| Property | Value |
|------------------|----------------------------------------------------------------------------------|
| Description:     | Polygon rasterization mode (front and back)                                      |
| Attribute group: | polygon                                                                          |
| Initial value:   | GL\_FILL                                                                         |
| Get command:     | [**glGetIntegerv**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) |



 

</dd> <dt><span id="GL_POLYGON_STIPPLE"></span><span id="gl_polygon_stipple"></span>GL\_POLYGON\_STIPPLE</dt> <dd> 

| Property | Value |
|------------------|------------------------------------|
| Description:     | Polygon stipple enable             |
| Attribute group: | polygon/enable                     |
| Initial value:   | GL\_FALSE                          |
| Get command:     | [**glIsEnabled**](glisenabled.md) |



 



| Property | Value |
|------------------|----------------------------------------------------|
| Description:     | Polygon stipple pattern                            |
| Attribute group: | polygon-stipple                                    |
| Initial value:   | 1's                                                |
| Get command:     | [**glGetPolygonStipple**](glgetpolygonstipple.md) |



 

</dd> </dl>

 

 




