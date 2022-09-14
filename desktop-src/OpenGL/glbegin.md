---
title: glBegin function (Gl.h)
description: The glBegin and glend functions delimit the vertices of a primitive or a group of like primitives. | glBegin function (Gl.h)
ms.assetid: 8e8e98f8-89e8-40f5-89c1-492c9e3bbd74
keywords:
- glBegin function OpenGL
topic_type:
- apiref
api_name:
- glBegin
api_location:
- Opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glBegin function

The **glBegin** and [**glend**](glend.md) functions delimit the vertices of a primitive or a group of like primitives.

## Syntax


```C++
void WINAPI glBegin(
   GLenum mode
);
```



## Parameters

<dl> <dt>

*mode* 
</dt> <dd>

The primitive or primitives that will be created from vertices presented between **glBegin** and the subsequent [**glend**](glend.md). The following are accepted symbolic constants and their meanings:



| Value                                                                                                                                                                      | Meaning                                                                                                                                                                                                                                                                                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="GL_POINTS"></span><span id="gl_points"></span><dl> <dt>**GL\_POINTS**</dt> </dl>                          | Treats each vertex as a single point. Vertex *n* defines point *n*. *N* points are drawn.<br/>                                                                                                                                                                                                                                                                                                      |
| <span id="GL_LINES"></span><span id="gl_lines"></span><dl> <dt>**GL\_LINES**</dt> </dl>                             | Treats each pair of vertices as an independent line segment. Vertices *2n - 1* and *2n* define line *n*. *N/2* lines are drawn.<br/>                                                                                                                                                                                                                                                                |
| <span id="GL_LINE_STRIP"></span><span id="gl_line_strip"></span><dl> <dt>**GL\_LINE\_STRIP**</dt> </dl>             | Draws a connected group of line segments from the first vertex to the last. Vertices *n* and *n+1* define line *n*. *N - 1* lines are drawn.<br/>                                                                                                                                                                                                                                                   |
| <span id="GL_LINE_LOOP"></span><span id="gl_line_loop"></span><dl> <dt>**GL\_LINE\_LOOP**</dt> </dl>                | Draws a connected group of line segments from the first vertex to the last, then back to the first. Vertices *n* and *n + 1* define line *n*. The last line, however, is defined by vertices *N* and *1*. *N* lines are drawn.<br/>                                                                                                                                                                 |
| <span id="GL_TRIANGLES"></span><span id="gl_triangles"></span><dl> <dt>**GL\_TRIANGLES**</dt> </dl>                 | Treats each triplet of vertices as an independent triangle. Vertices *3n - 2*, *3n - 1*, and *3n* define triangle *n*. *N/3* triangles are drawn.<br/>                                                                                                                                                                                                                                              |
| <span id="GL_TRIANGLE_STRIP"></span><span id="gl_triangle_strip"></span><dl> <dt>**GL\_TRIANGLE\_STRIP**</dt> </dl> | Draws a connected group of triangles. One triangle is defined for each vertex presented after the first two vertices. For odd *n*, vertices *n*, *n + 1*, and *n + 2* define triangle *n*. For even *n*, vertices *n + 1*, *n*, and *n + 2* define triangle *n*. *N - 2* triangles are drawn.<br/>                                                                                                  |
| <span id="GL_TRIANGLE_FAN"></span><span id="gl_triangle_fan"></span><dl> <dt>**GL\_TRIANGLE\_FAN**</dt> </dl>       | Draws a connected group of triangles. one triangle is defined for each vertex presented after the first two vertices. Vertices *1*, *n + 1*, *n + 2* define triangle *n*. *N - 2* triangles are drawn.<br/>                                                                                                                                                                                         |
| <span id="GL_QUADS"></span><span id="gl_quads"></span><dl> <dt>**GL\_QUADS**</dt> </dl>                             | Treats each group of four vertices as an independent quadrilateral. Vertices *4n - 3*, *4n - 2*, *4n - 1*, and *4n* define quadrilateral *n*. *N/4* quadrilaterals are drawn.<br/>                                                                                                                                                                                                                  |
| <span id="GL_QUAD_STRIP"></span><span id="gl_quad_strip"></span><dl> <dt>**GL\_QUAD\_STRIP**</dt> </dl>             | Draws a connected group of quadrilaterals. One quadrilateral is defined for each pair of vertices presented after the first pair. Vertices *2n - 1*, *2n*, *2n + 2*, and *2n + 1* define quadrilateral *n*. *N/2 - 1* quadrilaterals are drawn. Note that the order in which vertices are used to construct a quadrilateral from strip data is different from that used with independent data.<br/> |
| <span id="GL_POLYGON"></span><span id="gl_polygon"></span><dl> <dt>**GL\_POLYGON**</dt> </dl>                       | Draws a single, convex polygon. Vertices *1* through *N* define this polygon.<br/>                                                                                                                                                                                                                                                                                                                  |



 

</dd> </dl>

## Return value

This function does not return a value.

## Error codes

The following error codes can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                                  | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|-------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**GL\_INVALID\_ENUM**</dt> </dl>      | *mode* was set to an unaccepted value.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | A function other than [glVertex](glvertex-functions.md), [glColor](glcolor-functions.md), [glIndex](glindex-functions.md), [glNormal](glnormal-functions.md), [glTexCoord](gltexcoord-functions.md), [glEvalCoord](glevalcoord-functions.md), [glEvalPoint](glevalpoint.md), [glMaterial](glmaterial-functions.md), [glEdgeFlag](gledgeflag-functions.md), [**glCallList**](glcalllist.md), or [**glCallLists**](glcalllists.md) was called between **glBegin** and the corresponding [**glend**](glend.md). The function **glend** was called before the corresponding **glBegin** was called, or **glBegin** was called within a **glBegin**/**glend** sequence. <br/> |



## Remarks

The **glBegin** and [**glend**](glend.md) functions delimit the vertices that define a primitive or a group of like primitives. The **glBegin** function accepts a single argument that specifies which of ten primitives the vertices compose. Taking *n* as an integer count starting at one, and *N* as the total number of vertices specified, the interpretations are as follows:

-   You can use only a subset of OpenGL functions between **glBegin** and [**glend**](glend.md). The functions you can use are:

    [**glVertex**](glvertex-functions.md)

     

    [**glColor**](glcolor-functions.md)

     

    [**glIndex**](glindex-functions.md)

     

    [**glNormal**](glnormal-functions.md)

     

    [**glTexCoord**](gltexcoord-functions.md)

     

    [**glEvalCoord**](glevalcoord-functions.md)

     

    [**glEvalPoint**](glevalpoint.md)

     

    [**glMaterial**](glmaterial-functions.md)

     

    [**glEdgeFlag**](gledgeflag-functions.md)

    You can also use [**glCallList**](glcalllist.md) or [**glCallLists**](glcalllists.md) to execute display lists that include only the preceding functions. If any other OpenGL function is called between **glBegin** and [**glend**](glend.md), the error flag is set and the function is ignored.

-   Regardless of the value chosen for *mode* in **glBegin**, there is no limit to the number of vertices you can define between **glBegin** and [**glend**](glend.md). Lines, triangles, quadrilaterals, and polygons that are incompletely specified are not drawn. Incomplete specification results when either too few vertices are provided to specify even a single primitive or when an incorrect multiple of vertices is specified. The incomplete primitive is ignored; the complete primitives are drawn.
-   The minimum specification of vertices for each primitive is: 

    | Minimum number of vertices | Type of primitive |
    |----------------------------|-------------------|
    | 1                          | point             |
    | 2                          | line              |
    | 3                          | triangle          |
    | 4                          | quadrilateral     |
    | 3                          | polygon           |

    

     

-   Modes that require a certain multiple of vertices are GL\_LINES (2), GL\_TRIANGLES (3), GL\_QUADS (4), and GL\_QUAD\_STRIP (2).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Gl.h</dt> </dl>         |
| Library<br/>                  | <dl> <dt>Opengl32.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Opengl32.dll</dt> </dl> |



## See also

<dl> <dt>

[**glCallList**](glcalllist.md)
</dt> <dt>

[**glCallLists**](glcalllists.md)
</dt> <dt>

[**glColor**](glcolor-functions.md)
</dt> <dt>

[**glEdgeFlag**](gledgeflag-functions.md)
</dt> <dt>

[**glEnd**](/windows/desktop/OpenGL/glend)
</dt> <dt>

[**glEvalCoord**](glevalcoord-functions.md)
</dt> <dt>

[**glEvalPoint**](glevalpoint.md)
</dt> <dt>

[**glIndex**](glindex-functions.md)
</dt> <dt>

[**glMaterial**](glmaterial-functions.md)
</dt> <dt>

[**glNormal**](glnormal-functions.md)
</dt> <dt>

[**glTexCoord**](gltexcoord-functions.md)
</dt> <dt>

[**glVertex**](glvertex-functions.md)
</dt> </dl>

 

