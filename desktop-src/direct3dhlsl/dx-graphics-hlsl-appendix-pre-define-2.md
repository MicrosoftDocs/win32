---
title: \#define directive (macro)
description: Preprocessor directive that creates a function-like macro.
ms.assetid: 73c19cf8-fbc5-444b-a51f-dc9f881f397b
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# \#define directive (macro)

Preprocessor directive that creates a function-like macro.



| \#define *identifier*( *argument0*, ... , *argumentN-1* ) *token-string* |
|--------------------------------------------------------------------------|



 

## Parameters



| Item                                                                                                                                                                                                                                                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="identifier"></span><span id="IDENTIFIER"></span>*identifier*<br/>                                                                                                                                                                             | Identifier of the macro. <br/> A second [\#define](dx-graphics-hlsl-appendix-pre-define.md) for a macro with an identifier that already exists in the current context generates an error unless the second token sequence is identical to the first. <br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| <span id="___________argument0___...___argumentN-1_________"></span><span id="___________argument0___...___argumentn-1_________"></span><span id="___________ARGUMENT0___...___ARGUMENTN-1_________"></span> ( *argument0*, ... , *argumentN-1* ) <br/> | List of arguments to the macro. The argument list is comma-delimited, can be of any length, and must be enclosed in parentheses. Each argument name in the list must be unique. No white space can separate the *identifier* parameter and the opening parenthesis. <br/> Use line concatenation place a backslash (\\) immediately before the newline character to split long directives onto multiple source lines. <br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| <span id="token-string__optional________"></span><span id="TOKEN-STRING__OPTIONAL________"></span>*token-string* \[optional\] <br/>                                                                                                                     | Value of the macro. This parameter consists of a series of tokens, such as keywords, constants, or complete statements. One or more white-space characters must separate this parameter from the *identifier* parameter; this white space is not considered part of the substituted text, nor is any white space following the last token of the text. Make liberal use of parentheses to ensure that complicated arguments are interpreted correctly. <br/> If the value of the *identifier* parameter occurs within the *token-string* parameter (even as a result of another macro expansion), it is not expanded. <br/> If you exclude this parameter, all instances of the *identifier* parameter are removed from the source file. The identifier remains defined, and can be tested using the [\#if defined](dx-graphics-hlsl-appendix-pre-ifdef.md), \#ifdef, and \#ifndef directives. <br/> |



 

## Remarks

All instances of the *identifier* parameter that occur after the [\#define](dx-graphics-hlsl-appendix-pre-define.md) directive in the source file constitute a macro call, and the identifier will be replaced by a version of the *token-string* parameter that has actual arguments substituted for formal parameters. The number of parameters in the call must match the number of parameters in the macro definition. The identifier is replaced only when it forms a token; for example, the identifier is not replaced if it appears in a comment, within a string, or as part of a longer identifier.

The [\#undef](dx-graphics-hlsl-appendix-pre-undef.md) directive instructs the preprocessor to forget the definition of an identifier; for more information, see \#undef Directive (DirectX HLSL).

Defining constants with the /D compiler option has the same effect as using the [\#define](dx-graphics-hlsl-appendix-pre-define.md) directive at the beginning of your file. Up to 30 macros can be defined with the /D option.

The actual arguments in the macro call are matched to the corresponding formal arguments in the macro definition. Each formal argument in the token string is replaced by the corresponding actual argument, unless the argument is preceded by a stringizing (\#), charizing (\#@), or token-pasting (\#\#) operator, or is followed by a \#\# operator. Any macros in the actual argument are expanded before the directive replaces the formal parameter.

Token pasting in the HLSL compiler is slightly different from token pasting in the C compiler, in that the pasted tokens must be valid tokens on their own. For example, consider the following macro definition:


```
#define MERGE(a, b) a##b
MERGE(float, 4x4) test;
```



In the C compiler, this results in the following:


```
float4x4 test
```



In the HLSL compiler however, this results in the following:


```
float4 x4 test
```



You can work around this behavior by using the following macro definition instead.


```
MERGE(MERGE(float, 4), x4) test;
```



## Examples

The following example uses a macro to define cursor lines.


```
#define CURSOR(top, bottom) (((top) << 8) | (bottom))
```



The following example defines a macro that retrieves a pseudorandom integer in the specified range.


```
#define getrandom(min, max) \
((rand()%(int)(((max) + 1)-(min)))+ (min))
```



## Related topics

<dl> <dt>

[Preprocessor Directives (DirectX HLSL)](dx-graphics-hlsl-appendix-preprocessor.md)
</dt> <dt>

[\#define Overloads](dx-graphics-hlsl-appendix-pre-define.md)
</dt> <dt>

[\#undef Directive (DirectX HLSL)](dx-graphics-hlsl-appendix-pre-undef.md)
</dt> </dl>

 

 





