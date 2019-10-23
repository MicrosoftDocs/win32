---
title: /char switch
description: The /char switch helps to ensure that the MIDL compiler and C compiler operate together correctly for all char and small types.
ms.assetid: 83f204cf-9cd0-42f3-bce7-b8f582e50e67
keywords:
- /char switch MIDL
topic_type:
- apiref
api_name:
- /char
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# /char switch

The **/char** switch helps to ensure that the MIDL compiler and C compiler operate together correctly for all [**char**](char-idl.md) and [**small**](small.md) types.

``` syntax
midl /char { signed | unsigned | ascii7 }
```

## Switch Options

<dl> <dt>

 
</dt> <dd>

<dt>

<span id="signed"></span><span id="SIGNED"></span>

<span id="signed"></span><span id="SIGNED"></span>****signed****


</dt> <dd>

Specifies that the default C-compiler type for [**char**](char-idl.md) is signed. All occurrences of **char** not accompanied by a sign specification are generated as unsigned char.

</dd> <dt>

<span id="unsigned"></span><span id="UNSIGNED"></span>

<span id="unsigned"></span><span id="UNSIGNED"></span>****unsigned****


</dt> <dd>

Specifies that the default C-compiler type for [**char**](char-idl.md) is unsigned. All uses of [**small**](small.md) not accompanied by a sign specification are generated as signed small.

</dd> <dt>

<span id="ascii7"></span><span id="ASCII7"></span>

<span id="ascii7"></span><span id="ASCII7"></span>****ascii7****


</dt> <dd>

Specifies that all [**char**](char-idl.md) values are to be passed into the generated files without a specific sign keyword. All uses of [**small**](small.md) not accompanied by a sign specification are generated as **small**.

</dd> </dl> </dd> </dl>

## Remarks

By definition, MIDL [**char**](char-idl.md) is unsigned. "Small" is defined in terms of **char** (\#define small char), and MIDL [**small**](small.md) is signed.

The **/char** switch directs the MIDL compiler to specify explicit [**signed**](signed.md) or [**unsigned**](unsigned.md) declarations in the generated files when the C-compiler sign declaration conflicts with the MIDL default for that type.

Remember that the MIDL compiler generates the stubs as C source code, which you must compile as part of your client and server programs. Some compilers use a **signed char** everywhere [**char**](char-idl.md) data is specified in the source code. The stub source code that the MIDL compiler generates treats all **char** data as **unsigned char**. If the MIDL compiler simply generated all **char** data in the IDL file as **char** data in the stubs, compilers that use a **signed char** for **char** data would cause a conflict in the stub source code.

The purpose of the **/char** command line switch is to resolve these potential conflicts. It preserves all data specified as [**char**](char-idl.md) in the IDL file as **unsigned char** in the stub source code. It also maintains [**small**](small.md) data as signed.

The following table summarizes the generated types.



| midl /char option       | Generated char type | Generated small type |
|-------------------------|---------------------|----------------------|
| **midl /char signed**   | **unsigned char**   | **small**            |
| **midl /char unsigned** | **char**            | **signed small**     |
| **midl /char ascii7**   | **char**            | **small**            |



 

The **/char** signed option indicates that the C-compiler char and small types are signed. To match the MIDL default for **char**, the MIDL compiler must convert all uses of **char** not accompanied by a sign specification to **unsigned char**. The [**small**](small.md) type is not modified because this C-compiler default matches the MIDL default for **small**.

The **/char** unsigned option indicates that the C-compiler [**char**](char-idl.md) type is unsigned. The MIDL compiler converts all uses of [**small**](small.md) not accompanied by a sign specification to **signed** **small**.

The ascii7 option indicates that no explicit sign specification is added to [**char**](char-idl.md) types. The type [**small**](small.md) is generated as **small**.

To avoid confusion, you should use explicit sign specifications for [**char**](char-idl.md) and small types whenever possible in the IDL file. Note that the use of explicitly signed **char** types in your IDL file is not supported by DCE IDL. Therefore, this feature is not available when you compile with the MIDL [**/osf**](-osf.md) switch.

For more information related to **/char**, see [**small**](small.md).

## Examples

**midl /char signed filename.idl**

**midl /char unsigned filename.idl**

**midl /char ascii7 filename.idl**

## See also

<dl> <dt>

[**char**](char-idl.md)
</dt> <dt>

[General MIDL Command-line Syntax](general-midl-command-line-syntax.md)
</dt> <dt>

[**/osf**](-osf.md)
</dt> <dt>

[**small**](small.md)
</dt> </dl>

 

 




