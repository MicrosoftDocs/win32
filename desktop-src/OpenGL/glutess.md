---
title: gluTessCallback function (Glu.h)
description: The gluTessCallback function defines a callback for a tessellation object.
ms.assetid: a9709919-d34c-42c4-82b8-6a503f2b39b0
keywords:
- gluTessCallback function OpenGL
topic_type:
- apiref
api_name:
- gluTessCallback
api_location:
- Glu32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# gluTessCallback function

The **gluTessCallback** function defines a callback for a tessellation object.

## Syntax


```C++
void WINAPI gluTessCallback(
   GLUtesselator *tess,
   GLenum        which,
   void (CALLBACK *fn)()
);
```



## Parameters

<dl> <dt>

*tess* 
</dt> <dd>

The tessellation object (created with [**gluNewTess**](glunewtess.md)).

</dd> <dt>

*which* 
</dt> <dd>

The callback being defined. The following values are valid: GLU\_TESS\_BEGIN, GLU\_TESS\_BEGIN\_DATA, GLU\_TESS\_EDGE\_FLAG, GLU\_TESS\_EDGE\_FLAG\_DATA, GLU\_TESS\_VERTEX, GLU\_TESS\_VERTEX\_DATA, GLU\_TESS\_END, GLU\_TESS\_END\_DATA, GLU\_TESS\_COMBINE, GLU\_TESS\_COMBINE\_DATA, GLU\_TESS\_ERROR, and GLU\_TESS\_ERROR\_DATA.

For more information on these callbacks, see the following Remarks section.

</dd> <dt>

*fn* 
</dt> <dd>

The function to be called.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

Use **gluTessCallback** to specify a callback to be used by a tessellation object. If the specified callback is already defined, then it is replaced. If *fn* is **NULL**, then the existing callback becomes undefined.

The tessellation object uses these callbacks to describe how a polygon that you specify is broken into triangles.

There are two versions of each callback, one with polygon data that you can define and one without. If both versions of a particular callback are specified, the callback with the polygon data you specify will be used. The *polygon\_data* parameter of [**gluTessBeginPolygon**](glutessbeginpolygon.md) is a copy of the pointer that was specified when **gluTessBeginPolygon** was called.

The following are valid callbacks:



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Callback</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>GLU_TESS_BEGIN</td>
<td>The GLU_TESS_BEGIN callback is invoked like <a href="glbegin.md"><strong>glBegin</strong></a> to indicate the start of a (triangle) primitive. The function takes a single argument of type <strong>GLenum</strong>. If you set the GLU_TESS_BOUNDARY_ONLY property to GL_FALSE, the argument is set to either GL_TRIANGLE_FAN, GL_TRIANGLE_STRIP, or GL_TRIANGLES. If you set the GLU_TESS_BOUNDARY_ONLY property to GL_TRUE, the argument is set to GL_LINE_LOOP. The function prototype for this callback is as follows: <strong>void</strong> <strong>begin</strong> (<strong>GLenum</strong> <em>type</em>);<br/></td>
</tr>
<tr class="even">
<td>GLU_TESS_BEGIN_DATA</td>
<td>GLU_TESS_BEGIN_DATA is the same as the GLU_TESS_BEGIN callback except that it takes an additional pointer argument. This pointer is identical to the opaque pointer provided when you call <a href="glutessbeginpolygon.md"><strong>gluTessBeginPolygon</strong></a>. The function prototype for this callback is: <strong>void</strong> <strong>beginData</strong> (<strong>GLenum</strong> <em>type</em>, <strong>void</strong> * <em>polygon_data</em>);<br/></td>
</tr>
<tr class="odd">
<td>GLU_TESS_EDGE_FLAG</td>
<td>The GLU_TESS_EDGE_FLAG callback is similar to <a href="gledgeflag-functions.md"><strong>glEdgeFlag</strong></a>. The function takes a single Boolean flag that indicates which edges lie on the polygon boundary. If the flag is GL_TRUE, then each vertex that follows begins an edge that lies on the polygon boundary; that is, an edge which separates an interior region from an exterior one. If the flag is GL_FALSE, then each vertex that follows begins an edge that lies in the polygon interior. The GLU_TESS_EDGE_FLAG callback (if defined) is invoked before the first vertex callback is made. Because triangle fans and triangle strips do not support edge flags, the begin callback is not called with GL_TRIANGLE_FAN or GL_TRIANGLE_STRIP if an edge flag callback is provided. Instead, the fans and strips are converted to independent triangles. The function prototype for this callback is:<br/> <strong>void</strong> <strong>edgeFlag</strong> (<strong>GLboolean</strong> <em>flag</em>);<br/></td>
</tr>
<tr class="even">
<td>GLU_TESS_EDGE_FLAG_DATA</td>
<td>The GLU_TESS_EDGE_FLAG_DATA callback is the same as the GLU_TESS_EDGE_FLAG callback except that it takes an additional pointer argument. This pointer is identical to the opaque pointer provided when you call <a href="glutessbeginpolygon.md"><strong>gluTessBeginPolygon</strong></a>. The function prototype for this callback is: <strong>void</strong> <strong>edgeFlagData</strong> (<strong>GLboolean</strong> <em>flag</em>, <strong>void</strong> * <em>polygon_data</em>);<br/></td>
</tr>
<tr class="odd">
<td>GLU_TESS_VERTEX</td>
<td>The GLU_TESS_VERTEX callback is invoked between the begin and end callbacks. It is similar to glVertex , and it defines the vertexes of the triangles created by the tessellation process. The function takes a pointer as its only argument. This pointer is identical to the opaque pointer that you provided when you defined the vertex (see <a href="glutessvertex.md"><strong>gluTessVertex</strong></a>). The function prototype for this callback is: <strong>void</strong> <strong>vertex</strong> (<strong>void</strong> * <em>vertex_data</em>);<br/></td>
</tr>
<tr class="even">
<td>GLU_TESS_VERTEX_DATA</td>
<td>The GLU_TESS_VERTEX_DATA is the same as the GLU_TESS_VERTEX callback except that it takes an additional pointer argument. This pointer is identical to the opaque pointer provided when you call <a href="glutessbeginpolygon.md"><strong>gluTessBeginPolygon</strong></a>. The function prototype for this callback is: <strong>void</strong>  <strong>vertexData</strong> (void * <em>vertex_data</em>, <strong>void</strong> * <em>polygon_data</em>);<br/></td>
</tr>
<tr class="odd">
<td>GLU_TESS_END</td>
<td>The GLU_TESS_END callback serves the same purpose as <a href="glend.md"><strong>glEnd</strong></a>. It indicates the end of a primitive, and it takes no arguments. The function prototype for this callback is: <strong>void</strong> <strong>end</strong> (<strong>void</strong>);<br/></td>
</tr>
<tr class="even">
<td>GLU_TESS_END_DATA</td>
<td>The GLU_TESS_END_DATA callback is the same as the GLU_TESS_END callback except that it takes an additional pointer argument. This pointer is identical to the opaque pointer provided when you call <a href="glutessbeginpolygon.md"><strong>gluTessBeginPolygon</strong></a>. The function prototype for this callback is: <strong>void</strong> <strong>endData</strong> (<strong>void</strong> * <em>polygon_data</em>);<br/></td>
</tr>
<tr class="odd">
<td>GLU_TESS_COMBINE</td>
<td>Call the GLU_TESS_COMBINE callback to create a new vertex when the tessellation detects an intersection, or to merge features. The function takes four arguments: An array of three elements, each of type Gldouble.<br/> An array of four pointers.<br/> An array of four elements, each of type GLfloat.<br/> A pointer to a pointer.<br/> The function prototype for this callback is: <br/> <strong>void</strong> <strong>combine</strong>(<strong>GLdouble</strong> <em>coords</em>[3], <strong>void</strong> * <em>vertex_data</em>[4], <strong>GLfloat</strong> <em>weight</em>[4], <strong>void</strong> **<em>outData</em>);<br/> The vertex is defined as a linear combination of up to four existing vertexes, stored in vertex_data. The coefficients of the linear combination are given by weight; these weights always sum to 1.0. All vertex pointers are valid even when some of the weights are zero. The coords parameter gives the location of the new vertex.<br/> Allocate another vertex, interpolate parameters using vertex_data and weight, and return the new vertex pointer in outData. This handle is supplied during rendering callbacks. Free the memory sometime after calling <a href="glutessendpolygon.md"><strong>gluTessEndPolygon</strong></a>.<br/> For example, if the polygon lies in an arbitrary plane in three-dimensional space, and you associate a color with each vertex, the GLU_TESS_COMBINE callback might look like the following:<br/>
<pre data-space="preserve"><code>void myCombine( GLdouble coords[3], VERTEX *d[4], 
                GLfloat w[4], VERTEX **dataOut ) 
{ 
    VERTEX *newVertex = new_vertex(); 
    newVertex->x = coords[0]; 
    newVertex->y = coords[1]; 
    newVertex->z = coords[2]; 
    newVertex->r = w[0]*d[0]->r + w[1]*d[1]->r + w[2]*d[2]->r + 
                   w[3]*d[3]->r; 
    newVertex->g = w[0]*d[0]->g + w[1]*d[1]->g + w[2]*d[2]->g + 
                   w[3]*d[3]->g; 
    newVertex->b = w[0]*d[0]->b + w[1]*d[1]->b + w[2]*d[2]->b + 
                   w[3]*d[3]->b; 
    newVertex->a = w[0]*d[0]->a + w[1]*d[1]->a + w[2]*d[2]->a + 
                   w[3]*d[3]->a; 
    *dataOut = newVertex; 
}</code></pre>
When the tessellation detects an intersection, the GLU_TESS_COMBINE or GLU_TESS_COMBINE_DATA callback (see below) must be defined, and must write a non-<strong>NULL</strong> pointer into dataOut. Otherwise the GLU_TESS_NEED_COMBINE_CALLBACK error occurs, and no output is generated. (This is the only error that can occur during tessellation and rendering.)<br/></td>
</tr>
<tr class="even">
<td>GLU_TESS_COMBINE_DATA</td>
<td>The GLU_TESS_COMBINE_DATA callback is the same as the GLU_TESS_COMBINE callback except that it takes an additional pointer argument. This pointer is identical to the opaque pointer provided when you call <a href="glutessbeginpolygon.md"><strong>gluTessBeginPolygon</strong></a>. The function prototype for this callback is: <strong>void</strong> <strong>combineData</strong> (<strong>GLdouble</strong> <em>coords</em>[3], <strong>void</strong> *<em>vertex_data</em>[4], <strong>GLfloat</strong> <em>weight</em>[4], <strong>void</strong> **<em>outData</em>, <strong>void</strong> * <em>polygon_data</em>);<br/></td>
</tr>
<tr class="odd">
<td>GLU_TESS_ERROR</td>
<td>The GLU_TESS_ERROR callback is called when an error is encountered. The one argument is of type <strong>GLenum</strong>; it indicates the specific error that occurred and is set to one of the following: GLU_TESS_MISSING_BEGIN_POLYGON<br/> GLU_TESS_MISSING_END_POLYGON<br/> GLU_TESS_MISSING_BEGIN_CONTOUR<br/> GLU_TESS_MISSING_END_CONTOUR<br/> GLU_TESS_COORD_TOO_LARGE<br/> GLU_TESS_NEED_COMBINE_CALLBACK<br/> Call gluErrorString to retrieve character strings describing these errors. The function prototype for this callback is as follows:<br/> <strong>void</strong> <strong>error</strong> (<strong>GLenum</strong> <em>errno</em>);<br/> The GLU library recovers from the first four errors by inserting the missing call or calls. GLU_TESS_COORD_TOO_LARGE indicates that some vertex coordinate exceeded the predefined constant GLU_TESS_MAX_COORD in absolute value, and that the value has been clamped. (Coordinate values must be small enough that two can be multiplied together without overflow.) GLU_TESS_NEED_COMBINE_CALLBACK indicates that the tessellation detected an intersection between two edges in the input data, and the GLU_TESS_COMBINE or GLU_TESS_COMBINE_DATA callback was not provided. No output will be generated.<br/></td>
</tr>
<tr class="even">
<td>GLU_TESS_ERROR_DATA</td>
<td>The GLU_TESS_ERROR_DATA callback is the same as the GLU_TESS_ERROR callback, except that it takes an additional pointer argument. This pointer is identical to the opaque pointer provided when you call <a href="glutessbeginpolygon.md"><strong>gluTessBeginPolygon</strong></a>. The function prototype for this callback is: <strong>void</strong> <strong>errorData</strong> (<strong>GLenum</strong> <em>errno</em>, <strong>void</strong> * <em>polygon_data</em>);<br/></td>
</tr>
</tbody>
</table>



 

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

[**glBegin**](glbegin.md)
</dt> <dt>

[**glEdgeFlag**](gledgeflag-functions.md)
</dt> <dt>

[**glEnd**](glend.md)
</dt> <dt>

[**glVertex**](glvertex-functions.md)
</dt> <dt>

[**gluDeleteTess**](gludeletetess.md)
</dt> <dt>

[**gluErrorString**](gluerrorstring.md)
</dt> <dt>

[**gluNewTess**](glunewtess.md)
</dt> <dt>

[**gluTessBeginPolygon**](glutessbeginpolygon.md)
</dt> <dt>

[**gluTessEndPolygon**](glutessendpolygon.md)
</dt> <dt>

[**gluTessVertex**](glutessvertex.md)
</dt> </dl>

 

 





