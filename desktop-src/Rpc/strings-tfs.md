---
title: Strings (RPC)
description: Three strings types and Remote Procedure Call (RPC).
ms.assetid: 186cabeb-ea3f-4213-ba71-53afe91e6e14
ms.topic: article
ms.date: 05/31/2018
---

# Strings (RPC)

There are three strings types denoted by the following ending sub-strings in the format character.



| Type                  | Substring |
|-----------------------|-----------|
| Character string      | CSTRING   |
| Wide character string | WSTRING   |
| String-able structure | SSTRING   |



 

### Nonconformant Strings

An example of nonconformant string is a **\[string\]** on a fixed-size array.

``` syntax
FC_CSTRING | FC _WSTRING 
FC_PAD 
string_size<2>
```

### Conformant Strings

``` syntax
FC_C_CSTRING | FC_C_WSTRING
FC_PAD 
```

–or–

``` syntax
FC_C_CSTRING | FC_C_WSTRING 
FC_STRING_SIZED 
conformance_description<> 
```

The first format describes common strings, like a **\[string\]** char \* argument. A sized conformant string has the latter description.

The conformance\_description<> is a correlation descriptor and has 4 or 6 bytes depending on whether [**/robust**](/windows/desktop/Midl/-robust) is used.

### Structure Strings

The following is a nonconformant string-able structure:

``` syntax
FC_SSTRING 
element_size<1> 
number_of_elements<2>
```

Conformant string-able structure:

``` syntax
FC_C_SSTRING 
element_size<1>
```

–or –

``` syntax
FC_C_SSTRING 
elements_size<1> 
FC_STRING_SIZED FC_PAD 
conformance_description<>
```

The latter description is for a sized string-able structure.

 

 