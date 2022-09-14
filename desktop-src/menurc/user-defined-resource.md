---
title: User-Defined Resource
description: A user-defined resource-definition statement defines a resource that contains application-specific data.
ms.assetid: b1cfec71-5733-4900-97f6-c1cbb350c728
keywords:
- user-defined resource
ms.topic: article
ms.date: 05/31/2018
---

# User-Defined Resource

A user-defined resource-definition statement defines a resource that contains application-specific data. The data can have any format and can be defined either as the content of a given file (if the *filename* parameter is given) or as a series of numbers and strings (if the *raw-data* block is specified).

``` syntax
nameID typeID filename
```

The *filename* specifies the name of a file containing the binary data of the resource. The contents of the file are included as the resource. RC does not interpret the binary data in any way. It is the programmer's responsibility to ensure that the data is properly aligned for the target computer architecture.

A user-defined resource can also be defined completely in the resource script using the following syntax:

``` syntax
nameID typeID  {  raw-data  }
```

## Parameters

<dl> <dt>

<span id="nameID"></span><span id="nameid"></span><span id="NAMEID"></span>*nameID*
</dt> <dd>

Unique name or a 16-bit unsigned integer that identifies the resource.

</dd> <dt>

<span id="typeID"></span><span id="typeid"></span><span id="TYPEID"></span>*typeID*
</dt> <dd>

Unique name or a 16-bit unsigned integer that identifies the resource type. If a number is given, it must be greater than 255. The numbers 1 through 255 are reserved for existing and future redefined resource types.

</dd> <dt>

<span id="filename"></span><span id="FILENAME"></span>*filename*
</dt> <dd>

Name of the file that contains the resource data. The parameter must be a valid file name; it must be a full path if the file is not in the current working directory.

</dd> <dt>

<span id="raw-data"></span><span id="RAW-DATA"></span>*raw-data*
</dt> <dd>

Raw data consisting of one or more integers or strings of characters. Integers can be specified in decimal, octal, or hexadecimal format. To be compatible with 16-bit Windows, integers are stored as WORD values. You can store an integer as a DWORD value by qualifying the integer with the "L" suffix.

Strings are enclosed in quotation marks. RC does not automatically append a terminating null character to a string. Each string is a sequence of the specified ANSI characters, unless you qualify it as a wide-character string with the "L" prefix.

The block of data begins on a **DWORD** boundary and RC performs no padding or alignment of data within the *raw-data* block. It is the programmer's responsibility to ensure the proper alignment of data within the block.

</dd> </dl>

## Example

The following example shows several user-defined statements:

``` syntax
array   MYRES   data.res
14      300     custom.res
18 MYRES2
{
   "Here is an ANSI string\0",    // explicitly null-terminated 
   L"Here is a Unicode string\0", // explicitly null-terminated 
   1024,                          // integer, stored as WORD 
   7L,                            // integer, stored as DWORD 
   0x029a,                        // hex integer 
   0o733,                         // octal integer 
}
```

 

 




