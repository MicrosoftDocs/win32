---
title: import attribute
description: The import directive specifies another IDL, ODL, or header file containing definitions you wish to reference from your main IDL file.
ms.assetid: b52fb2c7-ce60-474f-8833-7a821844f747
keywords:
- import attribute MIDL
topic_type:
- apiref
api_name:
- import
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# import attribute

The **import** directive specifies another IDL, ODL, or header file containing definitions you wish to reference from your main IDL file.

``` syntax
import "filename" [[ , ... ]] ;
```

## Parameters

<dl> <dt>

*filename* 
</dt> <dd>

Specifies the name of the header, IDL, or ODL file to import.

</dd> </dl>

## Remarks

With the **import** directive, all IDL statements in the imported file, such as typedefs, constant declarations, and interface definitions become available to the importing .IDL file.

The imported file is processed separately (meaning that CPP preprocessor is invoked independently) from the importing IDL file. In this way, pre-processor directives, such as \#define, do not carry over from an imported header or IDL file to the importing IDL file.

Like the C-language preprocessor macro **\#include**, the **import** directive tells the compiler to include data types that were defined in the imported IDL files. Unlike the **\#include** directive, the **import** directive ignores procedure prototypes, since no stubs are generated for anything in the imported file.

For specific information on using **import** to include header files in an IDL file, see [Importing System Header Files](importing-system-header-files.md).

The C-language header (.H) file generated for the interface does not directly contain the imported types but instead generates a **\#include** directive for the header file corresponding to the imported interface. For example, when you import BASE.IDL into your DERIVED.IDL, the generated header file DERIVED.H will contain the directive **\#include** BASE.H.

The following rules apply:

-   The **import** keyword is optional and can appear zero or more times in the IDL file.
-   Each **import** keyword can be associated with more than one file name.
-   Separate multiple file names with commas.
-   You must enclose the file name within quotation marks and end the import statement with a semicolon (;).
-   You can import an interface that has no attributes into another IDL file. However, the interface must contain only datatypes; it cannot contain any procedures. If even one procedure is contained in the imported interface, you must specify a [**local**](local.md) or [**UUID**](uuid.md) attribute.
-   The **import** function is idempotentÂ â€”Â that is, importing an interface more than once has no additional effect.

> [!Note]  
> The behavior of the **import** directive is independent of the MIDL compiler mode switches [**/ms\_ext**](-ms-ext.md) (the default), [**/osf**](-osf.md), and [**/app\_config**](-app-config.md). However, the compiler mode (**/osf** or **/ms\_ext**) can affect pointer attribute decoration on imported types. For details see [Pointer-Attribute Type Inheritance](/windows/desktop/Rpc/pointer-attribute-type-inheritance).

 

## Examples

``` syntax
import "myoldodl.odl";  
import "unknwn.idl";
import "part1.idl", "part2.idl", "part3.idl"; 
```

## See also

<dl> <dt>

[**/app\_config**](-app-config.md)
</dt> <dt>

[Interface Definition (IDL) File](interface-definition-idl-file.md)
</dt> <dt>

[**importlib**](importlib.md)
</dt> <dt>

[**include**](include.md)
</dt> <dt>

[Importing System Header Files](importing-system-header-files.md)
</dt> <dt>

[Importing Files and Type Libraries](importing-files-and-type-libraries.md)
</dt> <dt>

[**/ms\_ext**](-ms-ext.md)
</dt> <dt>

[**/osf**](-osf.md)
</dt> </dl>

 

 