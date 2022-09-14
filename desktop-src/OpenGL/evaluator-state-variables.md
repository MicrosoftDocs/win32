---
title: Evaluator State Variables
description: Evaluator State Variables
ms.assetid: e7d710be-de17-46a0-8ad8-0f65b943ece8
keywords:
- Evaluator State Variables OpenGL
topic_type:
- apiref
api_name:
- Evaluator State Variables
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# Evaluator State Variables

<dl> <dt><span id="GL_ORDER"></span><span id="gl_order"></span>GL\_ORDER</dt> <dd> 

| Property | Value |
|------------------|--------------------------------|
| Description:     | 1-D map order                  |
| Attribute group: |                                |
| Initial value:   | 1                              |
| Get command:     | [**glGetMapiv**](glgetmap.md) |



 

</dd> <dt><span id="GL_ORDER"></span><span id="gl_order"></span>GL\_ORDER</dt> <dd> 

| Property | Value |
|------------------|--------------------------------|
| Description:     | 2-D map orders                 |
| Attribute group: |                                |
| Initial value:   | 1,1                            |
| Get command:     | [**glGetMapiv**](glgetmap.md) |



 

</dd> <dt><span id="GL_COEFF"></span><span id="gl_coeff"></span>GL\_COEFF</dt> <dd> 

| Property | Value |
|------------------|--------------------------------|
| Description:     | 1-D control points             |
| Attribute group: |                                |
| Initial value:   |                                |
| Get command:     | [**glGetMapfv**](glgetmap.md) |



 

</dd> <dt><span id="GL_COEFF"></span><span id="gl_coeff"></span>GL\_COEFF</dt> <dd> 

| Property | Value |
|------------------|--------------------------------|
| Description:     | 2-D control points             |
| Attribute group: |                                |
| Initial value:   |                                |
| Get command:     | [**glGetMapfv**](glgetmap.md) |



 

</dd> <dt><span id="GL_DOMAIN"></span><span id="gl_domain"></span>GL\_DOMAIN</dt> <dd> 

| Property | Value |
|------------------|--------------------------------|
| Description:     | 1-D domain endpoints           |
| Attribute group: |                                |
| Initial value:   |                                |
| Get command:     | [**glGetMapfv**](glgetmap.md) |



 

</dd> <dt><span id="GL_DOMAIN"></span><span id="gl_domain"></span>GL\_DOMAIN</dt> <dd> 

| Property | Value |
|------------------|--------------------------------|
| Description:     | 2-D domain endpoints           |
| Attribute group: |                                |
| Initial value:   |                                |
| Get command:     | [**glGetMapfv**](glgetmap.md) |



 

</dd> <dt><span id="GL_MAP1_x"></span><span id="gl_map1_x"></span><span id="GL_MAP1_X"></span>GL\_MAP1\_x</dt> <dd> 

| Property | Value |
|------------------|------------------------------------|
| Description:     | 1-D map enables: *x* is map type   |
| Attribute group: | eval/enable                        |
| Initial value:   | GL\_FALSE                          |
| Get command:     | [**glIsEnabled**](glisenabled.md) |



 

</dd> <dt><span id="GL_MAP2_x"></span><span id="gl_map2_x"></span><span id="GL_MAP2_X"></span>GL\_MAP2\_x</dt> <dd> 

| Property | Value |
|------------------|------------------------------------|
| Description:     | 2-D map enables: *x* is map type   |
| Attribute group: | eval/enable                        |
| Initial value:   | GL\_FALSE                          |
| Get command:     | [**glIsEnabled**](glisenabled.md) |



 

</dd> <dt><span id="GL_MAP1_GRID_DOMAIN"></span><span id="gl_map1_grid_domain"></span>GL\_MAP1\_GRID\_DOMAIN</dt> <dd> 

| Property | Value |
|------------------|--------------------------------------------------------------------------------|
| Description:     | 1-D grid endpoints                                                             |
| Attribute group: | eval                                                                           |
| Initial value:   | 0,1                                                                            |
| Get command:     | [**glGetFloatv**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) |



 

</dd> <dt><span id="GL_MAP2_GRID_DOMAIN"></span><span id="gl_map2_grid_domain"></span>GL\_MAP2\_GRID\_DOMAIN</dt> <dd> 

| Property | Value |
|------------------|--------------------------------------------------------------------------------|
| Description:     | 2-D grid endpoints                                                             |
| Attribute group: | eval                                                                           |
| Initial value:   | 0, 1; 0, 1                                                                     |
| Get command:     | [**glGetFloatv**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) |



 

</dd> <dt><span id="GL_MAP1_GRID_SEGMENTS"></span><span id="gl_map1_grid_segments"></span>GL\_MAP1\_GRID\_SEGMENTS</dt> <dd> 

| Property | Value |
|------------------|------------------------------------|
| Description:     | 1-D grid divisions                 |
| Attribute group: | eval                               |
| Initial value:   | 1                                  |
| Get command:     | [**glGetFloatv**](glgetfloatv.md) |



 

</dd> <dt><span id="GL_MAP1_GRID_SEGMENTS"></span><span id="gl_map1_grid_segments"></span>GL\_MAP1\_GRID\_SEGMENTS</dt> <dd> 

| Property | Value |
|------------------|--------------------------------------------------------------------------------|
| Description:     | 2-D grid segments                                                              |
| Attribute group: | eval                                                                           |
| Initial value:   | 1, 1                                                                           |
| Get command:     | [**glGetFloatv**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) |



 

</dd> <dt><span id="GL_AUTO_NORMAL"></span><span id="gl_auto_normal"></span>GL\_AUTO\_NORMAL</dt> <dd> 

| Property | Value |
|------------------|---------------------------------------------|
| Description:     | True if automatic normal generation enabled |
| Attribute group: | eval                                        |
| Initial value:   | GL\_FALSE                                   |
| Get command:     | [**glIsEnabled**](glisenabled.md)          |



 

</dd> </dl>

 

 




