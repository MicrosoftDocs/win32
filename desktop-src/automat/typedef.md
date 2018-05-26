---
title: typedef macro
description: This statement creates an alias for a type.
ms.assetid: 355001fb-ed63-49e6-9d72-0d56a5b558b4
keywords:
- typedef macro Automation
topic_type:
- apiref
api_name:
- coclass
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# typedef macro

This statement creates an alias for a type.

## Syntax


```C++
 coclass(
    attributes,
    basetype,
    aliasname
);
```



## Parameters

<dl> <dt>

**attributes** 
</dt> <dd>

Any attribute specifications must follow the typedef keyword. If no attributes and no other type (for example, enum, struct, or union) are specified, the alias is treated as a \#define and does not appear in the type library. If no other attribute is desired, public can be used to explicitly include the alias in the type library. The helpstring, helpcontext, and uuidattributes are accepted before a typedef. For more information, see Attribute Descriptions. If uuid is omitted, the typedef is not uniquely specified in the system.

</dd> <dt>

**basetype** 
</dt> <dd>

The type for which the alias is defined.

</dd> <dt>

**aliasname** 
</dt> <dd>

The name by which the type will be known in the type library.

</dd> </dl>

## Remarks

``` syntax
typedef [attributes] basetype aliasname;
```

The typedef keyword must also be used whenever a struct or enum is defined. The name recorded for the enum or struct is the typedef name, and not the tag for the enumeration. No attributes are required to make sure the alias appears in the type library.

Enumerations, structures, and unions must be defined with the typedef keyword. The attributes for a type defined with typedef are enclosed in brackets following the typedef keyword. If a simple alias typedef has no attributes, it is treated like a \#define, and the aliasname does not appear in the library. Any attribute (public can be used if no others are desired) specified between the typedef keyword and the rest of a simple alias definition causes the alias to appear explicitly in the type library. The attributes typically include such items as a Help string and Help context.

### Examples

This example creates a type description for an alias type with the name DWORD.


```C++
typedef [public]  long DWORD;
```



The second example creates a type description for an enumeration named OBJTYPE, which has four enumerator values.


```C++
typedef enum {
      TYPE_FUNCTION = 0,
      TYPE_PROPERTY = 1,
      TYPE_CONSTANT = 2,
      TYPE_PARAMETER = 3
   } OBJTYPE;
```



 

 




