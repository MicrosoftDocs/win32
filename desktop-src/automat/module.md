---
title: module
description: This statement defines a group of functions, typically a set of DLL entry points.
ms.assetid: 'd032e90f-d9e4-4d5a-ad95-177c8dcd5607'
---

# module

This statement defines a group of functions, typically a set of DLL entry points.

## Syntax

``` syntax
[attributes]
module modulename {
   elementlist
};
```

<dl> <dt>

<span id="attributes"></span><span id="ATTRIBUTES"></span>*attributes*
</dt> <dd>

The attributes uuid, version, helpstring, helpcontext, hidden, and dllname are accepted before a module statement. The dllname attribute is required. If uuidis omitted, the module is not uniquely specified in the system.

</dd> <dt>

<span id="modulename"></span><span id="MODULENAME"></span>*modulename*
</dt> <dd>

The name of the module.

</dd> <dt>

<span id="elementlist"></span><span id="ELEMENTLIST"></span>*elementlist*
</dt> <dd>

The list of constant definitions and function prototypes for each function in the DLL. Any number of function definitions can appear in the function list. A function in the function list has the following form:

``` syntax
[attributes] returntype [calling convention] funcname(params);
[attributes] const constanttype constname = constval;
```

Only the attributes helpstring and helpcontext are accepted for a const.

The following attributes are accepted on a function in a module: helpstring,helpcontext, string, entry, propget, propput, propputref, vararg. If vararg is specified, the last parameter must be a safe array of VARIANT type.

The optional calling convention can be one of \_\_pascal/\_pascal/pascal, \_\_cdecl/\_cdecl/cdecl, or \_\_stdcall/\_stdcall/stdcall. The calling convention can include up to two leading underscores.

The parameter list is a comma-delimited list.

``` syntax
[attributes] type paramname
```

</dd> </dl>

## Remarks

The type can be any previously declared type or built-in type, a pointer to any type, or a pointer to a built-in type. Attributes on parameters are in, out, and optional.

If optional is specified, it must only be specified on the right-most parameters, and the types of those parameters must be VARIANT.

The header file (.h) output for modules is a series of function prototypes. The module keyword and surrounding brackets are stripped from the header file output, but a comment (\\\\**module***modulename*) is inserted before the prototypes. The keyword **extern** is inserted before the declarations.

## Example


```C++
[uuid(D00BED00-CEDE-B1FF-F001-A100FF001ED),
   helpstring("This is not GDI.EXE"), helpcontext(190), dllname("MATH.DLL")] 
module somemodule{
   [helpstring("Color for the frame")] unsigned long const COLOR_FRAME 
      = 0xH80000006;
   [helpstring("Not a rectangle but a square"), entry(1)] pascal double square([in] double x);
};
```



## Related topics

<dl> <dt>

[ODL Statements and Directives](odl-statements-and-directives.md)
</dt> </dl>

 

 




