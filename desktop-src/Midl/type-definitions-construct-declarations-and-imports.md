---
title: Type Definitions, Construct Declarations, and Imports
description: Type definitions, construct declarations, and imports can occur outside of the interface body.
ms.assetid: 5d9011ab-bfc4-41f6-bd69-953660191652
keywords:
- interfaces MIDL , type definitions
- interfaces MIDL , construct declarations
- interfaces MIDL , imports
- type definitions MIDL
- construct declarations MIDL
- imports MIDL
ms.topic: article
ms.date: 05/31/2018
---

# Type Definitions, Construct Declarations, and Imports

Type definitions, construct declarations, and imports can occur outside of the interface body. All definitions from the main IDL file will appear in the generated header file, and all the procedures from all the interfaces in the main IDL file will generate stub routines. This enables applications that support multiple interfaces to merge IDL files into a single, combined IDL file.

As a result, it requires less time to compile the files and also allows MIDL to reduce redundancies in the generated stubs. This can significantly improve [**object**](object.md) interfaces through the ability to share common code for base interfaces and derived interfaces. For non- **object** interfaces, the procedure names must be unique across all the interfaces. For **object** interfaces, the procedure names need to be unique only within an interface. Note that multiple interfaces are not permitted when you use the [**/osf**](-osf.md) switch.

## Declarative Constructs

The syntax for declarative constructs in the IDL file is similar to that for C. MIDL supports all Microsoft C/C++ declarative constructs except the following:

-   Older style declarators that allow a declarator to be specified without a type specifier, such as:

    ``` syntax
    x (y) 
    short x (y)
    ```

-   Declarations with initializers (MIDL only accepts declarations that conform to the MIDL [**const**](const.md) syntax).

The [**import**](import.md) keyword specifies the names of one or more IDL files to import. The import directive is similar to the C [**include**](include.md) directive, except that only data types are assimilated into the importing IDL file.

## Constant Declaration

The constant declaration specifies [**Boolean**](boolean.md), integer, character, wide-character, string, and **void \*** constants. For more information, see [**const**](const.md).

## General Declaration

A general declaration is similar to the C [**typedef**](typedef.md) statement with the addition of IDL type attributes. Except in [**/osf**](-osf.md) mode, the MIDL compiler also allows an implicit declaration in the form of a variable definition.

## Function Declaration

The function declarator is a special case of the general declaration. You can use IDL attributes to specify the behavior of the function return type and each of the parameters.

## Examples

``` syntax
[ 
    uuid(12345678-1234-1234-1234-123456789ABC), 
    version(3.1), 
    pointer_default(unique) 
] 
interface IdlGrammarExample 
{ 
    import "windows.idl", "other.idl"; 
    const wchar_t * NAME = L"Example Program"; 
    typedef char * PCHAR; 
 
    HRESULT DictCheckSpelling( 
        [in, string] PCHAR   word,     // word to look up 
        [out]        short * isPresent // 0 if not present 
    ); 
}
```

 

 




