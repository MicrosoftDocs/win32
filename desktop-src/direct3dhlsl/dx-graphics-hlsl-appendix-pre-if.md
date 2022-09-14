---
title: ' if,  elif,  else, and  endif Directives'
description: Preprocessor directives that control compilation of portions of a source file.
ms.assetid: f29e5a9b-cc0c-4fca-aac7-809a226eda58
keywords:
- if, elif, else, and endif Directives HLSL
topic_type:
- apiref
api_name:
- if, elif, else, and endif Directives
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# \#if, \#elif, \#else, and \#endif Directives

Preprocessor directives that control compilation of portions of a source file.



| \#if *ifCondition* ...         |
|--------------------------------|
| \[\#elif *elifCondition* ...\] |
| \[\#else ...\]                 |
| \#endif                        |



 

## Parameters



| Item                                                                                                                                                                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="ifCondition"></span><span id="ifcondition"></span><span id="IFCONDITION"></span>*ifCondition*<br/>                                                                                   | Primary condition to evaluate. If this parameter evaluates to a nonzero value, all text between this \#if directive and the next instance of the \#elif, \#else, or \#endif directive is retained in the translation unit; otherwise, the subsequent source code is not retained. <br/> The condition can use the preprocessor operator defined to determine whether a specific preprocessor constant or macro is defined; this usage is equivalent to the use of the [\#ifdef](dx-graphics-hlsl-appendix-pre-ifdef.md) directive. <br/> See the Remarks section for restrictions on the value of the *ifCondition* parameter. <br/>                                                                                        |
| <span id="elifCondition__optional__________"></span><span id="elifcondition__optional__________"></span><span id="ELIFCONDITION__OPTIONAL__________"></span>*elifCondition* \[optional\] <br/> | Other condition to evaluate. If the *ifCondition* parameter and all previous \#elif directives evaluate to zero, and this parameter evaluates to a nonzero value, all text between this \#elif directive and the next instance of the \#elif, \#else, or \#endif directive is retained in the translation unit; otherwise, the subsequent source code is not retained. <br/> The condition can use the preprocessor operator defined to determine whether a specific preprocessor constant or macro is defined; this usage is equivalent to the use of the [\#ifdef](dx-graphics-hlsl-appendix-pre-ifdef.md) directive. <br/> See the Remarks section for restrictions on the value of the *elifCondition* parameter. <br/> |



 

## Remarks

Each \#if directive in a source file must be matched by a closing \#endif directive. Any number of \#elif directives can appear between the \#if and \#endif directives, but at most one \#else directive is allowed. The \#else directive, if present, must be the last directive before \#endif. Conditional-compilation directives contained in include files must satisfy the same conditions.

The \#if, \#elif, \#else, and \#endif directives can nest in the text portions of other \#if directives. Each nested \#else, \#elif, or \#endif directive belongs to the closest preceding \#if directive.

If no conditions evaluate to a nonzero value, the preprocessor selects the text block after the \#else directive. If the \#else clause is omitted and no conditions evaluate to a nonzero value, no text block is selected.

The *ifCondition* and *elifCondition* parameters much meet the following requirements:

-   Conditional compilation expressions are treated as [**signed long**](https://msdn.microsoft.com/library/cc953fe1(v=VS.71).aspx) values, and these expressions are evaluated using the same rules as expressions in C++.
-   Expressions must have integral type and can include only integer constants, character constants, and the defined operator.
-   Expressions cannot use **sizeof** or a type-cast operator.
-   The target environment may not be able to represent all ranges of integers.
-   The translation represents type [**int**](/windows/desktop/WinProg/windows-data-types) the same as type **long**, and [**unsigned int**](https://msdn.microsoft.com/library/cc953fe1(v=VS.71).aspx) the same as **unsigned long**.
-   The translator can translate character constants to a set of code values different from the set for the target environment. To determine the properties of the target environment, check values of macros from LIMITS.H in an application built for the target environment.
-   The expression must not perform any environmental inquiries and must remain insulated from implementation details on the target computer.

## Examples

This section contains examples that demonstrate how to use conditional compilation preprocessor directives.

### Use of the defined operator

The following example shows the use of the defined operator. If the identifier CREDIT is defined, the call to the **credit** function is compiled. If the identifier DEBIT is defined, the call to the **debit** function is compiled. If neither identifier is defined, the call to the **printerror** function is compiled. Note that "CREDIT" and "credit" are distinct identifiers in C and C++ because their cases are different.


```
#if defined(CREDIT)
    credit();
#elif defined(DEBIT)
    debit();
#else
    printerror();
#endif
```



### Use of nested \#if directives

The following example shows how to nest \#if directives. This example assumes that a symbolic constant named DLEVEL has been previously defined. The \#elif and \#else directives are used to make one of four choices, based on the value of DLEVEL. The constant STACK is set to 0, 100, or 200, depending on the definition of DLEVEL. If DLEVEL is greater than 5, then STACK is not defined.


```
#if DLEVEL > 5
    #define SIGNAL  1
    #if STACKUSE == 1
        #define STACK   200
    #else
        #define STACK   100
    #endif
#else
    #define SIGNAL  0
    #if STACKUSE == 1
        #define STACK   100
    #else
        #define STACK   50
    #endif
#endif
#if DLEVEL == 0
    #define STACK 0
#elif DLEVEL == 1
    #define STACK 100
#elif DLEVEL > 5
    display( debugptr );
#else
    #define STACK 200
#endif
```



### Use for including header files

A common use for conditional compilation is to prevent multiple inclusions of the same header file. In C++, where classes are often defined in header files, conditional compilation constructs can be used to prevent multiple definitions. The following example determines whether the symbolic constant EXAMPLE\_H is defined. If so, the file has already been included and does not need to be reprocessed; if not, the constant EXAMPLE\_H is defined to indicate that EXAMPLE.H has already been processed.


```
#if !defined( EXAMPLE_H )
#define EXAMPLE_H

class Example
{
...
};

#endif // !defined( EXAMPLE_H )
```



## See also

<dl> <dt>

[Preprocessor Directives (DirectX HLSL)](dx-graphics-hlsl-appendix-preprocessor.md)
</dt> </dl>

 

