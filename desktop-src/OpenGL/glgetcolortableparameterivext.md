---
title: glGetColorTableParameterivEXT function (Gl.h)
description: The glGetColorTableParameterfvEXT and glGetColorTableParameterivEXT functions get palette parameters from color tables. | glGetColorTableParameterivEXT function (Gl.h)
ms.assetid: 39a0b346-d103-4426-8536-95e7e1548f7a
keywords:
- glGetColorTableParameterivEXT function OpenGL
topic_type:
- apiref
api_name:
- glGetColorTableParameterivEXT
api_location:
- Gl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# glGetColorTableParameterivEXT function

The [**glGetColorTableParameterfvEXT**](glgetcolortableparameterfvext.md) and **glGetColorTableParameterivEXT** functions get palette parameters from color tables.

## Syntax


```C++
void WINAPI glGetColorTableParameterivEXT(
   GLenum target,
   GLenum pname,
   GLint  *params
);
```



## Parameters

<dl> <dt>

*target* 
</dt> <dd>

The target texture of the palette for which you want parameter data. Must be TEXTURE\_1D, TEXTURE\_2D, PROXY\_TEXTURE\_1D, or PROXY\_TEXTURE\_2D.

</dd> <dt>

*pname* 
</dt> <dd>

A symbolic constant for the type of palette parameter data pointed to by *params*.

The following are the accepted symbolic constants and their meanings.



| Value                                                                                                                                                                                                             | Meaning                                                                                                                                     |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="GL_COLOR_TABLE_FORMAT_EXT"></span><span id="gl_color_table_format_ext"></span><dl> <dt>**GL\_COLOR\_TABLE\_FORMAT\_EXT**</dt> </dl>              | Return the internal format specified by the most recent call to [**glColorTableEXT**](glcolortableext.md) or the default value.<br/> |
| <span id="GL_COLOR_TABLE_WIDTH_EXT"></span><span id="gl_color_table_width_ext"></span><dl> <dt>**GL\_COLOR\_TABLE\_WIDTH\_EXT**</dt> </dl>                 | Return the width of the current palette.<br/>                                                                                         |
| <span id="GL_COLOR_TABLE_RED_SIZE_EXT"></span><span id="gl_color_table_red_size_ext"></span><dl> <dt>**GL\_COLOR\_TABLE\_RED\_SIZE\_EXT**</dt> </dl>       | Return the actual size used internally to store the red component of the palette data.<br/>                                           |
| <span id="GL_COLOR_TABLE_GREEN_SIZE_EXT"></span><span id="gl_color_table_green_size_ext"></span><dl> <dt>**GL\_COLOR\_TABLE\_GREEN\_SIZE\_EXT**</dt> </dl> | Return the actual size used internally to store the green component of the palette data.<br/>                                         |
| <span id="GL_COLOR_TABLE_BLUE_SIZE_EXT"></span><span id="gl_color_table_blue_size_ext"></span><dl> <dt>**GL\_COLOR\_TABLE\_BLUE\_SIZE\_EXT**</dt> </dl>    | Return the actual size used internally to store the blue component of the palette data.<br/>                                          |
| <span id="GL_COLOR_TABLE_ALPHA_SIZE_EXT"></span><span id="gl_color_table_alpha_size_ext"></span><dl> <dt>**GL\_COLOR\_TABLE\_ALPHA\_SIZE\_EXT**</dt> </dl> | Return the actual size used internally to store the alpha component of the palette data.<br/>                                         |



 

</dd> <dt>

*params* 
</dt> <dd>

Points to the color table parameter data specified by the *pname* parameter.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

You use the **glGetColorTableParameterivEXT** and [**glGetColorTableParameterfvEXT**](glgetcolortableparameterfvext.md) functions to retrieve specific parameter data from color tables set with [**glColorTableEXT**](glcolortableext.md) for targeted texture palettes. Also you can use these functions to determine the number of color table entries that **glGetColorTableEXT** returns.

When the *target* parameter is GL\_PROXY\_TEXTURE\_1D or GL\_PROXY\_TEXTURE\_2D, and the implementation does not support the values specified for either *format* or *width*, **glColorTableEXT** can fail to create the requested color table. In this case, the color table is empty and all parameters retrieved will be zero. You can determine whether OpenGL supports a particular color table format and size by calling **glColorTableEXT** with a proxy target, and then calling **glGetColorTableParameterivEXT** or [**glGetColorTableParameterfvEXT**](glgetcolortableparameterfvext.md) to determine whether the width parameter matches that set by **glColorTableEXT**. If the retrieved width is zero, the color table request by **glColorTable** failed. If the retrieved width is not zero, you can call **glColorTable** with the real target with TEXTURE\_1D or TEXTURE\_2D to set the color table.

The **glGetColorTableParameterivEXT** and [**glGetColorTableParameterfvEXT**](glgetcolortableparameterfvext.md) functions are extension functions that are not part of the standard OpenGL library but are part of the GL\_EXT\_paletted\_texture extension. To check whether your implementation of OpenGL supports **glGetColorTableParameterivEXT** and **glGetColorTableParameterfvEXT**, call [**glGetString**](glgetstring.md)**(**GL\_EXTENSIONS**)**. If it returns GL\_EXT\_paletted\_texture, **glGetColorTableParameterivEXT** and **glGetColorTableParameterfvEXT** are supported. To obtain the function address of an extension function, call [**wglGetProcAddress**](/windows/desktop/api/wingdi/nf-wingdi-wglgetprocaddress).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                      |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                            |
| Header<br/>                   | <dl> <dt>Gl.h</dt> </dl> |



## See also

<dl> <dt>

[**glColorSubTableEXT**](glcolorsubtableext.md)
</dt> <dt>

[**glColorTableEXT**](glcolortableext.md)
</dt> <dt>

[**glGetColorTableEXT**](glgetcolortableext.md)
</dt> <dt>

[**glGetColorTableParameterfvEXT**](glgetcolortableparameterfvext.md)
</dt> <dt>

[**wglGetProcAddress**](/windows/desktop/api/wingdi/nf-wingdi-wglgetprocaddress)
</dt> </dl>

 

 





