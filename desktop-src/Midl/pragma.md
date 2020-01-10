---
title: pragma attribute
description: The \ pragma midl\_echo directive instructs MIDL to emit the specified string, without the quotation characters, into the generated header file.
ms.assetid: b8a175d2-ea07-4103-ab45-0de7e477d27a
keywords:
- pragma attribute MIDL
topic_type:
- apiref
api_name:
- pragma
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# pragma attribute

The \#**pragma midl\_echo** directive instructs MIDL to emit the specified string, without the quotation characters, into the generated header file.

``` syntax
#pragma midl_echo("string")
#pragma token-sequence
#pragma pack (n)
#pragma pack ( [push] [, id] [, n} )
#pragma pack ( [pop] [, id] [, n} )
```

## Parameters

<dl> <dt>

*string* 
</dt> <dd>

Specifies a string that is inserted into the generated header file. The quotation marks are removed during the insertion process.

</dd> <dt>

*token-sequence* 
</dt> <dd>

Specifies a sequence of tokens that are inserted into the generated header file as part of a **\#pragma** directive without processing by the MIDL compiler.

</dd> <dt>

*n* 
</dt> <dd>

Specifies the current pack size. Valid values are 1, 2, 4, 8, and 16.

</dd> <dt>

*id* 
</dt> <dd>

Specifies the user identifier.

</dd> </dl>

## Remarks

C-language preprocessing directives that appear in the IDL file are processed by the C compiler's preprocessor. The **\#define** directives in the IDL file are available during MIDL compilation, although not to the C compiler.

For example, when the preprocessor encounters the directive "\#define WINDOWS 4", the preprocessor replaces all occurrences of "WINDOWS" in the IDL file with "4". The symbol "WINDOWS" is not available at C-compile time.

To allow the C-preprocessor macro definitions to pass through the MIDL compiler to the C compiler, use the **\#pragma midl\_echo** or [**cpp\_quote**](cpp-quote.md) directive. These directives instruct the MIDL compiler to generate a header file that contains the parameter string with the quotation marks removed. The **\#pragma midl\_echo** and **cpp\_quote** directives are equivalent.

The **\#pragma pack** directive is used by the MIDL compiler to control the packing of structures. It overrides the [**/Zp**](-zp.md) command-line switch. The pack (*n*) option sets the current pack size to a specific value: 1, 2, 4, 8, or 16. The pack (push) and pack (pop) options have the following characteristics:

-   The compiler maintains a packing stack. The elements of the packing stack include a pack size and an optional *id*. The stack is limited only by available memory with the current pack size at the top of the stack.
-   Pack (push) results in the current pack size pushed onto the packing stack. The stack is limited by available memory.
-   Pack (push,*n*) is the same as pack (push) followed by pack (*n*).
-   Pack (push, *id*) also pushes *id* onto the packing stack along with the pack size.
-   Pack (push, *id*, *n*) is the same as pack (push, *id*) followed by pack (*n*).
-   Pack (pop) results in popping the packing stack. Unbalanced pops cause warnings and set the current pack size to the command-line value.
-   If pack (pop, *id*, *n*) is specified, then *n* is ignored.

The MIDL compiler places the strings specified in the [**\\cpp\_quote**](cpp-quote.md) and **pragma** directives in the header file in the sequence in which they are specified in the IDL file and relative to other interface components in the IDL file. The strings should usually appear in the interface-body section of the IDL file after all [**import**](import.md) operations.

The MIDL compiler does not attempt to process **\#pragma** directives that do not start with the prefix "midl\_." Other **\#pragma** directives in the IDL file are passed into the generated header file without changes.

## Examples

``` syntax
/* IDL file */ 
#pragma midl_echo("#define UNICODE") 
cpp_quote("#define __DELAYED_PREPROCESSING__ 1") 
#pragma hdrstop 
#pragma check_pointer(on) 
 
/* generated header file */ 
#define UNICODE 
#define __DELAYED_PREPROCESSING__ 1 
#pragma hdrstop 
#pragma check_pointer(on)
```

## See also

<dl> <dt>

[**cpp\_quote**](cpp-quote.md)
</dt> <dt>

[Interface Definition (IDL) File](interface-definition-idl-file.md)
</dt> <dt>

[**import**](import.md)
</dt> <dt>

[**/Zp**](-zp.md)
</dt> </dl>

 

 




