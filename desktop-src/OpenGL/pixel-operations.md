---
title: Pixel Operations
description: Pixel Operations
ms.assetid: e60cc45b-867c-441a-b579-8c7dbd46ecd9
keywords:
- Pixel Operations OpenGL
topic_type:
- apiref
api_name:
- Pixel Operations
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# Pixel Operations

<dl> <dt><span id="GL_SCISSOR_TEST"></span><span id="gl_scissor_test"></span>GL\_SCISSOR\_TEST</dt> <dd> 

| Property | Value |
|------------------|------------------------------------|
| Description:     | Scissoring enabled                 |
| Attribute group: | scissor/enable                     |
| Initial value:   | GL\_FALSE                          |
| Get command:     | [**glIsEnabled**](glisenabled.md) |



 

</dd> <dt><span id="GL_SCISSOR_BOX"></span><span id="gl_scissor_box"></span>GL\_SCISSOR\_BOX</dt> <dd> 

| Property | Value |
|------------------|----------------------------------------------------------------------------------|
| Description:     | Scissor box                                                                      |
| Attribute group: | scissor                                                                          |
| Initial value:   |                                                                                  |
| Get command:     | [**glGetIntegerv**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) |



 

</dd> <dt><span id="GL_STENCIL_TEST"></span><span id="gl_stencil_test"></span>GL\_STENCIL\_TEST</dt> <dd> 

| Property | Value |
|------------------|------------------------------------|
| Description:     | Stenciling enabled                 |
| Attribute group: | stencil-buffer/enable              |
| Initial value:   | GL\_FALSE                          |
| Get command:     | [**glIsEnabled**](glisenabled.md) |



 

</dd> <dt><span id="GL_STENCIL_FUNC"></span><span id="gl_stencil_func"></span>GL\_STENCIL\_FUNC</dt> <dd> 

| Property | Value |
|------------------|----------------------------------------------------------------------------------|
| Description:     | Stencil function                                                                 |
| Attribute group: | stencil-buffer                                                                   |
| Initial value:   | GL\_ALWAYS                                                                       |
| Get command:     | [**glGetIntegerv**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) |



 

</dd> <dt><span id="GL_STENCIL_VALUE_MASK"></span><span id="gl_stencil_value_mask"></span>GL\_STENCIL\_VALUE\_MASK</dt> <dd> 

| Property | Value |
|------------------|----------------------------------------------------------------------------------|
| Description:     | Stencil mask                                                                     |
| Attribute group: | stencil-buffer                                                                   |
| Initial value:   | 1's                                                                              |
| Get command:     | [**glGetIntegerv**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) |



 

</dd> <dt><span id="GL_STENCIL_REF"></span><span id="gl_stencil_ref"></span>GL\_STENCIL\_REF</dt> <dd> 

| Property | Value |
|------------------|----------------------------------------------------------------------------------|
| Description:     | Stencil reference value                                                          |
| Attribute group: | stencil-buffer                                                                   |
| Initial value:   | 0                                                                                |
| Get command:     | [**glGetIntegerv**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) |



 

</dd> <dt><span id="GL_STENCIL_FAIL"></span><span id="gl_stencil_fail"></span>GL\_STENCIL\_FAIL</dt> <dd> 

| Property | Value |
|------------------|----------------------------------------------------------------------------------|
| Description:     | Stencil fail action                                                              |
| Attribute group: | stencil-buffer                                                                   |
| Initial value:   | GL\_KEEP                                                                         |
| Get command:     | [**glGetIntegerv**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) |



 

</dd> <dt><span id="GL_STENCIL_PASS_DEPTH_FAIL"></span><span id="gl_stencil_pass_depth_fail"></span>GL\_STENCIL\_PASS\_DEPTH\_FAIL</dt> <dd> 

| Property | Value |
|------------------|----------------------------------------------------------------------------------|
| Description:     | Stencil depth buffer fail action                                                 |
| Attribute group: | stencil-buffer                                                                   |
| Initial value:   | GL\_KEEP                                                                         |
| Get command:     | [**glGetIntegerv**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) |



 

</dd> <dt><span id="GL_STENCIL_PASS_DEPTH_PASS"></span><span id="gl_stencil_pass_depth_pass"></span>GL\_STENCIL\_PASS\_DEPTH\_PASS</dt> <dd> 

| Property | Value |
|------------------|----------------------------------------------------------------------------------|
| Description:     | Stencil depth buffer pass action                                                 |
| Attribute group: | stencil-buffer                                                                   |
| Initial value:   | GL\_KEEP                                                                         |
| Get command:     | [**glGetIntegerv**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) |



 

</dd> <dt><span id="GL_ALPHA_TEST"></span><span id="gl_alpha_test"></span>GL\_ALPHA\_TEST</dt> <dd> 

| Property | Value |
|------------------|------------------------------------|
| Description:     | Alpha test enabled                 |
| Attribute group: | color-buffer/enable                |
| Initial value:   | GL\_FALSE                          |
| Get command:     | [**glIsEnabled**](glisenabled.md) |



 

</dd> <dt><span id="GL_ALPHA_TEST_FUNC"></span><span id="gl_alpha_test_func"></span>GL\_ALPHA\_TEST\_FUNC</dt> <dd> 

| Property | Value |
|------------------|----------------------------------------------------------------------------------|
| Description:     | Alpha test function                                                              |
| Attribute group: | color-buffer                                                                     |
| Initial value:   | GL\_ALWAYS                                                                       |
| Get command:     | [**glGetIntegerv**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) |



 

</dd> <dt><span id="GL_ALPHA_TEST_REF"></span><span id="gl_alpha_test_ref"></span>GL\_ALPHA\_TEST\_REF</dt> <dd> 

| Property | Value |
|------------------|----------------------------------------------------------------------------------|
| Description:     | Alpha test reference value                                                       |
| Attribute group: | color-buffer                                                                     |
| Initial value:   | 0                                                                                |
| Get command:     | [**glGetIntegerv**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) |



 

</dd> <dt><span id="GL_DEPTH_TEST"></span><span id="gl_depth_test"></span>GL\_DEPTH\_TEST</dt> <dd> 

| Property | Value |
|------------------|------------------------------------|
| Description:     | Depth buffer enabled               |
| Attribute group: | depth-buffer/enable                |
| Initial value:   | GL\_FALSE                          |
| Get command:     | [**glIsEnabled**](glisenabled.md) |



 

</dd> <dt><span id="GL_DEPTH_FUNC"></span><span id="gl_depth_func"></span>GL\_DEPTH\_FUNC</dt> <dd> 

| Property | Value |
|------------------|----------------------------------------------------------------------------------|
| Description:     | Depth buffer test function                                                       |
| Attribute group: | depth-buffer                                                                     |
| Initial value:   | GL\_LESS                                                                         |
| Get command:     | [**glGetIntegerv**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) |



 

</dd> <dt><span id="GL_BLEND"></span><span id="gl_blend"></span>GL\_BLEND</dt> <dd> 

| Property | Value |
|------------------|------------------------------------|
| Description:     | Blending enabled                   |
| Attribute group: | color-buffer/enable                |
| Initial value:   | GL\_FALSE                          |
| Get command:     | [**glIsEnabled**](glisenabled.md) |



 

</dd> <dt><span id="GL_BLENC_SRC"></span><span id="gl_blenc_src"></span>GL\_BLENC\_SRC</dt> <dd> 

| Property | Value |
|------------------|----------------------------------------------------------------------------------|
| Description:     | Blending source function                                                         |
| Attribute group: | color-buffer                                                                     |
| Initial value:   | GL\_ONE                                                                          |
| Get command:     | [**glGetIntegerv**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) |



 

</dd> <dt><span id="GL_BLEND_DST"></span><span id="gl_blend_dst"></span>GL\_BLEND\_DST</dt> <dd> 

| Property | Value |
|------------------|----------------------------------------------------------------------------------|
| Description:     | Blending destination function                                                    |
| Attribute group: | color-buffer                                                                     |
| Initial value:   | GL\_ZERO                                                                         |
| Get command:     | [**glGetIntegerv**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) |



 

</dd> <dt><span id="GL_DITHER"></span><span id="gl_dither"></span>GL\_DITHER</dt> <dd> 

| Property | Value |
|------------------|------------------------------------|
| Description:     | Dithering enabled                  |
| Attribute group: | color-buffer/enable                |
| Initial value:   | GL\_TRUE                           |
| Get command:     | [**glIsEnabled**](glisenabled.md) |



 

</dd> <dt><span id="GL_LOGIC_OP"></span><span id="gl_logic_op"></span>GL\_LOGIC\_OP</dt> <dd> 

| Property | Value |
|------------------|------------------------------------|
| Description:     | Logical operation enabled          |
| Attribute group: | color-buffer/enable                |
| Initial value:   | GL\_FALSE                          |
| Get command:     | [**glIsEnabled**](glisenabled.md) |



 

</dd> <dt><span id="GL_LOGIC_OP_MODE"></span><span id="gl_logic_op_mode"></span>GL\_LOGIC\_OP\_MODE</dt> <dd> 

| Property | Value |
|------------------|----------------------------------------------------------------------------------|
| Description:     | Logical operation function                                                       |
| Attribute group: | color-buffer                                                                     |
| Initial value:   | GL\_COPY                                                                         |
| Get command:     | [**glGetIntegerv**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) |



 

</dd> </dl>

 

 




