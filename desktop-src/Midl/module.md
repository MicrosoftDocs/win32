---
title: module attribute
description: The module statement defines a group of functions, typically a set of DLL entry points.
ms.assetid: 4dec207f-98bc-4784-a3c9-506ffe7523fe
keywords:
- module attribute MIDL
topic_type:
- apiref
api_name:
- module
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# module attribute

The **module** statement defines a group of functions, typically a set of DLL entry points.

``` syntax
[
    attributes
]
module modulename 
{
    elementlist
};
```

## Parameters

<dl> <dt>

*attributes* 
</dt> <dd>

The \[[**uuid**](uuid.md)\], \[[**version**](version.md)\], \[[**helpstring**](helpstring.md)\], \[[**helpcontext**](helpcontext.md)\], \[[**hidden**](hidden.md)\], and \[[**dllname**](dllname-str-.md)\] attributes are accepted before a **module** statement. See [Attribute Descriptions](/previous-versions/windows/desktop/automat/attribute-descriptions), in the OLE Automation book, for more information on the attributes accepted before a module definition. The \[**dllname**\] attribute is required. If the \[**uuid**\] attribute is omitted, the module is not uniquely specified in the system.

</dd> <dt>

*modulename* 
</dt> <dd>

The name of the module.

</dd> <dt>

*elementlist* 
</dt> <dd>

List of constant definitions and function prototypes for each function in the DLL. Any number of function definitions can appear in the function list. A function in the function list has the following form:

\[*attributes*\] *returntype* \[*calling convention funcname*\](*params*);

\[*attributes*\] [**const**](const.md) constanttype *constname* = *constval*;

Only the \[[**helpstring**](helpstring.md)\] and \[[**helpcontext**](helpcontext.md)\] attributes are accepted for a [**const**](const.md).

The following attributes are accepted on a function in a module: \[[**helpstring**](helpstring.md)\], \[[**helpcontext**](helpcontext.md)\], \[[**string**](string.md)\], \[[**entry**](entry.md)\], \[[**propget**](propget.md)\], \[[**propput**](propput.md)\], \[[**propputref**](propputref.md)\], and \[[**vararg**](vararg.md)\]. If \[**vararg**\] is specified, the last parameter must be a safe array of **VARIANT** type.

The optional calling convention can be one of \_\_pascal/\_pascal/pascal, \_\_cdecl/\_cdecl/cdecl, or \_\_stdcall/\_stdcall/stdcall. The *calling convention type paramname* can include up to two leading underscores.

The parameter list is a comma-delimited list of:

\[*attributes*\]

The type can be any previously declared type or built-in type, a pointer to any type, or a pointer to a built-in type. Attributes on parameters are:

\[[**in**](in.md)\], \[[**out**](out-idl.md)\], \[[**optional**](optional.md)\].

If \[[**optional**](optional.md)\] is used, the types of those parameters must be **VARIANT** or **VARIANT**\*.

</dd> </dl>

## Remarks

The header file (.h) output for modules is a series of function prototypes. The **module** keyword and surrounding brackets are stripped from the header (.h) file output, but a comment (// **module** *modulename*) is inserted before the prototypes. The keyword **extern** is inserted before the declarations.

## Examples

``` syntax
[
    uuid(12345678-1234-1234-1234-123456789ABC), 
    helpstring("This is not GDI.EXE"), 
    helpcontext(190), 
    dllname("MATH.DLL")
] 
module somemodule
{ 
    [helpstring("Color for the frame")] 
            unsigned long const COLOR_FRAME = 0xH80000006; 
    [helpstring("Not a rectangle but a square"), 
     entry(1)] 
            pascal double square([in] double x); 
};
```

## See also

<dl> <dt>

[**const**](const.md)
</dt> <dt>

[Contents of a Type Library](/previous-versions/windows/desktop/automat/contents-of-a-type-library)
</dt> <dt>

[**dllname**](dllname-str-.md)
</dt> <dt>

[**entry**](entry.md)
</dt> <dt>

[Generating a Type Library With MIDL](generating-a-type-library-with-midl-2.md)
</dt> <dt>

[**helpcontext**](helpcontext.md)
</dt> <dt>

[**helpstring**](helpstring.md)
</dt> <dt>

[**hidden**](hidden.md)
</dt> <dt>

[ODL File Syntax](/previous-versions/windows/desktop/automat/odl-file-syntax)
</dt> <dt>

[**propget**](propget.md)
</dt> <dt>

[**propput**](propput.md)
</dt> <dt>

[**propputref**](propputref.md)
</dt> <dt>

[**string**](string.md)
</dt> <dt>

[**TYPEFLAGS**](/windows/win32/api/oaidl/ne-oaidl-typeflags)
</dt> <dt>

[**uuid**](uuid.md)
</dt> <dt>

[**vararg**](vararg.md)
</dt> <dt>

[**version**](version.md)
</dt> </dl>

 

 