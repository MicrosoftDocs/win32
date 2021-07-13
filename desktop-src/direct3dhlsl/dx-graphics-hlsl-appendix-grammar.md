---
title: Grammar
description: HLSL statements are constructed using the following rules for grammar.
ms.assetid: 683248e9-6fc7-451a-906b-6e0aab1b0c8c
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# Grammar

HLSL statements are constructed using the following rules for grammar.

-   [Whitespace](#whitespace)
-   [Floating point numbers](#floating-point-numbers)
-   [Integer numbers](#integer-numbers)
-   [Characters](#characters)
-   [Strings](#strings)
-   [Identifiers](#identifiers)
-   [Operators](#operators)
-   [Related topics](#related-topics)

## Whitespace

The following characters are recognized as white space.

- SPACE
- TAB
- EOL
- C style comments (/\* \*/)
- C++ style comments (//)

## Floating point numbers

Floating point numbers are represented in HLSL as follows:

-   fractional-constant exponent-part(opt) floating-suffix(opt)

    digit-sequence exponent-part floating-suffix(opt)

-   fractional-constant :

    digit-sequence(opt) . digit-sequence

    digit-sequence .

-   exponent-part :

    e sign(opt) digit-sequence

    E sign(opt) digit-sequence

-   sign : one of

    \+ -

-   digit-sequence :

    digit

    digit-sequence digit

-   floating-suffix : one of

    h H f F l L

    Use the “L” suffix to specify a full 64-bit precision floating-point literal. A 32-bit float literal is the default.

    For example, the compiler recognizes the following literal value as a 32-bit precision floating-point literal and ignores the lower bits:

    ```
    double x = -0.6473313946860445;
    ```

    

    The compiler recognizes the following literal value as a 64-bit precision floating-point literal:

    ```
    double x = -0.6473313946860445L;
    ```

    

## Integer numbers

Integer numbers are represented in HLSL as follows:

-   integer-constant integer-suffix(opt)
-   integer-constant: one of

    \# (decimal number)

    0\# (octal number)

    0x\# (hex number)

-   integer-suffix can be any one of these:

    u U l L

## Characters

Characters are represented in HLSL as follows:



| Character                                          | Description                                                                |
|-------------------------------------------|-----------------------------------------------------------------|
| 'c'                                       | (character)                                                     |
| '\\a' '\\b' '\\f' '\\b' '\\r' '\\t' '\\v' | (escapes)                                                       |
| '\\\#\#\#'                                | (octal escape, each \# is an octal digit)                       |
| '\\x\#'                                   | (hex escape, \# is hex number, any number of digits)            |
| '\\c'                                     | (c is other character, including backslash and quotation marks) |



 

Escapes are not supported in preprocessor expressions.

## Strings

Strings are represented in HLSL as follows:

"s" (s is any string with escapes).

## Identifiers

Identifiers are represented in HLSL as follows:


```
    [A-Za-z_][A-Za-z0-9_]*
```



## Operators


```
##, #@, ++, --, &, &, &, ||, ==, ::, <<, <<=, >>, >>=, ..., 
<=, >=, !=, *=, /=, +=, -=, %=, &=, |=, ^=, ->
```



Also any other single character that did not match another rule.

## Related topics

<dl> <dt>

[Appendix (DirectX HLSL)](dx-graphics-hlsl-appendix.md)
</dt> </dl>

 

 




