---
title: cpp_quote attribute
description: The cpp\_quote keyword instructs MIDL to emit the specified string, without the quote characters, into the generated header file.
ms.assetid: 0e5a929e-b564-43f7-9270-e79486279834
keywords:
- cpp_quote attribute MIDL
topic_type:
- apiref
api_name:
- cpp_quote
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# cpp\_quote attribute

The **cpp\_quote** keyword instructs MIDL to emit the specified string, without the quote characters, into the generated header file.

``` syntax
cpp_quote("string")
```

## Parameters

<dl> <dt>

*string* 
</dt> <dd>

Specifies a quoted string that is emitted in the generated header file. The string must be quoted to prevent expansion by the C preprocessor.

</dd> </dl>

## Remarks

C-language preprocessing directives that appear in the IDL file are processed by the C compiler's preprocessor. The **\#define** directives in the IDL file are available during MIDL compilation but are not available to the C compiler.

For example, when the preprocessor encounters the directive "\#define WINDOWS 4", the preprocessor replaces all occurrences of "WINDOWS" in the IDL file with "4". The symbol "WINDOWS" is not available during C-language compilation.

To allow the C-preprocessor macro definitions to pass through the MIDL compiler to the C compiler, use the **\#pragma midl\_echo** or **cpp\_quote** directive. These directives instruct the MIDL compiler to generate a header file that contains the parameter string with the quotation marks removed. The **\#pragma midl\_echo** and **cpp\_quote** directives are equivalent.

The MIDL compiler places the strings specified in the **cpp\_quote** and [**pragma**](pragma.md) directives into the header file in the sequence in which they are specified in the IDL file, and relative to other interface components in the IDL file. The strings should usually appear in the IDL file interface body section after all [**import**](import.md) operations.

## Examples

``` syntax
cpp_quote("#include \"myfile.h\" ")  
cpp_quote("#define UNICODE")
```

## See also

<dl> <dt>

[Interface Definition (IDL) File](interface-definition-idl-file.md)
</dt> <dt>

[**import**](import.md)
</dt> <dt>

[**pragma**](pragma.md)
</dt> </dl>

 

 




