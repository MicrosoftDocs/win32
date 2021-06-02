---
description: Templates define how the data stream is interpreted - the data is modulated by the template definition. This section discusses the following aspects of a template and provides an example template.
ms.assetid: f84978a8-8315-4626-be68-f00f3a72e5ac
title: Templates (X file format, text encoding)
ms.topic: article
ms.date: 05/31/2018
---

# Templates (X file format, text encoding)

Templates define how the data stream is interpreted - the data is modulated by the template definition. This section discusses the following aspects of a template and provides an example template.

There is one special template - the header template. It is recommended that each application define a header template and use it to define application-specific information, such as version information. If present, this header is read by the .x file format API. If a flags member is available, it is used to determine how the following data is interpreted. The flags member, if defined, should be a DWORD. One bit is currently defined - bit 0. If this bit is clear, the following data in the file is binary. If set, the following data is text. You can use multiple header data objects to switch between binary and text within the file.

## Template Form, Name, and UUID

A template has the following form.


```
template <template-name> {
<UUID>
    <member 1>;
...
    <member n>;
[restrictions]
}
```



The template name is an alphanumeric name that can include the underscore character (\_). It must not begin with a digit. The UUID is a universally unique identifier formatted to the Open Software Foundation's Distributed Computing Environment standard and enclosed by angle brackets (< >). For example: <3D82AB43-62DA-11cf-AB39-0020AF71E433>.

## Template Members

Template members consist of a named data type followed by an optional name or an array of a named data type. Valid primitive data types are defined in the following table.



| Type    | Size                               |
|---------|------------------------------------|
| WORD    | 16 bits                            |
| DWORD   | 32 bits                            |
| FLOAT   | IEEE float                         |
| DOUBLE  | 64 bits                            |
| CHAR    | 8 bits                             |
| UCHAR   | 8 bits                             |
| BYTE    | 8 bits                             |
| STRING  | NULL terminated string             |
| CSTRING | Formatted C string (not supported) |
| UNICODE | Unicode string (not supported)     |



 

Additional data types defined by templates encountered earlier in the data stream can also be referenced within a template definition. No forward references are allowed.

Any valid data type can be expressed as an array in the template definition. The basic syntax is shown in the following example.


```
array <data-type> <name>[<dimension-size>];
```



<dimension-size> can either be an integer or a named reference to another template member whose value is then substituted. Arrays can be n-dimensional, where n is determined by the number of paired square brackets trailing the statement, as in the following example.


```
array DWORD FixedHerd[24];
array DWORD Herd[nCows];
array FLOAT Matrix4x4[4][4];
```



## Template Restrictions

Templates can be open, closed, or restricted. These restrictions determine which data types can appear in the immediate hierarchy of a data object defined by the template. An open template has no restrictions, a closed template rejects all data types, and a restricted template allows a named list of data types.

The syntax for indicating an open template is three periods enclosed by square brackets.


```
[ ... ]
```



A comma-separated list of named data types followed optionally by their UUIDs enclosed by square brackets indicates a restricted template.


```
[ { data-type [ UUID ] , } ... ]
```



The absence of either of the above indicates a closed template.

## Template Example

The following shows an example template.


```
template Mesh {
<3D82AB44-62DA-11cf-AB39-0020AF71E433>
DWORD nVertices;
array Vector vertices[nVertices];
DWORD nFaces;
array MeshFace faces[nFaces];
 [ ... ]                // An open template
}
template Vector {
<3D82AB5E-62DA-11cf-AB39-0020AF71E433>
FLOAT x;
FLOAT y;
FLOAT z;
}                        // A closed template
template FileSystem {
<UUID>
STRING name;
[ Directory <UUID>, File <UUID> ]    // A restricted template
}
```



## Related topics

<dl> <dt>

[Text Encoding](text-encoding.md)
</dt> </dl>

 

 



