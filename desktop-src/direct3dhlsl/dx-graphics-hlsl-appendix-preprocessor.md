---
title: Preprocessor Directives (HLSL)
description: Preprocessor directives, such as \ define and \ ifdef, are typically used to make source programs easy to change and easy to compile in different execution environments.
ms.assetid: b5164c0e-62ab-4da5-9c22-efb5e6319bd6
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# Preprocessor Directives (HLSL)

Preprocessor directives, such as [\#define](dx-graphics-hlsl-appendix-pre-define.md) and [\#ifdef](dx-graphics-hlsl-appendix-pre-ifdef.md), are typically used to make source programs easy to change and easy to compile in different execution environments. Directives in the source file tell the preprocessor to perform specific actions. For example, the preprocessor can replace tokens in the text, insert the contents of other files into the source file, or suppress compilation of part of the file by removing sections of text. Preprocessor lines are recognized and carried out before macro expansion. Therefore, if a macro expands into something that looks like a preprocessor command, that command is not recognized by the preprocessor.

Preprocessor statements use the same character set as source file statements, with the exception that escape sequences are not supported. The character set used in preprocessor statements is the same as the execution character set. The preprocessor also recognizes negative character values.

The HLSL preprocessor recognizes the following directives:

-   [\#define](dx-graphics-hlsl-appendix-pre-define.md)
-   [\#elif](dx-graphics-hlsl-appendix-pre-if.md)
-   [\#else](dx-graphics-hlsl-appendix-pre-if.md)
-   [\#endif](dx-graphics-hlsl-appendix-pre-if.md)
-   [\#error](dx-graphics-hlsl-appendix-pre-error.md)
-   [\#if](dx-graphics-hlsl-appendix-pre-if.md)
-   [\#ifdef](dx-graphics-hlsl-appendix-pre-ifdef.md)
-   [\#ifndef](dx-graphics-hlsl-appendix-pre-ifdef.md)
-   [\#include](dx-graphics-hlsl-appendix-pre-include.md)
-   [\#line](dx-graphics-hlsl-appendix-pre-line.md)
-   [\#pragma](dx-graphics-hlsl-appendix-pre-pragma.md)
-   [\#undef](dx-graphics-hlsl-appendix-pre-undef.md)

The number sign (\#) must be the first nonwhite-space character on the line containing the directive; white-space characters can appear between the number sign and the first letter of the directive. Some directives include arguments or values. Any text that follows a directive (except an argument or value that is part of the directive) must be preceded by the single-line comment delimiter (//) or enclosed in comment delimiters (/\* \*/). Lines containing preprocessor directives can be continued by immediately preceding the end-of-line marker with a backslash (\\).

Preprocessor directives can appear anywhere in a source file, but they apply only to the remainder of the source file.

## Related topics

<dl> <dt>

[Appendix (DirectX HLSL)](dx-graphics-hlsl-appendix.md)
</dt> </dl>

 

 




