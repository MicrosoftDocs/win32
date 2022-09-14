---
title: RCDATA resource
description: Defines a raw data resource for an application. Raw data resources permit the inclusion of binary data directly in the executable file.
ms.assetid: 7535cb06-858b-4726-aaa5-43519f84d0e4
keywords:
- RCDATA resource Menus and Other Resources
topic_type:
- apiref
api_name:
- RCDATA
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# RCDATA resource

Defines a raw data resource for an application. Raw data resources permit the inclusion of binary data directly in the executable file.

``` syntax
nameID RCDATA  [optional-statements] {raw-data  ...}
```

## Parameters

<dl> <dt>

<span id="nameID"></span><span id="nameid"></span><span id="NAMEID"></span>*nameID*
</dt> <dd>

Unique name or a 16-bit unsigned integer value that identifies the resource.

</dd> <dt>

<span id="optional-statements"></span><span id="OPTIONAL-STATEMENTS"></span>*optional-statements*
</dt> <dd>

This parameter can be zero or more of the following statements.



| Statement                                                        | Description                                                                                                                                                                             |
|------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CHARACTERISTICS**](characteristics-statement.md) *dword*     | User-defined information about a resource that can be used by tools that read and write resource files. For more information, see [**CHARACTERISTICS**](characteristics-statement.md). |
| [**LANGUAGE**](language-statement.md) *language*, *sublanguage* | Language for the resource. For more information, see [**LANGUAGE**](language-statement.md).                                                                                            |
| [**VERSION**](version-statement.md) *dword*                     | User-defined version number for the resource that can be used by tools that read and write resource files. For more information, see [**VERSION**](version-statement.md).              |



 

</dd> <dt>

<span id="raw-data"></span><span id="RAW-DATA"></span>*raw-data*
</dt> <dd>

Raw data consisting of one or more integers or strings of characters. Integers can be specified in decimal, octal, or hexadecimal format. To be compatible with 16-bit Windows, integers are stored as **WORD** values. You can store an integer as a **DWORD** value by qualifying the integer with the "L" suffix.

Strings are enclosed in quotation marks. RC does not automatically append a terminating null character to a string. Each string is a sequence of the specified ANSI characters, unless you qualify it as a wide-character string with the L prefix.

The block of data begins on a **DWORD** boundary and RC performs no padding or alignment of data within the *raw-data* block. It is your responsibility to ensure the proper alignment of data within the block.

</dd> </dl>

Certain attributes are also supported for backward compatibility. For more information, see [Common Resource Attributes](common-resource-attributes.md).

## Examples

The following example demonstrates the use of the **RCDATA** statement:

``` syntax
resname RCDATA
{
   "Here is an ANSI string\0",    // explicitly null-terminated 
   L"Here is a Unicode string\0", // explicitly null-terminated 
   1024,                          // integer, stored as WORD 
   7L,                            // integer, stored as DWORD 
   0x029a,                        // hex integer 
   0o733,                         // octal integer 
}
```

## See also

<dl> <dt>

[**ACCELERATORS**](accelerators-resource.md)
</dt> <dt>

[**CHARACTERISTICS**](characteristics-statement.md)
</dt> <dt>

[**LANGUAGE**](language-statement.md)
</dt> <dt>

[**MENU**](menu-resource.md)
</dt> <dt>

[**STRINGTABLE**](stringtable-resource.md)
</dt> <dt>

[**VERSION**](version-statement.md)
</dt> </dl>

 

 




