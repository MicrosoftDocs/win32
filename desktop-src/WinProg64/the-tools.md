---
title: The Tools
description: This topic describes the tools available for you to use in making your application 64-bit ready. Windows 10 is available for both x64 and ARM64 based processors.
ms.assetid: 457b7cc1-8517-4a36-9a0c-cf191ff3b374
keywords:
- 64-bit Windows programming guide 64-bit Windows Programming , tools
- tools 64-bit Windows Programming
ms.topic: article
ms.date: 05/31/2018
---

# The Tools

This topic describes the tools available for you to use in making your application 64-bit ready. Windows 10 is available for both x64 and ARM64 based processors.

## Include Files

The API elements are virtually identical between 32- and 64-bit Windows. The Windows header files have been modified so that they can be used for both 32- and 64-bit code. The new 64-bit types and macros are defined in a new header file, Basetsd.h, which is in the set of header files included by Windows.h. Basetsd.h includes the new data-type definitions to assist in making source code word-size independent.

## New Data Types

The Windows header files contain new data types. These types are primarily for type compatibility with the 32-bit data types. The new types provide exactly the same typing as the existing types, while at the same time providing support for the 64-bit Windows. For more information, see [The New Data Types](the-new-data-types.md) or the Basetsd.h header file.

## Predefined Macros

The compiler defines the following macros to identify the platform.



| Macro   | Meaning                                                                                                     |
|---------|-------------------------------------------------------------------------------------------------------------|
| \_WIN64 | A 64-bit platform. This includes both x64 and ARM64.                                                        |
| \_WIN32 | A 32-bit platform. This value is also defined by the 64-bit compiler for backward compatibility.<br/> |
| \_WIN16 | A 16-bit platform                                                                                           |



 

The following macros are specific to the architecture.



| Macro      | Meaning                |
|------------|------------------------|
| \_M\_IA64  | Intel Itanium platform |
| \_M\_IX86  | x86 platform           |
| \_M\_X64   | x64 platform           |
| \_M\_ARM64 | ARM64 platform         |



 

Do not use these macros except with architecture-specific code, instead, use \_WIN64, \_WIN32, and \_WIN16 whenever possible.

## Helper Functions

The following inline functions (defined in Basetsd.h) can help you safely convert values from one type to another.

``` syntax
void            * Handle64ToHandle( const void * POINTER_64 h ) 
void * POINTER_64 HandleToHandle64( const void *h )
long              HandleToLong(     const void *h )
unsigned long     HandleToUlong(    const void *h )
void            * IntToPtr(         const int i )
void            * LongToHandle(     const long h )
void            * LongToPtr(        const long l )
void            * Ptr64ToPtr(       const void * POINTER_64 p )
int               PtrToInt(         const void *p )
long              PtrToLong(        const void *p )
void * POINTER_64 PtrToPtr64(       const void *p )
short             PtrToShort(       const void *p )
unsigned int      PtrToUint(        const void *p )
unsigned long     PtrToUlong(       const void *p )
unsigned short    PtrToUshort(      const void *p )
void            * UIntToPtr(        const unsigned int ui )
void            * ULongToPtr(       const unsigned long ul )
```

> [!WARNING]
> **IntToPtr** sign-extends the **int** value, **UIntToPtr** zero-extends the **unsigned int** value, **LongToPtr** sign-extends the **long** value, and **ULongToPtr** zero-extends the **unsigned long** value.

 

## 64-bit Compiler

The 64-bit compilers can be used to identify pointer truncation, improper type casts, and other 64-bit-specific problems.

When the compiler is first run, it will probably generate many pointer truncation or type mismatch warnings, such as the following:

`warning C4311: 'type cast' : pointer truncation from 'unsigned char *' to 'unsigned long '`

Use these warnings as a guide to make the code more robust. It is good practice to eliminate all warnings, especially pointer-truncation warnings.

## 64-bit Compiler Switches and Warnings

Note that this compiler enables the LLP64 data model.

There is a warning option to assist porting to LLP64. The -Wp64 -W3 switch enables the following warnings:

-   C4305: Truncation warning. For example, "return": truncation from "unsigned int64" to "long."
-   C4311: Truncation warning. For example, "type cast": pointer truncation from "int\*\_ptr64" to "int."
-   C4312: Conversion to bigger-size warning. For example, "type cast": conversion from "int" to "int\*\_ptr64" of greater size.
-   C4318: Passing zero length. For example, passing constant zero as the length to the **memset** function.
-   C4319: Not operator. For example, "~": zero extending "unsigned long" to "unsigned \_int64" of greater size.
-   C4313: Calling the **printf** family of functions with conflicting conversion type specifiers and arguments. For example, "printf": "%p" in format string conflicts with argument 2 of type "\_int64." Another example is the call printf("%x", pointer\_value); this causes a truncation of the upper 32 bits. The correct call is printf("%p", pointer\_value).
-   C4244: Same as the existing warning C4242. For example, "return": conversion from "\_int64" to "unsigned int," possible loss of data.

## 64-bit Linker and Libraries

To build applications, use the linker and libraries provided by the Windows SDK. Most 32-bit libraries have a corresponding 64-bit version, but certain legacy libraries are available only in 32-bit versions. Code that calls into these libraries will not link when the application is built for 64-bit Windows.

 

 





