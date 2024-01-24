---
title: gluNurbsProperty function (Glu.h)
description: The gluNurbsProperty function sets a Non-Uniform Rational B-Spline (NURBS) property.
ms.assetid: c8c3b0c3-11b8-4123-91b6-75fed78932ce
keywords:
- gluNurbsProperty function OpenGL
topic_type:
- apiref
api_name:
- gluNurbsProperty
api_location:
- glu32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# gluNurbsProperty function

The **gluNurbsProperty** function sets a Non-Uniform Rational B-Spline ([NURBS](using-nurbs-curves-and-surfaces.md)) property.

## Syntax


```C++
void WINAPI gluNurbsProperty(
   GLUnurbs *nobj,
   GLenum   property,
   GLfloat  value
);
```



## Parameters

<dl> <dt>

*nobj* 
</dt> <dd>

The NURBS object (created with [**gluNewNurbsRenderer**](glunewnurbsrenderer.md)).

</dd> <dt>

*property* 
</dt> <dd>

The property to be set. The following values are valid:



| Value                                                                                                                                                                                           | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="GLU_SAMPLING_TOLERANCE"></span><span id="glu_sampling_tolerance"></span><dl> <dt>**GLU\_SAMPLING\_TOLERANCE**</dt> </dl>       | Specifies the maximum length, in pixels, to use when the sampling method is set to GLU\_PATH\_LENGTH. The default value is 50.0 pixels.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| <span id="GLU_DISPLAY_MODE"></span><span id="glu_display_mode"></span><dl> <dt>**GLU\_DISPLAY\_MODE**</dt> </dl>                         | The *value* parameter defines how a NURBS surface is to be rendered. You can set *value* to GLU\_FILL, GLU\_OUTLINE\_POLYGON, or GLU\_OUTLINE\_PATCH. <br/> GLU\_FILL. The surface is rendered as a set of polygons. This is the default value. <br/> GLU\_OUTLINE\_POLYGON. The NURBS library draws only the outlines of the polygons created by tessellation. <br/> GLU\_OUTLINE\_PATCH. Only the outlines of patches and trim curves defined by the user are drawn.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| <span id="GLU_CULLING"></span><span id="glu_culling"></span><dl> <dt>**GLU\_CULLING**</dt> </dl>                                         | The *value* parameter is a Boolean value. When value is set to GL\_TRUE, NURBS curves whose control points lie outside the current viewport are discarded prior to tessellation. The default is GL\_FALSE (because a NURBS curve cannot fall entirely within the convex hull of its control points).<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| <span id="GLU_AUTO_LOAD_MATRIX"></span><span id="glu_auto_load_matrix"></span><dl> <dt>**GLU\_AUTO\_LOAD\_MATRIX**</dt> </dl>            | The *value* parameter is a Boolean value. When set to GL\_TRUE, the NURBS code downloads the projection matrix, modelview matrix, and viewport from the OpenGL server to compute sampling and culling matrices for each NURBS curve that is rendered. Sampling and culling matrices are required to determine the tessellation of a NURBS surface into line segments or polygons and to cull a NURBS surface if it lies outside of the viewport. <br/> If this mode is set to GL\_FALSE, you must provide a projection matrix, modelview matrix, and viewport for the NURBS renderer to use to construct sampling and culling matrices. You can do this with the [**gluLoadSamplingMatrices**](gluloadsamplingmatrices.md) function.<br/> The default for this mode is GL\_TRUE. Changing this mode from GL\_TRUE to GL\_FALSE does not affect the sampling and culling matrices until you call [**gluLoadSamplingMatrices**](gluloadsamplingmatrices.md). <br/> The following property parameters are supported in GLU version 1.1 or later and are not valid for GLU version 1.0: GLU\_PARAMETRIC\_TOLERANCE, GLU\_SAMPLING\_METHOD, GLU\_U\_STEP, and GLU\_V\_STEP.<br/> The following value parameters are supported in GLU version 1.1 or later and are not valid for GLU version 1.0: GLU\_PATH\_LENGTH, GLU\_PARAMETRIC\_ERROR, and GLU\_DOMAIN\_DISTANCE.<br/> |
| <span id="GLU_PARAMETRIC_TOLERANCE"></span><span id="glu_parametric_tolerance"></span><dl> <dt>**GLU\_PARAMETRIC\_TOLERANCE**</dt> </dl> | Specifies the maximum distance, in pixels, to use when the sampling method is set to GLU\_PARAMETRIC\_ERROR. The default value is 0.5.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| <span id="GLU_SAMPLING_METHOD"></span><span id="glu_sampling_method"></span><dl> <dt>**GLU\_SAMPLING\_METHOD**</dt> </dl>                | Specifies how to tessallate a NURBS surface. GLU\_SAMPLING\_METHOD can have one of the following three values. <br/> GLU\_PATH\_LENGTH. The default value. Specifies that surfaces rendered with the maximum length, in pixels, of the edges of the tessellation polygons are no greater than the value specified by GLU\_SAMPLING\_TOLERANCE. <br/> GLU\_PARAMETRIC\_ERROR. Specifies that in rendering the surface, the value of GLU\_PARAMETRIC\_TOLERANCE specifies the maximum distance, in pixels, between the tessellation polygons and the surfaces they approximate. <br/> GLU\_DOMAIN\_DISTANCE. Specifies, in parametric coordinates, how many sample points per unit length to take in the *u* and *v* dimensions.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| <span id="GLU_U_STEP"></span><span id="glu_u_step"></span><dl> <dt>**GLU\_U\_STEP**</dt> </dl>                                           | Specifies the number of sample points per unit length taken along the *u* dimension in parametric coordinates. The value of GLU\_U\_STEP is used when GLU\_SAMPLING\_METHOD is set to GLU\_DOMAIN\_DISTANCE. The default value is 100.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| <span id="GLU_V_STEP"></span><span id="glu_v_step"></span><dl> <dt>**GLU\_V\_STEP**</dt> </dl>                                           | Specifies the number of sample points per unit length taken along the *v* dimension in parametric coordinates. The value of GLU\_V\_STEP is used when GLU\_SAMPLING\_METHOD is set to GLU\_DOMAIN\_DISTANCE. The default value is 100.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |



 

</dd> <dt>

*value* 
</dt> <dd>

The value to which to set the indicated property. The *value* parameter can be a numeric value or one of the following three values: GLU\_PATH\_LENGTH, GLU\_PARAMETRIC\_ERROR, or GLU\_DOMAIN\_DISTANCE.



| Value                                                                                                                                                                               | Meaning                                                                                                                                                                                                           |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="GLU_PATH_LENGTH"></span><span id="glu_path_length"></span><dl> <dt>**GLU\_PATH\_LENGTH**</dt> </dl>                | The default value. Specifies that surfaces rendered with the maximum length, in pixels, of the edges of the tessellation polygons are no greater than the value specified by GLU\_SAMPLING\_TOLERANCE.<br/> |
| <span id="GLU_PARAMETRIC_ERROR"></span><span id="glu_parametric_error"></span><dl> <dt>**GLU\_PARAMETRIC\_ERROR**</dt> </dl> | Specifies that in rendering the surface, the value of GLU\_PARAMETRIC\_TOLERANCE specifies the maximum distance, in pixels, between the tessellation polygons and the surfaces they approximate.<br/>       |
| <span id="GLU_DOMAIN_DISTANCE"></span><span id="glu_domain_distance"></span><dl> <dt>**GLU\_DOMAIN\_DISTANCE**</dt> </dl>    | Specifies, in parametric coordinates, how many sample points per unit length to take in the *u* and *v* dimensions.<br/>                                                                                    |



 

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

Use **gluNurbsProperty** to control properties stored in a NURBS object. These properties affect the way a NURBS curve is rendered.





 

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Glu.h</dt> </dl>     |
| Library<br/>                  | <dl> <dt>Glu32.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Glu32.dll</dt> </dl> |



## See also

<dl> <dt>

[**gluGetNurbsProperty**](glugetnurbsproperty.md)
</dt> <dt>

[**gluGetString**](glugetstring.md)
</dt> <dt>

[**gluLoadSamplingMatrices**](gluloadsamplingmatrices.md)
</dt> <dt>

[**gluNewNurbsRenderer**](glunewnurbsrenderer.md)
</dt> </dl>

 

 





